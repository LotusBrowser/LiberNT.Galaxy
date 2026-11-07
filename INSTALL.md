# Installing LiberNT: Galaxy Edition

> **English** | [中文](translations/zh-CN/INSTALL.md) | [Français](translations/fr-FR/INSTALL.md) | [Español](translations/es-ES/INSTALL.md) | [日本語](translations/ja-JP/INSTALL.md) | [العربية](translations/ar-MA/INSTALL.md) | [Українська](translations/uk-UA/INSTALL.md)

## Building the images

Set up the build environment and configure a build as described in [Building](README.md#building-libernt-galaxy-edition-yourself). Then build the image you need from the output folder, for example `output-Clang-amd64-debug`:

| Command | Creates | Use it to |
|---|---|---|
| `ninja bootcd` | `bootcd.iso` | Run LiberNT: Galaxy Edition from a CD image, or start LiberNT: Galaxy Edition Setup from it and install LiberNT: Galaxy Edition on a disk. |

The target builds everything it needs first, and `bootcd.iso` is written to the output folder.

## Installing from the setup CD

Boot `bootcd.iso` in a virtual machine or on a PC, and follow the instructions of LiberNT: Galaxy Edition Setup. Setup lists the drives the way Windows Setup does, and can create, delete, format, shrink and extend partitions. It installs LiberNT: Galaxy Edition on NTFS and creates the EFI system partition it needs.

## Help

If something goes wrong, report it in [Issues](https://github.com/LotusBrowser/LiberNT.Galaxy/issues) with the architecture, the build type, the commit you built and the steps that lead to the problem. Guides and notes are in the [Wiki](https://github.com/LotusBrowser/LiberNT.Galaxy/wiki).
