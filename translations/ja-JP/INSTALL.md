# LiberNT: Galaxy Edition のインストール

> [English](../../INSTALL.md) | [中文](../zh-CN/INSTALL.md) | [Français](../fr-FR/INSTALL.md) | [Español](../es-ES/INSTALL.md) | **日本語** | [العربية](../ar-MA/INSTALL.md) | [Українська](../uk-UA/INSTALL.md)

## イメージをビルドする

[LiberNT: Galaxy Edition を自分でビルドする](README.md#libernt-galaxy-edition-を自分でビルドする)の説明に従ってビルド環境を整え、ビルドを構成します。次に、出力フォルダー（たとえば `output-Clang-amd64-debug`）で必要なイメージをビルドします。

| コマンド | 作成されるもの | 用途 |
|---|---|---|
| `ninja bootcd` | `bootcd.iso` | CD イメージから LiberNT: Galaxy Edition を実行する、または LiberNT: Galaxy Edition セットアップを起動してディスクに LiberNT: Galaxy Edition をインストールする。 |

このターゲットは必要なものをすべて先にビルドし、`bootcd.iso` は出力フォルダーに書き出されます。

## セットアップ CD からインストールする

仮想マシンまたは PC で `bootcd.iso` を起動し、LiberNT: Galaxy Edition セットアップの指示に従います。セットアップは Windows セットアップと同じようにドライブを一覧表示し、パーティションの作成、削除、フォーマット、縮小、拡張ができます。LiberNT: Galaxy Edition を NTFS にインストールし、必要な EFI システムパーティションを作成します。

## ヘルプ

問題が起きたら、アーキテクチャ、ビルドの種類、ビルドしたコミット、問題に至る手順を添えて [Issues](https://github.com/LotusBrowser/LiberNT.Galaxy/issues) で報告してください。ガイドやメモは [Wiki](https://github.com/LotusBrowser/LiberNT.Galaxy/wiki) にあります。
