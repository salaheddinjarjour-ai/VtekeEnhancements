/**
 * VTEKE Global Translation Engine
 * Single source of truth for all page translations.
 * Usage: include this script on every page, use data-i18n="key.path" attributes.
 */

(function() {
  'use strict';

  var translations = {};
  var currentLang = 'en';

  /** Resolve a dot-path key like "nav.home" from the translations object */
  function getValue(obj, path) {
    return path.split('.').reduce(function(o, k) {
      return (o && o[k] !== undefined) ? o[k] : null;
    }, obj);
  }

  /** Apply all translations to data-i18n elements on the page */
  function applyTranslations() {
    // Text content
    document.querySelectorAll('[data-i18n]').forEach(function(el) {
      var key = el.getAttribute('data-i18n');
      var val = getValue(translations, key);
      if (val) el.textContent = val;
    });

    // Placeholder attributes (for input/textarea)
    document.querySelectorAll('[data-i18n-placeholder]').forEach(function(el) {
      var key = el.getAttribute('data-i18n-placeholder');
      var val = getValue(translations, key);
      if (val) el.placeholder = val;
    });

    // Aria-label attributes
    document.querySelectorAll('[data-i18n-aria]').forEach(function(el) {
      var key = el.getAttribute('data-i18n-aria');
      var val = getValue(translations, key);
      if (val) el.setAttribute('aria-label', val);
    });

    // Update html lang attribute
    document.documentElement.lang = currentLang;

    // Update language button display
    var flagEl = document.getElementById('currentLangFlag');
    var textEl = document.getElementById('currentLangText');
    if (textEl) textEl.textContent = currentLang.toUpperCase();
    if (flagEl) _vtekeSetFlagEl(flagEl, currentLang);

    // Update active state on dropdown items
    document.querySelectorAll('.lang-dropdown-item').forEach(function(item) {
      var onclick = item.getAttribute('onclick') || '';
      item.classList.toggle('active', onclick.includes("'" + currentLang + "'"));
    });

    // Update mobile lang buttons
    var btnEN = document.getElementById('mobileLangEN');
    var btnTR = document.getElementById('mobileLangTR');
    if (btnEN) btnEN.classList.toggle('active', currentLang === 'en');
    if (btnTR) btnTR.classList.toggle('active', currentLang === 'tr');
  }

  /** Load a language's JSON file and apply */
  function loadTranslations(lang) {
    // Normalise — only support en/tr, fall back to en
    var supported = ['en', 'tr'];
    lang = supported.indexOf(lang) > -1 ? lang : 'en';

    currentLang = lang;
    localStorage.setItem('vteke_language', lang);

    // If we already have it cached, just apply
    if (window._vtekeTranslationCache && window._vtekeTranslationCache[lang]) {
      translations = window._vtekeTranslationCache[lang];
      applyTranslations();
      return;
    }

    // Detect base path for the translations folder
    var basePath = '/translations/';
    // If running from file:// or non-root, figure out the relative path
    if (window.location.protocol === 'file:' || window.location.pathname.includes('/translations/') === false) {
      // Try to detect the project root by finding the vteke project
      basePath = _detectBasePath() + 'translations/';
    }

    fetch(basePath + lang + '.json')
      .then(function(res) {
        if (!res.ok) throw new Error('Translation file not found: ' + lang);
        return res.json();
      })
      .then(function(data) {
        if (!window._vtekeTranslationCache) window._vtekeTranslationCache = {};
        window._vtekeTranslationCache[lang] = data;
        translations = data;
        applyTranslations();
      })
      .catch(function(err) {
        console.warn('[VTEKE i18n] Failed to load translations for "' + lang + '":', err);
        // Fallback: if TR failed, try EN
        if (lang !== 'en') loadTranslations('en');
      });
  }

  /** Detect base path relative to current page location */
  function _detectBasePath() {
    var path = window.location.pathname;
    // Count how many directories deep we are
    var parts = path.split('/').filter(Boolean);
    var depth = parts.length > 0 && !path.endsWith('/') ? parts.length - 1 : parts.length;
    return depth > 0 ? '../'.repeat(depth) : './';
  }

  /** Global entry points */
  window.setLanguage = function(lang) {
    loadTranslations(lang);
  };

  window.toggleLanguageDropdown = function() {
    var wrapper = document.getElementById('langDropdown');
    if (wrapper) {
      var isActive = wrapper.classList.toggle('active');
      var btn = wrapper.querySelector('.lang-dropdown-btn');
      if (btn) btn.setAttribute('aria-expanded', isActive ? 'true' : 'false');
    }
  };

  // Close dropdown on outside click
  document.addEventListener('click', function(e) {
    var wrapper = document.getElementById('langDropdown');
    if (wrapper && !wrapper.contains(e.target)) {
      wrapper.classList.remove('active');
      var btn = wrapper.querySelector('.lang-dropdown-btn');
      if (btn) btn.setAttribute('aria-expanded', 'false');
    }
  });

  // Auto-load on DOMContentLoaded
  document.addEventListener('DOMContentLoaded', function() {
    var saved = localStorage.getItem('vteke_language') || 'en';
    loadTranslations(saved);
  });

})();
