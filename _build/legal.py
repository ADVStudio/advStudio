"""Юридичні та службові сторінки ADV (UA + EN): політика конфіденційності, cookie, умови,
сторінка 404, sitemap.xml, robots.txt. Викликається з _build/build.py.

⚠️ Перед публікацією заповніть реквізити в OWNER (ПІБ ФОП / назва ТОВ, РНОКПП / ЄДРПОУ, адреса)
і покажіть тексти юристу — це шаблони, а не юридична консультація.
"""
import os

UPDATED = {"uk": "12 листопада 2026 р.", "en": "12 November 2026"}

# Реквізити власника сайту — ЗАПОВНІТЬ
OWNER = {
    "uk": "[ПІБ ФОП або назва ТОВ], РНОКПП / код ЄДРПОУ: [__________], адреса: [__________], м. Львів, Україна",
    "en": "[Full name of sole proprietor or company name], tax ID: [__________], address: [__________], Lviv, Ukraine",
}

PAGES = ["privacy", "cookies", "terms"]

TXT = {
"uk": {
  "home": "На головну", "updated": "Оновлено", "contents": "Зміст", "other": "Інші документи", "contact": "Питання щодо документа",
  "titles": {"privacy": "Політика конфіденційності", "cookies": "Політика cookie", "terms": "Умови використання сайту"},
  "desc": {"privacy": "Як ADV Development Studio збирає, використовує та захищає персональні дані.",
           "cookies": "Які cookie та подібні технології використовує сайт ADV.",
           "terms": "Правила користування сайтом ADV Development Studio."},
  "404_t": "Сторінку не знайдено", "404_p": "Можливо, її перенесли або в адресі помилка. Поверніться на головну або напишіть нам — допоможемо.",
  "404_b": "На головну",
},
"en": {
  "home": "Home", "updated": "Last updated", "contents": "Contents", "other": "Other documents", "contact": "Questions about this document",
  "titles": {"privacy": "Privacy policy", "cookies": "Cookie policy", "terms": "Terms of use"},
  "desc": {"privacy": "How ADV Development Studio collects, uses and protects personal data.",
           "cookies": "Which cookies and similar technologies the ADV website uses.",
           "terms": "Rules for using the ADV Development Studio website."},
  "404_t": "Page not found", "404_p": "It may have moved, or there’s a typo in the address. Go back home or write to us — we’ll help.",
  "404_b": "Back to home",
},
}


def body(lang, page, E, owner):
    m = f'<a href="mailto:{E}">{E}</a>'
    if lang == "uk":
        if page == "privacy":
            return [
                ("Загальні положення", [
                    f"Ця Політика пояснює, як ADV Development Studio (далі — «ADV», «ми») обробляє персональні дані відвідувачів сайту та клієнтів. Володілець персональних даних: {owner}. Контакт з питань захисту даних: {m}.",
                    "Ми обробляємо дані відповідно до Закону України «Про захист персональних даних» № 2297-VI, а для відвідувачів і клієнтів з Європейського Союзу — також відповідно до Регламенту (ЄС) 2016/679 (GDPR)."]),
                ("Які дані ми збираємо", [
                    "<ul><li><b>Дані з форми заявки:</b> ім’я, контакт для звʼязку (телефон, Telegram або email), орієнтовний бюджет, опис задачі.</li>"
                    "<li><b>Листування:</b> зміст повідомлень, які ви надсилаєте нам email, у месенджерах чи соцмережах.</li>"
                    "<li><b>Дані за договором:</b> реквізити, необхідні для укладення й виконання договору та виставлення рахунків.</li>"
                    "<li><b>Технічні дані:</b> IP-адреса, тип браузера та пристрою, час запиту — фіксуються сервером хостингу та постачальниками шрифтів і бібліотек під час завантаження сторінок.</li></ul>",
                    "Ми не збираємо спеціальні категорії даних (про здоров’я, релігійні переконання тощо) і просимо не надсилати їх у формі."]),
                ("Мета та правові підстави обробки", [
                    "<ul><li>Відповісти на заявку та підготувати комерційну пропозицію — <b>ваша згода</b> та <b>дії до укладення договору</b> (GDPR ст. 6(1)(a), (b)).</li>"
                    "<li>Укласти й виконати договір, вести облік та звітність — <b>виконання договору</b> і <b>юридичні обов’язки</b> (ст. 6(1)(b), (c)).</li>"
                    "<li>Забезпечити роботу та безпеку сайту — <b>законний інтерес</b> (ст. 6(1)(f)).</li></ul>",
                    "Ми не використовуємо ваші дані для розсилок без окремої згоди і не продаємо їх третім особам."]),
                ("Строки зберігання", [
                    "<ul><li>Заявки, за якими договір не укладено, — до 12 місяців після останнього контакту.</li>"
                    "<li>Дані за договором — протягом строку його дії та 3 роки після завершення (строк позовної давності), а бухгалтерські документи — стільки, скільки вимагає законодавство.</li>"
                    "<li>Технічні логи — відповідно до налаштувань хостинг-провайдера, зазвичай до 30 днів.</li></ul>"]),
                ("Кому ми передаємо дані", [
                    "Дані можуть отримувати лише постачальники, без яких неможлива робота студії, і лише в потрібному обсязі:",
                    "<ul><li>хостинг-провайдер сайту (GitHub Pages);</li><li>Google (Gmail, Google Таблиці, Apps Script) — для приймання заявок із форми, листування та зберігання робочих матеріалів;</li><li>Telegram — для миттєвих сповіщень команди про нові заявки;</li>"
                    "<li>месенджери (Viber, WhatsApp), якщо ви самі обрали їх для звʼязку;</li>"
                    "<li>Google Fonts, jsDelivr, cdnjs — завантаження шрифтів і бібліотек (отримують технічні дані запиту);</li>"
                    "<li>бухгалтер, банк, податкові органи — у межах вимог законодавства.</li></ul>",
                    "Деякі з цих постачальників можуть обробляти дані за межами України та ЄС. У таких випадках ми покладаємося на їхні стандартні договірні умови щодо захисту даних."]),
                ("Ваші права", [
                    "Відповідно до ст. 8 Закону № 2297-VI та ст. 15–22 GDPR ви маєте право:",
                    "<ul><li>знати, які ваші дані ми обробляємо, з якою метою та кому їх передаємо;</li><li>отримати копію своїх даних;</li>"
                    "<li>вимагати виправлення неточних або видалення даних;</li><li>обмежити обробку чи заперечити проти неї;</li>"
                    "<li>відкликати згоду в будь-який момент (це не впливає на законність обробки до відкликання);</li>"
                    "<li>отримати дані у машиночитному форматі для передачі іншому постачальнику.</li></ul>",
                    f"Щоб скористатися правами, напишіть на {m}. Ми відповімо протягом 30 днів. Ви також можете звернутися зі скаргою до Уповноваженого Верховної Ради України з прав людини (ombudsman.gov.ua), а мешканці ЄС — до наглядового органу своєї країни."]),
                ("Безпека", ["Ми обмежуємо доступ до даних колом людей, яким вони потрібні для роботи, використовуємо двофакторну автентифікацію в робочих акаунтах і передаємо дані лише захищеними каналами (HTTPS, TLS)."]),
                ("Діти", ["Сайт і послуги ADV призначені для бізнесу й не орієнтовані на осіб до 16 років. Якщо ви дізналися, що дитина надіслала нам дані, повідомте нас — ми їх видалимо."]),
                ("Зміни до Політики", ["Ми можемо оновлювати цю Політику. Актуальна версія завжди доступна на цій сторінці, а дата останнього оновлення вказана вгорі."]),
            ]
        if page == "cookies":
            return [
                ("Що таке cookie", ["Cookie — це невеликі файли, які сайт зберігає у вашому браузері. Схожі технології — localStorage і sessionStorage — дозволяють зберігати дані на вашому пристрої без надсилання на сервер."]),
                ("Що використовує наш сайт зараз", [
                    "<ul><li><b>Рекламних та аналітичних cookie немає.</b> Ми не використовуємо Google Analytics, Meta Pixel чи подібні інструменти відстеження.</li>"
                    "<li><b>localStorage у концептах.</b> У демонстраційному концепті KAVA LAB у вашому браузері зберігається вміст демо-кошика, щоб він не зникав після перезавантаження. Ці дані нікуди не передаються.</li>"
                    "<li><b>Сторонні ресурси.</b> Шрифти Google Fonts і бібліотеки з jsDelivr та cdnjs завантажуються з серверів постачальників. Вони отримують технічні дані запиту (IP-адресу, браузер), але не встановлюють cookie на нашому домені.</li></ul>"]),
                ("Якщо ми додамо аналітику", ["Якщо ми почнемо використовувати аналітичні або рекламні інструменти, ми оновимо цю сторінку та покажемо банер, у якому ви зможете дати або не дати згоду. Необов’язкові cookie не встановлюватимуться без вашої згоди."]),
                ("Як керувати cookie", ["Ви можете переглянути й видалити cookie та дані сайтів у налаштуваннях браузера: Chrome — «Налаштування → Конфіденційність і безпека», Safari — «Параметри → Конфіденційність», Firefox — «Налаштування → Приватність і захист». Очищення даних сайту також видалить демо-кошик у концептах."]),
                ("Контакти", [f"Питання щодо cookie надсилайте на {m}."]),
            ]
        return [
            ("Загальні положення", [f"Ці Умови регулюють користування сайтом ADV Development Studio. Власник сайту: {owner}. Користуючись сайтом, ви погоджуєтеся з цими Умовами. Якщо ви не згодні — будь ласка, не користуйтеся сайтом."]),
            ("Інформація на сайті", [
                "Інформація про послуги, пакети, строки та ціни має довідковий характер і <b>не є публічною офертою</b> у розумінні ст. 641 Цивільного кодексу України. Ціни з позначкою «від» — орієнтир для типового проєкту.",
                "Остаточні обсяг робіт, вартість і строки визначаються в договорі, який укладається з кожним клієнтом окремо після брифу."]),
            ("Концептуальні роботи", [
                "У розділі «Концепти» представлено концептуальні роботи студії. Бренди BUDMIST, KAVA LAB, DENTALIA, FLOWDESK, їхні товари, ціни, відгуки, лікарі та інші дані є вигаданими й не належать реальним компаніям чи людям. Форми в концептах нічого не надсилають і нічого не продають."]),
            ("Інтелектуальна власність", [
                "Дизайн, тексти, логотип ADV, код сайту та концептів належать ADV або використовуються на законних підставах. Копіювання, відтворення чи використання матеріалів у комерційних цілях без письмової згоди ADV заборонено.",
                "Фотографії в концептах використано за безкоштовними ліцензіями Unsplash (unsplash.com/license) та Pexels (pexels.com/license). Права на них належать їхнім авторам."]),
            ("Правила користування", ["Заборонено втручатися в роботу сайту, намагатися отримати несанкціонований доступ, надсилати через форму спам, шкідливий код або завідомо неправдиві дані про інших осіб."]),
            ("Відповідальність", ["Ми докладаємо зусиль, щоб сайт працював стабільно, а інформація була актуальною, проте не гарантуємо безперервну роботу сайту. ADV не відповідає за збитки, спричинені користуванням сайтом, у межах, дозволених законодавством. Посилання на сторонні сайти надаються для зручності — ми не відповідаємо за їхній зміст."]),
            ("Персональні дані", ['Обробка персональних даних описана в <a href="../privacy/">Політиці конфіденційності</a>, а використання cookie — у <a href="../cookies/">Політиці cookie</a>.']),
            ("Застосовне право", ["До цих Умов застосовується законодавство України. Спори вирішуються шляхом переговорів, а в разі недосягнення згоди — у суді за місцезнаходженням власника сайту, якщо інше не передбачено договором чи імперативними нормами права країни споживача."]),
            ("Контакти", [f"Звертайтеся на {m}."]),
        ]
    # ---------------- EN ----------------
    if page == "privacy":
        return [
            ("General", [
                f"This Policy explains how ADV Development Studio (“ADV”, “we”) processes personal data of website visitors and clients. Data controller: {owner}. Data protection contact: {m}.",
                "We process data in accordance with the Law of Ukraine “On Personal Data Protection” No. 2297-VI and, for visitors and clients in the European Union, the General Data Protection Regulation (EU) 2016/679 (GDPR)."]),
            ("Data we collect", [
                "<ul><li><b>Request form:</b> name, contact details (phone, Telegram or email), estimated budget, project description.</li>"
                "<li><b>Correspondence:</b> the content of messages you send us by email, messengers or social media.</li>"
                "<li><b>Contract data:</b> details needed to sign and perform a contract and issue invoices.</li>"
                "<li><b>Technical data:</b> IP address, browser and device type, request time — logged by our hosting provider and by font and library providers when pages load.</li></ul>",
                "We do not collect special categories of data (health, religious beliefs, etc.) and ask you not to submit them through the form."]),
            ("Purposes and legal bases", [
                "<ul><li>To respond to your request and prepare a proposal — <b>consent</b> and <b>pre-contractual steps</b> (GDPR Art. 6(1)(a), (b)).</li>"
                "<li>To sign and perform a contract, keep accounts and reporting — <b>contract</b> and <b>legal obligations</b> (Art. 6(1)(b), (c)).</li>"
                "<li>To keep the website working and secure — <b>legitimate interest</b> (Art. 6(1)(f)).</li></ul>",
                "We do not send marketing emails without separate consent and we never sell your data."]),
            ("Retention", [
                "<ul><li>Requests that did not lead to a contract — up to 12 months after the last contact.</li>"
                "<li>Contract data — for the term of the contract and 3 years after it ends (limitation period); accounting records — as long as the law requires.</li>"
                "<li>Technical logs — per the hosting provider’s settings, usually up to 30 days.</li></ul>"]),
            ("Who receives data", [
                "Data may be received only by providers we need to run the studio, and only to the extent necessary:",
                "<ul><li>our website hosting provider (GitHub Pages);</li><li>Google (Gmail, Google Sheets, Apps Script) — to receive form requests, for correspondence and working files;</li><li>Telegram — for instant team notifications about new requests;</li>"
                "<li>messengers (Viber, WhatsApp) if you chose them for contact;</li>"
                "<li>Google Fonts, jsDelivr, cdnjs — delivery of fonts and libraries (they receive technical request data);</li>"
                "<li>our accountant, bank and tax authorities — as required by law.</li></ul>",
                "Some of these providers may process data outside Ukraine and the EU. In such cases we rely on their standard contractual data protection terms."]),
            ("Your rights", [
                "Under Art. 8 of Law No. 2297-VI and Art. 15–22 GDPR you have the right to:",
                "<ul><li>know what data we process, why, and who receives it;</li><li>get a copy of your data;</li>"
                "<li>have inaccurate data corrected or data erased;</li><li>restrict or object to processing;</li>"
                "<li>withdraw consent at any time (without affecting prior lawful processing);</li><li>receive your data in a portable format.</li></ul>",
                f"To exercise your rights, write to {m}. We reply within 30 days. You may also complain to the Ukrainian Parliament Commissioner for Human Rights (ombudsman.gov.ua) or, in the EU, to your local supervisory authority."]),
            ("Security", ["Access to data is limited to people who need it for work; we use two-factor authentication on work accounts and transmit data only over secure channels (HTTPS, TLS)."]),
            ("Children", ["ADV’s website and services are intended for businesses and are not directed at people under 16. If you learn that a child has sent us data, let us know and we will delete it."]),
            ("Changes", ["We may update this Policy. The current version is always on this page, with the last update date shown at the top."]),
        ]
    if page == "cookies":
        return [
            ("What cookies are", ["Cookies are small files a website stores in your browser. Similar technologies — localStorage and sessionStorage — store data on your device without sending it to a server."]),
            ("What our website uses today", [
                "<ul><li><b>No advertising or analytics cookies.</b> We do not use Google Analytics, Meta Pixel or similar tracking tools.</li>"
                "<li><b>localStorage in concepts.</b> The KAVA LAB demo concept stores the demo cart in your browser so it survives a reload. This data is never sent anywhere.</li>"
                "<li><b>Third-party resources.</b> Google Fonts and libraries from jsDelivr and cdnjs are loaded from the providers’ servers. They receive technical request data (IP address, browser) but do not set cookies on our domain.</li></ul>"]),
            ("If we add analytics", ["If we start using analytics or advertising tools, we will update this page and show a banner where you can give or refuse consent. Non-essential cookies will not be set without your consent."]),
            ("Managing cookies", ["You can view and delete cookies and site data in your browser settings: Chrome — “Settings → Privacy and security”, Safari — “Settings → Privacy”, Firefox — “Settings → Privacy & Security”. Clearing site data also removes the demo cart in the concepts."]),
            ("Contact", [f"Send questions about cookies to {m}."]),
        ]
    return [
        ("General", [f"These Terms govern the use of the ADV Development Studio website. Website owner: {owner}. By using the website you agree to these Terms. If you do not agree, please do not use the website."]),
        ("Information on the website", [
            "Information about services, packages, timelines and prices is for reference only and <b>is not a public offer</b>. Prices marked “from” are a guide for a typical project.",
            "The final scope, price and timeline are set in a contract signed with each client individually after the brief."]),
        ("Concept work", ["The “Concepts” section shows the studio’s concept work. The brands BUDMIST, KAVA LAB, DENTALIA and FLOWDESK, their products, prices, reviews, doctors and other details are fictional and do not belong to real companies or people. Forms in the concepts send nothing and sell nothing."]),
        ("Intellectual property", [
            "The design, copy, ADV logo and the code of the website and concepts belong to ADV or are used lawfully. Copying, reproducing or using these materials commercially without ADV’s written consent is prohibited.",
            "Photos in the concepts are used under the free Unsplash (unsplash.com/license) and Pexels (pexels.com/license) licenses; the rights belong to their authors."]),
        ("Acceptable use", ["You may not interfere with the website, attempt unauthorised access, or submit spam, malicious code or knowingly false data about other people through the form."]),
        ("Liability", ["We work to keep the website available and the information up to date but do not guarantee uninterrupted operation. To the extent permitted by law, ADV is not liable for losses arising from use of the website. Links to third-party sites are provided for convenience; we are not responsible for their content."]),
        ("Personal data", ['Processing of personal data is described in the <a href="../privacy/">Privacy policy</a>, and the use of cookies in the <a href="../cookies/">Cookie policy</a>.']),
        ("Governing law", ["These Terms are governed by the laws of Ukraine. Disputes are resolved by negotiation and, failing that, by the courts at the owner’s location, unless a contract or mandatory consumer law of your country provides otherwise."]),
        ("Contact", [f"Write to us at {m}."]),
    ]


CSS = """
.legal{max-width:880px;margin:0 auto;padding:130px var(--pad) 40px}
.legal__crumbs{font-size:12px;color:var(--muted);margin-bottom:26px}
.legal__crumbs a{color:var(--accent-2)}.legal__crumbs a:hover{color:var(--lime)}
.legal h1{font-size:clamp(32px,5vw,64px);margin-bottom:14px}
.legal__meta{color:var(--muted);font-size:13px;margin-bottom:34px}
.legal__toc{border:1px solid var(--line);padding:20px 24px;margin-bottom:44px;background:var(--bg-2)}
.legal__toc b{display:block;font-family:var(--head);font-size:12px;text-transform:uppercase;letter-spacing:.06em;margin-bottom:10px;color:var(--accent)}
.legal__toc ol{margin-left:20px;display:grid;gap:4px;font-size:14px}
.legal__toc a{color:var(--text)}.legal__toc a:hover{color:var(--lime)}
.legal section{padding:26px 0;border-top:1px solid var(--line);scroll-margin-top:90px}
.legal h2{font-family:var(--head);font-size:clamp(18px,2vw,24px);text-transform:uppercase;margin-bottom:14px}
.legal h2 span{color:var(--accent);margin-right:10px}
.legal p,.legal li{font-size:15px;line-height:1.7;color:#e3d7c3}
.legal p+p,.legal p+ul,.legal ul+p{margin-top:12px}
.legal ul{margin-left:20px;display:grid;gap:6px}
.legal a{color:var(--accent-2);text-decoration:underline;text-underline-offset:3px}
.legal a:hover{color:var(--lime)}
.legal__fill{background:rgba(244,207,59,.14);color:var(--lime);padding:0 4px}
.legal__other{margin-top:40px;display:flex;flex-wrap:wrap;gap:10px}
.legal__other a{text-decoration:none;border:1px solid var(--line);padding:9px 14px;border-radius:30px;font-size:13px;color:var(--text)}
.legal__other a:hover{border-color:var(--accent);color:var(--accent)}
.legal-top{position:fixed;top:0;left:0;right:0;z-index:50;display:flex;justify-content:space-between;align-items:center;padding:14px var(--pad);background:rgba(15,11,8,.88);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
.legal-top .logo .logo-svg{height:20px}
.legal-top__r{display:flex;align-items:center;gap:14px;font-size:12px}
.legal-top__r a.home{color:var(--accent)}.legal-top__r a.home:hover{color:var(--lime)}
.nf{min-height:100vh;display:grid;place-items:center;text-align:center;padding:120px var(--pad) 60px}
.nf__code{font-family:var(--head);font-weight:800;font-size:clamp(110px,24vw,280px);line-height:.9;color:transparent;-webkit-text-stroke:2px var(--accent)}
.nf h1{font-size:clamp(24px,3.4vw,44px);margin:16px 0 12px}
.nf p{color:var(--muted);max-width:520px;margin:0 auto 26px}
.nf__owl{width:min(56vw,240px);margin:0 auto -10px;filter:drop-shadow(0 18px 30px rgba(0,0,0,.55))}
"""


def render_all(root, ctx):
    """ctx: LOGO, EMAIL, DOMAIN, VERSION, T (головні тексти), COORDS"""
    LOGO, E, DOMAIN, V, T = ctx["LOGO"], ctx["EMAIL"], ctx["DOMAIN"], ctx["VERSION"], ctx["T"]
    written = []

    def head(lang, base, title, desc, path, extra_alt=True, noindex=False):
        alts = (f'<link rel="alternate" hreflang="uk" href="{DOMAIN}{path["uk"]}">\n<link rel="alternate" hreflang="en" href="{DOMAIN}{path["en"]}">\n') if extra_alt else ""
        return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — ADV Development Studio</title>
<meta name="description" content="{desc}">
{'<meta name="robots" content="noindex">' if noindex else ''}
<link rel="canonical" href="{DOMAIN}{path[lang]}">
{alts}<meta name="theme-color" content="#0f0b08">
<link rel="icon" type="image/svg+xml" href="{base}assets/img/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fira+Mono:wght@400;500;700&family=Unbounded:wght@700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{base}assets/css/style.css?v={V}">
<style>{CSS}</style>
</head>
<body>"""

    def top(lang, base, other_href):
        t = TXT[lang]
        ua_cls, en_cls = ("on", "") if lang == "uk" else ("", "on")
        ua_href, en_href = ("./", other_href) if lang == "uk" else (other_href, "./")
        home = f"{base}" if lang == "uk" else f"{base}en/"
        return f"""<header class="legal-top">
  <a href="{home}" class="logo" aria-label="ADV">{LOGO("lg-legal")}</a>
  <div class="legal-top__r"><nav class="lang" aria-label="Language"><a href="{ua_href}" class="{ua_cls}" hreflang="uk">UA</a><a href="{en_href}" class="{en_cls}" hreflang="en">EN</a></nav><a class="home" href="{home}">← {t['home']}</a></div>
</header>"""

    def foot(lang, base):
        L = T[lang]; pre = "" if lang == "uk" else "en/"
        links = " · ".join(f'<a href="{base}{pre}{p}/">{x}</a>' for p, x in zip(PAGES, L["f_legal"]))
        return f"""<footer class="footer" style="padding-top:40px">
  <div class="footer__bottom" style="margin-top:0"><span>{links}</span><span><a href="mailto:{E}">{E}</a></span><span>{L['f_copy']}</span></div>
</footer>
</body>
</html>"""

    for lang in ("uk", "en"):
        t = TXT[lang]
        for pg in PAGES:
            rel = f"{pg}/index.html" if lang == "uk" else f"en/{pg}/index.html"
            base = "../" if lang == "uk" else "../../"
            other = f"../en/{pg}/" if lang == "uk" else f"../../{pg}/"
            path = {"uk": f"/{pg}/", "en": f"/en/{pg}/"}
            owner = f'<span class="legal__fill">{OWNER[lang]}</span>'
            secs = body(lang, pg, E, owner)
            toc = "".join(f'<li><a href="#s{i+1}">{h}</a></li>' for i, (h, _) in enumerate(secs))
            html_secs = "".join(
                f'<section id="s{i+1}"><h2><span>{i+1:02d}</span>{h}</h2>' + "".join(x if x.startswith("<ul") else f"<p>{x}</p>" for x in paras) + "</section>"
                for i, (h, paras) in enumerate(secs))
            others = "".join(f'<a href="../{p}/">{t["titles"][p]}</a>' for p in PAGES if p != pg)
            sw = ("./", f"../en/{pg}/") if lang == "uk" else (f"../../{pg}/", "./")
            content = (f"""<div class="legal">
  <div class="legal__crumbs"><a href="{base if lang == 'uk' else base + 'en/'}">ADV</a> / {t['titles'][pg]}</div>
  <h1 class="h">{t['titles'][pg]}</h1>
  <div class="legal__meta">{t['updated']}: {UPDATED[lang]}</div>
  <nav class="legal__toc"><b>{t['contents']}</b><ol>{toc}</ol></nav>
  {html_secs}
  <section><h2>{t['contact']}</h2><p><a href="mailto:{E}">{E}</a></p></section>
  <div class="legal__other"><span class="mono-s" style="align-self:center;margin-right:6px">{t['other']}:</span>{others}</div>
</div>""")
            html = ctx["SUBPAGE"](T[lang], base, pg + "/", sw, t["titles"][pg], t["desc"][pg], path, content, extra_head=f"<style>{CSS}</style>\n")
            p = os.path.join(root, rel); os.makedirs(os.path.dirname(p), exist_ok=True)
            open(p, "w", encoding="utf-8").write(html); written.append(rel)

    # 404 (bilingual, absolute paths from the site root — works at any URL depth)
    from urllib.parse import urlparse
    R = urlparse(DOMAIN).path.rstrip("/") + "/"
    uk, en = TXT["uk"], TXT["en"]
    nf = (head("uk", R, uk["404_t"], uk["404_p"], {"uk": "/404.html", "en": "/404.html"}, extra_alt=False, noindex=True) +
          f"""<header class="legal-top"><a href="{R}" class="logo" aria-label="ADV">{LOGO("lg-404")}</a><div class="legal-top__r"><a class="home" href="{R}en/">EN</a></div></header>
<main class="nf"><div>
  <img class="nf__owl" src="{R}assets/img/owl-spin-0.webp" alt="" width="360" height="360">
  <div class="nf__code">404</div>
  <h1 class="h">{uk['404_t']}</h1><p>{uk['404_p']}</p>
  <p style="margin-top:-14px;font-size:13px">{en['404_t']}. {en['404_p']}</p>
  <div style="display:flex;gap:10px;justify-content:center;flex-wrap:wrap"><a class="btn" href="{R}">{uk['404_b']}</a><a class="btn btn--ghost" href="{R}en/">{en['404_b']}</a></div>
  <p style="margin-top:22px"><a href="mailto:{E}" style="color:var(--accent-2)">{E}</a></p>
</div></main>
</body>
</html>""")
    open(os.path.join(root, "404.html"), "w", encoding="utf-8").write(nf); written.append("404.html")

    # sitemap + robots
    urls = ["/", "/en/", "/price/", "/en/price/", "/projects/", "/en/projects/"] + [f"/{p}/" for p in PAGES] + [f"/en/{p}/" for p in PAGES]
    for s in ("budmist", "kava-lab", "dentalia", "flowdesk"):
        urls += [f"/concepts/{s}/", f"/concepts/{s}/en/"]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + \
         "".join(f"  <url><loc>{DOMAIN}{u}</loc><lastmod>2026-11-11</lastmod></url>\n" for u in urls) + "</urlset>\n"
    open(os.path.join(root, "sitemap.xml"), "w", encoding="utf-8").write(sm); written.append("sitemap.xml")
    robots = f"User-agent: *\nAllow: /\nDisallow: /_build/\n\nSitemap: {DOMAIN}/sitemap.xml\n"
    open(os.path.join(root, "robots.txt"), "w", encoding="utf-8").write(robots); written.append("robots.txt")
    return written
