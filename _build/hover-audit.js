/* Аудит hover-станів. Вставте в консоль сторінки (або виконайте через інструмент браузера).
   Імітує :hover для кожного посилання/кнопки (правила підмінюються на місці, порядок каскаду зберігається),
   рахує контраст тексту до фону і повертає елементи з контрастом < 3 або зі зміною display.
   Позначка [img/grad] = під елементом фото чи градієнт: контраст порахований приблизно, перевірте очима. */
(async () => {
  const H = '__advh';
  const changed = [];
  for (const sh of document.styleSheets) {
    let rules; try { rules = sh.cssRules; } catch (e) { continue; }
    const walk = list => { for (const r of list) {
      if (r.cssRules) walk(r.cssRules);
      if (r.selectorText && r.selectorText.includes(':hover')) { changed.push([r, r.selectorText]); r.selectorText = r.selectorText.replaceAll(':hover', '.' + H); }
    } };
    walk(rules);
  }
  const off = document.createElement('style'); off.textContent = '*,*::before,*::after{transition:none!important;animation:none!important}'; document.head.appendChild(off);
  const parse = c => (c.match(/[\d.]+/g) || [0, 0, 0, 0]).map(Number);
  const lum = ([r, g, b]) => { const f = v => { v /= 255; return v <= .03928 ? v / 12.92 : ((v + .055) / 1.055) ** 2.4; }; return .2126 * f(r) + .7152 * f(g) + .0722 * f(b); };
  const blend = (t, b) => { const a = t[3] ?? 1; return [0, 1, 2].map(i => t[i] * a + b[i] * (1 - a)); };
  const bgOf = el => { const st = []; for (let e = el; e; e = e.parentElement) { const cs = getComputedStyle(e); const c = parse(cs.backgroundColor); if (cs.backgroundColor !== 'rgba(0, 0, 0, 0)') st.push(c.length === 3 ? [...c, 1] : c); if (c.length === 3 || c[3] === 1) break; } let col = [255, 255, 255]; for (let i = st.length - 1; i >= 0; i--) col = blend(st[i], col); return col; };
  const hasImg = el => { for (let x = el; x; x = x.parentElement) { const cs = getComputedStyle(x); if (cs.backgroundImage !== 'none') return true; if (cs.backgroundColor !== 'rgba(0, 0, 0, 0)' && parse(cs.backgroundColor)[3] !== 0 && (parse(cs.backgroundColor).length === 3 || parse(cs.backgroundColor)[3] === 1)) return false; if (cs.position === 'fixed' && x.tagName === 'HEADER') return true; } return false; };
  const ratio = (a, b) => { const [x, y] = [lum(a), lum(b)].sort((p, q) => q - p); return (x + .05) / (y + .05); };
  const snap = el => { const cs = getComputedStyle(el); return { fg: cs.color, d: cs.display, r: ratio(parse(cs.color).slice(0, 3), bgOf(el)) }; };
  const out = [];
  for (const el of document.querySelectorAll('a, button, summary, [role=button]')) {
    if (!el.innerText.trim() || !(el.offsetParent || getComputedStyle(el).position === 'fixed')) continue;
    const n = snap(el); el.classList.add(H); const h = snap(el); el.classList.remove(H);
    if (n.r < 3 || h.r < 3 || n.d !== h.d) out.push({ text: el.innerText.trim().replace(/\s+/g, ' ').slice(0, 40), normal: +n.r.toFixed(2), hover: +h.r.toFixed(2), hoverColor: h.fg, overImage: hasImg(el), display: n.d === h.d ? n.d : n.d + '→' + h.d });
  }
  changed.forEach(([r, s]) => { r.selectorText = s; }); off.remove();
  return out;
})();
