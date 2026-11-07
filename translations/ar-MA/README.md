<div dir="rtl" lang="ar">

> [English](../../README.md) | [中文](../zh-CN/README.md) | [Français](../fr-FR/README.md) | [Español](../es-ES/README.md) | [日本語](../ja-JP/README.md) | **العربية** | [Українська](../uk-UA/README.md)

<p align="center">
  <img src="../../media/graphics/branding/libernt-banner.png" width="480" alt="LiberNT: Galaxy Edition">
</p>

> [!IMPORTANT]
> نظام LiberNT: Galaxy Edition قيد التطوير النشط. النسخ المتوفرة في صفحة [Releases](https://github.com/LotusBrowser/LiberNT.Galaxy/releases) هي إصدارات تجريبية من نوع Debug مخصصة للاختبار: شغّلها في آلة افتراضية أو على جهاز احتياطي، وليس على حاسوب تعتمد عليه.

<div align="center">

# [LiberNT: Galaxy Edition](https://github.com/LotusBrowser/LiberNT.Galaxy)
### نظام تشغيل NT حر

**صُنع حبًّا في معمارية NT. متوافق مع Windows® 11، لمعماريات amd64 وarm64 وriscv64.**

[![Build](https://img.shields.io/github/actions/workflow/status/LotusBrowser/LiberNT.Galaxy/build.yml?branch=main-nt10&label=Build&style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/LotusBrowser/LiberNT.Galaxy/actions/workflows/build.yml)
[![License: GPL 3.0](https://img.shields.io/badge/License-GPL_3.0-0161B6?style=for-the-badge&logo=gnu&logoColor=white)](#الترخيص)

<img src="https://img.shields.io/github/repo-size/LotusBrowser/LiberNT.Galaxy?style=flat-square&color=blue" alt="Repo Size">
<img src="https://img.shields.io/github/stars/LotusBrowser/LiberNT.Galaxy?style=flat-square&color=yellow" alt="Stars">
<img src="https://img.shields.io/github/forks/LotusBrowser/LiberNT.Galaxy?style=flat-square&color=lightgrey" alt="Forks">
<img src="https://img.shields.io/github/last-commit/LotusBrowser/LiberNT.Galaxy/main-nt10?style=flat-square&color=green" alt="Last Commit">
<img src="https://img.shields.io/github/issues/LotusBrowser/LiberNT.Galaxy?style=flat-square&color=orange" alt="Issues">

<br>

[![Download the latest build](https://img.shields.io/badge/Download-Latest_build-0161B6?style=for-the-badge&logo=github&logoColor=white)](https://github.com/LotusBrowser/LiberNT.Galaxy/releases)

</div>

---

<p align="center">
  <img width="1000" alt="سطح مكتب LiberNT: Galaxy Edition على arm64" src="../../media/graphics/screenshots/libernt-desktop-arm64.png">
</p>

<p align="center"><sub>سطح مكتب LiberNT: Galaxy Edition على arm64، من النسخة nt10.0-043-2555 في QEMU</sub></p>

---

LiberNT: Galaxy Edition نسخة متفرعة (fork) من [LiberNT](https://github.com/LiberNT/LiberNT) بسمة Galaxy. تملكه [Lotus](https://github.com/LotusBrowser) وتتولى صيانته، وتبقى LiberNT من عمل مساهميها أنفسهم.

LiberNT نظام تشغيل NT حر. والاسم يدل على ذلك: كلمة *liber* تعني **حر** باللاتينية. يهدف النظام إلى **التوافق مع Windows® 11**، مع ترك مساحة لميزات حرة وتجريبية.

يقدّم LiberNT: Galaxy Edition عملًا واسعًا على مكونات فضاء النواة وبرامج التشغيل، موجّهًا نحو الاستقرار والعتاد الحديث، ويركّز على منصات 64 بت: **amd64 وarm64 وriscv64**.

هدفنا نظام يبقى قابلًا للصيانة على المدى الطويل: **مستقر وموثوق وفعّال**، يعمل أيضًا على الأجهزة المدمجة، وقادر على دعم كل ميزة ينبغي أن يوفرها نظام تشغيل حديث.

> [!NOTE]
> جديد على NT؟ **NT** هي المعمارية التي تقوم عليها كل الإصدارات الحديثة من Windows: نواتها ونموذج برامج التشغيل وخدمات النظام. LiberNT: Galaxy Edition نظام تشغيل حر مبني على هذه المعمارية، ويتخذ من Windows 11 مرجعًا يقيس نفسه به.

---

## جدول المحتويات

- [ما الذي يتضمنه LiberNT: Galaxy Edition](#ما-الذي-يتضمنه-libernt-galaxy-edition)
- [المنصات المدعومة](#المنصات-المدعومة)
- [البدء](#البدء)
  - [الخطوة 1: تنزيل نسخة](#الخطوة-1-تنزيل-نسخة)
  - [الخطوة 2: الإقلاع](#الخطوة-2-الإقلاع)
  - [الخطوة 3: تثبيت LiberNT: Galaxy Edition](#الخطوة-3-تثبيت-libernt-galaxy-edition)
- [بناء LiberNT: Galaxy Edition بنفسك](#بناء-libernt-galaxy-edition-بنفسك)
- [أنظمة البناء](#أنظمة-البناء)
- [بنية المشروع](#بنية-المشروع)
- [المساهمة](#المساهمة)
- [استخدام الذكاء الاصطناعي](#استخدام-الذكاء-الاصطناعي)
- [الترخيص](#الترخيص)
- [حول المشروع](#حول-المشروع)

---

## ما الذي يتضمنه LiberNT: Galaxy Edition

يجلب LiberNT: Galaxy Edition العتاد والمنصات الحديثة إلى معمارية NT.

| الميزة | ما تعنيه لك |
| --- | --- |
| **64 بت أولًا** | تعمل النواة وطبقة HAL وFreeLoader على amd64 وarm64 وriscv64. |
| **الإقلاع عبر UEFI** | يقلع على برامج UEFI الثابتة، مع مخزن إطارات GOP ودعم مبكر للشاشة. |
| **ناقلات وتخزين حديثة** | PCIe وPCI والتوصيل والتشغيل (Plug and Play) وUSB عبر xHCI وSD/eMMC، إضافة إلى برامج تشغيل التخزين والناقلات. |
| **دعم اللوحات** | لوحات حقيقية، منها Raspberry Pi ووحدة التحكم في الإدخال والإخراج RP1 الخاصة بها. |
| **نموذج برامج التشغيل في Windows 11** | التوافق مع Windows 11 (NT10) والعمل على نموذج برامج التشغيل، مع التحقق من ذلك مقارنةً بـ Windows 11 نفسه. |
| **الرسوميات وتطبيقات x86 على Arm** | نموذج برامج تشغيل الرسوميات مع Mesa، وWoW64 مع FEX، خيارات بناء يمكنك تفعيلها. |
| **برنامج إعداد LiberNT: Galaxy Edition** | يعرض الأقراص كما يفعل برنامج إعداد Windows، وينشئ الأقسام ويحذفها ويهيئها ويقلّصها ويوسّعها، ويثبّت LiberNT: Galaxy Edition على NTFS مع قسم نظام EFI الذي يحتاجه. |
| **نسختك الخاصة** | تتيح لك ‎`menuconfig`‎ اختيار الهدف والمترجم ونوع البناء، وتفعيل الميزات أو تعطيلها. |

> [!TIP]
> كل نسخة في صفحة [Releases](https://github.com/LotusBrowser/LiberNT.Galaxy/releases) تذكر ما تغيّر منذ النسخة السابقة.

---

## المنصات المدعومة

| المعمارية | صور جاهزة | البناء من المصدر | ملاحظات |
| --- | :---: | :---: | --- |
| **amd64** | ✓ | ✓ | Clang (الافتراضي) أو GCC |
| **arm64** | ✓ | ✓ | يتضمن دعم Raspberry Pi |
| **riscv64** | ✓ | ✓ | تُبنى صورة منفصلة للوحات JH7110 |
| **i386** | | ✓ | x86 بمعمارية 32 بت |

تتضمن نسخ الإصدار أيضًا صورًا لـ PowerPC.

---

## البدء

### الخطوة 1: تنزيل نسخة

تأتي كل نسخة في صفحة [Releases](https://github.com/LotusBrowser/LiberNT.Galaxy/releases) على شكل ملف ZIP لكل صورة ومعمارية:

| الملف | ما هو |
| --- | --- |
| ‎`bootcd-iso-…-<arch>-…zip`‎ | ‎`bootcd.iso`‎، صورة قرص مضغوط تشغّل LiberNT: Galaxy Edition أو تبدأ برنامج إعداد LiberNT: Galaxy Edition |

> [!NOTE]
> هذه نسخ Debug مبنية بـ Clang، تنتجها GitHub Actions من الفرع ‎`main-nt10`‎.

### الخطوة 2: الإقلاع

أسرع طريقة لتجربة LiberNT: Galaxy Edition هي صورة القرص المضغوط:

1. فك ضغط الملف الذي نزّلته لتحصل على ‎`bootcd.iso`‎
2. شغّله في آلة افتراضية مثل **QEMU**، أو أقلع حاسوبًا منه

يشغّل LiberNT: Galaxy Edition من القرص، أو يبدأ برنامج إعداد LiberNT: Galaxy Edition.

### الخطوة 3: تثبيت LiberNT: Galaxy Edition

أقلع ‎`bootcd.iso`‎ في آلة افتراضية أو على حاسوب، واتبع تعليمات **برنامج إعداد LiberNT: Galaxy Edition**.

> [!CAUTION]
> يستطيع برنامج الإعداد حذف الأقسام وتهيئتها. انسخ احتياطيًا كل ما هو مهم على القرص الهدف قبل التثبيت.

راجع [INSTALL.md](INSTALL.md) للاطلاع على دليل التثبيت الكامل.

---

## بناء LiberNT: Galaxy Edition بنفسك

يُبنى LiberNT: Galaxy Edition باستخدام RosBE، وهي سلسلة أدوات للبناء المتقاطع. تعمل الخطوات التالية على Linux وmacOS، وعلى Windows عبر WSL2.

### 1. تثبيت سلسلة الأدوات

تحتاج إلى Git وCMake وNinja ومترجم C/C++ لجهازك. يضيف RosBE المترجمات التي تبني LiberNT: Galaxy Edition.

<div dir="ltr">

```sh
curl -fsSL https://raw.githubusercontent.com/LiberNT/libernt-build-toolchain/main/rosbe-unix-bootstrap.sh | sh
```

</div>

> [!TIP]
> على Windows، ننصح باستخدام WSL2. ثبّته بالأمر ‎`wsl --install`‎، وافتح طرفية Linux التي يضيفها، واتبع فيها خطوات Linux. احتفظ بالمصدر داخل نظام ملفات Linux بدلًا من ‎`/mnt/c`‎، حيث يكون البناء أبطأ.

### 2. الحصول على المصدر

<div dir="ltr">

```sh
git clone https://github.com/LotusBrowser/LiberNT.Galaxy.git
cd LiberNT.Galaxy
```

</div>

> [!NOTE]
> يجلب أول تشغيل للإعداد أيضًا الوحدة الفرعية والمصادر الخارجية التي يحتاجها البناء.

### 3. الإعداد

<div dir="ltr">

```sh
./configure.sh
```

</div>

دون أي خيار، يجهّز هذا الأمر بناء AMD64 من نوع Debug باستخدام Clang في المجلد ‎`output-Clang-amd64-debug`‎. يتبع اسم المجلد دائمًا النمط ‎`output-<المترجم>-<المعمارية>-<debug|release>`‎.

| الخيار | ما يفعله |
| --- | --- |
| ‎`-a`‎، ‎`--arch <arch>`‎ | يختار المعمارية الهدف: ‎`amd64`‎ (الافتراضية) أو ‎`i386`‎ أو ‎`arm64`‎ أو ‎`riscv64`‎. |
| ‎`--clang`‎ | يبني باستخدام Clang/LLVM من RosBE. وهذا هو الافتراضي. |
| ‎`--gcc`‎ | يبني باستخدام GCC من RosBE بدلًا من Clang. نسخة RosBE لـ macOS لا تتضمن GCC. |
| ‎`-r`‎، ‎`--release`‎ | ينتج بناء Release محسّنًا. من دونه تحصل على بناء Debug، وهو أسهل في التنقيح. |
| ‎`menuconfig`‎ | يفتح قائمة أولًا لاختيار المكونات الاختيارية. تُحفظ اختياراتك في مجلد الإخراج. |
| ‎`makefiles`‎ | يستخدم ‎`make`‎ بدلًا من Ninja. |
| ‎`--no-feeds-update`‎ | يتخطى جلب المصادر الخارجية المذكورة في ‎`feeds.conf`‎، مثلًا عند العمل دون اتصال. |
| ‎`-D<name>=<value>`‎ | يمرّر إعدادًا مباشرة إلى CMake. |

على سبيل المثال:

<div dir="ltr">

```sh
./configure.sh -a arm64              # بناء ARM64 من نوع Debug باستخدام Clang
./configure.sh -a i386 --gcc         # بناء x86 بمعمارية 32 بت باستخدام GCC
./configure.sh -a amd64 --release    # بناء AMD64 محسّن
```

</div>

لبناء أكثر تخصيصًا، أضف ‎`menuconfig`‎:

<div dir="ltr">

```sh
./configure.sh menuconfig
```

</div>

يفتح قائمة، تشبه كثيرًا قائمة نواة Linux، تختار فيها الهدف والمترجم ونوع البناء، وتفعّل الميزات أو تعطّلها: توليد الشيفرة وضبطها، ونموذج برامج تشغيل الرسوميات وMesa، وWoW64 وFEX، وتنقيح النواة، وتشغيل الاختبارات، وغير ذلك. اضغط ‎`?`‎ على أي خيار للمساعدة، و‎`S`‎ للحفظ، و‎`Q`‎ للخروج. تُحفظ اختياراتك في مجلد الإخراج وتُستخدم في كل مرة تعيد فيها إعداده.

### 4. البناء

انتقل إلى مجلد الإخراج وشغّل Ninja مع الهدف الذي تريده:

<div dir="ltr">

```sh
cd output-Clang-amd64-debug
ninja bootcd
```

</div>

| الأمر | ينشئ | استخدمه من أجل |
| --- | --- | --- |
| ‎`ninja bootcd`‎ | ‎`bootcd.iso`‎ | تثبيت LiberNT: Galaxy Edition من صورة قرص مضغوط، في آلة افتراضية أو على حاسوب. |

يبني الهدف أولًا كل ما يحتاجه، ويُكتب ‎`bootcd.iso`‎ في مجلد الإخراج.

---

## أنظمة البناء

| النظام | المترجمات | ملاحظات |
| --- | --- | --- |
| **Linux** x86_64 / aarch64 | Clang وGCC | سلسلة أدوات RosBE كاملة |
| **macOS** Intel / Apple Silicon | Clang | لا يوفر RosBE نسخة GCC لـ macOS |
| **Windows** | Clang وGCC | عبر WSL2، باتباع خطوات Linux |

على كل نظام، ثبّت Git وCMake وNinja وFlex وBison من مدير الحزم لديك. لا يوفر RosBE إلا المترجمات المتقاطعة. توجد سلاسل الأدوات الجاهزة في [LiberNT/libernt-build-toolchain](https://github.com/LiberNT/libernt-build-toolchain).

---

## بنية المشروع

<div dir="ltr">

```text
LiberNT.Galaxy/
├── base/            # التطبيقات والخدمات وبرنامج الإعداد والصدفة
├── boot/            # FreeLoader وبيانات الإقلاع وصور الإقلاع
├── bootloader/      # مدير الإقلاع ومحمّل Windows ودعم UEFI وOpen Firmware
├── dll/             # مكتبات DLL في وضع المستخدم، ومنها ntdll ومكتبات Win32
├── drivers/         # برامج التشغيل في وضع النواة: الناقلات والتخزين وأنظمة الملفات والشبكة والإدخال وغيرها
├── hal/             # طبقات تجريد العتاد لـ x86 وArm وArm64 وPowerPC وRISC-V
├── media/           # الخطوط والسمات وملفات INF والأصوات والهوية البصرية
├── modules/         # تطبيقات اختيارية واختبارات وخلفيات
├── ntoskrnl/        # نواة NT والطبقة التنفيذية
├── sdk/             # الترويسات والمكتبات وأدوات البناء
├── submodules/      # وصفات المكونات الخارجية ورقعها
├── subsystems/      # CSRSS ونظام Windows الفرعي
├── win32ss/         # win32k وUSER وGDI وبرامج تشغيل العرض
├── configure.sh     # يجهّز البناء على Linux وmacOS وWSL2
└── configure.cmd    # يجهّز البناء على Windows
```

</div>

---

## المساهمة

أبلغ عن الأخطاء واقترح الميزات في [Issues](https://github.com/LotusBrowser/LiberNT.Galaxy/issues)، وستجد الأدلة والملاحظات في [Wiki](https://github.com/LotusBrowser/LiberNT.Galaxy/wiki).

راجع [CONTRIBUTING.md](CONTRIBUTING.md) و[PULL_REQUEST_MANAGEMENT.md](PULL_REQUEST_MANAGEMENT.md). إن كنت تخطط لتغيير كبير، فاسأل أولًا في [Issues](https://github.com/LotusBrowser/LiberNT.Galaxy/issues).

> [!WARNING]
> **تنبيه قانوني:** إذا كنت قد اطّلعت على الشيفرة المصدرية المملوكة لـ Microsoft Windows (بما في ذلك على سبيل المثال لا الحصر الشيفرة المسرّبة لـ Windows NT 3.5 وNT 4 و2000، وWindows Research Kernel)، فلن تُقبل مساهمتك بسبب احتمال انتهاك حقوق النشر.

---

## استخدام الذكاء الاصطناعي

نريد أن نكون واضحين: الذكاء الاصطناعي جزء من طريقة بناء LiberNT: Galaxy Edition. فهو يساعدنا في مراجعة الشيفرة وكتابتها، وكل ما يكتبه يراجعه إنسان بعد ذلك. وقبل أن يصل أي شيء إلى الفرع الرئيسي، يشغّل شخص اختبارات شاملة من البداية إلى النهاية ويتحقق منها. نحن نهتم بهذا المشروع أكثر من أن نترك تراجعًا يمرّ دون أن نلاحظه.

ويساعدنا أيضًا في قراءة التوثيق واستخراج التعريفات وإصلاح الأخطاء. فلكل خطأ، يقارن ما يقوله التوثيق الرسمي في Microsoft Learn بما تفعله دالتنا فعلًا، لنرى بالضبط أين يختلف سلوكنا.

ومثل أي أداة أخرى، الذكاء الاصطناعي موجود لمساعدتنا على تحقيق أهدافنا. وهو يتبع القواعد نفسها التي نلزم بها أنفسنا، والمحددة في [AGENTS.md](../../AGENTS.md):

- نبني اعتمادًا على ترويسات Windows SDK وWDK، والرموز العامة لـ Windows 11، وتوثيق Microsoft، والتشغيل كصندوق أسود على Windows 11.
- نعمل بأسلوب الغرفة النظيفة: لا ننسخ أبدًا شيفرة Windows مفككة أو معاد تجميعها، ولا ننسخ أبدًا شيفرة GPL من Linux.
- لا يُعدّ الإصلاح إصلاحًا إلا بعد أن نراه يعمل في إقلاع حقيقي أو تشغيل للاختبارات. وبعد نجاح الاختبارات، سيحافظ نظام CI مستقبلي على نجاحها ويحفظ تقدّمنا العام.
- نقارن نتائج اختباراتنا، فحصًا بفحص، بنتائج الاختبارات نفسها عند تشغيلها على Windows 11.

> [!TIP]
> إذا كنت تستخدم الذكاء الاصطناعي في مساهماتك، فأنت مرحّب بك أيضًا. فقط أخبرنا في طلب السحب بالأجزاء التي ساعد فيها وكيف اختبرتها. هذه الصراحة هي كل ما نطلبه.

---

## الترخيص

يُرخَّص LiberNT: Galaxy Edition بموجب [GNU GPL 3.0](../../COPYING). وتحتفظ الشيفرة الموروثة من مشاريع أخرى بالترخيص المذكور في ترويسات ملفاتها، ومعظمها GPL 2.0 أو أحدث. نصوص GPL 2.0 وLGPL 2.1 وBSD التي تشير إليها تلك الملفات موجودة في [COPYING2](../../COPYING2) و[COPYING.LIB](../../COPYING.LIB) و[COPYING.ARM](../../COPYING.ARM).

التغييرات التي أُجريت في LiberNT: Galaxy Edition محمية بحقوق النشر © 2026 لـ Lotus. وتحتفظ الشيفرة الموروثة وشيفرة الأطراف الثالثة بإشعارات حقوق النشر الخاصة بمؤلفيها. راجع [CREDITS.md](../../CREDITS.md).

LiberNT: Galaxy Edition مشروع مستقل. وهو غير تابع لشركة Microsoft، ولا تؤيده ولا ترعاه. Windows® علامة تجارية مسجلة لشركة Microsoft Corporation.

---

## حول المشروع

يملك [Lotus](https://github.com/LotusBrowser) المشروع LiberNT: Galaxy Edition وتتولى صيانته. وهو نسخة متفرعة من LiberNT الذي يبنيه **مساهمو LiberNT**؛ بدأ [Ahmed Arif](https://github.com/ahmedarif193) مشروع LiberNT ويتولى صيانته [Ahmed Arif](https://github.com/ahmedarif193) و[Ostap Brehin](https://github.com/osbre) و[Vivyy](https://github.com/enginelesscc).

- [زُر منظمة Lotus](https://github.com/LotusBrowser)
- [المشروع الأصلي: LiberNT](https://github.com/LiberNT/LiberNT)
- [موقع LiberNT الإلكتروني](https://libernt.com)
- [نزّل أحدث نسخة](https://github.com/LotusBrowser/LiberNT.Galaxy/releases)
- [Wiki](https://github.com/LotusBrowser/LiberNT.Galaxy/wiki)

</div>
