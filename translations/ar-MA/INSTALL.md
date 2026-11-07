<div dir="rtl" lang="ar">

# تثبيت LiberNT: Galaxy Edition

> [English](../../INSTALL.md) | [中文](../zh-CN/INSTALL.md) | [Français](../fr-FR/INSTALL.md) | [Español](../es-ES/INSTALL.md) | [日本語](../ja-JP/INSTALL.md) | **العربية** | [Українська](../uk-UA/INSTALL.md)

## بناء الصور

جهّز بيئة البناء واضبط عملية بناء كما هو موضّح في [بناء LiberNT: Galaxy Edition بنفسك](README.md#بناء-libernt-galaxy-edition-بنفسك). ثم ابنِ الصورة التي تحتاجها من مجلد الإخراج، مثلًا ‎`output-Clang-amd64-debug`‎:

| الأمر | ينشئ | استخدمه من أجل |
|---|---|---|
| ‎`ninja bootcd`‎ | ‎`bootcd.iso`‎ | تشغيل LiberNT: Galaxy Edition من صورة قرص مضغوط، أو بدء برنامج إعداد LiberNT: Galaxy Edition منها وتثبيت LiberNT: Galaxy Edition على قرص. |

يبني الهدف أولًا كل ما يحتاجه، ويُكتب ‎`bootcd.iso`‎ في مجلد الإخراج.

## التثبيت من قرص الإعداد

أقلع ‎`bootcd.iso`‎ في آلة افتراضية أو على حاسوب، واتبع تعليمات برنامج إعداد LiberNT: Galaxy Edition. يعرض برنامج الإعداد الأقراص كما يفعل برنامج إعداد Windows، ويستطيع إنشاء الأقسام وحذفها وتهيئتها وتقليصها وتوسيعها. ويثبّت LiberNT: Galaxy Edition على NTFS وينشئ قسم نظام EFI الذي يحتاجه.

## المساعدة

إذا حدث خطأ ما، فأبلغ عنه في [Issues](https://github.com/LotusBrowser/LiberNT.Galaxy/issues) مع ذكر المعمارية ونوع البناء والإيداع الذي بنيته والخطوات التي تؤدي إلى المشكلة. توجد الأدلة والملاحظات في [Wiki](https://github.com/LotusBrowser/LiberNT.Galaxy/wiki).

</div>
