#!/usr/bin/env python3
"""
Convert ALL-CAPS text in HTML nav items, buttons, and section headings
to proper Title Case, matching the Siemens/ABB enterprise style.

Targets:
- data-lang-en="ALL CAPS TEXT"  → data-lang-en="Title Case Text"
- data-lang-tr stays as-is (Turkish strings are fine)
- Visible button text in view-btn, action-btn classes
- Section heading text that is fully uppercase
"""
import os, re, glob

ROOT = "/Users/marwaghalayini/Salaheddin's Work/Websites/vteke_Upgrades"

# ALL-CAPS nav/button data-lang-en values → proper Title Case
NAV_REPLACEMENTS = {
    'data-lang-en="HOME"':         'data-lang-en="Home"',
    'data-lang-en="ABOUT US"':     'data-lang-en="About Us"',
    'data-lang-en="NEWS"':         'data-lang-en="News"',
    'data-lang-en="CATALOG"':      'data-lang-en="Catalog"',
    'data-lang-en="PRODUCTS"':     'data-lang-en="Products"',
    'data-lang-en="CERTIFICATES"': 'data-lang-en="Certificates"',
    'data-lang-en="CONTACT"':      'data-lang-en="Contact"',
    # Nav link visible text
    '>HOME<':         '>Home<',
    '>ABOUT US<':     '>About Us<',
    '>NEWS<':         '>News<',
    '>CATALOG<':      '>Catalog<',
    '>PRODUCTS<':     '>Products<',
    '>CERTIFICATES<': '>Certificates<',
    '>CONTACT<':      '>Contact<',
    # Buttons
    '>VIEW DETAILS<': '>View Details<',
    '>VIEW SPECS<':   '>View Specs<',
    '>MORE DETAILS<': '>More Details<',
    '>DETAILS<':      '>Details<',
    '>CONTACT US<':   '>Contact Us<',
    '>GET A QUOTE<':  '>Get A Quote<',
    '>VIEW ALL<':     '>View All<',
    '>LEARN MORE<':   '>Learn More<',
    '>DOWNLOAD<':     '>Download<',
    '>REQUEST INFO<': '>Request Info<',
    # Section headings in hero/title elements
    '>INDUSTRIAL EXCELLENCE<': '>Industrial Excellence<',
    '>OUR PRODUCTS<':          '>Our Products<',
    '>OUR VALUES<':            '>Our Values<',
    '>ABOUT US<':              '>About Us<',
    '>CONTACT US<':            '>Contact Us<',
    '>CERTIFICATES<':          '>Certificates<',
}

html_files = glob.glob(f'{ROOT}/**/*.html', recursive=True) + glob.glob(f'{ROOT}/*.html')
html_files = sorted(set(html_files))

fixed = 0
for path in html_files:
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    new_content = content
    for old, new in NAV_REPLACEMENTS.items():
        new_content = new_content.replace(old, new)

    if new_content != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        fixed += 1
        print(f'  Fixed: {os.path.relpath(path, ROOT)}')

print(f'\n✅ Done — {fixed} files updated')
