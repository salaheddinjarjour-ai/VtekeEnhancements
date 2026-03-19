#!/usr/bin/env python3
"""
Update Products.html category cards to navigate to existing category pages
and also update the sidebar buttons to link to those pages.
"""

import re

ROOT = "/Users/marwaghalayini/Salaheddin's Work/Websites/vteke_Upgrades"

# ─── Map category key → existing page URL ───────────────────────────────────
CATEGORY_URLS = {
    'transformers': 'Current Transformer.html',
    'relays':       'protection relay.html',
    'meters':       'analog meters.html',       # covers both analog+digital
    'analyzers':    'energy analyzer.html',
    'power':        'power supply.html',
    'transducers':  'volt transducer.html',
}

# ─── 1. Update Products.html ─────────────────────────────────────────────────
products_path = f"{ROOT}/Products.html"
with open(products_path, 'r', encoding='utf-8') as f:
    html = f.read()

# A) Replace category-card onclick → window.location.href navigation
# Old: <div class="category-card" onclick="filterProducts('${cat.key}')">
# New: Use href on an <a> tag instead, passing URL via categoriesConfig

# Add href field to categoriesConfig (find the config object and add href)
old_configs = {
    'transformers': "image: '/vtekeimg/Current Transformers/TK30N.png'\n    }",
    'relays':       "image: '/vtekeimg/electronic relays/pcr-04.jpg'\n    }",
    'meters':       "image: '/vtekeimg/Analog Meters/AK-V96-500.jpg'\n    }",
    'analyzers':    "image: '/vtekeimg/Energy Analyzer/EA-C1.png'\n    }",
    'power':        "image: '/vtekeimg/Power Supply/PSU-2406.jpg'\n    }",
    'transducers':  "image: '/vtekeimg/favicon.png'\n    }",
}
new_configs = {
    'transformers': "image: '/vtekeimg/Current Transformers/TK30N.png',\n        href: 'Current Transformer.html'\n    }",
    'relays':       "image: '/vtekeimg/electronic relays/pcr-04.jpg',\n        href: 'protection relay.html'\n    }",
    'meters':       "image: '/vtekeimg/Analog Meters/AK-V96-500.jpg',\n        href: 'analog meters.html'\n    }",
    'analyzers':    "image: '/vtekeimg/Energy Analyzer/EA-C1.png',\n        href: 'energy analyzer.html'\n    }",
    'power':        "image: '/vtekeimg/Power Supply/PSU-2406.jpg',\n        href: 'power supply.html'\n    }",
    'transducers':  "image: '/vtekeimg/favicon.png',\n        href: 'volt transducer.html'\n    }",
}
for key in old_configs:
    html = html.replace(old_configs[key], new_configs[key])

# B) Update renderCategories() to use <a href> instead of onclick div
old_render = """    grid.innerHTML = categoriesConfig.map(cat => `
        <div class="category-card" onclick="filterProducts('${cat.key}')">
            <div class="category-card-image">
                <img src="${cat.image}" alt="${cat.label}"
                     onerror="this.src='/vtekeimg/favicon.png'; this.style.objectFit='contain'; this.style.padding='1.5rem';">
            </div>
            <div class="category-card-body">
                <h3 class="category-card-title">${cat.label}</h3>
                <p class="category-card-desc">${cat.desc}</p>
                <span class="category-card-btn">View Products →</span>
            </div>
        </div>
    `).join('');"""

new_render = """    grid.innerHTML = categoriesConfig.map(cat => `
        <a class="category-card" href="${cat.href}">
            <div class="category-card-image">
                <img src="${cat.image}" alt="${cat.label}"
                     onerror="this.src='/vtekeimg/favicon.png'; this.style.objectFit='contain'; this.style.padding='1.5rem';">
            </div>
            <div class="category-card-body">
                <h3 class="category-card-title">${cat.label}</h3>
                <p class="category-card-desc">${cat.desc}</p>
                <span class="category-card-btn">View Products →</span>
            </div>
        </a>
    `).join('');"""

html = html.replace(old_render, new_render)

# C) Update sidebar buttons to link to category pages instead of filtering
sidebar_replacements = [
    (
        'onclick="filterProducts(\'transformers\')"',
        'onclick="window.location.href=\'Current Transformer.html\'"'
    ),
    (
        'onclick="filterProducts(\'relays\')"',
        'onclick="window.location.href=\'protection relay.html\'"'
    ),
    (
        'onclick="filterProducts(\'meters\')"',
        'onclick="window.location.href=\'analog meters.html\'"'
    ),
    (
        'onclick="filterProducts(\'analyzers\')"',
        'onclick="window.location.href=\'energy analyzer.html\'"'
    ),
    (
        'onclick="filterProducts(\'power\')"',
        'onclick="window.location.href=\'power supply.html\'"'
    ),
    (
        'onclick="filterProducts(\'transducers\')"',
        'onclick="window.location.href=\'volt transducer.html\'"'
    ),
]
for old, new in sidebar_replacements:
    html = html.replace(old, new)

with open(products_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("✅ Products.html updated — category cards now navigate to dedicated pages")

# ─── 2. Add breadcrumb to each category page ─────────────────────────────────
CATEGORY_PAGES = [
    {
        'file': 'Current Transformer.html',
        'label': 'Current Transformers',
        'label_tr': 'Akım Transformatörleri',
    },
    {
        'file': 'protection relay.html',
        'label': 'Protection Relays',
        'label_tr': 'Koruma Röleleri',
    },
    {
        'file': 'analog meters.html',
        'label': 'Analog Meters',
        'label_tr': 'Analog Sayaçlar',
    },
    {
        'file': 'digital meters.html',
        'label': 'Digital Meters',
        'label_tr': 'Dijital Sayaçlar',
    },
    {
        'file': 'energy analyzer.html',
        'label': 'Energy Analyzers',
        'label_tr': 'Enerji Analizörleri',
    },
    {
        'file': 'power supply.html',
        'label': 'Power Supplies',
        'label_tr': 'Güç Kaynakları',
    },
    {
        'file': 'battery charger.html',
        'label': 'Battery Chargers',
        'label_tr': 'Akü Şarj Cihazları',
    },
    {
        'file': 'timers.html',
        'label': 'Timers',
        'label_tr': 'Zaman Röleleri',
    },
    {
        'file': 'control relay.html',
        'label': 'Control Relays',
        'label_tr': 'Kontrol Röleleri',
    },
    {
        'file': 'power factor controller.html',
        'label': 'Power Factor Controllers',
        'label_tr': 'Güç Faktörü Kontrolörleri',
    },
    {
        'file': 'volt transducer.html',
        'label': 'Volt Transducers',
        'label_tr': 'Volt Transdüserler',
    },
    {
        'file': 'ampere transducer.html',
        'label': 'Ampere Transducers',
        'label_tr': 'Amper Transdüserler',
    },
]

BREADCRUMB_CSS = """
<style>
.vteke-breadcrumb {
    background: #ffffff;
    border-bottom: 1px solid #ebebeb;
    padding: 12px 0;
    font-size: 0.82rem;
    color: #888;
}
.vteke-breadcrumb-inner {
    max-width: 1400px;
    margin: 0 auto;
    padding: 0 24px;
    display: flex;
    align-items: center;
    gap: 8px;
}
.vteke-breadcrumb a {
    color: #555;
    text-decoration: none;
    font-weight: 500;
    transition: color 0.2s;
}
.vteke-breadcrumb a:hover { color: #E10600; }
.vteke-breadcrumb-sep { color: #ccc; }
.vteke-breadcrumb-current { color: #E10600; font-weight: 600; }
</style>
"""

BREADCRUMB_HTML = """<nav class="vteke-breadcrumb" aria-label="Breadcrumb">
  <div class="vteke-breadcrumb-inner">
    <a href="index.html" data-lang-en="Home" data-lang-tr="Ana Sayfa">Home</a>
    <span class="vteke-breadcrumb-sep">›</span>
    <a href="Products.html" data-lang-en="Products" data-lang-tr="Ürünler">Products</a>
    <span class="vteke-breadcrumb-sep">›</span>
    <span class="vteke-breadcrumb-current" data-lang-en="{label}" data-lang-tr="{label_tr}">{label}</span>
  </div>
</nav>
"""

injected = 0
skipped = 0
for cat in CATEGORY_PAGES:
    path = f"{ROOT}/{cat['file']}"
    try:
        with open(path, 'r', encoding='utf-8') as f:
            page = f.read()
    except FileNotFoundError:
        print(f"  ⚠️  Not found: {cat['file']}")
        skipped += 1
        continue

    # Skip if breadcrumb already exists
    if 'vteke-breadcrumb' in page:
        print(f"  ℹ️  Already has breadcrumb: {cat['file']}")
        continue

    # Inject breadcrumb CSS into <head>
    if '</head>' in page:
        page = page.replace('</head>', BREADCRUMB_CSS + '</head>', 1)

    # Inject breadcrumb HTML after opening <body> tag or after header
    breadcrumb = BREADCRUMB_HTML.format(label=cat['label'], label_tr=cat['label_tr'])
    # Place after </header>
    if '</header>' in page:
        page = page.replace('</header>', '</header>\n' + breadcrumb, 1)
    elif '<body' in page:
        # fallback — place right after <body>
        page = re.sub(r'(<body[^>]*>)', r'\1\n' + breadcrumb, page, count=1)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(page)
    print(f"  ✅  Breadcrumb added: {cat['file']}")
    injected += 1

print(f"\n✅ Breadcrumbs: {injected} added, {skipped} skipped")
print("Done!")
