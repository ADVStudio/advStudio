/**
 * ADV — прийом заявок із сайту → Google Таблиця + Telegram + пошта.
 *
 * Як розгорнути: integrations/form-to-sheet-telegram/README.md
 * Секрети НЕ пишіть у код — лише у «Властивості скрипту» (Project Settings → Script properties):
 *   TELEGRAM_TOKEN   — токен бота від @BotFather
 *   TELEGRAM_CHAT_ID — id чату або групи (можна кілька через кому)
 *   NOTIFY_EMAIL     — куди дублювати лист (напр. adv.development.studio@gmail.com)
 */

const SHEET_NAME = 'Заявки';
const HEADERS = ['Дата', 'Тема', "Ім'я", 'Контакт', 'Бюджет', 'Повідомлення', 'Мова', 'Сторінка',
                 'utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content', 'Статус'];
const TOPICS = {
  business: 'Business website', landing: 'Landing page', ecom: 'E-commerce',
  redesign: 'Редизайн / підтримка', other: 'Інше'
};

function doPost(e) {
  try {
    const p = (e && e.parameter) || {};

    // антиспам: приховане поле-пастка та надто швидке заповнення
    if (p.company) return json_({ ok: true });
    if (p.t && Date.now() - Number(p.t) < 2500) return json_({ ok: true });

    const name = clean_(p.name, 120);
    const contact = clean_(p.contact, 160);
    if (!name || !contact) return json_({ ok: false, error: 'required' });

    // не більше 5 заявок з одного контакту за 10 хвилин
    const cache = CacheService.getScriptCache();
    const key = 'c_' + Utilities.base64EncodeWebSafe(contact.toLowerCase()).slice(0, 200);
    const n = Number(cache.get(key) || 0);
    if (n >= 5) return json_({ ok: false, error: 'rate' });
    cache.put(key, String(n + 1), 600);

    const row = {
      date: new Date(),
      topic: TOPICS[p.topic] || clean_(p.topic, 60) || '—',
      name: name,
      contact: contact,
      budget: clean_(p.budget, 60),
      msg: clean_(p.msg, 3000),
      lang: clean_(p.lang, 5),
      page: clean_(p.page, 300),
      utm: ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content'].map(k => clean_(p[k], 150))
    };

    const lock = LockService.getScriptLock();
    lock.waitLock(10000);
    try {
      const sh = sheet_();
      // апостроф попереду — щоб таблиця не сприймала «+380…» чи «=…» як формулу
      sh.appendRow([row.date, row.topic, safe_(row.name), safe_(row.contact), safe_(row.budget), safe_(row.msg),
                    row.lang, row.page].concat(row.utm.map(safe_)).concat(['Нова']));
    } finally {
      lock.releaseLock();
    }

    notifyTelegram_(row);
    notifyEmail_(row);
    return json_({ ok: true });
  } catch (err) {
    console.error(err);
    return json_({ ok: false, error: 'server' });
  }
}

function doGet() {
  return json_({ ok: true, service: 'ADV form endpoint' });
}

/* ---------- helpers ---------- */

function sheet_() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let sh = ss.getSheetByName(SHEET_NAME);
  if (!sh) sh = ss.insertSheet(SHEET_NAME);
  if (sh.getLastRow() === 0) {
    sh.appendRow(HEADERS);
    sh.getRange(1, 1, 1, HEADERS.length).setFontWeight('bold').setBackground('#f4e3c3');
    sh.setFrozenRows(1);
    sh.getRange('A:A').setNumberFormat('dd.mm.yyyy hh:mm');
  }
  return sh;
}

function notifyTelegram_(r) {
  const props = PropertiesService.getScriptProperties();
  const token = props.getProperty('TELEGRAM_TOKEN');
  const chats = (props.getProperty('TELEGRAM_CHAT_ID') || '').split(',').map(s => s.trim()).filter(String);
  if (!token || !chats.length) return;
  const h = s => String(s || '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  const utm = r.utm.filter(String).length ? '\n📊 ' + h(r.utm.filter(String).join(' / ')) : '';
  const text =
    '🦉 <b>Нова заявка — ADV</b>\n\n' +
    '📌 <b>' + h(r.topic) + '</b>\n' +
    '👤 ' + h(r.name) + '\n' +
    '📞 ' + h(r.contact) + '\n' +
    (r.budget ? '💰 ' + h(r.budget) + '\n' : '') +
    (r.msg ? '\n💬 ' + h(r.msg) + '\n' : '') +
    '\n🌐 ' + h(r.lang.toUpperCase()) + ' · ' + h(r.page) + utm;
  chats.forEach(chat => {
    UrlFetchApp.fetch('https://api.telegram.org/bot' + token + '/sendMessage', {
      method: 'post', contentType: 'application/json', muteHttpExceptions: true,
      payload: JSON.stringify({ chat_id: chat, text: text, parse_mode: 'HTML', disable_web_page_preview: true })
    });
  });
}

function notifyEmail_(r) {
  const to = PropertiesService.getScriptProperties().getProperty('NOTIFY_EMAIL');
  if (!to) return;
  const body = [
    'Тема: ' + r.topic, "Ім'я: " + r.name, 'Контакт: ' + r.contact, 'Бюджет: ' + (r.budget || '—'),
    '', 'Повідомлення:', r.msg || '—', '', 'Мова: ' + r.lang + ' · Сторінка: ' + r.page,
    'UTM: ' + (r.utm.filter(String).join(' / ') || '—')
  ].join('\n');
  MailApp.sendEmail({ to: to, subject: 'ADV · Нова заявка: ' + r.topic + ' — ' + r.name, body: body, name: 'ADV — сайт' });
}

function clean_(v, max) {
  return String(v == null ? '' : v).replace(/[\u0000-\u0008\u000B\u000C\u000E-\u001F]/g, '').trim().slice(0, max);
}

function safe_(v) {
  return /^[=+\-@]/.test(v) ? "'" + v : v;
}

function json_(o) {
  return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON);
}

/* ---------- службові функції (запускаються вручну з редактора) ---------- */

/** Крок налаштування: показує chat id тих, хто написав боту /start (див. README). */
function showTelegramChats() {
  const token = PropertiesService.getScriptProperties().getProperty('TELEGRAM_TOKEN');
  if (!token) throw new Error('Спершу додайте TELEGRAM_TOKEN у Script properties');
  const res = JSON.parse(UrlFetchApp.fetch('https://api.telegram.org/bot' + token + '/getUpdates').getContentText());
  const seen = {};
  (res.result || []).forEach(u => {
    const c = (u.message || u.my_chat_member || u.channel_post || {}).chat;
    if (c && !seen[c.id]) { seen[c.id] = 1; console.log(c.id + '  ←  ' + (c.title || [c.first_name, c.last_name].join(' ')) + ' (' + c.type + ')'); }
  });
  if (!Object.keys(seen).length) console.log('Порожньо: напишіть боту /start (або додайте його в групу й напишіть там), потім запустіть ще раз.');
}

/** Тестова заявка: перевіряє таблицю, Telegram і пошту одним кліком. */
function sendTestLead() {
  const res = doPost({ parameter: { topic: 'business', name: 'Тест', contact: '@test', budget: 'Ще не знаю', msg: 'Перевірка інтеграції', lang: 'uk', page: '/', t: '0' } });
  console.log(res.getContent());
}
