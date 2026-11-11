/* Плашка «Концепт від ADV» для всіх концепт-сайтів.
   Підключення: <script src="../concept-bar.js" defer></script>
   Усередині вікна перегляду на сайті ADV (iframe) плашка ховається — там є своя панель. */
(() => {
  const me = document.currentScript;
  const root = me ? new URL('../', me.src).href : '../../';
  const inFrame = window.self !== window.top;
  const lang = (document.documentElement.lang || 'uk').slice(0, 2);
  const t = lang === 'en'
    ? { tag: 'Concept by ADV', note: 'not a real client', back: '← Back to ADV' }
    : { tag: 'Концепт від ADV', note: 'не реальний клієнт', back: '← До ADV' };
  // Службовий режим для скріншотів превʼю (?shot=1): без плашки, анімації першого екрана одразу у фінальному стані
  if (/[?&]shot=1/.test(location.search)) {
    const finish = () => {
      if (!window.gsap) return;
      for (let i = 0; i < 4; i++) {
        gsap.globalTimeline.getChildren(true, true, true).forEach(t => {
          const st = t.scrollTrigger;
          if (st && (st.vars.scrub || st.vars.pin)) return;
          if (t.totalDuration() < 30 && t.repeat() !== -1) t.progress(1);
        });
        if (window.ScrollTrigger) ScrollTrigger.update();
      }
    };
    window.addEventListener('load', () => { finish(); setTimeout(finish, 300); setTimeout(finish, 1200); });
    return;
  }
  if (inFrame) return;
  const css = `
  .adv-cbar{position:fixed;left:16px;bottom:16px;z-index:2147483000;display:flex;align-items:center;gap:12px;
    padding:8px 8px 8px 14px;border-radius:40px;background:rgba(15,11,8,.92);color:#f1e7d6;backdrop-filter:blur(8px);
    font:500 12px/1.2 'Fira Mono',ui-monospace,monospace;box-shadow:0 10px 30px rgba(0,0,0,.35);border:1px solid rgba(217,151,58,.55)}
  .adv-cbar b{color:#f4cf3b;font-weight:700;letter-spacing:.04em;text-transform:uppercase}
  .adv-cbar span{color:#a8977f}
  .adv-cbar a{color:#1a1108;background:#d9973a;padding:7px 12px;border-radius:30px;text-decoration:none;white-space:nowrap}
  .adv-cbar a:hover{background:#f4cf3b;color:#1a1108}
  .adv-cbar a.adv-cbar__lang{background:transparent;color:#f1e7d6;border:1px solid rgba(255,236,210,.28);padding:6px 10px}
  .adv-cbar a.adv-cbar__lang:hover{background:#f1e7d6;color:#1a1108}
  @media (max-width:520px){.adv-cbar span{display:none}.adv-cbar{left:10px;bottom:10px}}`;
  const s = document.createElement('style'); s.textContent = css; document.head.appendChild(s);
  const bar = document.createElement('div');
  bar.className = 'adv-cbar';
  const home = root + (lang === 'en' ? 'en/#work' : '#work');
  const other = lang === 'en' ? { href: '../', label: 'UA' } : { href: 'en/', label: 'EN' };
  bar.innerHTML = `<b>${t.tag}</b><span>${t.note}</span><a class="adv-cbar__lang" href="${other.href}">${other.label}</a><a href="${home}">${t.back}</a>`;
  document.body.appendChild(bar);
})();
