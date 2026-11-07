#!/usr/bin/env bash
# Rule-based "smart merge" for LiberNT: Galaxy Edition. No AI, no paid services.
# Put this at .github/scripts/galaxy-merge.sh
#
# Reads two optional config files from the repo (copied BEFORE the merge starts):
#   .github/galaxy/keep-ours.txt  one glob per line; our version always wins (* matches across folders)
#   .github/galaxy/rewrites.txt   lines like:  glob::sed-expression   (applied to files upstream changed)
#
# Env: UPSTREAM_BRANCH (required), RUNNER_TEMP, GITHUB_OUTPUT, BUILD_CMD (optional)
set -uo pipefail

UP="libernt/${UPSTREAM_BRANCH:?UPSTREAM_BRANCH not set}"
OUT="${RUNNER_TEMP:-/tmp}/galaxy"
mkdir -p "$OUT"
: > "$OUT/review.md"

# --- Load config before the merge touches the tree ---------------------------
touch "$OUT/keep.txt" "$OUT/rewrites.txt"
[ -f .github/galaxy/keep-ours.txt ] && cp .github/galaxy/keep-ours.txt "$OUT/keep.txt"
[ -f .github/galaxy/rewrites.txt ]  && cp .github/galaxy/rewrites.txt  "$OUT/rewrites.txt"

is_kept() {
  local f="$1" pat
  while IFS= read -r pat || [ -n "$pat" ]; do
    pat="${pat%$'\r'}"
    [[ -z "$pat" || "$pat" == \#* ]] && continue
    # shellcheck disable=SC2053
    [[ "$f" == $pat ]] && return 0
  done < "$OUT/keep.txt"
  return 1
}

staged_changes() { git diff --name-only --cached HEAD; }

# --- 1. Start the merge, uncommitted ----------------------------------------
git merge "$UP" --no-ff --no-commit --allow-unrelated-histories || true

kept=(); theirs=(); upstream_deleted=(); we_deleted=(); rewritten=()

# --- 2. Protected files: our version always wins ----------------------------
while IFS= read -r f; do
  [ -z "$f" ] && continue
  if is_kept "$f" && git cat-file -e "HEAD:$f" 2>/dev/null; then
    git checkout HEAD -- "$f" && kept+=("$f")
  fi
done < <( { staged_changes; git diff --name-only --diff-filter=U; } | sort -u )

# --- 3. Remaining conflicts --------------------------------------------------
while IFS= read -r f; do
  [ -z "$f" ] && continue
  stages=$(git ls-files -u -- "$f" | awk '{print $3}' | sort -u | tr '\n' ' ')
  has2=0; has3=0
  [[ "$stages" == *2* ]] && has2=1
  [[ "$stages" == *3* ]] && has3=1

  if [ $has2 -eq 1 ] && [ $has3 -eq 1 ]; then
    # Both sides changed it. Keep our non-conflicting edits, prefer upstream on overlapping hunks.
    if git show ":2:$f" 2>/dev/null | grep -qI .; then
      git show ":2:$f" > "$OUT/ours"
      git show ":3:$f" > "$OUT/theirs"
      if git show ":1:$f" > "$OUT/base" 2>/dev/null; then :; else : > "$OUT/base"; fi
      git merge-file -p --theirs "$OUT/ours" "$OUT/base" "$OUT/theirs" > "$OUT/result" || true
      cp "$OUT/result" "$f"
    else
      git checkout --theirs -- "$f"   # binary: take upstream
    fi
    git add -- "$f"
    theirs+=("$f")
  elif [ $has2 -eq 1 ]; then
    # We changed it, upstream deleted it: accept the deletion, flag it.
    git rm -q -f -- "$f"
    upstream_deleted+=("$f")
  elif [ $has3 -eq 1 ]; then
    # We deleted it, upstream changed it: keep it deleted.
    git rm -q -f -- "$f"
    we_deleted+=("$f")
  fi
done < <(git diff --name-only --diff-filter=U)

# --- 4. Rewrites: adapt incoming upstream changes to Galaxy -----------------
while IFS= read -r line || [ -n "$line" ]; do
  line="${line%$'\r'}"
  [[ -z "$line" || "$line" == \#* || "$line" != *"::"* ]] && continue
  glob="${line%%::*}"
  expr="${line#*::}"
  while IFS= read -r f; do
    [ -f "$f" ] || continue
    # shellcheck disable=SC2053
    [[ "$f" == $glob ]] || continue
    grep -qI . "$f" || continue
    before=$(git hash-object "$f")
    sed -E -i "$expr" "$f"
    after=$(git hash-object "$f")
    if [ "$before" != "$after" ]; then
      git add -- "$f"
      rewritten+=("$f")
    fi
  done < <(staged_changes)
done < "$OUT/rewrites.txt"

# --- 5. Safety checks --------------------------------------------------------
if git grep -nIE '^(<<<<<<< |>>>>>>> )' -- . >/dev/null 2>&1; then
  echo "::error::Conflict markers remain. Aborting."
  git merge --abort || true
  exit 1
fi
if [ -n "$(git diff --name-only --diff-filter=U)" ]; then
  echo "::error::Unmerged paths remain. Aborting."
  git merge --abort || true
  exit 1
fi
if [ -n "${BUILD_CMD:-}" ]; then
  echo "Running build check: $BUILD_CMD"
  if ! bash -c "$BUILD_CMD"; then
    echo "::error::Build check failed after merge. Aborting."
    git merge --abort || true
    exit 1
  fi
fi

# --- 6. Report ---------------------------------------------------------------
list() { local title="$1"; shift; [ $# -eq 0 ] && return; echo "### $title"; printf -- '- `%s`\n' "$@"; echo; }
{
  echo "## LiberNT upstream sync"
  echo
  list "Kept Galaxy version (protected)" "${kept[@]}"
  list "Both sides changed; overlapping hunks took upstream (REVIEW)" "${theirs[@]}"
  list "Upstream deleted a file we had modified; deletion accepted (REVIEW)" "${upstream_deleted[@]}"
  list "We had deleted; upstream changes ignored" "${we_deleted[@]}"
  list "Auto-rewritten for Galaxy Edition" "${rewritten[@]}"
} > "$OUT/review.md"

needs_review=false
if [ ${#theirs[@]} -gt 0 ] || [ ${#upstream_deleted[@]} -gt 0 ]; then needs_review=true; fi

{
  echo "needs_review=$needs_review"
} >> "${GITHUB_OUTPUT:-/dev/null}"

echo "Merge prepared. needs_review=$needs_review"
