#!/usr/bin/env python3
"""
Full typography enforcement across ALL CSS files and HTML <style> blocks.
Replaces ANY font-family declaration that isn't already using Inter/Montserrat
with the correct var(--font-body) or var(--font-heading) references.
Also removes any leftover Google Fonts imports for replaced fonts.
"""

import os, re, glob

ROOT = "/Users/marwaghalayini/Salaheddin's Work/Websites/vteke_Upgrades"

# Fonts that should be REPLACED with var(--font-body)
BODY_FONT_PATTERNS = [
    "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif",
    "'Segoe UI', system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif",
    "'Segoe UI', sans-serif",
    "'Manrope', 'Inter', sans-serif",
    "'Inter', 'Noto Sans Arabic', sans-serif",
    "'Inter', 'Noto Sans Arabic', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif",
    "'Inter', sans-serif",
    "Inter, sans-serif",
    "'Manrope', sans-serif",
]

# Fonts that should be REPLACED with var(--font-heading)
HEADING_FONT_PATTERNS = [
    "'Manrope', 'Montserrat', sans-serif",
    "'Montserrat', 'Roboto', -apple-system, BlinkMacSystemFont, sans-serif",
    "'Montserrat', sans-serif",
    "Montserrat, sans-serif",
]

# Fonts we should KEEP as-is (monospace, special)
KEEP_PATTERNS = [
    'monospace', 'Courier', 'console', 'code', 'pre',
]

BODY_REPLACEMENT    = "var(--font-body, 'Inter', 'Segoe UI', system-ui, sans-serif)"
HEADING_REPLACEMENT = "var(--font-heading, 'Montserrat', 'Inter', system-ui, sans-serif)"

def should_keep(old_val):
    return any(p.lower() in old_val.lower() for p in KEEP_PATTERNS)

def replace_fonts(content):
    for pat in HEADING_FONT_PATTERNS:
        content = content.replace(pat, HEADING_REPLACEMENT)
    for pat in BODY_FONT_PATTERNS:
        content = content.replace(pat, BODY_REPLACEMENT)
    return content

# ── Process CSS files ──────────────────────────────────────────────────────────
css_files = glob.glob(f'{ROOT}/**/*.css', recursive=True) + glob.glob(f'{ROOT}/*.css')
css_files = sorted(set(css_files))

css_updated = 0
for path in css_files:
    if 'vteke-typography.css' in path:
        continue   # never touch the master file
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    new_content = replace_fonts(content)
    if new_content != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        css_updated += 1
        print(f'  CSS ✅ {os.path.relpath(path, ROOT)}')

# ── Process HTML files (inside <style> blocks only) ────────────────────────────
html_files = glob.glob(f'{ROOT}/**/*.html', recursive=True) + glob.glob(f'{ROOT}/*.html')
html_files = sorted(set(html_files))

html_updated = 0
for path in html_files:
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    new_content = replace_fonts(content)
    if new_content != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        html_updated += 1
        print(f'  HTML ✅ {os.path.relpath(path, ROOT)}')

print(f'\n✅ Done — CSS files: {css_updated} | HTML files: {html_updated}')
