#!/usr/bin/env python3
"""
Replace emoji flags in all HTML files with inline SVGs.
Works on ALL browsers and operating systems (no emoji font needed).

Replaces:
  🇬🇧  → UK flag SVG
  🇹🇷  → Turkish flag SVG
"""
import os, glob

ROOT = "/Users/marwaghalayini/Salaheddin's Work/Websites/vteke_Upgrades"

# Compact inline SVG flags — cross-browser, cross-OS
EN_FLAG = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 60 30" width="20" height="14" style="display:inline-block;vertical-align:middle;border-radius:2px"><clipPath id="vtek-a"><path d="M0 0v30h60V0z"/></clipPath><clipPath id="vtek-b"><path d="M30 15h30v15zM30 15H0v15zM30 15h30V0zM30 15H0V0z"/></clipPath><g clip-path="url(#vtek-a)"><path d="M0 0v30h60V0z" fill="#012169"/><path d="M0 0l60 30m0-30L0 30" stroke="#fff" stroke-width="6"/><path d="M0 0l60 30m0-30L0 30" clip-path="url(#vtek-b)" stroke="#C8102E" stroke-width="4"/><path d="M30 0v30M0 15h60" stroke="#fff" stroke-width="10"/><path d="M30 0v30M0 15h60" stroke="#C8102E" stroke-width="6"/></g></svg>'

TR_FLAG = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 30 20" width="20" height="14" style="display:inline-block;vertical-align:middle;border-radius:2px"><rect width="30" height="20" fill="#E30A17"/><circle cx="10" cy="10" r="6" fill="#fff"/><circle cx="11.5" cy="10" r="4.8" fill="#E30A17"/><polygon points="16.5,10 18.6,10.7 17.3,8.8 17.3,11.2 18.6,9.3" fill="#fff"/></svg>'

html_files = glob.glob(f'{ROOT}/**/*.html', recursive=True) + glob.glob(f'{ROOT}/*.html')
html_files = sorted(set(html_files))

fixed = 0
for path in html_files:
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Replace emoji flags with SVG
    new_content = content.replace('🇬🇧', EN_FLAG).replace('🇸🇦', EN_FLAG)
    new_content = new_content.replace('🇹🇷', TR_FLAG)

    if new_content != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        fixed += 1
        print(f'  Fixed: {os.path.relpath(path, ROOT)}')

print(f'\n✅ Done — {fixed} files updated')
