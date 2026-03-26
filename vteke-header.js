
(function() {
  'use strict';

  const CONFIG = {
    scrollThreshold: 50,
    selectors: {
      header: '.vteke-pro-header-main-container',
      spaceReserver: '.vteke-header-space-reserver',
      mobileToggle: '#vtekeMenuToggleBtn',
      mobileClose: '#vtekeCloseMenuBtn',
      mobileOverlay: '#vtekeMobileMenuOverlay',
      mobileContainer: '#vtekeMobileMenuContainer',
      mobileDropdownToggle: '#vtekeMobileProductsToggle',
      mobileDropdownMenu: '#vtekeMobileProductsMenu',
      mobileDropdownContainer: '.vteke-pro-mobile-dropdown-container'
    }
  };

  let lastScrollY = 0;
  let ticking = false;
  const elements = {};

  function cacheElements() {
    elements.header = document.querySelector(CONFIG.selectors.header);
    elements.spaceReserver = document.querySelector(CONFIG.selectors.spaceReserver);
    elements.mobileToggle = document.querySelector(CONFIG.selectors.mobileToggle);
    elements.mobileClose = document.querySelector(CONFIG.selectors.mobileClose);
    elements.mobileOverlay = document.querySelector(CONFIG.selectors.mobileOverlay);
    elements.mobileContainer = document.querySelector(CONFIG.selectors.mobileContainer);
    elements.mobileDropdownToggle = document.querySelector(CONFIG.selectors.mobileDropdownToggle);
    elements.mobileDropdownMenu = document.querySelector(CONFIG.selectors.mobileDropdownMenu);
    elements.mobileDropdownContainer = document.querySelector(CONFIG.selectors.mobileDropdownContainer);
  }

  function updateHeaderHeight() {
    if (elements.header && elements.spaceReserver) {
      elements.spaceReserver.style.height = `${elements.header.offsetHeight}px`;
    }
  }

  function onScroll() {
    const currentScrollY = window.scrollY;
    if (!elements.header) return;

    // Hide on Scroll Down
    if (currentScrollY > lastScrollY && currentScrollY > CONFIG.scrollThreshold) {
      elements.header.classList.add('vteke-header-hidden');
      elements.header.classList.remove('vteke-header-scrolled');
    } 
    // Show on Scroll Up
    else {
      elements.header.classList.remove('vteke-header-hidden');
      if (currentScrollY > CONFIG.scrollThreshold) {
        elements.header.classList.add('vteke-header-scrolled');
      } else {
        elements.header.classList.remove('vteke-header-scrolled');
      }
    }
    lastScrollY = currentScrollY;
    ticking = false;
  }

  function handleScrollRequest() {
    if (!ticking) {
      window.requestAnimationFrame(onScroll);
      ticking = true;
    }
  }

  function toggleMobileMenu(isOpen) {
    if (!elements.mobileContainer || !elements.mobileOverlay) return;
    const body = document.body;

    if (isOpen) {
      elements.mobileContainer.classList.add('vteke-menu-active');
      elements.mobileOverlay.classList.add('vteke-menu-active');
      elements.mobileOverlay.setAttribute('aria-hidden', 'false');
      elements.mobileContainer.setAttribute('aria-hidden', 'false');
      
      // Lock Body Scroll
      body.style.overflow = 'hidden';
      body.style.position = 'fixed';
      body.style.width = '100%';
      body.style.top = `-${window.scrollY}px`;
      if(elements.mobileClose) elements.mobileClose.focus();
    } else {
      elements.mobileContainer.classList.remove('vteke-menu-active');
      elements.mobileOverlay.classList.remove('vteke-menu-active');
      elements.mobileOverlay.setAttribute('aria-hidden', 'true');
      elements.mobileContainer.setAttribute('aria-hidden', 'true');
      
      // Unlock Body Scroll
      const scrollY = body.style.top;
      body.style.overflow = '';
      body.style.position = '';
      body.style.width = '';
      body.style.top = '';
      window.scrollTo(0, parseInt(scrollY || '0', 10) * -1);
      if(elements.mobileToggle) elements.mobileToggle.focus();
    }
  }

  function toggleMobileDropdown() {
    if (!elements.mobileDropdownContainer) return;
    const isOpen = elements.mobileDropdownContainer.classList.contains('vteke-mobile-dropdown-open');
    
    if (isOpen) {
      elements.mobileDropdownContainer.classList.remove('vteke-mobile-dropdown-open');
      if(elements.mobileDropdownToggle) elements.mobileDropdownToggle.setAttribute('aria-expanded', 'false');
    } else {
      elements.mobileDropdownContainer.classList.add('vteke-mobile-dropdown-open');
      if(elements.mobileDropdownToggle) elements.mobileDropdownToggle.setAttribute('aria-expanded', 'true');
    }
  }

  function setupEventListeners() {
    // Passive scroll for performance
    window.addEventListener('scroll', handleScrollRequest, { passive: true });
    
    window.addEventListener('resize', () => {
      clearTimeout(window.vtekeResizeTimer);
      window.vtekeResizeTimer = setTimeout(updateHeaderHeight, 100);
      if (window.innerWidth > 992) toggleMobileMenu(false);
    }, { passive: true });

    if (elements.mobileToggle) {
      elements.mobileToggle.addEventListener('click', (e) => {
        e.preventDefault();
        toggleMobileMenu(true);
      });
    }

    if (elements.mobileClose) {
      elements.mobileClose.addEventListener('click', (e) => {
        e.preventDefault();
        toggleMobileMenu(false);
      });
    }

    if (elements.mobileOverlay) {
      elements.mobileOverlay.addEventListener('click', () => toggleMobileMenu(false));
    }

    if (elements.mobileDropdownToggle) {
      elements.mobileDropdownToggle.addEventListener('click', (e) => {
        e.preventDefault();
        toggleMobileDropdown();
      });
    }

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && elements.mobileContainer && elements.mobileContainer.classList.contains('vteke-menu-active')) {
        toggleMobileMenu(false);
      }
    });
  }

  function injectFavicon() {
    if (!document.querySelector('link[rel~="icon"]')) {
      var link = document.createElement('link');
      link.rel = 'icon';
      link.type = 'image/png';
      // Resolve path relative to where header JS lives (root of site)
      var script = document.currentScript ||
        document.querySelector('script[src*="vteke-header"]');
      var base = script ? script.src.replace(/vteke-header\.js.*$/, '') : '/';
      link.href = base + 'favicon.ico';
      document.head.appendChild(link);
    }
  }

  function init() {
    injectFavicon();
    cacheElements();
    if (!elements.header) return;
    updateHeaderHeight();
    setupEventListeners();
    if (window.scrollY > CONFIG.scrollThreshold) {
      elements.header.classList.add('vteke-header-scrolled');
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();

/* ─── SVG Flag helpers (reliable on all OS/browsers, no emoji font needed) ─── */
var _vtekeFlagSVG = {
  en: '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 60 30" width="18" height="18"><clipPath id="a"><path d="M0 0v30h60V0z"/></clipPath><clipPath id="b"><path d="M30 15h30v15zM30 15H0v15zM30 15h30V0zM30 15H0V0z"/></clipPath><g clip-path="url(#a)"><path d="M0 0v30h60V0z" fill="#012169"/><path d="M0 0l60 30m0-30L0 30" stroke="#fff" stroke-width="6"/><path d="M0 0l60 30m0-30L0 30" clip-path="url(#b)" stroke="#C8102E" stroke-width="4"/><path d="M30 0v30M0 15h60" stroke="#fff" stroke-width="10"/><path d="M30 0v30M0 15h60" stroke="#C8102E" stroke-width="6"/></g></svg>',
  tr: '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 30 20" width="18" height="12"><rect width="30" height="20" fill="#E30A17"/><circle cx="10" cy="10" r="6" fill="#fff"/><circle cx="11.5" cy="10" r="4.8" fill="#E30A17"/><polygon points="16.5,10 18.6,10.7 17.3,8.8 17.3,11.2 18.6,9.3" fill="#fff"/></svg>'
};

function _vtekeSetFlagEl(el, lang) {
  if (!el) return;
  // Replace any existing SVG or text
  el.innerHTML = _vtekeFlagSVG[lang] || _vtekeFlagSVG['en'];
  el.style.display = 'inline-flex';
  el.style.alignItems = 'center';
  el.style.lineHeight = '1';
}

/* ─── Language Dropdown (global, used by all pages via vteke-header.js) ─── */
function toggleLanguageDropdown() {
  var wrapper = document.getElementById('langDropdown');
  if (!wrapper) return;
  wrapper.classList.toggle('active');
  var btn = wrapper.querySelector('.lang-dropdown-btn');
  if (btn) btn.setAttribute('aria-expanded', wrapper.classList.contains('active'));
}

// Close when clicking anywhere outside the dropdown
document.addEventListener('click', function(e) {
  var wrapper = document.getElementById('langDropdown');
  if (wrapper && !wrapper.contains(e.target)) {
    wrapper.classList.remove('active');
    var btn = wrapper.querySelector('.lang-dropdown-btn');
    if (btn) btn.setAttribute('aria-expanded', 'false');
  }
});

/* ─── setLanguage — shared language switcher for all pages ─── */
function setLanguage(lang) {
  localStorage.setItem('vteke_language', lang);

  // Update html lang attribute
  document.documentElement.lang = lang;

  // Update all data-lang-en / data-lang-tr elements
  document.querySelectorAll('[data-lang-en]').forEach(function(el) {
    el.textContent = lang === 'tr' ? (el.getAttribute('data-lang-tr') || el.textContent) : (el.getAttribute('data-lang-en') || el.textContent);
  });

  // Update desktop language button SVG flag + text
  var flagEl = document.getElementById('currentLangFlag');
  var textEl = document.getElementById('currentLangText');
  _vtekeSetFlagEl(flagEl, lang);
  if (textEl) textEl.textContent = lang === 'tr' ? 'TR' : 'EN';

  // Update mobile language button active states
  var btnEN = document.getElementById('mobileLangEN');
  var btnTR = document.getElementById('mobileLangTR');
  if (btnEN) btnEN.classList.toggle('active', lang === 'en');
  if (btnTR) btnTR.classList.toggle('active', lang === 'tr');

  // Update desktop dropdown item active states
  document.querySelectorAll('.lang-dropdown-item').forEach(function(item) {
    var isEn = item.textContent.trim().toLowerCase().includes('english');
    item.classList.toggle('active', (lang === 'en' && isEn) || (lang === 'tr' && !isEn));
  });

  // Close the dropdown
  var wrapper = document.getElementById('langDropdown');
  if (wrapper) wrapper.classList.remove('active');
}

// Apply saved language on page load + inject SVGs into initial flag elements
(function() {
  var saved = localStorage.getItem('vteke_language') || 'en';
  // Inject SVG into flag elements even before setLanguage is called
  document.addEventListener('DOMContentLoaded', function() {
    _vtekeSetFlagEl(document.getElementById('currentLangFlag'), saved);
    var textEl = document.getElementById('currentLangText');
    if (textEl) textEl.textContent = saved === 'tr' ? 'TR' : 'EN';
    // Apply translations on initial page load
    applyTranslations(saved);
  });
  if (saved && saved !== 'en') setLanguage(saved);
})();

// Global translation function - applies to all [data-lang-en]/[data-lang-tr] elements
function applyTranslations(lang) {
  document.querySelectorAll('[data-lang-en]').forEach(function(el) {
    var translated = el.getAttribute('data-lang-' + lang);
    if (translated) {
      el.textContent = translated;
    }
  });
}
