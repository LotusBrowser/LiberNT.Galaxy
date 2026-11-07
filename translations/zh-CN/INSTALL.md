# 安装 LiberNT: Galaxy Edition

> [English](../../INSTALL.md) | **中文** | [Français](../fr-FR/INSTALL.md) | [Español](../es-ES/INSTALL.md) | [日本語](../ja-JP/INSTALL.md) | [العربية](../ar-MA/INSTALL.md) | [Українська](../uk-UA/INSTALL.md)
>
> 翻译说明：本译文由 AI 初译并排版；术语、代码块、链接与锚点已与英文原版核对，中文术语已经人工核对。如有纰漏，请提交 issue 指出；表述以英文版为准。

## 构建镜像

先按[构建](README.md#自行构建-libernt-galaxy-edition)一节搭好构建环境并完成配置，再在输出目录(例如 `output-Clang-amd64-debug`)里构建所需镜像：

| 命令 | 生成 | 用途 |
|---|---|---|
| `ninja bootcd` | `bootcd.iso` | 从 CD 镜像运行 LiberNT: Galaxy Edition，或从该镜像启动 LiberNT: Galaxy Edition 安装程序，把 LiberNT: Galaxy Edition 装到磁盘。 |

该目标会先把它依赖的内容构建好，`bootcd.iso` 会写入输出目录。

## 从安装光盘安装

在虚拟机或 PC 上启动 `bootcd.iso`，按 LiberNT: Galaxy Edition 安装程序的提示操作。安装程序的磁盘列表与 Windows 安装程序一致，可新建、删除、格式化、压缩和扩展分区。它会把 LiberNT: Galaxy Edition 装到 NTFS 分区，并创建所需的 EFI 系统分区。

## 求助

遇到问题请在 [Issues](https://github.com/LotusBrowser/LiberNT.Galaxy/issues) 反馈，并附上架构、构建类型、所用提交，以及复现步骤。指南和笔记见 [Wiki](https://github.com/LotusBrowser/LiberNT.Galaxy/wiki)。
