"""Генератор сайту ADV (UA + EN).

Увесь текст сайту — у словнику T нижче. Після змін запустіть:
    python3 _build/build.py
Скрипт перезапише index.html (UA) та en/index.html (EN).
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMAIN = "https://advstudio.github.io/advStudio"  # коли підключите власний домен — замініть, напр. "https://advstudio.com"
EMAIL = "adv.development.studio@gmail.com"
VERSION = "27"

# Маскот: "owl" — 3D-скан фігурки сови (assets/models/owl-figure.glb, див. _build/optimize_owl.py)
#          "lowpoly" — згенерована геометрична сова (_build/owl.py)
MASCOT = "owl"
M = {
    "owl": dict(hero="owl-figure", tabs=("owl-figure", "owl-figure", "owl-figure"), orbit="0deg 84deg 108%", exp="0.88",
                style="", fallback="logo-badge.svg"),
    "lowpoly": dict(hero="owl", tabs=("owl-business", "owl-landing", "owl-ecom"), orbit="-20deg 80deg 105%", exp="0.8",
                    style="", fallback="logo-badge.svg"),
}[MASCOT]  # збільшуйте після змін CSS/JS, щоб скинути кеш браузера

T = {
# =====================================================================
"uk": {
  "lang": "uk", "locale": "uk_UA", "base": "", "path": "/",
  "title": "ADV — Web Development Studio. Сайти для бізнесу під ключ",
  "desc": "ADV — вебстудія зі Львова. Розробляємо корпоративні сайти, лендінги та інтернет-магазини під ключ, готові до реклами, аналітики та конверсій. Працюємо по всій Україні, у Польщі та Німеччині.",
  "loading": "// ADV LOADING...",
  "menu": "МЕНЮ", "close": "ЗАКРИТИ ×",
  "nav": [("#services", "Послуги"), ("price/", "Прайс"), ("projects/", "Проєкти"), ("#work", "Концепти"), ("#team", "Команда"), ("#contact", "Контакти")],
  "m_mail": "Загальні питання", "m_office": "Офіс", "office": "Львів, Україна", "m_social": "Соцмережі", "m_cta": "Обговорити проєкт",
  "hero_tag": "DEVELOPMENT STUDIO",
  "hero_pitch_b": "Сайти, які працюють на ваш бізнес",
  "hero_pitch": "Розробка під ключ: структура, дизайн, код, аналітика та запуск.",
  "scroll": "ГОРТАЙ ВНИЗ ↓",
  "intro": [
    "Створюємо сайти для бізнесу під ключ — від структури й дизайну до запуску та підтримки.",
    "Знаємо медіабаїнг зсередини, тому робимо сайти, готові до реклами, аналітики та конверсій.",
    "Працюємо з клієнтами з усієї України. Далі — Польща та Німеччина.",
  ],
  "lead_badge": "ADV // WEB STUDIO",
  "lead_title": "Не просто<br>код, а <span class=\"acc\">сайт,<br>що продає</span>",
  "lead_num": "3", "lead_num_s": "напрями",
  "lead_sub": "BUSINESS · LANDING · E-COMMERCE",
  "why_h": "Чому<br><span class=\"acc\">ADV</span>",
  "why_lines": [
    "Ми знаємо не лише, як написати сайт, а й як зробити його зручним для маркетингу, реклами та подальшого розвитку.",
    "Кожне рішення в дизайні й коді перевіряємо питанням: чи допоможе це отримати більше заявок?",
  ],
  "why": [
    ("stat-ftd", "Фокус на конверсіях", "Структура, тексти й форми, що перетворюють відвідувачів на заявки.", True),
    ("stat-traffic", "Готові до реклами", "Пікселі, UTM, події та швидкі сторінки для Google, Meta й TikTok.", False),
    ("stat-projects", "Під ключ", "Від брифу й дизайну до запуску, хостингу та підтримки.", False),
    ("stat-offices", "Ніші, які знаємо", "Будівництво, медицина, e-commerce, HoReCa, SaaS, послуги.", False),
    ("stat-partnerships", "Прозора співпраця", "Договір, етапи, щотижневі звіти й гарантія.", False),
    ("stat-employees", "Одна команда", "PM, дизайнер, розробники, маркетолог і QA.", False),
    ("stat-geo", "UA · PL · DE", "Уся Україна, далі — Польща та Німеччина.", False),
  ],
  "marquee": ["Business websites", "Landing pages", "E-commerce", "Редизайн", "SEO-технічна підготовка", "CRM", "Аналітика", "Швидкість", "Підтримка"],
  "aud_h": "З ким ми<br><span class=\"acc\">працюємо</span>",
  "aud_p": "Від локальних сервісів до інтернет-магазинів і стартапів — підбираємо рішення під задачі, бюджет і етап розвитку вашого бізнесу.",
  "aud": [
    ("Малий і середній бізнес", "Сайти компаній і послуг, що презентують бізнес та збирають заявки.", "BUSINESS"),
    ("Інтернет-магазини", "Каталоги, кошик, оплати й доставка з інтеграціями в CRM.", "E-COMMERCE"),
    ("Локальні компанії та сервіси", "Клініки, салони, ремонт, освіта — сайти під локальний пошук і рекламу.", "LOCAL"),
    ("Стартапи", "Лендінги для запуску продукту, тесту гіпотез і збору waitlist.", "LAUNCH"),
    ("Маркетингові агенції", "White-label розробка для ваших клієнтів під NDA.", "WHITE-LABEL"),
    ("Медіабаїнг-команди", "Ленди, преленди та PWA, якщо є відповідні замовлення.", "MEDIA BUYING"),
  ],
  "niche_tag": "ГАЛУЗЕВІ РІШЕННЯ",
  "niche_h": "Знаємо специфіку<br><span class=\"lime\">вашої ніші</span>",
  "niche_p": "Кожна галузь має свої сценарії: де клієнт шукає, що порівнює і що його переконує залишити заявку. Ми закладаємо це в структуру сайту з першого дня.",
  "niche_cta": "Обговорити проєкт",
  "niches": [
    ("build", "Будівництво", "stat-offices", "Сайти для будівельних компаній", "Презентуємо об’єкти так, щоб клієнт залишив заявку ще до візиту у відділ продажів.",
     ["Каталог ЖК і квартир з плануваннями", "Калькулятор вартості та розстрочки", "Хід будівництва з фото- і відеозвітами", "Заявки в CRM і Telegram відділу продажів"], "budmist"),
    ("med", "Медицина", "stat-employees", "Сайти для клінік і медичних центрів", "Довіра, зрозумілі ціни й онлайн-запис без дзвінків.",
     ["Послуги з прайсом і сторінки лікарів", "Онлайн-запис із вибором лікаря та часу", "Локальне SEO та Google Maps", "Інтеграція з МІС і CRM клініки"], "dentalia"),
    ("ecom", "E-commerce", "stat-ftd", "Інтернет-магазини та D2C-бренди", "Зручний каталог і швидке оформлення, які підвищують конверсію та середній чек.",
     ["Фільтри, кошик, підписки", "Оплати LiqPay, Monobank, Stripe", "Нова Пошта, Укрпошта, InPost", "E-commerce аналітика в GA4"], "kava-lab"),
    ("saas", "Стартапи і SaaS", "stat-projects", "Лендінги для продуктів і стартапів", "Пояснюємо продукт за 5 секунд і збираємо перших користувачів.",
     ["Оффер, демо та тарифи", "Waitlist і онбординг", "A/B-тести гіпотез", "Мультимовність для виходу за кордон"], "flowdesk"),
    ("horeca", "HoReCa", "stat-partnerships", "Сайти для ресторанів, кафе і готелів", "Меню, бронювання та доставка — усе, що потрібно гостю, з телефону.",
     ["Онлайн-меню з фото і QR-кодом", "Бронювання столиків і номерів", "Замовлення доставки та самовивозу", "Відгуки та інтеграція з Google Maps"], None),
    ("services", "Послуги та освіта", "stat-traffic", "Сайти для сервісів, шкіл і експертів", "Для салонів краси, автосервісів, юристів, курсів і тренерів.",
     ["Каталог послуг із цінами", "Онлайн-запис або оплата курсу", "Кейси, відгуки, сертифікати", "Лендінги під рекламні кампанії"], None),
  ],
  "svc_h": "Послуги",
  "tabs": [
    ("business", "owl-business", "#d9973a", "Business websites", "Корпоративні сайти, сайти компаній і послуг", [
      "Презентують компанію, послуги та кейси й збирають заявки від клієнтів.",
      "Індивідуальний дизайн, CMS для самостійного редагування, SEO-технічна основа.",
      "Для МСБ, локальних сервісів, будівельних і виробничих компаній."], "від 70 000 ₴"),
    ("landing", "owl-landing", "#f4cf3b", "Landing pages", "Сторінки для реклами, запуску продуктів і збору заявок", [
      "Сфокусована структура під одну дію: заявку, дзвінок чи покупку.",
      "Готові до реклами: пікселі, UTM, події, швидке завантаження.",
      "Для запусків, рекламних кампаній, стартапів і медіабаїнг-команд."], "від 28 000 ₴"),
    ("ecom", "owl-ecom", "#c9828a", "E-commerce", "Інтернет-магазини", [
      "Каталог, фільтри, кошик і зручне оформлення замовлення.",
      "Оплати LiqPay, Monobank, WayForPay, Stripe; доставка Нова Пошта, Укрпошта, InPost.",
      "Інтеграції з CRM, складським обліком і маркетплейсами."], "індивідуальна оцінка"),
  ],
  "pk_h": "Пакети<br><span class=\"acc\">послуг</span>",
  "pk_p": "Три зрозумілі пакети, щоб ви одразу бачили, що купуєте. Точну вартість рахуємо після брифу — за реальними трудовитратами.",
  "pk_rows": ["Сторінки", "Адаптивність", "Дизайн", "CMS", "Форми та інтеграції", "SEO-технічна база", "Раунди правок", "Строки", "Гарантія"],
  "pk_badge": "Найпопулярніший",
  "pk": [
    ("Start", "Лендінг або невеликий сайт послуг", "від 28 000 ₴", "≈ 45–60 год роботи команди",
     ["1–5 сторінок", "Mobile / tablet / desktop", "На основі нашої дизайн-системи, адаптований під ваш бренд", "За потреби (WordPress / Webflow)", "Форма заявки → Telegram / email, GA4, Meta Pixel", "Мета-теги, sitemap, robots, швидкість 90+", "2 раунди", "2–3 тижні", "1 місяць"], False),
    ("Business", "Багатосторінковий корпоративний сайт", "від 70 000 ₴", "≈ 110–170 год роботи команди",
     ["6–15 сторінок", "Mobile / tablet / desktop", "Індивідуальний дизайн + UX-прототип", "WordPress або headless CMS — редагуєте самі", "CRM (KeyCRM, Bitrix24, HubSpot), GA4 + GTM, пікселі", "Структура, мікророзмітка, 301-редиректи, швидкість", "3 раунди", "4–7 тижнів", "3 місяці"], True),
    ("Custom", "Складні сайти, каталоги, інтеграції, нестандартний функціонал", "індивідуально", "оцінка за трудовитратами",
     ["15+ сторінок, каталоги, особистий кабінет", "Mobile / tablet / desktop", "Індивідуальний дизайн, UX-дослідження", "CMS або кастомна адмінка", "ERP, оплати, доставка, API, маркетплейси", "Розширена SEO-тех + міграція без втрати позицій", "За погодженим ТЗ", "Від 8 тижнів, за оцінкою", "6 місяців"], False),
  ],
  "pk_btn": "Обрати пакет",
  "calc_h": "Як ми рахуємо вартість",
  "calc": [("Декомпозиція", "Розбиваємо проєкт на задачі й етапи."), ("Трудовитрати", "Години кожного спеціаліста × його ставка."), ("Резерв 15–20%", "На комунікацію, тестування та непередбачені зміни."), ("Фіксуємо", "Ціну, строки й обсяг — у договорі.")],
  "calc_note": "Ціни «від» — орієнтир для типового проєкту. Ми не робимо сайти «за $100»: рахуємо мінімальну рентабельну вартість години й закладаємо час на якість.",
  "ex_h": "Додатково",
  "ex": [
    ("REDESIGN", "Редизайн наявних сайтів", "Оновлюємо дизайн і структуру без втрати SEO-позицій і контенту.", "від 20 000 ₴"),
    ("SUPPORT", "Технічна підтримка", "Оновлення, резервні копії, моніторинг і дрібні доопрацювання.", "від 4 000 ₴/міс"),
    ("SPEED", "Оптимізація швидкості", "Core Web Vitals, зображення, кешування — PageSpeed 90+.", "від 8 000 ₴"),
    ("SEO-TECH", "SEO-технічна підготовка", "Структура, мета-теги, мікророзмітка, sitemap, редиректи, індексація.", "від 7 000 ₴"),
    ("INTEGRATIONS", "Інтеграції", "CRM, аналітика (GA4, GTM, пікселі, CAPI), форми заявок, Telegram.", "від 5 000 ₴"),
    ("MEDIA BUYING", "Для медіабаїнг-команд", "Ленди, преленди та PWA з інтеграцією трекерів — якщо є відповідні замовлення.", "за запитом"),
  ],
  "pf_h": "Концепти<br><span class=\"acc\">робіт</span>",
  "pf_p": "Студія на старті, тому чесно показуємо концептуальні роботи, а не вигадані клієнтські кейси. Вони демонструють наш підхід до дизайну, структури та конверсій у різних нішах.",
  "pf_tag": "Концепт", "pf_view": "Переглянути концепт", "v_open": "Відкрити в новій вкладці ↗", "v_close": "Закрити", "v_desktop": "Десктоп", "v_mobile": "Мобільний",
  "pf": [
    ("BUDMIST", "budmist.ua", "#b6ff3b", "#0f1210", "#e8f0dc", "concepts/budmist/img/hero-tower", "Сайт будівельної компанії", "Каталог ЖК, калькулятор кошторису, хід будівництва, заявки в CRM.", ["Business website", "WordPress", "CRM"], "Будуємо дім, у який хочеться повертатися", "Обрати квартиру"),
    ("KAVA LAB", "kavalab.com.ua", "#d9a066", "#1a1410", "#f3e7da", "concepts/kava-lab/img/pour-3", "Інтернет-магазин кави", "Каталог з фільтрами, підписка, оплата Monobank, доставка Нова Пошта.", ["E-commerce", "Оплати", "Доставка"], "Свіжообсмажена кава щотижня", "До каталогу"),
    ("DENTALIA", "dentalia.lviv.ua", "#5ec8ff", "#0d1419", "#e2f1fb", "concepts/dentalia/img/smile-hero", "Сайт стоматологічної клініки", "Послуги з цінами, лікарі, онлайн-запис і локальне SEO.", ["Business website", "Онлайн-запис", "Local SEO"], "Усмішка без страху і болю", "Записатися"),
    ("FLOWDESK", "flowdesk.app", "#8b3dff", "#100d18", "#ece6fb", "concepts/flowdesk/img/team-2", "Лендінг SaaS-стартапу", "Запуск продукту: оффер, демо, тарифи та збір waitlist з A/B-тестами.", ["Landing page", "A/B-тести", "Analytics"], "CRM, яку команда справді відкриває", "Спробувати безкоштовно"),
  ],
  "team_h": "Хто працює<br><span class=\"acc\">над проєктом</span>",
  "team_lines": ["Невелика команда, де кожен відповідає за свою частину — без посередників і втраченої інформації.", "Ви спілкуєтеся з одним менеджером і бачите прогрес щотижня."],
  "team": [
    ("Project Manager", "Ваш єдиний контакт. Веде проєкт від брифу до запуску, контролює строки й бюджет.", ["Бриф і ТЗ", "План і дедлайни", "Щотижневі звіти", "Приймання робіт"]),
    ("UI/UX Designer", "Проєктує структуру та інтерфейс, який веде відвідувача до заявки.", ["Прототип", "Дизайн-система", "Адаптив", "UI-кит"]),
    ("Frontend Developer", "Перетворює дизайн на швидкий адаптивний сайт.", ["Верстка", "Анімації", "PageSpeed 90+", "Кросбраузерність"]),
    ("Backend / CMS Developer", "Налаштовує CMS, каталоги, оплати й інтеграції.", ["WordPress / headless CMS", "Каталоги й фільтри", "Оплати й доставка", "API та CRM"]),
    ("Marketing & Analytics", "Наша експертиза з медіабаїнгу: готуємо сайт до реклами та вимірювання результатів.", ["GA4 / GTM", "Meta Pixel / CAPI", "Цілі й воронки", "A/B-тести"]),
    ("QA Engineer", "Тестує сайт на пристроях і в браузерах до запуску.", ["Функціональні тести", "Мобільні пристрої", "Форми й інтеграції", "Чек-лист запуску"]),
  ],
  "process": [("Бриф", "Цілі, аудиторія, конкуренти, бюджет"), ("Прототип", "Структура, UX, оцінка в годинах"), ("Дизайн", "Унікальний дизайн під ваш бренд"), ("Розробка", "Код, CMS, інтеграції, тестування"), ("Запуск", "Аналітика, навчання, гарантія")],
  "geo_h": "Україна<br><span class=\"acc\">і далі</span>",
  "geo_p": "Базуємося у Львові, але не обмежуємося одним містом: працюємо віддалено з клієнтами з усієї України та готуємося до виходу на ринки ЄС. Англійська версія сайту — для міжнародних клієнтів.",
  "geo": [("01", "Україна", "зараз", True), ("02", "Польща", "наступний крок", False), ("03", "Німеччина", "наступний крок", False), ("04", "Інші ринки ЄС", "у планах", False)],
  "faq_h": "Часті<br><span class=\"acc\">питання</span>",
  "faq": [
    ("Скільки коштує сайт?", "Залежить від обсягу. Орієнтири — у пакетах вище, а точну вартість ми рахуємо після брифу за трудовитратами кожного спеціаліста плюс 15–20% резерву. Ціну й строки фіксуємо в договорі."),
    ("Скільки триває розробка?", "Лендінг — 2–3 тижні, корпоративний сайт — 4–7 тижнів, складні проєкти — від 8 тижнів. Графік з етапами ви отримуєте до старту."),
    ("Чи зможу я сам редагувати сайт?", "Так. У пакетах Business і Custom ми налаштовуємо CMS і проводимо навчання, щоб ви могли змінювати тексти, фото, ціни та новини без розробника."),
    ("Ви працюєте з клієнтами з інших міст і країн?", "Так. Працюємо віддалено з усією Україною, а також з клієнтами з Польщі та Німеччини. Комунікація — українською, англійською або польською."),
    ("Що відбувається після запуску?", "Діє гарантійний період: виправляємо помилки безкоштовно. Далі можна підключити технічну підтримку, оптимізацію та розвиток сайту."),
    ("Чи показуєте ви реальні кейси?", "Студія на старті, тому на сайті — концептуальні роботи, чесно позначені як концепти. На зустрічі покажемо прототипи й пояснимо, як будуємо процес."),
  ],
  "c_h": "Обговорімо<br><span class=\"acc\">ваш проєкт</span>",
  "c_p": "Розкажіть коротко про задачу — менеджер відповість протягом робочого дня й запропонує формат і орієнтовну оцінку.",
  "c_topics": [("business", "Business website"), ("landing", "Landing page"), ("ecom", "E-commerce"), ("redesign", "Редизайн / підтримка"), ("other", "Інше")],
  "c_name": "Ім’я", "c_contact": "Telegram, телефон або email", "c_ph": "@username / +380", "c_budget": "Орієнтовний бюджет",
  "c_budgets": ["Ще не знаю", "до 30 000 ₴", "30 000 – 80 000 ₴", "80 000 – 200 000 ₴", "200 000 ₴ +"],
  "c_msg": "Коротко про задачу", "c_send": "Надіслати заявку", "c_consent": 'Надсилаючи заявку, ви погоджуєтеся з <a href="privacy/">Політикою конфіденційності</a>.', "c_ok": "✓ Дякуємо! Ми зв’яжемося з вами найближчим часом.",
  "f_big": "<span>ADV —</span><br>сайти, які працюють на ваш бізнес.",
  "f_mail": "Загальні питання:", "f_office": "Офіс:", "f_social": "Ми в соцмережах:", "f_cta": "Обговорити<br>проєкт",
  "f_legal": ["Політика конфіденційності", "Політика cookie", "Умови використання"],
  "f_copy": "© ADV™ 2026. Усі права захищено",
  "cta_more": "Обговорити проєкт →", "cta_pk": "Переглянути пакети",
},
# =====================================================================
"en": {
  "lang": "en", "locale": "en_US", "base": "../", "path": "/en/",
  "title": "ADV — Web Development Studio. Turnkey websites for business",
  "desc": "ADV is a web development studio from Lviv, Ukraine. We build business websites, landing pages and e-commerce stores that are ready for advertising, analytics and conversions. Working with clients in Ukraine, Poland, Germany and beyond.",
  "loading": "// ADV LOADING...",
  "menu": "MENU", "close": "CLOSE ×",
  "nav": [("#services", "Services"), ("price/", "Pricing"), ("projects/", "Projects"), ("#work", "Concepts"), ("#team", "Team"), ("#contact", "Contact")],
  "m_mail": "General enquiries", "m_office": "Office", "office": "Lviv, Ukraine", "m_social": "Social", "m_cta": "Discuss a project",
  "hero_tag": "DEVELOPMENT STUDIO",
  "hero_pitch_b": "Websites that work for your business",
  "hero_pitch": "Turnkey development: structure, design, code, analytics and launch.",
  "scroll": "SCROLL DOWN ↓",
  "intro": [
    "We build turnkey business websites — from structure and design to launch and support.",
    "We know media buying from the inside, so our sites are ready for ads, analytics and conversions.",
    "Working with clients across Ukraine, Poland, Germany and the wider EU.",
  ],
  "lead_badge": "ADV // WEB STUDIO",
  "lead_title": "Not just<br>code — <span class=\"acc\">a site<br>that sells</span>",
  "lead_num": "3", "lead_num_s": "services",
  "lead_sub": "BUSINESS · LANDING · E-COMMERCE",
  "why_h": "Why<br><span class=\"acc\">ADV</span>",
  "why_lines": [
    "We know not only how to build a website, but how to make it work for marketing, advertising and future growth.",
    "Every design and code decision is tested against one question: will it bring more leads?",
  ],
  "why": [
    ("stat-ftd", "Conversion-focused", "Structure, copy and forms that turn visitors into leads.", True),
    ("stat-traffic", "Ad-ready", "Pixels, UTMs, events and fast pages for Google, Meta and TikTok.", False),
    ("stat-projects", "Turnkey", "From brief and design to launch, hosting and support.", False),
    ("stat-offices", "Industries we know", "Construction, healthcare, e-commerce, hospitality, SaaS, services.", False),
    ("stat-partnerships", "Transparent process", "Contract, milestones, weekly reports and warranty.", False),
    ("stat-employees", "One team", "PM, designer, developers, marketer and QA.", False),
    ("stat-geo", "UA · PL · DE", "Ukraine, Poland, Germany and the EU.", False),
  ],
  "marquee": ["Business websites", "Landing pages", "E-commerce", "Redesign", "Technical SEO", "CRM", "Analytics", "Speed", "Support"],
  "aud_h": "Who we<br><span class=\"acc\">work with</span>",
  "aud_p": "From local services to online stores and startups — we tailor the solution to your goals, budget and stage of growth.",
  "aud": [
    ("Small & medium businesses", "Company and service websites that present your business and capture leads.", "BUSINESS"),
    ("Online stores", "Catalogues, cart, payments and shipping with CRM integrations.", "E-COMMERCE"),
    ("Local companies & services", "Clinics, salons, repairs, education — built for local search and ads.", "LOCAL"),
    ("Startups", "Landing pages for product launches, hypothesis tests and waitlists.", "LAUNCH"),
    ("Marketing agencies", "White-label development for your clients under NDA.", "WHITE-LABEL"),
    ("Media buying teams", "Landers, pre-landers and PWAs when the project fits.", "MEDIA BUYING"),
  ],
  "niche_tag": "INDUSTRY SOLUTIONS",
  "niche_h": "We know<br><span class=\"lime\">your industry</span>",
  "niche_p": "Every industry has its own scenarios: where clients search, what they compare and what convinces them to get in touch. We build that into the site structure from day one.",
  "niche_cta": "Discuss a project",
  "niches": [
    ("build", "Construction", "stat-offices", "Websites for construction companies", "We present projects so that clients enquire before they even visit the sales office.",
     ["Project and apartment catalogue with floor plans", "Price and instalment calculator", "Build progress with photo and video reports", "Leads straight to CRM and messengers"], "budmist"),
    ("med", "Healthcare", "stat-employees", "Websites for clinics and medical centres", "Trust, clear pricing and online booking without phone calls.",
     ["Services with prices and doctor pages", "Online booking by doctor and time", "Local SEO and Google Maps", "Integration with clinic CRM / EMR"], "dentalia"),
    ("ecom", "E-commerce", "stat-ftd", "Online stores and D2C brands", "A convenient catalogue and fast checkout that lift conversion and average order value.",
     ["Filters, cart, subscriptions", "Stripe, PayPal, Przelewy24, LiqPay", "InPost, DHL, Nova Poshta", "E-commerce analytics in GA4"], "kava-lab"),
    ("saas", "Startups & SaaS", "stat-projects", "Landing pages for products and startups", "We explain the product in 5 seconds and bring in your first users.",
     ["Offer, demo and pricing", "Waitlist and onboarding", "A/B tests of hypotheses", "Multilingual for new markets"], "flowdesk"),
    ("horeca", "Hospitality", "stat-partnerships", "Websites for restaurants, cafés and hotels", "Menu, reservations and delivery — everything a guest needs, on their phone.",
     ["Online menu with photos and QR code", "Table and room reservations", "Delivery and pick-up orders", "Reviews and Google Maps integration"], None),
    ("services", "Services & education", "stat-traffic", "Websites for services, schools and experts", "For beauty salons, car services, lawyers, courses and coaches.",
     ["Service catalogue with prices", "Online booking or course payment", "Case studies, reviews, certificates", "Landing pages for ad campaigns"], None),
  ],
  "svc_h": "Services",
  "tabs": [
    ("business", "owl-business", "#d9973a", "Business websites", "Corporate, company and service websites", [
      "Present your company, services and work — and capture client enquiries.",
      "Custom design, a CMS you can edit yourself, a solid technical SEO base.",
      "For SMBs, local services, construction and manufacturing companies."], "from €3,900"),
    ("landing", "owl-landing", "#f4cf3b", "Landing pages", "Pages for ads, product launches and lead capture", [
      "A focused structure built around one action: a lead, a call or a purchase.",
      "Ad-ready: pixels, UTMs, events and fast load times.",
      "For launches, ad campaigns, startups and media buying teams."], "from €1,500"),
    ("ecom", "owl-ecom", "#c9828a", "E-commerce", "Online stores", [
      "Catalogue, filters, cart and a smooth checkout.",
      "Payments via Stripe, PayPal, Przelewy24, LiqPay; shipping via InPost, DHL, Nova Poshta.",
      "Integrations with CRM, inventory and marketplaces."], "custom estimate"),
  ],
  "pk_h": "Service<br><span class=\"acc\">packages</span>",
  "pk_p": "Three clear packages so you know exactly what you are buying. The final price is calculated after the brief, based on real effort.",
  "pk_rows": ["Pages", "Responsive", "Design", "CMS", "Forms & integrations", "Technical SEO", "Revision rounds", "Timeline", "Warranty"],
  "pk_badge": "Most popular",
  "pk": [
    ("Start", "Landing page or a small service website", "from €1,500", "≈ 45–60 team hours",
     ["1–5 pages", "Mobile / tablet / desktop", "Based on our design system, adapted to your brand", "If needed (WordPress / Webflow)", "Lead form → email / Telegram, GA4, Meta Pixel", "Meta tags, sitemap, robots, PageSpeed 90+", "2 rounds", "2–3 weeks", "1 month"], False),
    ("Business", "Multi-page corporate website", "from €3,900", "≈ 110–170 team hours",
     ["6–15 pages", "Mobile / tablet / desktop", "Custom design + UX prototype", "WordPress or headless CMS — edit it yourself", "CRM (HubSpot, Pipedrive, Bitrix24), GA4 + GTM, pixels", "Structure, schema markup, 301 redirects, speed", "3 rounds", "4–7 weeks", "3 months"], True),
    ("Custom", "Complex websites, catalogues, integrations, custom features", "custom", "estimated by effort",
     ["15+ pages, catalogues, client area", "Mobile / tablet / desktop", "Custom design, UX research", "CMS or custom admin panel", "ERP, payments, shipping, APIs, marketplaces", "Advanced technical SEO + safe migration", "As per agreed spec", "From 8 weeks, by estimate", "6 months"], False),
  ],
  "pk_btn": "Choose package",
  "calc_h": "How we price projects",
  "calc": [("Breakdown", "We split the project into tasks and milestones."), ("Effort", "Hours of each specialist × their rate."), ("15–20% buffer", "For communication, testing and unexpected changes."), ("Fixed", "Price, timeline and scope — in the contract.")],
  "calc_note": "“From” prices are a guide for a typical project. We don’t build “$100 websites”: we price from a sustainable hourly rate and budget time for quality.",
  "ex_h": "Also",
  "ex": [
    ("REDESIGN", "Website redesign", "We refresh design and structure without losing SEO rankings or content.", "from €900"),
    ("SUPPORT", "Technical support", "Updates, backups, monitoring and small improvements.", "from €180/mo"),
    ("SPEED", "Speed optimisation", "Core Web Vitals, images, caching — PageSpeed 90+.", "from €400"),
    ("SEO-TECH", "Technical SEO setup", "Structure, meta tags, schema, sitemap, redirects, indexing.", "from €350"),
    ("INTEGRATIONS", "Integrations", "CRM, analytics (GA4, GTM, pixels, CAPI), lead forms, messengers.", "from €250"),
    ("MEDIA BUYING", "For media buying teams", "Landers, pre-landers and PWAs with tracker integration — when the project fits.", "on request"),
  ],
  "pf_h": "Concept<br><span class=\"acc\">work</span>",
  "pf_p": "We are a young studio, so we honestly show concept projects rather than invented client cases. They demonstrate our approach to design, structure and conversion across niches.",
  "pf_tag": "Concept", "pf_view": "View concept", "v_open": "Open in new tab ↗", "v_close": "Close", "v_desktop": "Desktop", "v_mobile": "Mobile",
  "pf": [
    ("BUDMIST", "budmist.ua", "#b6ff3b", "#0f1210", "#e8f0dc", "concepts/budmist/img/hero-tower", "Construction company website", "Project catalogue, estimate calculator, build progress, leads to CRM.", ["Business website", "WordPress", "CRM"], "Homes you want to come back to", "Choose an apartment"),
    ("KAVA LAB", "kavalab.com", "#d9a066", "#1a1410", "#f3e7da", "concepts/kava-lab/img/pour-3", "Coffee online store", "Filterable catalogue, subscriptions, online payments, shipping.", ["E-commerce", "Payments", "Shipping"], "Freshly roasted coffee every week", "Shop now"),
    ("DENTALIA", "dentalia.clinic", "#5ec8ff", "#0d1419", "#e2f1fb", "concepts/dentalia/img/smile-hero", "Dental clinic website", "Services with prices, doctors, online booking and local SEO.", ["Business website", "Booking", "Local SEO"], "A smile without fear or pain", "Book a visit"),
    ("FLOWDESK", "flowdesk.app", "#8b3dff", "#100d18", "#ece6fb", "concepts/flowdesk/img/team-2", "SaaS startup landing page", "Product launch: offer, demo, pricing and waitlist with A/B tests.", ["Landing page", "A/B tests", "Analytics"], "The CRM your team actually opens", "Try it free"),
  ],
  "team_h": "Who works<br><span class=\"acc\">on your project</span>",
  "team_lines": ["A compact team where everyone owns their part — no middlemen, nothing lost in translation.", "You talk to one manager and see progress every week."],
  "team": [
    ("Project Manager", "Your single point of contact. Runs the project from brief to launch, owns timeline and budget.", ["Brief & spec", "Plan & deadlines", "Weekly reports", "Acceptance"]),
    ("UI/UX Designer", "Designs the structure and interface that lead visitors to convert.", ["Prototype", "Design system", "Responsive", "UI kit"]),
    ("Frontend Developer", "Turns the design into a fast, responsive website.", ["Markup", "Animations", "PageSpeed 90+", "Cross-browser"]),
    ("Backend / CMS Developer", "Sets up the CMS, catalogues, payments and integrations.", ["WordPress / headless CMS", "Catalogues & filters", "Payments & shipping", "APIs & CRM"]),
    ("Marketing & Analytics", "Our media buying expertise: we make the site ready for ads and measurement.", ["GA4 / GTM", "Meta Pixel / CAPI", "Goals & funnels", "A/B tests"]),
    ("QA Engineer", "Tests the site across devices and browsers before launch.", ["Functional tests", "Mobile devices", "Forms & integrations", "Launch checklist"]),
  ],
  "process": [("Brief", "Goals, audience, competitors, budget"), ("Prototype", "Structure, UX, effort estimate"), ("Design", "A unique design for your brand"), ("Development", "Code, CMS, integrations, QA"), ("Launch", "Analytics, training, warranty")],
  "geo_h": "Ukraine<br><span class=\"acc\">and beyond</span>",
  "geo_p": "Based in Lviv but not limited to one city: we work remotely with clients across Ukraine and are expanding into EU markets. Communication in English, Ukrainian or Polish.",
  "geo": [("01", "Ukraine", "now", True), ("02", "Poland", "next", False), ("03", "Germany", "next", False), ("04", "Other EU markets", "planned", False)],
  "faq_h": "Frequently<br><span class=\"acc\">asked</span>",
  "faq": [
    ("How much does a website cost?", "It depends on scope. The packages above give a guide; the exact price is calculated after the brief from each specialist’s hours plus a 15–20% buffer, and fixed in the contract."),
    ("How long does it take?", "A landing page takes 2–3 weeks, a corporate website 4–7 weeks, complex projects from 8 weeks. You get a milestone schedule before we start."),
    ("Can I edit the website myself?", "Yes. In Business and Custom packages we set up a CMS and train your team to update copy, images, prices and news without a developer."),
    ("Do you work with international clients?", "Yes. We work remotely with clients in Poland, Germany and across the EU, with contracts and invoices in EUR."),
    ("What happens after launch?", "A warranty period covers bug fixes free of charge. After that you can add technical support, optimisation and ongoing development."),
    ("Do you show real case studies?", "We are a young studio, so our site shows concept projects clearly labelled as concepts. On a call we’ll walk you through prototypes and our process."),
  ],
  "c_h": "Let’s discuss<br><span class=\"acc\">your project</span>",
  "c_p": "Tell us briefly about your task — a manager will reply within one business day with a format and a rough estimate.",
  "c_topics": [("business", "Business website"), ("landing", "Landing page"), ("ecom", "E-commerce"), ("redesign", "Redesign / support"), ("other", "Other")],
  "c_name": "Name", "c_contact": "Email, phone or Telegram", "c_ph": "you@company.com", "c_budget": "Estimated budget",
  "c_budgets": ["Not sure yet", "up to €1,500", "€1,500 – €4,000", "€4,000 – €10,000", "€10,000 +"],
  "c_msg": "About the project", "c_send": "Send request", "c_consent": 'By sending a request you agree to our <a href="privacy/">Privacy policy</a>.', "c_ok": "✓ Thank you! We’ll get back to you shortly.",
  "f_big": "<span>ADV —</span><br>websites that work for your business.",
  "f_mail": "General enquiries:", "f_office": "Office:", "f_social": "Follow us:", "f_cta": "Discuss<br>a project",
  "f_legal": ["Privacy policy", "Cookie policy", "Terms of use"],
  "f_copy": "© ADV™ 2026. All rights reserved",
  "cta_more": "Discuss a project →", "cta_pk": "See packages",
},
}

SLUGS = {"BUDMIST": "budmist", "KAVA LAB": "kava-lab", "DENTALIA": "dentalia", "FLOWDESK": "flowdesk"}
COORDS = ("49° 50' 24.00\" N", "24° 01' 48.00\" E")
def LOGO(gid, cls="logo-svg"):
    """Логотип ADV (векторна версія з assets/img/logo.svg)."""
    return (f'<svg class="{cls}" viewBox="0 0 300 80" role="img" aria-label="ADV">'
            f'<defs><linearGradient id="{gid}" x1="0" y1="1" x2="1" y2="0"><stop offset="0" stop-color="#b9761f"/><stop offset="1" stop-color="#f4cf3b"/></linearGradient></defs>'
            '<g fill="currentColor"><path d="M0 80L30 0H56L86 80H62L43 26L24 80Z"/>'
            '<path fill-rule="evenodd" d="M96 0H142A34 34 0 0 1 176 34V46A34 34 0 0 1 142 80H96ZM118 18V62H138A16 16 0 0 0 154 46V34A16 16 0 0 0 138 18Z"/>'
            '<path d="M182 0H206L226 54L246 0H270L238 80H214Z"/></g>'
            f'<path fill="url(#{gid})" d="M280 0H300L284 32H264Z"/></svg>')


def no(i, text, cls=""):
    return f'<div class="no rv {cls}"><span class="no__tag">NO_{i:03d}</span><div class="no__text">{text}</div></div>'


def chrome(L, b, cur="home", sw=None):
    """Хедер (десктоп-навігація + бургер для мобільних) і повноекранне меню — спільні для всіх сторінок.
    b — шлях до кореня сайту; cur — поточна сторінка ('home', 'price/', 'projects/', ...);
    sw — (href_uk, href_en) для перемикача мови."""
    pre = "" if L["lang"] == "uk" else "en/"
    home = b + pre
    on_home = cur == "home"
    def href(t):
        if t.startswith("#"):
            return t if on_home else home + t
        return home + t
    sw = sw or (("./", "en/") if L["lang"] == "uk" else ("../", "./"))
    lang_sw = (f'<a href="{sw[0]}" class="{"on" if L["lang"] == "uk" else ""}" hreflang="uk">UA</a>'
               f'<a href="{sw[1]}" class="{"on" if L["lang"] == "en" else ""}" hreflang="en">EN</a>')
    hnav = "".join(f'<a href="{href(h)}"{" class=\"cur\" aria-current=\"page\"" if h == cur else ""}>{t}</a>' for h, t in L["nav"])
    mnav = "\n    ".join(f'<a href="{href(h)}"><small>{i+1:02d}</small>{t}</a>' for i, (h, t) in enumerate(L["nav"]))
    logo_href = "#top" if on_home else home
    return f"""<header class="header">
  <a href="{logo_href}" class="logo" aria-label="ADV">{LOGO("lg-h")}</a>
  <nav class="hnav" aria-label="Main">{hnav}</nav>
  <div class="header__right">
    <nav class="lang" aria-label="Language">{lang_sw}</nav>
    <a href="{href('#contact')}" class="btn hcta" data-topic="business">{L['m_cta']}</a>
    <button class="menu-btn" id="menuOpen" aria-label="Menu" aria-controls="menu" aria-expanded="false">{L['menu']} <i><b></b><b></b><b></b></i></button>
  </div>
</header>

<nav class="menu" id="menu" aria-hidden="true">
  <button class="menu__close" id="menuClose">{L['close']}</button>
  <div class="menu__nav">
    {mnav}
  </div>
  <div class="menu__side">
    <div><div class="mono-s">{L['m_mail']}</div><a href="mailto:{EMAIL}">{EMAIL}</a></div>
    <div><div class="mono-s">{L['m_office']}</div>{L['office']}</div>
    <div><div class="mono-s">{L['m_social']}</div><a href="#">Telegram</a> · <a href="#">Instagram</a> · <a href="#">LinkedIn</a> · <a href="#">Behance</a></div>
    <a href="{href('#contact')}" class="btn" style="width:max-content">{L['m_cta']}</a>
  </div>
</nav>
"""


def page(L):
    b = L["base"]
    other = "en" if L["lang"] == "uk" else "uk"
    ld = {
        "@context": "https://schema.org", "@type": "ProfessionalService", "name": "ADV",
        "description": L["desc"], "url": DOMAIN + L["path"], "email": EMAIL,
        "address": {"@type": "PostalAddress", "addressLocality": "Lviv", "addressCountry": "UA"},
        "areaServed": ["UA", "PL", "DE"],
    }
    nav = "\n    ".join(f'<a href="{h}"><small>{i+1:02d}</small>{t}</a>' for i, (h, t) in enumerate(L["nav"]))
    why = "\n    ".join(
        f'<div class="stat {"stat--wide" if w else ""} rv"><img src="{b}assets/img/{img}.webp?v={VERSION}" alt="" loading="lazy"><span class="stat__label">NO_{i+1:03d}</span>'
        f'<div class="stat__title">{t}<small>{d}</small></div></div>'
        for i, (img, t, d, w) in enumerate(L["why"]))
    mq = "".join(f"<span>{w}</span><span class=\"acc\">✦</span>" for w in L["marquee"] * 2)
    aud = "\n    ".join(
        f'<div class="aud__item rv {"aud__item--lime" if i == 5 else ""}"><small>0{i+1} / {tag}</small><b>{t}</b><span>{d}</span></div>'
        for i, (t, d, tag) in enumerate(L["aud"]))
    niche_tabs = "".join(f'<button type="button" class="ntab{" on" if i == 0 else ""}" data-n="{k}" data-img="{b}assets/img/{img}.webp?v={VERSION}">{t}</button>' for i, (k, t, img, h, d, li, slug) in enumerate(L["niches"]))
    niche_panels = ""
    for i, (k, t, img, h, d, li, slug) in enumerate(L["niches"]):
        view = (f'<button type="button" class="btn btn--ghost" data-view="{b}concepts/{slug}/{'en/' if L['lang'] == 'en' else ''}" data-title="{h}" data-url="{L["pf_tag"]}">{L["pf_view"]} ↗</button>') if slug else ""
        niche_panels += (f'<div class="npanel" data-n="{k}"{"" if i == 0 else " hidden"}><h3 class="h">{h}</h3><p>{d}</p>'
                         f'<ul>{"".join(f"<li>{x}</li>" for x in li)}</ul>'
                         f'<div class="npanel__cta"><a href="#contact" class="btn" data-topic="business">{L["niche_cta"]}</a>{view}</div></div>')
    tab_btns = "".join(
        f'<button class="tab{" active" if i == 0 else ""}" data-p="{k}">{title}</button>'
        for i, (k, m, c, title, sub, items, price) in enumerate(L["tabs"]))
    tab_panels = "".join(
        f'<div class="proj-panel" data-p="{k}" data-model="{b}assets/models/{M['tabs'][i]}.glb?v={VERSION}" data-c="{c}"{"" if i == 0 else " hidden"}>'
        f'<h2 class="h">{title}</h2><div class="sub">{sub}</div>'
        + "".join(f'<div class="no"><span class="no__tag">NO_00{j+1}</span><div class="no__text">{t}</div></div>' for j, t in enumerate(items))
        + f'<div class="price">{price}</div><a href="#packages" class="btn btn--ghost" style="width:max-content">{L["cta_pk"]}</a></div>'
        for i, (k, m, c, title, sub, items, price) in enumerate(L["tabs"]))
    pkgs = ""
    for (name, for_, price, hours, vals, hot) in L["pk"]:
        rows = "".join(f"<div><dt>{r}</dt><dd>{v}</dd></div>" for r, v in zip(L["pk_rows"], vals))
        topic = {"Start": "landing", "Business": "business", "Custom": "other"}[name]
        pkgs += (f'<article class="pkg rv{" pkg--hot" if hot else ""}" data-badge="{L["pk_badge"]}">'
                 f'<span class="mono-s">PACKAGE // {name.upper()}</span><h3 class="h">{name}</h3><div class="pkg__for">{for_}</div>'
                 f'<div class="pkg__price">{price}<small>{hours}</small></div><dl>{rows}</dl>'
                 f'<a href="#contact" class="btn{"" if hot else " btn--ghost"}" data-topic="{topic}">{L["pk_btn"]}</a></article>\n')
    calc = "".join(f"<div><span>0{i+1}</span><b>{t}</b>{d}</div>" for i, (t, d) in enumerate(L["calc"]))
    icons = ['<path d="M4 4h16v12H4z"/><path d="M8 20h8M12 16v4M8 8l3 3-3 3"/>', '<path d="M12 3l8 4v5c0 5-3.5 8-8 9-4.5-1-8-4-8-9V7z"/><path d="M9 12l2 2 4-4"/>',
             '<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>', '<circle cx="11" cy="11" r="7"/><path d="M21 21l-5-5"/>', '<path d="M8 7h8M8 12h8M8 17h5"/><rect x="3" y="3" width="18" height="18" rx="2"/>',
             '<path d="M3 17l6-6 4 4 8-8"/><path d="M14 7h7v7"/>']
    ex = "".join(
        f'<article class="svc rv{" svc--lime" if i in (2, 5) else ""}" style="min-height:300px"><div class="svc__top"><div class="svc__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">{icons[i]}</svg></div><span class="mono-s">NO-{i+1:03d} / {tag}</span></div>'
        f'<h3 class="h">{t}</h3><p>{d}</p><div class="svc__price" style="margin-top:auto"><span></span><b>{p}</b></div></article>'
        for i, (tag, t, d, p) in enumerate(L["ex"]))
    pf = ""
    for (name, url, c, bgc, fg, img, title, d, chips, h, btn) in L["pf"]:
        slug = SLUGS[name]
        src = f"{b}concepts/{slug}/{'en/' if L['lang'] == 'en' else ''}"
        pf += (f'<article class="case rv" style="--c:{c};--bgc:{bgc};--fg:{fg}">'
               f'<button type="button" class="case__shot" data-view="{src}" data-title="{name} — {title}" data-url="{url}" aria-label="{L["pf_view"]}: {name}">'
               f'<span class="case__hover">{L["pf_view"]} ↗</span><div class="case__bar"><i></i><i></i><i></i><em>{url}</em></div>'
               f'<img class="case__img" src="{b}assets/img/concepts/{slug}{"-en" if L["lang"] == "en" else ""}.webp?v={VERSION}" '
               f'width="1280" height="720" loading="lazy" alt="{name} — {title}"></button>'
               f'<div class="case__meta"><div><h3 class="h">{name} — {title}</h3><p>{d}</p></div><span class="case__tag">{L["pf_tag"]}</span></div>'
               f'<div class="case__chips">{"".join(f"<span>{x}</span>" for x in chips)}</div>'
               f'<button type="button" class="case__link" data-view="{src}" data-title="{name} — {title}" data-url="{url}">{L["pf_view"]} →</button></article>\n')
    team_btns = "".join(f'<button class="dept{" active" if i == 0 else ""}" data-i="{i}">{t}</button>' for i, (t, d, r) in enumerate(L["team"]))
    team_panels = "".join(
        f'<div class="dept__card" data-i="{i}"{"" if i == 0 else " hidden"}><span class="dept__count">{i+1:02d}</span>'
        f'<div class="mono-s" style="margin-bottom:10px">ROLE // {i+1:03d}</div><h3 class="h">{t}</h3><p>{d}</p>'
        f'<ul class="dept__roles">{"".join(f"<li>{x}</li>" for x in r)}</ul></div>'
        for i, (t, d, r) in enumerate(L["team"]))
    process = "".join(f'<div class="step rv"><span class="mono-s">0{i+1}</span><b>{t}</b><span>{d}</span></div>' for i, (t, d) in enumerate(L["process"]))
    geo = "".join(f'<div class="rv"><span class="mono-s">{n}</span><b>{t}</b><em class="{"now" if now else ""}">{s}</em></div>' for n, t, s, now in L["geo"])
    faq = "".join(f'<details class="rv"><summary>{q}</summary><p>{a}</p></details>' for q, a in L["faq"])
    topics = "".join(f'<label><input type="radio" name="topic" value="{v}"{" checked" if i == 0 else ""}><span>{t}</span></label>' for i, (v, t) in enumerate(L["c_topics"]))
    budgets = "".join(f"<option>{x}</option>" for x in L["c_budgets"])
    legal = " · ".join(f'<a href="{p}/">{x}</a>' for p, x in zip(("privacy", "cookies", "terms"), L["f_legal"]))
    intro = "\n    ".join(no(i + 1, t) for i, t in enumerate(L["intro"]))
    why_lines = "".join(no(i + 1, t) for i, t in enumerate(L["why_lines"]))
    team_lines = "".join(no(i + 1, t) for i, t in enumerate(L["team_lines"]))
    lang_sw = (f'<a href="{b}./" class="{"on" if L["lang"] == "uk" else ""}" hreflang="uk">UA</a>'
               f'<a href="{"./" if L["lang"] == "en" else "en/"}" class="{"on" if L["lang"] == "en" else ""}" hreflang="en">EN</a>')

    return f"""<!DOCTYPE html>
<html lang="{L['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{L['title']}</title>
<meta name="description" content="{L['desc']}">
<link rel="canonical" href="{DOMAIN}{L['path']}">
<link rel="alternate" hreflang="uk" href="{DOMAIN}/">
<link rel="alternate" hreflang="en" href="{DOMAIN}/en/">
<link rel="alternate" hreflang="x-default" href="{DOMAIN}/en/">
<meta property="og:type" content="website">
<meta property="og:locale" content="{L['locale']}">
<meta property="og:title" content="{L['title']}">
<meta property="og:description" content="{L['desc']}">
<meta property="og:image" content="{DOMAIN}/assets/img/og.png">
<meta name="theme-color" content="#0f0b08">
<link rel="icon" type="image/svg+xml" href="{b}assets/img/favicon.svg">
<link rel="apple-touch-icon" href="{b}assets/img/logo-badge.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fira+Mono:wght@400;500;700&family=Unbounded:wght@700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{b}assets/css/style.css?v={VERSION}">
<script type="module" src="https://cdn.jsdelivr.net/npm/@google/model-viewer@3.5.0/dist/model-viewer.min.js"></script>
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body class="locked m-{MASCOT}" data-base="{b}">

<div class="preloader" id="preloader">
  <div class="preloader__owl" id="preOwl" role="img" aria-label="ADV owl"></div>
  <div class="preloader__frame">{LOGO("lg-pre")}</div>
  <div class="preloader__pct"><span id="prePct">0</span>%</div>
  <div class="preloader__label">{L['loading']}</div>
  <div class="preloader__bar" id="preBar"></div>
</div>

{chrome(L, b)}
<main id="top">

<section class="hero">
  <div class="hero__light"></div>
  <div class="hero__word"><h1 class="visually-hidden">ADV — {L['hero_tag']}</h1>{LOGO("lg-hero")}</div>
  <div class="hero__tag">{L['hero_tag']}</div>
  <model-viewer class="hero__model" id="heroModel" src="{b}assets/models/{M['hero']}.glb?v={VERSION}" alt="ADV mascot"
    camera-orbit="{M['orbit']}" disable-zoom disable-pan interaction-prompt="none"
    auto-rotate auto-rotate-delay="0" rotation-per-second="14deg" camera-controls
    exposure="{M['exp']}" shadow-intensity="1" environment-image="neutral"{M['style']}></model-viewer>
  <img class="hero__fallback" id="heroFallback" src="{b}assets/img/logo-badge.svg" alt="">
  <div class="hero__pitch"><b>{L['hero_pitch_b']}</b>{L['hero_pitch']}</div>
  <div class="hero__coords mono-s"><span>{COORDS[0]}</span><span>{COORDS[1]}</span></div>
  <div class="hero__scroll mono-s">{L['scroll']}<br>© 2026 / LVIV</div>
  <div class="hero__marks"><span style="left:var(--pad);top:45%"></span><span style="right:var(--pad);top:62%"></span></div>
</section>

<section class="intro" id="about">
  <div class="intro__lines">
    {intro}
  </div>
  <div class="leaders">
    <div>
      <div class="badge-holding rv">{L['lead_badge']}</div>
      <h2 class="h leaders__title rv">{L['lead_title']}</h2>
    </div>
    <div class="leaders__meta">
      <div class="leaders__years rv">{L['lead_num']}<small>{L['lead_num_s']}</small></div>
      <div class="mono-s rv" style="text-align:right">{L['lead_sub']}</div>
    </div>
  </div>
</section>

<section class="stats">
  <div class="stats__head">
    <h2 class="h rv">{L['why_h']}</h2>
    <div class="lines">{why_lines}</div>
  </div>
  <div class="stats__grid">
    {why}
  </div>
</section>

<div class="marquee"><div class="marquee__track">{mq}</div></div>

<section class="aud">
  <div class="aud__head">
    <h2 class="h rv">{L['aud_h']}</h2>
    <p class="rv">{L['aud_p']}</p>
  </div>
  <div class="aud__grid">
    {aud}
  </div>
</section>

<section class="niche rv" id="niches">
  <div class="niche__img" id="nicheImg"></div>
  <div class="niche__body">
    <span class="mono-s lime">{L['niche_tag']}</span>
    <h2 class="h">{L['niche_h']}</h2>
    <p>{L['niche_p']}</p>
    <div class="ntabs" id="nicheTabs">{niche_tabs}</div>
    {niche_panels}
  </div>
</section>

<section class="projects" id="services">
  <div class="projects__bg" style="background-image:url({b}assets/img/grid-bg.webp)"></div>
  <div class="projects__glow"></div>
  <model-viewer class="projects__model" id="projModel" src="{b}assets/models/{M['tabs'][0]}.glb?v={VERSION}" alt="3D"
    camera-orbit="25deg 80deg 105%" disable-zoom disable-pan interaction-prompt="none" camera-controls
    auto-rotate rotation-per-second="18deg" exposure="0.85" shadow-intensity="1" environment-image="neutral"></model-viewer>
  <div class="projects__info" id="projInfo">
    <span class="mono-s">// {L['svc_h'].upper()}</span>
    {tab_panels}
  </div>
  <div class="tabs" id="projTabs">{tab_btns}</div>
</section>

<section class="pk" id="packages">
  <div class="pk__head">
    <h2 class="h rv">{L['pk_h']}</h2>
    <p class="rv">{L['pk_p']}</p>
  </div>
  <div class="pk__grid">
{pkgs}  </div>
  <div class="calc rv">
    <h3 class="h">{L['calc_h']}</h3>
    <div><div class="calc__steps">{calc}</div><p class="note">{L['calc_note']}</p></div>
  </div>
</section>

<section class="ex">
  <h2 class="h rv" style="font-size:clamp(28px,4vw,64px);margin-bottom:36px">{L['ex_h']}</h2>
  <div class="ex__grid">{ex}</div>
  <div class="process">{process}</div>
</section>

<section class="pf" id="work">
  <div class="pf__head">
    <h2 class="h rv">{L['pf_h']}</h2>
    <p class="rv">{L['pf_p']}</p>
  </div>
  <div class="pf__grid">
{pf}  </div>
</section>

<section class="infra" id="team">
  <div class="infra__stars"></div>
  <div class="infra__planet"></div>
  <div class="infra__orbit"><i style="--k:0px"></i><i style="--k:80px"></i><i style="--k:170px"></i><i style="--k:270px"></i></div>
  <div class="infra__head">
    <h2 class="h rv">{L['team_h']}</h2>
    {team_lines}
  </div>
  <div class="depts">
    <div class="depts__list" id="deptList">{team_btns}</div>
    <div class="dept__panel" id="deptPanel">{team_panels}</div>
  </div>
</section>

<section class="geo">
  <div>
    <h2 class="h rv">{L['geo_h']}</h2>
    <p class="rv">{L['geo_p']}</p>
    <div class="geo__steps">{geo}</div>
  </div>
  <div class="geo__map rv"></div>
</section>

<section class="faq" id="faq">
  <h2 class="h rv">{L['faq_h']}</h2>
  <div>{faq}</div>
</section>

<section class="contact" id="contact">
  <div>
    <h2 class="h rv">{L['c_h']}</h2>
    <p class="rv">{L['c_p']}</p>
  </div>
  <form class="form rv" id="form">
    <div class="chips" id="topics">{topics}</div>
    <label>{L['c_name']}<input name="name" required autocomplete="name"></label>
    <label>{L['c_contact']}<input name="contact" required placeholder="{L['c_ph']}"></label>
    <label>{L['c_budget']}<select name="budget">{budgets}</select></label>
    <label>{L['c_msg']}<textarea name="msg"></textarea></label>
    <button class="btn" type="submit">{L['c_send']}</button>
    <p class="form__consent">{L['c_consent']}</p>
    <div class="form__ok" id="formOk">{L['c_ok']}</div>
  </form>
</section>

</main>

<div class="viewer" id="viewer" hidden role="dialog" aria-modal="true" aria-labelledby="vTitle">
  <div class="viewer__bar">
    <span class="viewer__tag">{L['pf_tag']}</span>
    <div class="viewer__title"><b id="vTitle"></b><em id="vUrl"></em></div>
    <div class="viewer__dev" role="group">
      <button type="button" data-dev="desktop" class="on">{L['v_desktop']}</button>
      <button type="button" data-dev="mobile">{L['v_mobile']}</button>
    </div>
    <a id="vOpen" class="viewer__open" target="_blank" rel="noopener">{L['v_open']}</a>
    <button type="button" class="viewer__close" id="vClose" aria-label="{L['v_close']}">×</button>
  </div>
  <div class="viewer__stage"><div class="viewer__frame" id="vFrame"><iframe id="vIframe" title="Concept preview" loading="lazy"></iframe></div></div>
</div>

{footer(L, "")}
<script src="{b}assets/js/main.js?v={VERSION}"></script>
</body>
</html>
"""


def footer(L, home):
    """Спільний футер. home — шлях до домашньої сторінки цієї мови ('' на головній)."""
    legal = " · ".join(f'<a href="{home}{p}/">{x}</a>' for p, x in zip(("privacy", "cookies", "terms"), L["f_legal"]))
    contact = "#contact" if home == "" else home + "#contact"
    return f"""<footer class="footer">
  <h2 class="h footer__big">{L['f_big']}</h2>
  <div class="footer__grid">
    <div><span class="plus">+</span><div class="mono-s">{L['f_mail']}</div><a href="mailto:{EMAIL}">{EMAIL}</a></div>
    <div><span class="plus">+</span><div class="mono-s">{L['f_office']}</div><span>{L['office']}</span></div>
    <div><span class="plus">+</span><div class="mono-s">{L['f_social']}</div><a href="#">Telegram</a><a href="#">Instagram</a><a href="#">LinkedIn</a><a href="#">Behance</a></div>
    <div><a href="{contact}" class="circle-btn circle-btn--lime" style="position:relative;top:0;width:150px;height:150px">{L['f_cta']}</a></div>
  </div>
  <div class="footer__bottom">
    <span>{legal}</span>
    <span>{COORDS[0]} / {COORDS[1]}</span>
    <span>{L['f_copy']}</span>
  </div>
  <a href="#top" class="to-top" aria-label="Top">↑</a>
</footer>
"""


def subpage(L, b, cur, sw, title, desc, path, content, extra_head=""):
    """Повна HTML-сторінка-підрозділ (прайс, проєкти, документи) у стилі сайту."""
    pre = "" if L["lang"] == "uk" else "en/"
    return f"""<!DOCTYPE html>
<html lang="{L['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — ADV Development Studio</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{DOMAIN}{path[L['lang']]}">
<link rel="alternate" hreflang="uk" href="{DOMAIN}{path['uk']}">
<link rel="alternate" hreflang="en" href="{DOMAIN}{path['en']}">
<meta property="og:type" content="website">
<meta property="og:locale" content="{L['locale']}">
<meta property="og:title" content="{title} — ADV Development Studio">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{DOMAIN}/assets/img/og.png">
<meta name="theme-color" content="#0f0b08">
<link rel="icon" type="image/svg+xml" href="{b}assets/img/favicon.svg">
<link rel="apple-touch-icon" href="{b}assets/img/logo-badge.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fira+Mono:wght@400;500;700&family=Unbounded:wght@700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{b}assets/css/style.css?v={VERSION}">
{extra_head}</head>
<body class="sub" data-base="{b}">
{chrome(L, b, cur, sw)}
<main id="top">
{content}
</main>
{footer(L, b + pre)}
<script src="{b}assets/js/main.js?v={VERSION}"></script>
</body>
</html>
"""


PRICE_T = {
    "uk": {"title": "Прайс", "desc": "Орієнтовна вартість розробки: backend та інтеграції, CMS і адмін-панелі, CRM і бізнес-системи, боти й автоматизація.",
           "kicker": "ПРАЙС // ADV STUDIO", "h1": "Скільки коштує<br><span class=\"acc\">розробка</span>",
           "lead": "Орієнтовні ціни на окремі роботи та модулі. Точну вартість рахуємо після брифу — за реальними трудовитратами, з фіксацією в договорі.",
           "search": "Пошук послуги, напр. «CRM» або «бот»", "service": "Послуга", "price": "Вартість", "empty": "Нічого не знайдено. Спробуйте інший запит або напишіть нам.",
           "note_h": "Як читати прайс", "notes": ["Ціни вказані в доларах США і є орієнтиром для типового обсягу робіт.", "«від» — мінімальна вартість; фінальна залежить від складності та інтеграцій.", "Оплата можлива в гривнях за курсом НБУ на день рахунку.", "Пакети «під ключ» (Start / Business / Custom) — на головній сторінці."],
           "cta_h": "Не знайшли потрібного?", "cta_p": "Опишіть задачу — підготуємо оцінку протягом робочого дня.", "cta": "Отримати оцінку", "packages": "Пакети сайтів",
           "updated": "Оновлено"},
    "en": {"title": "Pricing", "desc": "Indicative development pricing: backend & integrations, CMS & admin panels, CRM & business systems, bots & automation.",
           "kicker": "PRICING // ADV STUDIO", "h1": "What development<br><span class=\"acc\">costs</span>",
           "lead": "Indicative prices for individual tasks and modules. The final price is calculated after the brief, based on real effort, and fixed in the contract.",
           "search": "Search a service, e.g. “CRM” or “bot”", "service": "Service", "price": "Price", "empty": "Nothing found. Try another query or write to us.",
           "note_h": "How to read this", "notes": ["Prices are in US dollars and indicate a typical scope of work.", "“From” is the minimum; the final price depends on complexity and integrations.", "Invoices for EU clients can be issued in EUR.", "Turnkey website packages (Start / Business / Custom) are on the home page."],
           "cta_h": "Didn’t find what you need?", "cta_p": "Describe the task — we’ll send an estimate within one business day.", "cta": "Get an estimate", "packages": "Website packages",
           "updated": "Updated"},
}

PROJ_T = {
    "uk": {"title": "Проєкти", "desc": "Проєкти та концепти ADV Development Studio: сайти для бізнесу, лендінги, інтернет-магазини, застосунки й боти.",
           "kicker": "ПОРТФОЛІО // ADV STUDIO", "h1": "Наші<br><span class=\"acc\">проєкти</span>",
           "lead": "Клієнтські роботи та концепти команди. Концепти чесно позначені — це демонстрація підходу, а не вигадані кейси.",
           "count": "проєктів", "cta_h": "Хочете такий самий?", "cta_p": "Розкажіть про задачу — запропонуємо рішення та оцінку.", "cta": "Обговорити проєкт"},
    "en": {"title": "Projects", "desc": "Projects and concepts by ADV Development Studio: business websites, landing pages, online stores, apps and bots.",
           "kicker": "PORTFOLIO // ADV STUDIO", "h1": "Our<br><span class=\"acc\">projects</span>",
           "lead": "Client work and team concepts. Concepts are clearly labelled — they show our approach, not invented case studies.",
           "count": "projects", "cta_h": "Want something similar?", "cta_p": "Tell us about your task — we’ll suggest a solution and an estimate.", "cta": "Discuss a project"},
}


def price_page(L):
    import html as _h
    lang = L["lang"]; t = PRICE_T[lang]; b = "../" if lang == "uk" else "../../"; home = b + ("" if lang == "uk" else "en/")
    data = json.load(open(os.path.join(ROOT, "data", "price.json"), encoding="utf-8"))
    tx = lambda v: v[lang] if isinstance(v, dict) else v
    fmt = lambda v: tx(v).replace(",", "\u202f") if lang == "uk" else tx(v)
    nav = "".join(f'<a href="#{c["id"]}"><span>{c["icon"]}</span>{tx(c["title"])}<i>{sum(len(g["items"]) for g in c["groups"])}</i></a>' for c in data["categories"])
    cats = ""
    for ci, c in enumerate(data["categories"]):
        groups = ""
        for g in c["groups"]:
            rows = "".join(f'<tr data-q="{_h.escape((tx(n) + " " + tx(g["title"]) + " " + tx(c["title"])).lower())}"><td>{tx(n)}</td><td>{fmt(pr)}</td></tr>' for n, pr in g["items"])
            groups += f'<div class="pgroup"><h3>{tx(g["title"])}</h3><table class="ptable"><thead><tr><th>{t["service"]}</th><th>{t["price"]}</th></tr></thead><tbody>{rows}</tbody></table></div>'
        cats += f'<section class="pcat rv" id="{c["id"]}"><div class="pcat__head"><span class="pcat__no">{ci+1:02d}</span><span class="pcat__icon">{c["icon"]}</span><h2 class="h">{tx(c["title"])}</h2></div>{groups}</section>'
    notes = "".join(f"<li>{n}</li>" for n in t["notes"])
    content = f"""<section class="phero">
  <span class="mono-s lime">{t['kicker']}</span>
  <h1 class="h">{t['h1']}</h1>
  <p>{t['lead']}</p>
  <label class="psearch"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"/><path d="M21 21l-5-5"/></svg><input id="priceSearch" type="search" placeholder="{t['search']}" autocomplete="off"></label>
</section>
<div class="pwrap">
  <aside class="pside"><nav class="pnav">{nav}</nav>
    <div class="pnote"><b>{t['note_h']}</b><ul>{notes}</ul><span class="mono-s">{t['updated']}: {data['updated']}</span></div>
  </aside>
  <div class="pbody">{cats}<p class="projects__empty" id="priceEmpty" hidden>{t['empty']}</p></div>
</div>
<section class="pcta rv"><div><h2 class="h">{t['cta_h']}</h2><p>{t['cta_p']}</p></div><div class="pcta__btns"><a class="btn" href="{home}#contact" data-topic="other">{t['cta']} →</a><a class="btn btn--ghost" href="{home}#packages">{t['packages']}</a></div></section>"""
    path = {"uk": "/price/", "en": "/en/price/"}
    sw = ("./", "../en/price/") if lang == "uk" else ("../../price/", "./")
    return subpage(L, b, "price/", sw, t["title"], t["desc"], path, content)


def projects_page(L):
    lang = L["lang"]; t = PROJ_T[lang]; b = "../" if lang == "uk" else "../../"; home = b + ("" if lang == "uk" else "en/")
    content = f"""<section class="phero">
  <span class="mono-s lime">{t['kicker']}</span>
  <h1 class="h">{t['h1']}</h1>
  <p>{t['lead']}</p>
</section>
<section class="projects-list">
  <div class="projects__bar"><div class="ntabs" id="projectFilters"></div><span class="mono-s"><b id="projectsCount">–</b> {t['count']}</span></div>
  <div class="pgrid" id="projectsGrid" aria-live="polite"></div>
</section>
<section class="pcta rv"><div><h2 class="h">{t['cta_h']}</h2><p>{t['cta_p']}</p></div><div class="pcta__btns"><a class="btn" href="{home}#contact" data-topic="business">{t['cta']} →</a></div></section>"""
    path = {"uk": "/projects/", "en": "/en/projects/"}
    sw = ("./", "../en/projects/") if lang == "uk" else ("../../projects/", "./")
    return subpage(L, b, "projects/", sw, t["title"], t["desc"], path, content)


if __name__ == "__main__":
    for code, out in (("uk", "index.html"), ("en", "en/index.html")):
        path = os.path.join(ROOT, out)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(page(T[code]))
        print("written", out)
    for code in ("uk", "en"):
        for rel, fn in (("price", price_page), ("projects", projects_page)):
            out = f"{rel}/index.html" if code == "uk" else f"en/{rel}/index.html"
            path = os.path.join(ROOT, out); os.makedirs(os.path.dirname(path), exist_ok=True)
            open(path, "w", encoding="utf-8").write(fn(T[code])); print("written", out)
    import sys as _sys
    _sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import legal
    for w in legal.render_all(ROOT, {"LOGO": LOGO, "SUBPAGE": subpage, "EMAIL": EMAIL, "DOMAIN": DOMAIN, "VERSION": VERSION, "T": T}):
        print("written", w)
