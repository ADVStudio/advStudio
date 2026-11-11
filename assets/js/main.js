(() => {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const base = document.body.dataset.base || '';

  /* ---------- PRELOADER ---------- */
  const pre = $('#preloader'), pct = $('#prePct'), bar = $('#preBar');
  const owl = $('#preOwl');
  const owlFrames = Array.from({ length: 12 }, (_, i) => `${base}assets/img/owl-spin-${i}.webp`);
  let of = 0, ready = 0;
  // обертання стартує лише коли всі кадри в кеші — без «блимання» порожнім кадром
  owlFrames.forEach(src => { const im = new Image(); im.onload = () => { ready++; }; im.src = src; });
  if (owl) owl.style.backgroundImage = `url(${owlFrames[0]})`;
  const spin = owl ? setInterval(() => { if (ready < owlFrames.length) return; owl.style.backgroundImage = `url(${owlFrames[++of % owlFrames.length]})`; }, 95) : 0;
  const t0 = performance.now(), DURATION = 1500;
  const tick = setInterval(() => {
    const p = Math.min(100, Math.round((performance.now() - t0) / DURATION * 100));
    pct.textContent = p; bar.style.width = p + '%';
    if (p >= 100) {
      clearInterval(tick);
      setTimeout(() => { clearInterval(spin); pre.classList.add('done'); document.body.classList.remove('locked'); }, 350);
    }
  }, 60);

  /* ---------- MENU ---------- */
  const menu = $('#menu');
  const toggle = open => { menu.classList.toggle('open', open); menu.setAttribute('aria-hidden', !open); document.body.classList.toggle('locked', open); };
  $('#menuOpen').onclick = () => toggle(true);
  $('#menuClose').onclick = () => toggle(false);
  $$('a', menu).forEach(a => a.addEventListener('click', () => toggle(false)));

  /* ---------- 3D fallback ---------- */
  const hm = $('#heroModel');
  const fallback = () => { hm.style.display = 'none'; $('#heroFallback').style.display = 'block'; };
  hm.addEventListener('error', fallback);
  setTimeout(() => { if (!customElements.get('model-viewer')) fallback(); }, 5000);

  /* ---------- TEAM ROLES ---------- */
  const list = $('#deptList');
  const showRole = i => {
    $$('.dept', list).forEach(b => b.classList.toggle('active', b.dataset.i === i));
    $$('.dept__card').forEach(c => { c.hidden = c.dataset.i !== i; });
  };
  list.addEventListener('click', e => { const b = e.target.closest('.dept'); if (b) showRole(b.dataset.i); });
  list.addEventListener('mouseover', e => { const b = e.target.closest('.dept'); if (b && matchMedia('(hover:hover)').matches) showRole(b.dataset.i); });

  /* ---------- SERVICE TABS ---------- */
  const sec = $('#services'), pm = $('#projModel');
  const setTab = k => {
    const panel = $(`.proj-panel[data-p="${k}"]`);
    $$('.proj-panel').forEach(x => { x.hidden = x !== panel; });
    $$('#projTabs .tab').forEach(t => t.classList.toggle('active', t.dataset.p === k));
    sec.style.setProperty('--c', panel.dataset.c);
    if (pm.getAttribute('src') !== panel.dataset.model) pm.src = panel.dataset.model;
  };
  $('#projTabs').addEventListener('click', e => { const t = e.target.closest('.tab'); if (t) setTab(t.dataset.p); });
  setTab($('#projTabs .tab').dataset.p);

  /* ---------- CTA → form topic ---------- */
  $$('[data-topic]').forEach(a => a.addEventListener('click', () => {
    const r = $(`#topics input[value="${a.dataset.topic}"]`); if (r) r.checked = true;
  }));
  $('#form').addEventListener('submit', e => {
    e.preventDefault();
    // TODO: підключіть відправку (Telegram-бот / CRM / email)
    $('#formOk').style.display = 'block'; e.target.reset();
  });

  /* ---------- REVEAL ---------- */
  const io = new IntersectionObserver(es => es.forEach(en => {
    if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
  }), { threshold: .12 });
  $$('.rv').forEach(el => io.observe(el));
})();

/* ---------- CONCEPT VIEWER ---------- */
(() => {
  const v = document.getElementById('viewer');
  if (!v) return;
  const frame = document.getElementById('vFrame'), ifr = document.getElementById('vIframe');
  let last = null;
  const open = btn => {
    last = btn;
    ifr.src = btn.dataset.view;
    document.getElementById('vTitle').textContent = btn.dataset.title;
    document.getElementById('vUrl').textContent = btn.dataset.url;
    document.getElementById('vOpen').href = btn.dataset.view;
    v.hidden = false; document.body.classList.add('locked');
    document.getElementById('vClose').focus();
  };
  const close = () => {
    v.hidden = true; ifr.src = 'about:blank'; document.body.classList.remove('locked');
    if (last) last.focus();
  };
  document.querySelectorAll('[data-view]').forEach(b => b.addEventListener('click', () => open(b)));
  document.getElementById('vClose').addEventListener('click', close);
  document.addEventListener('keydown', e => { if (e.key === 'Escape' && !v.hidden) close(); });
  v.querySelectorAll('[data-dev]').forEach(b => b.addEventListener('click', () => {
    v.querySelectorAll('[data-dev]').forEach(x => x.classList.toggle('on', x === b));
    frame.classList.toggle('mobile', b.dataset.dev === 'mobile');
  }));
})();

/* ---------- NICHE TABS ---------- */
(() => {
  const tabs = document.getElementById('nicheTabs');
  if (!tabs) return;
  const img = document.getElementById('nicheImg');
  const set = btn => {
    tabs.querySelectorAll('.ntab').forEach(b => b.classList.toggle('on', b === btn));
    document.querySelectorAll('.npanel').forEach(p => { p.hidden = p.dataset.n !== btn.dataset.n; });
    img.style.backgroundImage = `url(${btn.dataset.img})`;
  };
  tabs.addEventListener('click', e => { const b = e.target.closest('.ntab'); if (b) set(b); });
  set(tabs.querySelector('.ntab.on'));
})();
