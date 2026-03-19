#!/usr/bin/env python3
"""
Convert ALL-CAPS section titles in data-lang-en attributes and visible HTML text
to proper Title Case across all HTML pages.

Targets ALL-CAPS strings inside:
  - data-lang-en="ALL CAPS STRING"
  - Visible text between tags: >ALL CAPS STRING<
"""
import os, re, glob

ROOT = "/Users/marwaghalayini/Salaheddin's Work/Websites/vteke_Upgrades"

# Words that should stay lowercase in Title Case
LOWERCASE_WORDS = {'a','an','the','and','but','or','for','nor','on','at','to','by',
                   'in','of','up','as','vs','via','per','with','from','into','than',
                   'that','this','is','are','was','were','be','been','being'}

def to_title_case(text):
    """Convert ALL CAPS string to Title Case, keeping short words lowercase."""
    words = text.split()
    result = []
    for i, word in enumerate(words):
        # Always capitalize first and last word
        if i == 0 or i == len(words) - 1:
            result.append(word.capitalize())
        elif word.lower() in LOWERCASE_WORDS:
            result.append(word.lower())
        else:
            result.append(word.capitalize())
    return ' '.join(result)

def is_all_caps(text):
    """True if string is all uppercase letters (allowing spaces, digits, punctuation)."""
    letters = [c for c in text if c.isalpha()]
    return len(letters) >= 3 and all(c.isupper() for c in letters)

def process_data_lang_en(content):
    """Replace data-lang-en="ALL CAPS" with Title Case version."""
    def replace_attr(m):
        val = m.group(1)
        if is_all_caps(val):
            return f'data-lang-en="{to_title_case(val)}"'
        return m.group(0)
    return re.sub(r'data-lang-en="([^"]+)"', replace_attr, content)

def process_visible_text(content):
    """Replace >ALL CAPS< visible text in tags with Title Case."""
    def replace_text(m):
        inner = m.group(1)
        if is_all_caps(inner.strip()):
            return f'>{to_title_case(inner.strip())}<'
        return m.group(0)
    # Only match short-medium strings (section titles, not paragraphs)
    return re.sub(r'>([A-Z][A-Z &\'/,\-]{2,60})<', replace_text, content)

html_files = glob.glob(f'{ROOT}/**/*.html', recursive=True) + glob.glob(f'{ROOT}/*.html')
html_files = sorted(set(html_files))

fixed = 0
for path in html_files:
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    new_content = process_data_lang_en(content)
    new_content = process_visible_text(new_content)

    if new_content != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        fixed += 1
        print(f'  Fixed: {os.path.relpath(path, ROOT)}')

print(f'\n✅ Done — {fixed} files updated')
