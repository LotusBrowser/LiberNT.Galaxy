# Installer LiberNT: Galaxy Edition

> [English](../../INSTALL.md) | [中文](../zh-CN/INSTALL.md) | **Français** | [Español](../es-ES/INSTALL.md) | [日本語](../ja-JP/INSTALL.md) | [العربية](../ar-MA/INSTALL.md) | [Українська](../uk-UA/INSTALL.md)

## Compiler les images

Préparez l'environnement de compilation et configurez une compilation comme décrit dans [Compiler LiberNT: Galaxy Edition vous-même](README.md#compiler-libernt-galaxy-edition-vous-même). Compilez ensuite l'image dont vous avez besoin depuis le dossier de sortie, par exemple `output-Clang-amd64-debug` :

| Commande | Crée | Pour |
|---|---|---|
| `ninja bootcd` | `bootcd.iso` | Lancer LiberNT: Galaxy Edition depuis une image de CD, ou y démarrer l'installation de LiberNT: Galaxy Edition et installer LiberNT: Galaxy Edition sur un disque. |

La cible compile d'abord tout ce dont elle a besoin, et `bootcd.iso` est écrit dans le dossier de sortie.

## Installer depuis le CD d'installation

Démarrez `bootcd.iso` dans une machine virtuelle ou sur un PC, et suivez les instructions de l'installation de LiberNT: Galaxy Edition. L'installation affiche les disques comme le programme d'installation de Windows, et peut créer, supprimer, formater, réduire et étendre des partitions. Elle installe LiberNT: Galaxy Edition sur NTFS et crée la partition système EFI dont il a besoin.

## Aide

En cas de problème, signalez-le dans les [Issues](https://github.com/LotusBrowser/LiberNT.Galaxy/issues) en précisant l'architecture, le type de compilation, le commit que vous avez compilé et les étapes qui mènent au problème. Les guides et les notes se trouvent dans le [Wiki](https://github.com/LotusBrowser/LiberNT.Galaxy/wiki).
