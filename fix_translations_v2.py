#!/usr/bin/env python3
"""
Script to fix remaining translation patterns in product pages.
Handles multiline patterns and edge cases.
"""

import re
from pathlib import Path

# Base path
BASE_PATH = Path("/Users/marwaghalayini/Salaheddin's Work/Websites/vteke_Upgrades/ProductsPages")

# Translation script to add after Products.js
TRANSLATION_SCRIPT = '''<!-- Translation System -->
<script>
function applyTranslations(lang) {
    document.querySelectorAll('[data-lang-en]').forEach(el => {
        const translation = el.getAttribute(`data-lang-${lang}`);
        if (translation) el.textContent = translation;
    });
}
function setLanguage(lang) {
    localStorage.setItem('vteke_language', lang);
    applyTranslations(lang);
    document.getElementById('currentLangText').textContent = lang.toUpperCase();
}
document.addEventListener('DOMContentLoaded', function() {
    applyTranslations(localStorage.getItem('vteke_language') || 'en');
});
</script>'''


def fix_description_spans(content):
    """Fix description spans that may be in different structures."""
    # Pattern for desc spans across multiple lines
    pattern = r'<span class="desc-en">([^<]+)</span>\s*</p>\s*<p class="product-description">\s*<span class="desc-tr" style="display:none">([^<]+)</span>'
    replacement = r'<span data-lang-en="\1" data-lang-tr="\2">\1</span></p>'
    content = re.sub(pattern, replacement, content)
    
    # Alternative pattern - desc spans inside p
    pattern = r'<p class="product-description">\s*<span class="desc-en">([^<]+)</span>\s*<span class="desc-tr" style="display:none">([^<]+)</span>\s*</p>'
    replacement = r'<p class="product-description"><span data-lang-en="\1" data-lang-tr="\2">\1</span></p>'
    content = re.sub(pattern, replacement, content)
    
    return content


def fix_remaining_patterns(content):
    """Fix remaining translation patterns."""
    
    # Fix any remaining title-en/title-tr pairs
    pattern = r'<span class="title-en">([^<]+)</span>\s*<span class="title-tr" style="display:none">([^<]+)</span>'
    replacement = r'<span data-lang-en="\1" data-lang-tr="\2">\1</span>'
    content = re.sub(pattern, replacement, content)
    
    # Fix any remaining label-en/label-tr pairs
    pattern = r'<span class="label-en">([^<]+)</span>\s*<span class="label-tr" style="display:none">([^<]+)</span>'
    replacement = r'<span data-lang-en="\1" data-lang-tr="\2">\1</span>'
    content = re.sub(pattern, replacement, content)
    
    # Fix any remaining text-en/text-tr pairs
    pattern = r'<span class="text-en">([^<]+)</span>\s*<span class="text-tr" style="display:none">([^<]+)</span>'
    replacement = r'<span data-lang-en="\1" data-lang-tr="\2">\1</span>'
    content = re.sub(pattern, replacement, content)
    
    # Fix any remaining btn-en/btn-tr pairs
    pattern = r'<span class="btn-en">([^<]+)</span>\s*<span class="btn-tr" style="display:none">([^<]+)</span>'
    replacement = r'<span data-lang-en="\1" data-lang-tr="\2">\1</span>'
    content = re.sub(pattern, replacement, content)
    
    # Fix any remaining ref-en/ref-tr pairs
    pattern = r'<span class="ref-en">([^<]+)</span>\s*<span class="ref-tr" style="display:none">([^<]+)</span>'
    replacement = r'<span data-lang-en="\1" data-lang-tr="\2">\1</span>'
    content = re.sub(pattern, replacement, content)
    
    return content


def add_translation_script(content):
    """Add translation script after Products.js script tag."""
    # Check if script already exists
    if '<!-- Translation System -->' in content:
        return content
    
    pattern = r'(<script src="\.\./Products\.js"></script>)'
    if re.search(pattern, content):
        content = re.sub(
            pattern,
            r'\1\n\n' + TRANSLATION_SCRIPT + '\n',
            content
        )
    return content


def process_file(file_path):
    """Process a single HTML file."""
    print(f"Processing: {file_path}")

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if file still has old patterns
        old_patterns = ['class="desc-en"', 'class="label-en"', 'class="text-en"', 
                       'class="btn-en"', 'class="ref-en"', 'class="title-en"']
        has_old_patterns = any(p in content for p in old_patterns)
        
        if has_old_patterns:
            content = fix_description_spans(content)
            content = fix_remaining_patterns(content)
            content = add_translation_script(content)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  Fixed remaining patterns in: {file_path.name}")
        else:
            # Just ensure translation script is added
            if '<!-- Translation System -->' not in content:
                content = add_translation_script(content)
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"  Added translation script to: {file_path.name}")
            else:
                print(f"  Already up to date: {file_path.name}")
        return True
    except Exception as e:
        print(f"  Error processing {file_path}: {e}")
        return False


def main():
    """Main function to process all files."""

    files_to_process = [
        ("BatteryCharger/VBC-1205.html", "VBC-1205"),
        ("BatteryCharger/VBC-1205A.html", "VBC-1205A"),
        ("BatteryCharger/VBC-2405.html", "VBC-2405"),
        ("BatteryCharger/VBC-2405A.html", "VBC-2405A"),
        ("BatteryCharger/VBC-A05.html", "VBC-A05"),
        ("BatteryCharger/VBC-1210.html", "VBC-1210"),
        ("BatteryCharger/VBC-1210A.html", "VBC-1210A"),
        ("BatteryCharger/VBC-2410.html", "VBC-2410"),
        ("PowerSupply/PSU-2406.html", "PSU-2406"),
        ("PowerSupply/PSU-2403.html", "PSU-2403"),
        ("ControlRelay/HPR-03M.html", "HPR-03M"),
        ("ControlRelay/LLR-05U.html", "LLR-05U"),
        ("ControlRelay/HPR-02M.html", "HPR-02M"),
        ("ControlRelay/LLR-06.html", "LLR-06"),
        ("ControlRelay/LLR-05.html", "LLR-05"),
        ("ControlRelay/PCR-03.html", "PCR-03"),
        ("ControlRelay/PCR-04.html", "PCR-04"),
        ("PowerFactorController/PFC-07.html", "PFC-07"),
        ("PowerFactorController/PFC-12S.html", "PFC-12S"),
        ("CurrentTransformer/TK40-Current-Transformer.html", "TK40"),
        ("CurrentTransformer/TK60D-Current-Transformer.html", "TK60D"),
        ("CurrentTransformer/SK820-Current-Transformer.html", "SK820"),
        ("CurrentTransformer/SK88-Current-Transformer.html", "SK88"),
        ("CurrentTransformer/TK100-Current-Transformer.html", "TK100"),
        ("CurrentTransformer/TK30-Current-Transformer.html", "TK30"),
        ("CurrentTransformer/TK60-Current-Transformer.html", "TK60"),
        ("CurrentTransformer/VST5-Current-Transformer.html", "VST5"),
        ("CurrentTransformer/SK58-Current-Transformer.html", "SK58"),
        ("CurrentTransformer/SK816-Current-Transformer.html", "SK816"),
        ("CurrentTransformer/BK-Current-Transformer.html", "BK"),
        ("CurrentTransformer/SK812-Current-Transformer.html", "SK812"),
        ("CurrentTransformer/TK120-Current-Transformer.html", "TK120"),
        ("CurrentTransformer/MSK24-Current-Transformer.html", "MSK24"),
        ("CurrentTransformer/TK80-Current-Transformer.html", "TK80"),
        ("CurrentTransformer/BK1C-Current-Transformer.html", "BK1C"),
        ("CurrentTransformer/TK30A-Current-Transformer.html", "TK30A"),
        ("CurrentTransformer/MSK36-Current-Transformer.html", "MSK36"),
        ("CurrentTransformer/TK40A-Current-Transformer.html", "TK40A"),
        ("CurrentTransformer/MSK50-Current-Transformer.html", "MSK50"),
        ("CurrentTransformer/DK125-Current-Transformer.html", "DK125"),
        ("CurrentTransformer/VTOR-Current-Transformer.html", "VTOR"),
    ]

    success_count = 0
    fail_count = 0

    for rel_path, product_code in files_to_process:
        file_path = BASE_PATH / rel_path
        if file_path.exists():
            if process_file(file_path):
                success_count += 1
            else:
                fail_count += 1
        else:
            print(f"  File not found: {file_path}")
            fail_count += 1

    print(f"\n{'='*60}")
    print(f"Summary: {success_count} files processed, {fail_count} failed")


if __name__ == "__main__":
    main()
