#!/usr/bin/env python3
"""
Remove text-transform: uppercase from inline <style> blocks in all HTML files.
Replaces the property with a comment so the rest of the rule is preserved.
"""
import os, re, glob

ROOT = "/Users/marwaghalayini/Salaheddin's Work/Websites/vteke_Upgrades"

html_files = glob.glob(f'{ROOT}/**/*.html', recursive=True) + glob.glob(f'{ROOT}/*.html')
html_files = sorted(set(html_files))

fixed = 0
for path in html_files:
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Only operate inside <style>...</style> blocks
    def remove_uppercase_in_style(m):
        style_content = m.group(0)
        # Remove text-transform: uppercase; lines (with varying whitespace)
        cleaned = re.sub(r'\s*text-transform\s*:\s*uppercase\s*;', '', style_content)
        # Also remove excessive letter-spacing that was paired with uppercase (>1.5px)
        cleaned = re.sub(r'letter-spacing\s*:\s*[2-9]px\s*;', 'letter-spacing: 0.02em;', cleaned)
        cleaned = re.sub(r'letter-spacing\s*:\s*[12]\.[0-9]px\s*;', 'letter-spacing: 0.02em;', cleaned)
        return cleaned

    new_content = re.sub(r'<style[^>]*>.*?</style>', remove_uppercase_in_style, content, flags=re.DOTALL)

    if new_content != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        fixed += 1
        print(f'  Fixed: {os.path.relpath(path, ROOT)}')

print(f'\n✅ Done — {fixed} files updated')
