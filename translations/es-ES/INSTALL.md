# Instalar LiberNT: Galaxy Edition

> [English](../../INSTALL.md) | [中文](../zh-CN/INSTALL.md) | [Français](../fr-FR/INSTALL.md) | **Español** | [日本語](../ja-JP/INSTALL.md) | [العربية](../ar-MA/INSTALL.md) | [Українська](../uk-UA/INSTALL.md)

## Compilar las imágenes

Prepara el entorno de compilación y configura una compilación como se describe en [Compilar LiberNT: Galaxy Edition por tu cuenta](README.md#compilar-libernt-galaxy-edition-por-tu-cuenta). Después compila la imagen que necesites desde la carpeta de salida, por ejemplo `output-Clang-amd64-debug`:

| Comando | Crea | Sirve para |
|---|---|---|
| `ninja bootcd` | `bootcd.iso` | Ejecutar LiberNT: Galaxy Edition desde una imagen de CD, o iniciar desde ella la instalación de LiberNT: Galaxy Edition e instalar LiberNT: Galaxy Edition en un disco. |

El destino compila primero todo lo que necesita, y `bootcd.iso` se escribe en la carpeta de salida.

## Instalar desde el CD de instalación

Arranca `bootcd.iso` en una máquina virtual o en un PC y sigue las instrucciones de la instalación de LiberNT: Galaxy Edition. La instalación muestra las unidades igual que el instalador de Windows, y puede crear, eliminar, formatear, reducir y ampliar particiones. Instala LiberNT: Galaxy Edition en NTFS y crea la partición del sistema EFI que necesita.

## Ayuda

Si algo sale mal, infórmalo en [Issues](https://github.com/LotusBrowser/LiberNT.Galaxy/issues) con la arquitectura, el tipo de compilación, el commit que compilaste y los pasos que llevan al problema. Las guías y notas están en la [Wiki](https://github.com/LotusBrowser/LiberNT.Galaxy/wiki).
