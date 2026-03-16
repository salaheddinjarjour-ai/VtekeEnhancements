import os
import json
import re
from bs4 import BeautifulSoup

base_dir = "/Users/marwaghalayini/Salaheddin's Work/Websites/vteke_Upgrades/ProductsPages"
products = []

category_map = {
    'AnalogMeters': 'meters',
    'BatteryCharger': 'power',
    'ControlRelay': 'relays',
    'CurrentTransformer': 'transformers',
    'DigitalMeters': 'meters',
    'EnergyAnalyzer': 'analyzers',
    'PowerFactorController': 'analyzers',
    'PowerSupply': 'power',
    'ProtectionRelay': 'relays',
    'Timers': 'relays',
    'volt_transducer': 'transducers', # in main dir
    'ampere transducer': 'transducers' # in main dir
}

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            rel_path = os.path.relpath(filepath, os.path.dirname(base_dir))
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                soup = BeautifulSoup(content, 'html.parser')
                
                # Get Title
                title_tag = soup.find('h1') or soup.find('h2', class_=re.compile('product-title|hero-title'))
                title = title_tag.text.strip() if title_tag else file.replace('.html', '').replace('-', ' ')
                
                # Get Description
                desc_tag = soup.find('meta', {'name': 'description'})
                desc = desc_tag['content'] if desc_tag and 'content' in desc_tag.attrs else ''
                
                # Get Image
                img_tag = soup.find('img', class_=re.compile('product-image|main-image|hero-img'))
                img_src = img_tag['src'] if img_tag and 'src' in img_tag.attrs else ''
                if not img_src:
                    # Look for any image in product container
                    prod_container = soup.find(class_=re.compile('product'))
                    if prod_container:
                        fallback_img = prod_container.find('img')
                        if fallback_img and 'src' in fallback_img.attrs:
                            img_src = fallback_img['src']
                
                if not img_src:
                    img_src = '/vtekeimg/favicon.png' # Fallback
                
                # Fix relative img paths
                if img_src.startswith('../../'):
                    img_src = img_src.replace('../../', '/')
                elif img_src.startswith('../'):
                    img_src = img_src.replace('../', '/')
                
                # Determine category
                cat_folder = os.path.basename(root)
                cat_key = category_map.get(cat_folder, 'all')
                
                products.append({
                    'title': title,
                    'description': desc,
                    'image': img_src,
                    'link': rel_path,
                    'category': cat_key,
                    'categoryLabel': cat_folder
                })

# Include any root level product files
root_dir = "/Users/marwaghalayini/Salaheddin's Work/Websites/vteke_Upgrades"
for file in os.listdir(root_dir):
    if file.endswith('.html') and ('transducer' in file.lower() or 'relay' in file.lower() or 'meters' in file.lower()):
        filepath = os.path.join(root_dir, file)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            soup = BeautifulSoup(content, 'html.parser')
            title_tag = soup.find('h1') or soup.find('h2')
            title = title_tag.text.strip() if title_tag else file.replace('.html', '').replace('-', ' ')
            desc_tag = soup.find('meta', {'name': 'description'})
            desc = desc_tag['content'] if desc_tag and 'content' in desc_tag.attrs else ''
            
            cat_key = 'all'
            if 'transducer' in file.lower(): cat_key = 'transducers'
            elif 'relay' in file.lower(): cat_key = 'relays'
            elif 'meter' in file.lower(): cat_key = 'meters'
            
            products.append({
                'title': title,
                'description': desc,
                'image': '/vtekeimg/favicon.png',
                'link': file,
                'category': cat_key,
                'categoryLabel': cat_key
            })

with open('/Users/marwaghalayini/Salaheddin\'s Work/Websites/vteke_Upgrades/products_data.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, indent=4)
print(f"Generated data for {len(products)} products.")
