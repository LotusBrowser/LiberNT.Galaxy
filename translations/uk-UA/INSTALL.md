# Встановлення LiberNT: Galaxy Edition

> [English](../../INSTALL.md) | [中文](../zh-CN/INSTALL.md) | [Français](../fr-FR/INSTALL.md) | [Español](../es-ES/INSTALL.md) | [日本語](../ja-JP/INSTALL.md) | [العربية](../ar-MA/INSTALL.md) | **Українська**

## Збирання образів

Налаштуйте середовище збирання та зконфігуруйте збірку, як описано в розділі [Збирання LiberNT: Galaxy Edition власноруч](README.md#збирання-libernt-galaxy-edition-власноруч). Потім зберіть необхідний образ із вихідної папки, наприклад `output-Clang-amd64-debug`:

| Команда | Створює | Призначення |
|---|---|---|
| `ninja bootcd` | `bootcd.iso` | Запуск LiberNT: Galaxy Edition з образу CD або запуск встановлення LiberNT: Galaxy Edition Setup з нього для встановлення LiberNT: Galaxy Edition на диск. |

Ціль спочатку збирає все необхідне, і `bootcd.iso` записується у вихідну папку.

## Встановлення з інсталяційного CD

Завантажте `bootcd.iso` у віртуальній машині або на комп'ютері та дотримуйтесь інструкцій LiberNT: Galaxy Edition Setup. Програма встановлення відображає диски так само, як і програма встановлення Windows, і дозволяє створювати, видаляти, форматувати, зменшувати та розширювати розділи. Вона встановлює LiberNT: Galaxy Edition на NTFS і створює необхідний системний розділ EFI.

## Допомога

Якщо щось піде не так, повідомте про це в [Issues](https://github.com/LotusBrowser/LiberNT.Galaxy/issues), зазначивши архітектуру, тип збірки, коміт, з якого збирали, та кроки для відтворення проблеми. Посібники та нотатки можна знайти у [Wiki](https://github.com/LotusBrowser/LiberNT.Galaxy/wiki).
