#!/usr/bin/env python3
"""
Fix broken image references in ProductsPages:
1. Remove <img> tags with src="/images/products/..." (never existed)
2. Replace <img> tags with src="/vtekeimg/mm.jpeg" → hide them (remove gallery items)
"""
import os, re, glob

ROOT = "/Users/marwaghalayini/Salaheddin's Work/Websites/vteke_Upgrades"

html_files = glob.glob(f'{ROOT}/ProductsPages/**/*.html', recursive=True)
fixed = 0

for path in sorted(html_files):
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    original = content

    # Remove any <img ... src="/images/products/..." ...> lines entirely
    content = re.sub(
        r'\s*<img[^>]+src=["\'/images/products/[^"\']+["\'][^>]*>',
        '',
        content
    )

    # Remove <img> lines using /vtekeimg/mm.jpeg (placeholder, no real image)
    content = re.sub(
        r'\s*<img[^>]+src=["\']/?vtekeimg/mm\.jpeg["\'][^>]*>',
        '',
        content
    )

    # Also handle unquoted and double-slashed refs
    content = re.sub(
        r'\s*<img[^>]+src="/images/products/[^"]*"[^>]*>',
        '',
        content
    )

    if content != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'  Fixed: {os.path.relpath(path, ROOT)}')
        fixed += 1

print(f'\n✅ Done — {fixed} files fixed')
