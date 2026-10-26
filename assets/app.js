(() => {
  'use strict';
  const $ = selector => document.querySelector(selector);
  const $$ = selector => [...document.querySelectorAll(selector)];
  const storage = {
    get(key, fallback) { try { return JSON.parse(localStorage.getItem(key)) ?? fallback; } catch { return fallback; } },
    set(key, value) { try { localStorage.setItem(key, JSON.stringify(value)); return true; } catch { return false; } }
  };
  let read = new Set(storage.get('python-notebook-read', []).filter(id => typeof id === 'string'));
  let toastTimer;
  function toast(message) {
    const element = $('.toast');
    element.textContent = message;
    element.classList.add('visible');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => element.classList.remove('visible'), 2600);
  }
  const themeButton = $('[data-theme-toggle]');
  function theme(value) {
    document.documentElement.dataset.theme = value;
    themeButton.setAttribute('aria-label', `Switch to ${value === 'dark' ? 'light' : 'dark'} theme`);
    themeButton.querySelector('span').textContent = value === 'dark' ? 'Light mode' : 'Dark mode';
  }
  const preferred = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  theme(storage.get('python-notebook-theme', preferred));
  themeButton.addEventListener('click', () => {
    const next = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
    theme(next);
    storage.set('python-notebook-theme', next);
  });
  function updateRead() {
    $$('.reading-progress').forEach(el => { el.textContent = `${read.size} / 27 explored`; });
    $$('[data-project-id]').forEach(card => {
      const indicator = card.querySelector('.read-indicator');
      const done = read.has(card.dataset.projectId);
      indicator.textContent = done ? '✓' : '○';
      indicator.setAttribute('aria-label', done ? 'Marked as explored' : 'Not yet explored');
    });
    $$('[data-mark-read]').forEach(button => {
      const done = read.has(button.dataset.markRead);
      button.setAttribute('aria-pressed', String(done));
      button.textContent = done ? '✓ Explored · undo' : '○ Mark as explored';
    });
  }
  $$('[data-mark-read]').forEach(button => button.addEventListener('click', () => {
    const id = button.dataset.markRead;
    if (read.has(id)) read.delete(id); else read.add(id);
    const persisted = storage.set('python-notebook-read', [...read]);
    updateRead();
    toast(persisted ? (read.has(id) ? 'Added to your explored pages.' : 'Removed from your checklist.') : 'Checklist updated for this page. Browser storage is unavailable.');
  }));
  updateRead();
  const search = $('#search');
  if (search) {
    const week = $('#week-filter');
    const kind = $('#kind-filter');
    const cards = $$('[data-project-id]');
    const initial = new URLSearchParams(location.search);
    search.value = initial.get('q') || '';
    week.value = initial.get('week') || '';
    kind.value = initial.get('kind') || '';
    function filter(updateUrl = true) {
      const terms = search.value.toLowerCase().trim().split(/\s+/).filter(Boolean);
      let total = 0;
      cards.forEach(card => {
        const show = (!week.value || card.dataset.week === week.value) && (!kind.value || card.dataset.kind === kind.value) && terms.every(term => card.dataset.search.includes(term));
        card.hidden = !show;
        if (show) total++;
      });
      $('#result-count').textContent = `${total} assignment${total === 1 ? '' : 's'} to explore`;
      $('.empty-state').hidden = total !== 0;
      if (updateUrl) {
        const params = new URLSearchParams();
        if (search.value) params.set('q', search.value);
        if (week.value) params.set('week', week.value);
        if (kind.value) params.set('kind', kind.value);
        try { history.replaceState(null, '', location.pathname + (params.size ? '?' + params : '') + location.hash); } catch { /* Direct file previews can restrict history changes. */ }
      }
    }
    search.addEventListener('input', () => filter());
    week.addEventListener('change', () => filter());
    kind.addEventListener('change', () => filter());
    $('#clear-filters').addEventListener('click', () => { search.value = ''; week.value = ''; kind.value = ''; filter(); search.focus(); });
    $('[data-surprise]').addEventListener('click', () => {
      const available = cards.filter(card => !card.hidden);
      const chosen = available[Math.floor(Math.random() * available.length)];
      if (chosen) location.href = chosen.querySelector('h3 a').href; else toast('Reset the filters to discover a project.');
    });
    filter(false);
  }
  const data = $('#project-data');
  if (data) {
    const project = JSON.parse(data.textContent);
    $('[data-copy-code]').addEventListener('click', async () => {
      try {
        if (navigator.clipboard?.writeText && window.isSecureContext) {
          await navigator.clipboard.writeText(project.source);
        } else {
          const temporary = document.createElement('textarea');
          temporary.value = project.source;
          temporary.style.position = 'fixed';
          temporary.style.left = '-9999px';
          document.body.append(temporary);
          temporary.select();
          const copied = document.execCommand('copy');
          temporary.remove();
          if (!copied) throw new Error('Clipboard unavailable');
        }
        toast('Python code copied.');
      } catch { toast('Select the code to copy it, or download the .py file.'); }
    });
    $('[data-open-source]').addEventListener('click', () => { $('#source').open = true; });
    if (location.hash === '#source' || location.hash.startsWith('#line-')) $('#source').open = true;
  }
})();
