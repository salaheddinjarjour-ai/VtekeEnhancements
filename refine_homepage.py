import re

html_path = "/Users/marwaghalayini/Salaheddin's Work/Websites/vteke_Upgrades/index.html"
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# =====================================================================
# 1. PRODUCTS SECTION CSS FIXES
# =====================================================================

# 1a. Fix product-card: remove scale(0.98) default, keep border clean
html = html.replace(
    '.product-card { background: var(--ps-white); border-radius: 14px; overflow: hidden; box-shadow: var(--ps-shadow-md); width: 100%; max-width: 480px; display: flex; flex-direction: column; height: 100%; transition: all 0.6s var(--ps-transition-ease); position: relative; transform: scale(0.98); will-change: transform, box-shadow; border: 1px solid #f0f0f0; }',
    '.product-card { background: #ffffff; border-radius: 14px; overflow: hidden; box-shadow: 0 2px 12px rgba(0,0,0,0.08); width: 100%; max-width: 480px; display: flex; flex-direction: column; height: 100%; transition: all 0.3s ease; position: relative; will-change: transform, box-shadow; border: 1px solid #f0f0f0; }'
)

# 1b. Fix product-card:hover — subtle lift, no red glow
html = html.replace(
    '.product-card:hover { transform: scale(1.01); box-shadow: var(--ps-shadow-xl); }',
    '.product-card:hover { transform: translateY(-4px); box-shadow: 0 12px 28px rgba(0,0,0,0.12); border-color: rgba(225,6,0,0.2); }'
)

# 1c. Fix product-card.active — no aggressive scale
html = html.replace(
    '.product-card.active { transform: scale(1.03); box-shadow: var(--ps-shadow-xl); z-index: 10; opacity: 1 !important; }',
    '.product-card.active { transform: translateY(-2px); box-shadow: 0 8px 20px rgba(0,0,0,0.1); z-index: 10; opacity: 1 !important; }'
)

# 1d. Fix product-image: standardize height to 220px, clean bg, no red radial
html = html.replace(
    '.product-image { height: 400px; background: linear-gradient(180deg, #fafafa 0%, #f2f2f2 100%); display: flex; align-items: center; justify-content: center; overflow: hidden; position: relative; }',
    '.product-image { height: 220px; background: #f6f6f6; display: flex; align-items: center; justify-content: center; overflow: hidden; position: relative; border-radius: 10px 10px 0 0; box-shadow: inset 0 2px 8px rgba(0,0,0,0.04); }'
)

# 1e. Remove red radial glow pseudo-element from product-image::before
html = html.replace(
    ".product-image::before { content: ''; position: absolute; width: 200%; height: 200%; background: radial-gradient(circle, rgba(200, 13, 44, 0.1) 0%, rgba(255,255,255,0) 70%); top: -50%; left: -50%; transform: scale(0.8); transition: transform 0.7s var(--ps-transition-ease); }",
    "/* product-image pseudo-element removed */"
)

# 1f. Remove red radial glow on hover
html = html.replace(
    '.product-card:hover .product-image::before { transform: scale(1.2); }',
    ''
)

# 1g. Fix image sizing: max-width/height 80%, object-fit: contain (not cover)
html = html.replace(
    '.product-image img { width: 100%; height: 100%; object-fit: cover; padding: 0; filter: drop-shadow(0 4px 8px rgba(0, 0, 0, 0.15)); transition: transform 0.7s var(--ps-transition-ease); }',
    '.product-image img { max-width: 80%; max-height: 80%; object-fit: contain; filter: drop-shadow(0 4px 8px rgba(0,0,0,0.1)); transition: transform 0.3s ease; }'
)

# 1h. Soften image scale on hover
html = html.replace(
    '.product-card:hover .product-image img { transform: scale(1.08); }',
    '.product-card:hover .product-image img { transform: scale(1.04); }'
)

# 1i. Fix product-content spacing
html = html.replace(
    '.product-content { padding: var(--ps-spacing-lg); padding-top: var(--ps-spacing-xl); padding-bottom: var(--ps-spacing-xl); background: linear-gradient(to bottom, rgba(255,255,255,0.95), rgba(255,255,255,0.85)); text-align: center; }',
    '.product-content { padding: 14px 16px 20px; background: #ffffff; text-align: center; }'
)

# 1j. Fix product-title spacing
html = html.replace(
    '.product-title { font-family: var(--ps-font-sans); font-size: 1.5rem; font-weight: 700; color: #111111; line-height: 1.3; }',
    '.product-title { font-family: var(--ps-font-sans); font-size: 1.4rem; font-weight: 700; color: #111111; line-height: 1.3; margin-bottom: 14px; }'
)

# 1k. Fix view-specs-btn (rename + fix hover)
html = html.replace(
    '.view-specs-btn { display: inline-block; margin-top: 14px; padding: 10px 24px; background: linear-gradient(135deg, #C40000 0%, #E10600 100%); color: #ffffff; font-size: 0.875rem; font-weight: 600; border-radius: 25px; text-decoration: none; transition: all 0.3s ease; box-shadow: 0 4px 12px rgba(196, 0, 0, 0.3); }',
    '.view-specs-btn { display: inline-block; padding: 9px 22px; background: #E10600; color: #ffffff; font-size: 0.82rem; font-weight: 600; border-radius: 6px; text-decoration: none; transition: all 0.3s ease; letter-spacing: 0.3px; }'
)

# 1l. Fix view-specs-btn hover — no heavy shadow
html = html.replace(
    '.view-specs-btn:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(196, 0, 0, 0.4); background: linear-gradient(135deg, #E10600 0%, #C40000 100%); }',
    '.view-specs-btn:hover { transform: translateY(-2px); background: #C40000; box-shadow: 0 4px 12px rgba(196,0,0,0.2); }'
)

# 1m. Fix responsive image heights to match new standardized 220px
html = html.replace(
    '@media (min-width: 768px) { .product-item { width: 50%; } .product-image { height: 360px; } .product-title { font-size: 1.625rem; } }',
    '@media (min-width: 768px) { .product-item { width: 50%; } .product-image { height: 220px; } .product-title { font-size: 1.5rem; } }'
)

html = html.replace(
    '@media (min-width: 1024px) { .product-item { width: 33.3333%; } .product-image { height: 400px; } .product-title { font-size: 1.75rem; } .slider-btn { width: 72px; height: 72px; font-size: 2rem; } .slider-btn.prev { left: 40px; } .slider-btn.next { right: 40px; } }',
    '@media (min-width: 1024px) { .product-item { width: 33.3333%; } .product-image { height: 220px; } .product-title { font-size: 1.5rem; } .slider-btn { width: 72px; height: 72px; font-size: 2rem; } .slider-btn.prev { left: 40px; } .slider-btn.next { right: 40px; } }'
)

html = html.replace(
    '@media (max-width: 767px) { .product-image { height: 280px; } .product-title { font-size: 1.375rem; } .slider-btn { width: 56px; height: 56px; font-size: 1.5rem; } .slider-btn.prev { left: 16px; } .slider-btn.next { right: 16px; } .slider-dots { margin-top: var(--ps-spacing-md); } }',
    '@media (max-width: 767px) { .product-image { height: 200px; } .product-title { font-size: 1.25rem; } .slider-btn { width: 56px; height: 56px; font-size: 1.5rem; } .slider-btn.prev { left: 16px; } .slider-btn.next { right: 16px; } .slider-dots { margin-top: var(--ps-spacing-md); } }'
)

# =====================================================================
# 2. INDUSTRIAL EXCELLENCE SECTION CSS FIXES
# =====================================================================

# 2a. Fix vp-industrial-card hover — remove red glow
html = html.replace(
    '.vp-industrial-card:hover { transform: translateY(-8px); box-shadow: 0 15px 40px rgba(200, 13, 44, 0.25); z-index: 30; border-color: rgba(200, 13, 44, 0.4); }',
    '.vp-industrial-card:hover { transform: translateY(-4px); box-shadow: 0 12px 28px rgba(0,0,0,0.12); z-index: 30; border-color: rgba(225,6,0,0.2); }'
)

# 2b. Standardize image container height and style
html = html.replace(
    '''.vp-industrial-img-container {
height: 280px;
overflow: visible;
position: relative;
display: flex;
align-items: center;
justify-content: center;
background: linear-gradient(135deg, #f0f0f0 0%, #ffffff 100%);
border-bottom: 2px solid #C40000;
transition: all 0.4s ease;
padding: 20px;
}''',
    '''.vp-industrial-img-container {
height: 200px;
overflow: hidden;
position: relative;
display: flex;
align-items: center;
justify-content: center;
background: #f6f6f6;
border-bottom: 1px solid #f0f0f0;
transition: all 0.3s ease;
padding: 16px;
box-shadow: inset 0 2px 8px rgba(0,0,0,0.04);
}'''
)

# 2c. Fix vp-industrial-img — max coverage, no heavy drop-shadow
html = html.replace(
    '''.vp-industrial-img {
width: 100%;
height: 100%;
max-width: 100%;
max-height: 100%;
object-fit: contain;
object-position: center;
transition: all 0.5s cubic-bezier(0.165, 0.84, 0.44, 1);
filter: drop-shadow(0 10px 20px rgba(0, 0, 0, 0.15));
}''',
    '''.vp-industrial-img {
max-width: 80%;
max-height: 80%;
object-fit: contain;
object-position: center;
transition: transform 0.3s ease;
filter: drop-shadow(0 4px 8px rgba(0,0,0,0.1));
}'''
)

# 2d. Remove heavy red glow on img hover
html = html.replace(
    '.vp-industrial-card:hover .vp-industrial-img-container { background: linear-gradient(135deg, #ffffff 0%, #fff8f8 100%); }',
    '.vp-industrial-card:hover .vp-industrial-img-container { background: #f0f0f0; }'
)

html = html.replace(
    '.vp-industrial-card:hover .vp-industrial-img { transform: scale(1.12); filter: drop-shadow(0 18px 35px rgba(200, 13, 44, 0.3)); }',
    '.vp-industrial-card:hover .vp-industrial-img { transform: scale(1.04); filter: drop-shadow(0 6px 14px rgba(0,0,0,0.12)); }'
)

# 2e. Remove red title color on hover
html = html.replace(
    '.vp-industrial-card:hover .vp-industrial-product-title { color: #C40000; }',
    '.vp-industrial-card:hover .vp-industrial-product-title { color: #111111; }'
)

# 2f. Remove red title hover scale
html = html.replace(
    '.vp-industrial-title:hover { color: #C40000; transform: scale(1.05); }',
    '.vp-industrial-title:hover { color: #1a1a1a; }'
)

# 2g. Fix vp-industrial-btn hover — no heavy shadow
html = html.replace(
    '.vp-industrial-btn:hover { transform: translateY(-2px); box-shadow: 0 10px 30px rgba(200, 13, 44, 0.5); letter-spacing: 1.2px; background: linear-gradient(135deg, #E70012, #C40000); }',
    '.vp-industrial-btn:hover { transform: translateY(-2px); box-shadow: 0 6px 16px rgba(196,0,0,0.2); background: linear-gradient(135deg, #E10600, #C40000); }'
)

# 2h. Fix vp-industrial-btn base shadow
html = html.replace(
    '.vp-industrial-btn { display: flex; align-items: center; justify-content: center; gap: 10px; padding: 12px 20px; background: linear-gradient(135deg, #C40000, #8B0000); color: #ffffff; text-decoration: none; border-radius: 8px; font-weight: 800; letter-spacing: 1px; transition: all 0.35s cubic-bezier(0.165, 0.84, 0.44, 1); text-align: center; width: 100%; box-shadow: 0 6px 20px rgba(200, 13, 44, 0.35); position: relative; font-size: 0.85rem; margin-top: auto; border: none; font-family: \'Segoe UI\', Tahoma, Geneva, Verdana, sans-serif; text-transform: uppercase; }',
    '.vp-industrial-btn { display: flex; align-items: center; justify-content: center; gap: 10px; padding: 11px 20px; background: #E10600; color: #ffffff; text-decoration: none; border-radius: 6px; font-weight: 700; letter-spacing: 0.5px; transition: all 0.3s ease; text-align: center; width: 100%; box-shadow: 0 4px 10px rgba(196,0,0,0.2); position: relative; font-size: 0.82rem; margin-top: auto; border: none; font-family: \'Segoe UI\', Tahoma, Geneva, Verdana, sans-serif; text-transform: uppercase; }'
)

# 2i. Reduce cards border red accent
html = html.replace(
    '.vp-industrial-card { background: #ffffff; border-radius: 12px; overflow: hidden; box-shadow: 0 8px 25px rgba(0, 0, 0, 0.12); transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1); position: relative; height: 100%; display: flex; flex-direction: column; border: 1px solid rgba(200, 13, 44, 0.15); }',
    '.vp-industrial-card { background: #ffffff; border-radius: 12px; overflow: hidden; box-shadow: 0 2px 12px rgba(0,0,0,0.08); transition: all 0.3s ease; position: relative; height: 100%; display: flex; flex-direction: column; border: 1px solid #f0f0f0; }'
)

# 2j. Fix responsive img container sizes
html = html.replace(
    '.vp-industrial-img-container { height: 260px; }',
    '.vp-industrial-img-container { height: 200px; }'
)
html = html.replace(
    '.vp-industrial-img-container { height: 250px; }',
    '.vp-industrial-img-container { height: 190px; }'
)

# 2k. Fix section padding (a bit less top padding — tighter layout)
html = html.replace(
    '''.vp-industrial-section {
background: #F5F5F5;
padding: 80px 0 60px;
position: relative;
overflow: visible;
box-shadow: 0 -1px 0 rgba(0, 0, 0, 0.02);
}''',
    '''.vp-industrial-section {
background: #F5F5F5;
padding: 60px 0 50px;
position: relative;
overflow: visible;
}'''
)

# =====================================================================
# 3. RENAME "View Specs" → "View Details" GLOBALLY
# =====================================================================
html = html.replace('View Specs', 'View Details')
html = html.replace('view-specs-btn', 'view-details-btn')

# =====================================================================
# 4. RENAME "View Specs" → "View Details" in Industrial Excellence
# =====================================================================
html = html.replace('VIEW PRODUCT', 'VIEW DETAILS')
html = html.replace('View Product', 'View Details')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ All refinements applied successfully to index.html")
