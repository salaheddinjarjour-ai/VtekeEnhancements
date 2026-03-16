import json

# Read products
with open('/Users/marwaghalayini/Salaheddin\'s Work/Websites/vteke_Upgrades/products_data.json', 'r', encoding='utf-8') as f:
    products = f.read()

# Generate JS code
js_code = f"""
const productsData = {products};

function renderProducts(category = 'all') {{
    const grid = document.getElementById('productGrid');
    if (!grid) return;
    
    // Filter products
    const filtered = category === 'all' 
        ? productsData 
        : productsData.filter(p => p.category === category);
        
    // Generate HTML
    grid.innerHTML = filtered.map(product => `
        <a href="${{product.link}}" class="product-card" data-category="${{product.category}}">
            <div class="card-image-container">
                <img src="${{product.image}}" alt="${{product.title.split('\\n')[0]}}" onerror="this.src='/vtekeimg/favicon.png'; this.style.objectFit='contain'; this.style.padding='2rem';">
            </div>
            <div class="card-content">
                <span class="category-label">${{product.categoryLabel.replace(/([A-Z])/g, ' $1').trim()}}</span>
                <h3 class="product-title">${{product.title.split('\\n')[0]}}</h3>
                <p class="product-description">${{product.title.includes('\\n') ? product.title.split('\\n')[1] : 'High-precision industrial electrical equipment.'}}</p>
            </div>
        </a>
    `).join('');
    
    // Add staggered animation delay
    const cards = grid.querySelectorAll('.product-card');
    cards.forEach((card, index) => {{
        card.style.animationDelay = `${{index * 0.05}}s`;
        card.classList.add('fade-in');
    }});
}}

function filterProducts(category) {{
    // Update active button
    document.querySelectorAll('.category-item').forEach(btn => {{
        btn.classList.remove('active');
        if (btn.getAttribute('data-category') === category) {{
            btn.classList.add('active');
        }}
    }});
    
    // Render products
    renderProducts(category);
}}

function updateCategoryCounts() {{
    const counts = {{
        all: productsData.length,
        transformers: productsData.filter(p => p.category === 'transformers').length,
        relays: productsData.filter(p => p.category === 'relays').length,
        meters: productsData.filter(p => p.category === 'meters').length,
        analyzers: productsData.filter(p => p.category === 'analyzers').length,
        power: productsData.filter(p => p.category === 'power').length,
        transducers: productsData.filter(p => p.category === 'transducers').length
    }};
    
    document.querySelectorAll('.category-item').forEach(btn => {{
        const cat = btn.getAttribute('data-category');
        const countSpan = btn.querySelector('.category-count');
        if (countSpan && counts[cat] !== undefined) {{
            countSpan.textContent = counts[cat];
        }}
    }});
}}

// Initialize on load
document.addEventListener('DOMContentLoaded', () => {{
    updateCategoryCounts();
    renderProducts('all');
}});
"""

# Read Products.html
html_path = '/Users/marwaghalayini/Salaheddin\'s Work/Websites/vteke_Upgrades/Products.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Replace the static grid contents
import re
# Find the product-grid div and empty its contents
grid_pattern = re.compile(r'(<div class="product-grid" id="productGrid">).*?(</div>\s*</div>\s*</div>)', re.DOTALL)
html = grid_pattern.sub(r'\1\n<!-- Products will be injected here by JavaScript -->\n\2', html)

# 2. Replace the old filterProducts script at the bottom
script_pattern = re.compile(r'<script>\s*// Product Filtering Logic.*?</script>', re.DOTALL)

new_script = f"""<script>
// Dynamic Product Rendering & Filtering Logic
{js_code}
</script>"""

if script_pattern.search(html):
    html = script_pattern.sub(new_script, html)
else:
    # If not found, insert before closing body
    html = html.replace('</body>', f"{new_script}\n</body>")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Injected dynamic product grid and JS logic into Products.html")
