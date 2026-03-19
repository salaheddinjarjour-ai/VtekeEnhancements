#!/usr/bin/env python3
"""
Inject Google Fonts (Inter + Montserrat) and vteke-typography.css
into every HTML file in the vteke_Upgrades project.
Skips files that already have the typography link.
"""

import os, glob, re

ROOT = "/Users/marwaghalayini/Salaheddin's Work/Websites/vteke_Upgrades"

FONTS_LINK = '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Montserrat:wght@500;600;700;800&display=swap" rel="stylesheet">'

# Helper: figure out the relative path prefix to root from a given file
def root_prefix(filepath):
    depth = filepath.replace(ROOT + '/', '').count('/')
    return '../' * depth

updated = 0
skipped = 0
already = 0

html_files = glob.glob(f'{ROOT}/**/*.html', recursive=True) + glob.glob(f'{ROOT}/*.html')
html_files = sorted(set(html_files))

for path in html_files:
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Skip if typography already injected
    if 'vteke-typography.css' in content:
        already += 1
        continue

    if '</head>' not in content:
        skipped += 1
        continue

    prefix = root_prefix(path)
    typo_link = f'<link rel="stylesheet" href="{prefix}vteke-typography.css">'

    # Build injection block (fonts + typography CSS)
    # Only add fonts link if not already present
    inject = ''
    if 'fonts.googleapis.com/css2?family=Inter' not in content:
        inject += FONTS_LINK + '\n'
    inject += typo_link

    # Inject before </head>
    new_content = content.replace('</head>', inject + '\n</head>', 1)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    updated += 1
    print(f'  ✅ {os.path.relpath(path, ROOT)}')

print(f'\n✅ Updated: {updated} | Already done: {already} | Skipped: {skipped}')
