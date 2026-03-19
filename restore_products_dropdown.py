#!/usr/bin/env python3
"""
Restore the Products dropdown in the top nav bar across all HTML pages.
Replaces the plain Products <li> with the dropdown container+menu.
"""
import os, re, glob

ROOT = "/Users/marwaghalayini/Salaheddin's Work/Websites/vteke_Upgrades"

# The old plain Products nav item (EN and TR variants)
OLD_PRODUCTS_LI = '''<li class="vteke-pro-nav-list-item">
<a href="Products.html" class="vteke-pro-nav-link-element" data-lang-en="PRODUCTS" data-lang-tr="ÜRÜNLER">PRODUCTS</a>
</li>'''

# The new dropdown Products nav item
NEW_PRODUCTS_LI = '''<li class="vteke-pro-nav-list-item vteke-pro-dropdown-container" style="position:relative;">
<a href="Products.html" class="vteke-pro-nav-link-element vteke-pro-dropdown-toggle-indicator" data-lang-en="PRODUCTS" data-lang-tr="ÜRÜNLER">PRODUCTS</a>
<div class="vteke-pro-mega-dropdown-container">
  <ul class="vteke-pro-dropdown-links-list">
    <li><a href="Current Transformer.html" class="vteke-pro-dropdown-link-item" data-lang-en="Current Transformers" data-lang-tr="Akım Transformatörleri">Current Transformers</a></li>
    <li><a href="protection relay.html" class="vteke-pro-dropdown-link-item" data-lang-en="Protection Relays" data-lang-tr="Koruma Röleleri">Protection Relays</a></li>
    <li><a href="timers.html" class="vteke-pro-dropdown-link-item" data-lang-en="Timers" data-lang-tr="Zamanlayıcılar">Timers</a></li>
    <li><a href="digital meters.html" class="vteke-pro-dropdown-link-item" data-lang-en="Digital Meters" data-lang-tr="Dijital Sayaçlar">Digital Meters</a></li>
    <li><a href="analog meters.html" class="vteke-pro-dropdown-link-item" data-lang-en="Analog Meters" data-lang-tr="Analog Sayaçlar">Analog Meters</a></li>
    <li><a href="energy analyzer.html" class="vteke-pro-dropdown-link-item" data-lang-en="Energy Analyzers" data-lang-tr="Enerji Analizörleri">Energy Analyzers</a></li>
    <li><a href="power factor controller.html" class="vteke-pro-dropdown-link-item" data-lang-en="Power Factor Controllers" data-lang-tr="Güç Faktörü Kontrolörleri">Power Factor Controllers</a></li>
    <li><a href="control relay.html" class="vteke-pro-dropdown-link-item" data-lang-en="Control Relays" data-lang-tr="Kontrol Röleleri">Control Relays</a></li>
    <li><a href="battery charger.html" class="vteke-pro-dropdown-link-item" data-lang-en="Battery Chargers" data-lang-tr="Akü Şarj Cihazları">Battery Chargers</a></li>
    <li><a href="power supply.html" class="vteke-pro-dropdown-link-item" data-lang-en="Power Supplies" data-lang-tr="Güç Kaynakları">Power Supplies</a></li>
    <li><a href="ampere transducer.html" class="vteke-pro-dropdown-link-item" data-lang-en="Ampere Transducers" data-lang-tr="Ampermetre Transdüserleri">Ampere Transducers</a></li>
    <li><a href="volt transducer.html" class="vteke-pro-dropdown-link-item" data-lang-en="Volt Transducers" data-lang-tr="Voltmetre Transdüserleri">Volt Transducers</a></li>
  </ul>
</div>
</li>'''

html_files = glob.glob(f'{ROOT}/**/*.html', recursive=True) + glob.glob(f'{ROOT}/*.html')
html_files = sorted(set(html_files))

fixed = 0
for path in html_files:
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Skip if already has dropdown-container for Products
    if 'vteke-pro-dropdown-container' in content and 'Products.html' in content:
        # check if it already has the mega dropdown
        if 'vteke-pro-mega-dropdown-container' in content:
            continue

    new_content = content.replace(OLD_PRODUCTS_LI.strip(), NEW_PRODUCTS_LI.strip())

    if new_content != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        fixed += 1
        print(f'  Fixed: {os.path.relpath(path, ROOT)}')

print(f'\n✅ Done — {fixed} files updated')
