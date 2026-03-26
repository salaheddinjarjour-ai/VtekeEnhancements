#!/usr/bin/env python3
"""
Final script to fix all remaining translation patterns.
"""

import re
from pathlib import Path

BASE_PATH = Path("/Users/marwaghalayini/Salaheddin's Work/Websites/vteke_Upgrades/ProductsPages")


def fix_all_patterns(content):
    """Fix all translation patterns in content."""
    
    # 1. Fix description spans (same line or different lines within p)
    pattern = r'<p class="product-description">\s*<span class="desc-en">([^<]+)</span>\s*<span class="desc-tr" style="display:none;">([^<]+)</span>\s*</p>'
    replacement = r'<p class="product-description"><span data-lang-en="\1" data-lang-tr="\2">\1</span></p>'
    content = re.sub(pattern, replacement, content)
    
    # 2. Fix any remaining title-en/title-tr pairs
    pattern = r'<span class="title-en">([^<]+)</span>\s*<span class="title-tr" style="display:none">([^<]+)</span>'
    replacement = r'<span data-lang-en="\1" data-lang-tr="\2">\1</span>'
    content = re.sub(pattern, replacement, content)
    
    # 3. Fix any remaining label-en/label-tr pairs
    pattern = r'<span class="label-en">([^<]+)</span>\s*<span class="label-tr" style="display:none">([^<]+)</span>'
    replacement = r'<span data-lang-en="\1" data-lang-tr="\2">\1</span>'
    content = re.sub(pattern, replacement, content)
    
    # 4. Fix any remaining text-en/text-tr pairs
    pattern = r'<span class="text-en">([^<]+)</span>\s*<span class="text-tr" style="display:none">([^<]+)</span>'
    replacement = r'<span data-lang-en="\1" data-lang-tr="\2">\1</span>'
    content = re.sub(pattern, replacement, content)
    
    # 5. Fix any remaining btn-en/btn-tr pairs
    pattern = r'<span class="btn-en">([^<]+)</span>\s*<span class="btn-tr" style="display:none">([^<]+)</span>'
    replacement = r'<span data-lang-en="\1" data-lang-tr="\2">\1</span>'
    content = re.sub(pattern, replacement, content)
    
    # 6. Fix any remaining ref-en/ref-tr pairs
    pattern = r'<span class="ref-en">([^<]+)</span>\s*<span class="ref-tr" style="display:none">([^<]+)</span>'
    replacement = r'<span data-lang-en="\1" data-lang-tr="\2">\1</span>'
    content = re.sub(pattern, replacement, content)
    
    # 7. Fix any remaining hint-en/hint-tr pairs
    pattern = r'<span class="hint-en">([^<]+)</span>\s*<span class="hint-tr" style="display:none">([^<]+)</span>'
    replacement = r'<span data-lang-en="\1" data-lang-tr="\2">\1</span>'
    content = re.sub(pattern, replacement, content)
    
    return content


def process_file(file_path):
    """Process a single HTML file."""
    print(f"Processing: {file_path}")

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check for old patterns
        old_patterns = ['class="desc-en"', 'class="label-en"', 'class="text-en"', 
                       'class="btn-en"', 'class="ref-en"', 'class="title-en"',
                       'class="hint-en"']
        has_old_patterns = any(p in content for p in old_patterns)
        
        if has_old_patterns:
            content = fix_all_patterns(content)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  Fixed in: {file_path.name}")
        else:
            print(f"  Already fixed: {file_path.name}")
        return True
    except Exception as e:
        print(f"  Error: {file_path}: {e}")
        return False


def main():
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
