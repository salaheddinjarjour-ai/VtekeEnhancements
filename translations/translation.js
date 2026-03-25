/**
 * VTEKE Global Translation Engine v2
 * Clean, simple, no path detection complexity.
 */
(function () {
  'use strict';

  var _cache = {};
  var _lang = 'en';

  function get(obj, path) {
    return path.split('.').reduce(function (o, k) {
      return o && o[k] !== undefined ? o[k] : null;
    }, obj);
  }

  function apply(dict) {
    document.querySelectorAll('[data-i18n]').forEach(function (el) {
      var v = get(dict, el.getAttribute('data-i18n'));
      if (v) el.textContent = v;
    });
    document.querySelectorAll('[data-i18n-placeholder]').forEach(function (el) {
      var v = get(dict, el.getAttribute('data-i18n-placeholder'));
      if (v) el.placeholder = v;
    });
    document.documentElement.lang = _lang;

    // Update dropdown button display
    var flagEl = document.getElementById('currentLangFlag');
    var textEl = document.getElementById('currentLangText');
    if (textEl) textEl.textContent = _lang.toUpperCase();
    if (flagEl && _lang === 'tr') {
      flagEl.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 30 20" width="20" height="14" style="display:inline-block;vertical-align:middle;border-radius:2px"><rect width="30" height="20" fill="#E30A17"/><circle cx="10" cy="10" r="6" fill="#fff"/><circle cx="11.5" cy="10" r="4.8" fill="#E30A17"/><polygon points="16.5,10 18.6,10.7 17.3,8.8 17.3,11.2 18.6,9.3" fill="#fff"/></svg>';
    } else if (flagEl && _lang === 'en') {
      flagEl.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 60 30" width="20" height="14" style="display:inline-block;vertical-align:middle;border-radius:2px"><clipPath id="vtek-a"><path d="M0 0v30h60V0z"/></clipPath><clipPath id="vtek-b"><path d="M30 15h30v15zM30 15H0v15zM30 15h30V0zM30 15H0V0z"/></clipPath><g clip-path="url(#vtek-a)"><path d="M0 0v30h60V0z" fill="#012169"/><path d="M0 0l60 30m0-30L0 30" stroke="#fff" stroke-width="6"/><path d="M0 0l60 30m0-30L0 30" clip-path="url(#vtek-b)" stroke="#C8102E" stroke-width="4"/><path d="M30 0v30M0 15h60" stroke="#fff" stroke-width="10"/><path d="M30 0v30M0 15h60" stroke="#C8102E" stroke-width="6"/></g></svg>';
    }

    // Active states
    document.querySelectorAll('.lang-dropdown-item').forEach(function (item) {
      var oc = item.getAttribute('onclick') || '';
      item.classList.toggle('active', oc.indexOf("'" + _lang + "'") > -1);
    });
    var btnEN = document.getElementById('mobileLangEN');
    var btnTR = document.getElementById('mobileLangTR');
    if (btnEN) btnEN.classList.toggle('active', _lang === 'en');
    if (btnTR) btnTR.classList.toggle('active', _lang === 'tr');
  }

  function loadLang(lang) {
    lang = (lang === 'tr') ? 'tr' : 'en';
    _lang = lang;
    localStorage.setItem('vteke_language', lang);

    if (_cache[lang]) { apply(_cache[lang]); return; }

    // Build absolute URL — works from any path depth on localhost or cPanel
    var base = window.location.origin + '/translations/';
    // If served from a subfolder (e.g. cPanel /vteke/), detect it
    var pathParts = window.location.pathname.split('/').filter(Boolean);
    // Find where the html files are — look backwards for known pages
    // If first segment is NOT a known page, it's a subfolder prefix
    var knownPages = ['index.html','aboutus.html','products.html','contactus.html',
                      'news.html','catalog.html','certificates.html'];
    var firstSeg = (pathParts[0] || '').toLowerCase();
    if (firstSeg && knownPages.indexOf(firstSeg) === -1 && firstSeg.indexOf('.html') === -1) {
      // We're in a subfolder like /vteke/
      base = window.location.origin + '/' + pathParts[0] + '/translations/';
    }

    fetch(base + lang + '.json')
      .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
      .then(function (d) { _cache[lang] = d; apply(d); })
      .catch(function (e) {
        console.warn('[i18n] fetch failed:', e, 'trying relative path');
        // Fallback: relative path (works when served from root)
        fetch('translations/' + lang + '.json')
          .then(function (r) { return r.json(); })
          .then(function (d) { _cache[lang] = d; apply(d); })
          .catch(function (e2) { console.error('[i18n] All fetch attempts failed', e2); });
      });
  }

  // Global API
  window.setLanguage = function (lang) { loadLang(lang); };
  window.toggleLanguageDropdown = function () {
    var w = document.getElementById('langDropdown');
    if (w) {
      var isOpen = w.classList.toggle('active');
      var btn = w.querySelector('.lang-dropdown-btn');
      if (btn) btn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    }
  };

  // Close on outside click
  document.addEventListener('click', function (e) {
    var w = document.getElementById('langDropdown');
    if (w && !w.contains(e.target)) {
      w.classList.remove('active');
      var btn = w.querySelector('.lang-dropdown-btn');
      if (btn) btn.setAttribute('aria-expanded', 'false');
    }
  });

  // Auto-load saved language on every page load
  document.addEventListener('DOMContentLoaded', function () {
    var saved = localStorage.getItem('vteke_language') || 'en';
    if (saved !== 'en') loadLang(saved);  // EN is default, only fetch if TR
  });

})();
