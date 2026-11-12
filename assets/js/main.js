/* ADV — спільний скрипт для всіх сторінок. Кожен блок запускається лише якщо на сторінці є його елементи. */
(() => {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const base = document.body.dataset.base || '';
  const lang = (document.documentElement.lang || 'uk').slice(0, 2);

  /* ---------- PRELOADER (головна) ---------- */
  const pre = $('#preloader');
  if (pre) {
    const pct = $('#prePct'), bar = $('#preBar'), owl = $('#preOwl');
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
  } else {
    document.body.classList.remove('locked');
  }

  /* ---------- HEADER: фон при прокрутці + активний пункт ---------- */
  const header = $('.header');
  if (header) {
    const onScroll = () => header.classList.toggle('scrolled', scrollY > 40);
    addEventListener('scroll', onScroll, { passive: true }); onScroll();
    const links = $$('.hnav a[href*="#"]').filter(a => a.hash && $(a.hash));
    if (links.length && 'IntersectionObserver' in window) {
      const map = new Map(links.map(a => [$(a.hash), a]));
      const so = new IntersectionObserver(es => es.forEach(en => {
        const a = map.get(en.target); if (!a) return;
        if (en.isIntersecting) { links.forEach(l => l.classList.remove('on')); a.classList.add('on'); }
      }), { rootMargin: '-45% 0px -50% 0px' });
      map.forEach((_, sec) => so.observe(sec));
    }
  }

  /* ---------- MENU (мобільне) ---------- */
  const menu = $('#menu');
  if (menu) {
    const toggle = open => { menu.classList.toggle('open', open); menu.setAttribute('aria-hidden', !open); document.body.classList.toggle('locked', open); $('#menuOpen')?.setAttribute('aria-expanded', open); };
    $('#menuOpen')?.addEventListener('click', () => toggle(true));
    $('#menuClose')?.addEventListener('click', () => toggle(false));
    $$('a', menu).forEach(a => a.addEventListener('click', () => toggle(false)));
    document.addEventListener('keydown', e => { if (e.key === 'Escape' && menu.classList.contains('open')) toggle(false); });
  }

  /* ---------- 3D fallback ---------- */
  const hm = $('#heroModel');
  if (hm) {
    const fallback = () => { hm.style.display = 'none'; const f = $('#heroFallback'); if (f) f.style.display = 'block'; };
    hm.addEventListener('error', fallback);
    setTimeout(() => { if (!customElements.get('model-viewer')) fallback(); }, 5000);
  }

  /* ---------- TEAM ROLES ---------- */
  const list = $('#deptList');
  if (list) {
    const showRole = i => {
      $$('.dept', list).forEach(b => b.classList.toggle('active', b.dataset.i === i));
      $$('.dept__card').forEach(c => { c.hidden = c.dataset.i !== i; });
    };
    list.addEventListener('click', e => { const b = e.target.closest('.dept'); if (b) showRole(b.dataset.i); });
    list.addEventListener('mouseover', e => { const b = e.target.closest('.dept'); if (b && matchMedia('(hover:hover)').matches) showRole(b.dataset.i); });
  }

  /* ---------- SERVICE TABS ---------- */
  const tabsEl = $('#projTabs');
  if (tabsEl) {
    const sec = $('#services'), pm = $('#projModel');
    const setTab = k => {
      const panel = $(`.proj-panel[data-p="${k}"]`);
      $$('.proj-panel').forEach(x => { x.hidden = x !== panel; });
      $$('#projTabs .tab').forEach(t => t.classList.toggle('active', t.dataset.p === k));
      sec.style.setProperty('--c', panel.dataset.c);
      if (pm && pm.getAttribute('src') !== panel.dataset.model) pm.src = panel.dataset.model;
    };
    tabsEl.addEventListener('click', e => { const t = e.target.closest('.tab'); if (t) setTab(t.dataset.p); });
    setTab($('#projTabs .tab').dataset.p);
  }

  /* ---------- CTA → form topic ---------- */
  $$('[data-topic]').forEach(a => a.addEventListener('click', () => {
    const r = $(`#topics input[value="${a.dataset.topic}"]`); if (r) r.checked = true;
  }));
  /* ---------- UTM: запам'ятати мітки реклами на час візиту ---------- */
  const UTM = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content'];
  try {
    const qs = new URLSearchParams(location.search);
    if (UTM.some(k => qs.get(k))) sessionStorage.setItem('adv_utm', JSON.stringify(Object.fromEntries(UTM.map(k => [k, qs.get(k) || '']))));
  } catch (e) { /* storage недоступний — не страшно */ }

  /* ---------- ФОРМА ЗАЯВКИ → Google Apps Script (таблиця + Telegram + пошта) ---------- */
  const form = $('#form');
  if (form) {
    const t0 = Date.now();
    const btn = $('button[type=submit]', form);
    const show = id => ['formOk', 'formErr', 'formMail'].forEach(x => { const el = $('#' + x); if (el) el.hidden = x !== id; });
    $('#formAgain')?.addEventListener('click', () => { form.classList.remove('is-sent'); show(null); $('input[name=name]', form)?.focus(); });
    form.addEventListener('submit', async e => {
      e.preventDefault();
      if (!form.reportValidity()) return;
      const fd = new FormData(form);
      fd.set('t', String(t0));
      fd.set('lang', form.dataset.lang || lang);
      fd.set('page', location.pathname + location.hash);
      try { const u = JSON.parse(sessionStorage.getItem('adv_utm') || '{}'); UTM.forEach(k => fd.set(k, u[k] || '')); } catch (e2) { /* ignore */ }
      const endpoint = form.dataset.endpoint;

      if (!endpoint) {
        // запасний варіант, поки не підключено Apps Script: лист у поштовий застосунок
        const topic = $('#topics input:checked')?.nextElementSibling?.textContent || '';
        const body = [`${topic}`, `${fd.get('name')}`, `${fd.get('contact')}`, `${fd.get('budget') || ''}`, '', `${fd.get('msg') || ''}`].join('\n');
        location.href = `mailto:${form.dataset.email}?subject=${encodeURIComponent('ADV · ' + topic + ' — ' + fd.get('name'))}&body=${encodeURIComponent(body)}`;
        show('formMail');
        return;
      }

      btn.disabled = true; btn.classList.add('is-loading'); btn.textContent = btn.dataset.sending;
      try {
        const res = await fetch(endpoint, { method: 'POST', body: new URLSearchParams(fd) });
        const data = await res.json().catch(() => ({}));
        if (!res.ok || data.ok === false) throw new Error(data.error || res.status);
        const done = $('#formOk'), h = $('h3', done), nm = String(fd.get('name') || '').trim().split(/\s+/)[0];
        h.textContent = nm ? h.dataset.tpl.replace('{name}', nm) : h.dataset.tpl.replace(/,?\s*\{name\}/, '');
        form.reset(); form.classList.add('is-sent'); show('formOk');
        done.focus({ preventScroll: true });
        done.scrollIntoView({ behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block: 'center' });
      } catch (err) {
        show('formErr');
      } finally {
        btn.disabled = false; btn.classList.remove('is-loading'); btn.textContent = btn.dataset.label;
      }
    });
  }

  /* ---------- REVEAL ---------- */
  const io = new IntersectionObserver(es => es.forEach(en => {
    if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
  }), { threshold: .12 });
  window.__advReveal = el => io.observe(el);
  $$('.rv').forEach(el => io.observe(el));

  /* ---------- PRICE: пошук і навігація ---------- */
  const priceSearch = $('#priceSearch');
  if (priceSearch) {
    const rows = $$('.ptable tr[data-q]');
    const empty = $('#priceEmpty');
    priceSearch.addEventListener('input', () => {
      const q = priceSearch.value.trim().toLowerCase(); let shown = 0;
      rows.forEach(r => { const ok = !q || r.dataset.q.includes(q); r.hidden = !ok; if (ok) shown++; });
      $$('.pgroup').forEach(g => { g.hidden = !$$('tr[data-q]', g).some(r => !r.hidden); });
      $$('.pcat').forEach(c => { c.hidden = !$$('.pgroup', c).some(g => !g.hidden); });
      if (empty) empty.hidden = shown > 0;
    });
    const navLinks = $$('.pnav a');
    const so = new IntersectionObserver(es => es.forEach(en => {
      if (!en.isIntersecting) return;
      navLinks.forEach(a => a.classList.toggle('on', a.hash === '#' + en.target.id));
    }), { rootMargin: '-30% 0px -60% 0px' });
    $$('.pcat').forEach(c => so.observe(c));
  }

  /* ---------- PROJECTS: рендер з data/projects.json ---------- */
  const grid = $('#projectsGrid');
  if (grid) {
    const T = lang === 'en'
      ? { all: 'All', concept: 'Concept', client: 'Client project', view: 'View project', open: 'Open', empty: 'No projects in this category yet.', err: 'Could not load projects.', cats: { business: 'Business websites', landing: 'Landing pages', ecommerce: 'E-commerce', app: 'Apps & systems', bot: 'Bots & automation', other: 'Other' } }
      : { all: 'Усі', concept: 'Концепт', client: 'Клієнтський проєкт', view: 'Переглянути', open: 'Відкрити', empty: 'У цій категорії поки немає проєктів.', err: 'Не вдалося завантажити проєкти.', cats: { business: 'Сайти для бізнесу', landing: 'Лендінги', ecommerce: 'E-commerce', app: 'Застосунки й системи', bot: 'Боти й автоматизація', other: 'Інше' } };
    const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
    const abs = u => /^(https?:)?\/\//.test(u) ? u : base + u;
    const pick = v => (v && typeof v === 'object') ? (v[lang] || v.uk || v.en || '') : (v || '');
    const filters = $('#projectFilters'), count = $('#projectsCount');
    let items = [], cat = 'all';
    const render = () => {
      const list = items.filter(p => cat === 'all' || p.category === cat);
      count && (count.textContent = list.length);
      grid.innerHTML = list.length ? list.map(p => {
        const url = lang === 'en' && p.url_en ? p.url_en : p.url;
        const isLocal = url && !/^(https?:)?\/\//.test(url);
        const tag = p.type === 'concept' ? T.concept : T.client;
        return `<article class="pcard rv">
          <a class="pcard__shot" href="${esc(abs(url || '#'))}" ${isLocal ? '' : 'target="_blank" rel="noopener"'}>
            <img src="${esc(abs(p.cover))}" alt="${esc(p.title)}" loading="lazy" width="1280" height="720">
            <span class="pcard__badge ${p.type === 'concept' ? 'is-concept' : 'is-client'}">${tag}</span>
            <span class="pcard__go">${T.view} ↗</span>
          </a>
          <div class="pcard__meta"><span>${esc(T.cats[p.category] || T.cats.other)}</span><span>${esc(p.year || '')}${p.author ? ' · ' + esc(p.author) : ''}</span></div>
          <h3 class="h">${esc(p.title)}</h3>
          <p>${esc(pick(p.summary))}</p>
          ${(() => { const tg = Array.isArray(p.tags) ? p.tags : (p.tags ? (p.tags[lang] || p.tags.uk || []) : []); return tg.length ? `<div class="case__chips">${tg.map(t => `<span>${esc(t)}</span>`).join('')}</div>` : ''; })()}
        </article>`;
      }).join('') : `<p class="projects__empty">${T.empty}</p>`;
      $$('.rv', grid).forEach(el => io.observe(el));
    };
    const renderFilters = () => {
      const cats = [...new Set(items.map(p => p.category || 'other'))];
      filters.innerHTML = [`<button type="button" class="ntab${cat === 'all' ? ' on' : ''}" data-c="all">${T.all} <i>${items.length}</i></button>`]
        .concat(cats.map(c => `<button type="button" class="ntab${cat === c ? ' on' : ''}" data-c="${esc(c)}">${esc(T.cats[c] || c)} <i>${items.filter(p => p.category === c).length}</i></button>`)).join('');
    };
    filters.addEventListener('click', e => { const b = e.target.closest('[data-c]'); if (!b) return; cat = b.dataset.c; renderFilters(); render(); });
    fetch(`${base}data/projects.json?v=${Date.now()}`)
      .then(r => r.json())
      .then(d => {
        items = (d.projects || []).filter(p => p && p.title && p.cover && !p.hidden)
          .sort((a, b) => (b.year || 0) - (a.year || 0) || (a.type === 'concept') - (b.type === 'concept'));
        renderFilters(); render();
      })
      .catch(() => { grid.innerHTML = `<p class="projects__empty">${T.err}</p>`; });
  }
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
