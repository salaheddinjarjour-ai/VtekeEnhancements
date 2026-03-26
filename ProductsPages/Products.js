/* ========================================
   VTEKE - Product Page Scripts (FIXED)
   ======================================== */

// Product Database - Maps product IDs to their file paths and details
const productsDatabase = {
    // Current Transformers
    'TK30': { file: 'TK30-Current-Transformer.html', folder: 'CurrentTransformer', name: 'TK30 Series', desc: '30-600A Window Type', category: 'Current Transformer' },
    'TK30N': { file: 'TK30N-Current-Transformer.html', folder: 'CurrentTransformer', name: 'TK30N Series', desc: '30-600A 1 Screw Terminal', category: 'Current Transformer' },
    'TK40': { file: 'TK40-Current-Transformer.html', folder: 'CurrentTransformer', name: 'TK40 Series', desc: '200-800A Window Type', category: 'Current Transformer' },
    'TK40A': { file: 'TK40A-Current-Transformer.html', folder: 'CurrentTransformer', name: 'TK40A Series', desc: 'High Accuracy', category: 'Current Transformer' },
    'TK60': { file: 'TK60-Current-Transformer.html', folder: 'CurrentTransformer', name: 'TK60 Series', desc: '400-1250A Window Type', category: 'Current Transformer' },
    'TK60D': { file: 'TK60D-Current-Transformer.html', folder: 'CurrentTransformer', name: 'TK60D Series', desc: '400-1250A Split Core', category: 'Current Transformer' },
    'TK80': { file: 'TK80-Current-Transformer.html', folder: 'CurrentTransformer', name: 'TK80 Series', desc: '600-2000A', category: 'Current Transformer' },
    'TK100': { file: 'TK100-Current-Transformer.html', folder: 'CurrentTransformer', name: 'TK100 Series', desc: '800-2500A', category: 'Current Transformer' },
    'TK120': { file: 'TK120-Current-Transformer.html', folder: 'CurrentTransformer', name: 'TK120 Series', desc: '1000-3000A', category: 'Current Transformer' },
    'CK20': { file: 'CK20-Current-Transformer.html', folder: 'CurrentTransformer', name: 'CK20 Series', desc: '30-300A Compact', category: 'Current Transformer' },
    'BK': { file: 'BK-Current-Transformer.html', folder: 'CurrentTransformer', name: 'BK Series', desc: 'Busbar Type', category: 'Current Transformer' },
    'BK1C': { file: 'BK1C-Current-Transformer.html', folder: 'CurrentTransformer', name: 'BK1C Series', desc: 'Compact Busbar', category: 'Current Transformer' },
    'DK125': { file: 'DK125-Current-Transformer.html', folder: 'CurrentTransformer', name: 'DK125 Series', desc: '1250A Split Core', category: 'Current Transformer' },
    'MSK24': { file: 'MSK24-Current-Transformer.html', folder: 'CurrentTransformer', name: 'MSK24 Series', desc: 'Mini Split Core', category: 'Current Transformer' },
    'MSK36': { file: 'MSK36-Current-Transformer.html', folder: 'CurrentTransformer', name: 'MSK36 Series', desc: 'Mini Split Core', category: 'Current Transformer' },
    'MSK50': { file: 'MSK50-Current-Transformer.html', folder: 'CurrentTransformer', name: 'MSK50 Series', desc: 'Medium Split Core', category: 'Current Transformer' },
    'SK58': { file: 'SK58-Current-Transformer.html', folder: 'CurrentTransformer', name: 'SK58 Series', desc: 'Split Core 50-800A', category: 'Current Transformer' },
    'SK812': { file: 'SK812-Current-Transformer.html', folder: 'CurrentTransformer', name: 'SK812 Series', desc: 'Split Core 100-1200A', category: 'Current Transformer' },
    'SK816': { file: 'SK816-Current-Transformer.html', folder: 'CurrentTransformer', name: 'SK816 Series', desc: 'Split Core 100-1600A', category: 'Current Transformer' },
    'SK820': { file: 'SK820-Current-Transformer.html', folder: 'CurrentTransformer', name: 'SK820 Series', desc: 'Split Core 100-2000A', category: 'Current Transformer' },
    'SK88': { file: 'SK88-Current-Transformer.html', folder: 'CurrentTransformer', name: 'SK88 Series', desc: 'Split Core 80-800A', category: 'Current Transformer' },
    'VST5': { file: 'VST5-Current-Transformer.html', folder: 'CurrentTransformer', name: 'VST5 Series', desc: 'Voltage Sensor', category: 'Current Transformer' },
    'VTOR': { file: 'VTOR-Current-Transformer.html', folder: 'CurrentTransformer', name: 'VTOR Series', desc: 'Voltage Output', category: 'Current Transformer' },
    
    // Protection Relays
    'VCR-02': { file: 'VCR-02.html', folder: 'ProtectionRelay', name: 'VCR-02', desc: 'Voltage Control Relay', category: 'Protection Relay' },
    'VCR-02F': { file: 'VCR-02F.html', folder: 'ProtectionRelay', name: 'VCR-02F', desc: 'Voltage Control Relay', category: 'Protection Relay' },
    'VCR-03F': { file: 'VCR-03F.html', folder: 'ProtectionRelay', name: 'VCR-03F', desc: '3-Phase Voltage Relay', category: 'Protection Relay' },
    'VCR-11': { file: 'VCR-11.html', folder: 'ProtectionRelay', name: 'VCR-11', desc: 'Phase Failure Relay', category: 'Protection Relay' },
    'PPR-06F': { file: 'PPR-06F.html', folder: 'ProtectionRelay', name: 'PPR-06F', desc: 'Phase Protection Relay', category: 'Protection Relay' },
    'PPR-14': { file: 'PPR-14.html', folder: 'ProtectionRelay', name: 'PPR-14', desc: 'Motor Protection Relay', category: 'Protection Relay' },
    'PPR-24F': { file: 'PPR-24F.html', folder: 'ProtectionRelay', name: 'PPR-24F', desc: '24V Protection Relay', category: 'Protection Relay' },
    'PPR-24FN': { file: 'PPR-24FN.html', folder: 'ProtectionRelay', name: 'PPR-24FN', desc: '24V Protection Relay N', category: 'Protection Relay' },
    'PPR-03N': { file: 'PPR-03N.html', folder: 'ProtectionRelay', name: 'PPR-03N', desc: 'Overload Relay', category: 'Protection Relay' },
    'PPR-05F': { file: 'PPR-05F.html', folder: 'ProtectionRelay', name: 'PPR-05F', desc: 'Phase Sequence Relay', category: 'Protection Relay' },
    'DVC-01': { file: 'DVC-01.html', folder: 'ProtectionRelay', name: 'DVC-01', desc: 'DC Voltage Monitor', category: 'Protection Relay' },
    'DVC-04': { file: 'DVC-04.html', folder: 'ProtectionRelay', name: 'DVC-04', desc: 'DC Voltage Monitor', category: 'Protection Relay' },
    'DVC-04F': { file: 'DVC-04F.html', folder: 'ProtectionRelay', name: 'DVC-04F', desc: 'DC Voltage Monitor', category: 'Protection Relay' },
    'DOR': { file: 'DOR.html', folder: 'ProtectionRelay', name: 'DOR', desc: 'Digital Output Relay', category: 'Protection Relay' },
    'ELR-V2': { file: 'ELR-V2.html', folder: 'ProtectionRelay', name: 'ELR-V2', desc: 'Earth Leakage Relay', category: 'Protection Relay' },
    
    // Control Relays
    'PCR-03': { file: 'PCR-03.html', folder: 'ControlRelay', name: 'PCR-03', desc: 'Programmable Control Relay', category: 'Control Relay' },
    'PCR-04': { file: 'PCR-04.html', folder: 'ControlRelay', name: 'PCR-04', desc: 'Programmable Control Relay', category: 'Control Relay' },
    'LLR-05': { file: 'LLR-05.html', folder: 'ControlRelay', name: 'LLR-05', desc: 'Liquid Level Relay', category: 'Control Relay' },
    'LLR-05U': { file: 'LLR-05U.html', folder: 'ControlRelay', name: 'LLR-05U', desc: 'Universal Level Relay', category: 'Control Relay' },
    'LLR-06': { file: 'LLR-06.html', folder: 'ControlRelay', name: 'LLR-06', desc: 'Dual Level Relay', category: 'Control Relay' },
    'HPR-02M': { file: 'HPR-02M.html', folder: 'ControlRelay', name: 'HPR-02M', desc: 'Hour Meter Relay', category: 'Control Relay' },
    'HPR-03M': { file: 'HPR-03M.html', folder: 'ControlRelay', name: 'HPR-03M', desc: 'Hour Meter Relay', category: 'Control Relay' },
    
    // Timers
    'DTR-03M': { file: 'DTR-03M.html', folder: 'Timers', name: 'DTR-03M', desc: 'Digital Timer', category: 'Timer' },
    'DTR-30': { file: 'DTR-30.html', folder: 'Timers', name: 'DTR-30', desc: '30A Digital Timer', category: 'Timer' },
    'DTR-60': { file: 'DTR-60.html', folder: 'Timers', name: 'DTR-60', desc: '60A Digital Timer', category: 'Timer' },
    'DTR-SC': { file: 'DTR-SC.html', folder: 'Timers', name: 'DTR-SC', desc: 'Schneider Compatible', category: 'Timer' },
    'DTR-SD': { file: 'DTR-SD.html', folder: 'Timers', name: 'DTR-SD', desc: 'DIN Rail Timer', category: 'Timer' },
    'FTR-07': { file: 'FTR-07.html', folder: 'Timers', name: 'FTR-07', desc: 'Flashing Timer', category: 'Timer' },
    'FTR-08': { file: 'FTR-08.html', folder: 'Timers', name: 'FTR-08', desc: 'Star Delta Timer', category: 'Timer' },
    'FTR-08M': { file: 'FTR-08M.html', folder: 'Timers', name: 'FTR-08M', desc: 'Star Delta Timer M', category: 'Timer' },
    'FTR-08MS': { file: 'FTR-08MS.html', folder: 'Timers', name: 'FTR-08MS', desc: 'Star Delta Timer MS', category: 'Timer' },
    'FTR-09': { file: 'FTR-09.html', folder: 'Timers', name: 'FTR-09', desc: 'Delay Timer', category: 'Timer' },
    'FTR-10': { file: 'FTR-10.html', folder: 'Timers', name: 'FTR-10', desc: 'Multi-function Timer', category: 'Timer' },
    
    // Digital Meters
    'VK-A72': { file: 'VK-A72.html', folder: 'DigitalMeters', name: 'VK-A72', desc: 'Ammeter 72mm', category: 'Digital Meter' },
    'VK-A96': { file: 'VK-A96.html', folder: 'DigitalMeters', name: 'VK-A96', desc: 'Ammeter 96mm', category: 'Digital Meter' },
    'VK-A96-T': { file: 'VK-A96-T.html', folder: 'DigitalMeters', name: 'VK-A96-T', desc: 'Ammeter with Timer', category: 'Digital Meter' },
    'VK-V72': { file: 'VK-V72.html', folder: 'DigitalMeters', name: 'VK-V72', desc: 'Voltmeter 72mm', category: 'Digital Meter' },
    'VK-V96': { file: 'VK-V96.html', folder: 'DigitalMeters', name: 'VK-V96', desc: 'Voltmeter 96mm', category: 'Digital Meter' },
    'VK-V96-T2': { file: 'VK-V96-T2.html', folder: 'DigitalMeters', name: 'VK-V96-T2', desc: 'Voltmeter T2', category: 'Digital Meter' },
    'VK-M96-C': { file: 'VK-M96-C.html', folder: 'DigitalMeters', name: 'VK-M96-C', desc: 'Multimeter Combined', category: 'Digital Meter' },
    'VK-M96S': { file: 'VK-M96S.html', folder: 'DigitalMeters', name: 'VK-M96S', desc: 'Multimeter Simon', category: 'Digital Meter' },
    
    // Analog Meters
    'AK-A72-XXX': { file: 'AK-A72-XXX.html', folder: 'AnalogMeters', name: 'AK-A72-XX/X', desc: 'Ammeter 72mm', category: 'Analog Meter' },
    'AK-A72-XXD': { file: 'AK-A72-XXD.html', folder: 'AnalogMeters', name: 'AK-A72-XX/D', desc: 'Ammeter 72mm DC', category: 'Analog Meter' },
    'AK-A96-XXX': { file: 'AK-A96-XXX.html', folder: 'AnalogMeters', name: 'AK-A96-XX/X', desc: 'Ammeter 96mm', category: 'Analog Meter' },
    'AK-A96-XXD': { file: 'AK-A96-XXD.html', folder: 'AnalogMeters', name: 'AK-A96-XX/D', desc: 'Ammeter 96mm DC', category: 'Analog Meter' },
    'AK-A96-XXX-1': { file: 'AK-A96-XXX-1.html', folder: 'AnalogMeters', name: 'AK-A96-XX/X-1', desc: 'Ammeter 96mm Type 1', category: 'Analog Meter' },
    'AK-V72-500V': { file: 'AK-V72-500V.html', folder: 'AnalogMeters', name: 'AK-V72-500V', desc: 'Voltmeter 72mm', category: 'Analog Meter' },
    'AK-V72-XX0,1': { file: 'AK-V72-XX0,1.html', folder: 'AnalogMeters', name: 'AK-V72-XX/0.1', desc: 'Voltmeter 72mm', category: 'Analog Meter' },
    'AK-V96-500V': { file: 'AK-V96-500V.html', folder: 'AnalogMeters', name: 'AK-V96-500V', desc: 'Voltmeter 96mm', category: 'Analog Meter' },
    'AK-V96-XX0,1': { file: 'AK-V96-XX0,1.html', folder: 'AnalogMeters', name: 'AK-V96-XX/0.1', desc: 'Voltmeter 96mm', category: 'Analog Meter' },
    'AK-F72': { file: 'AK-F72.html', folder: 'AnalogMeters', name: 'AK-F72', desc: 'Frequency Meter 72mm', category: 'Analog Meter' },
    'AK-F96': { file: 'AK-F96.html', folder: 'AnalogMeters', name: 'AK-F96', desc: 'Frequency Meter 96mm', category: 'Analog Meter' },
    
    // Power Factor Controllers
    'PFC-07': { file: 'PFC-07.html', folder: 'PowerFactorController', name: 'PFC-07', desc: '6-Step Power Factor', category: 'Power Factor Controller' },
    'PFC-12S': { file: 'PFC-12S.html', folder: 'PowerFactorController', name: 'PFC-12S', desc: '12-Step Power Factor', category: 'Power Factor Controller' },
    
    // Energy Analyzers
    'EA-C1': { file: 'EA-C1.html', folder: 'EnergyAnalyzer', name: 'EA-C1', desc: 'Energy Analyzer C1', category: 'Energy Analyzer' },
    'EA-C4': { file: 'EA-C4.html', folder: 'EnergyAnalyzer', name: 'EA-C4', desc: 'Energy Analyzer C4', category: 'Energy Analyzer' },
    'EA-C5': { file: 'EA-C5.html', folder: 'EnergyAnalyzer', name: 'EA-C5', desc: 'Energy Analyzer C5', category: 'Energy Analyzer' },
    'EA-4DIN': { file: 'EA-4DIN.html', folder: 'EnergyAnalyzer', name: 'EA-4DIN', desc: 'Energy Analyzer DIN', category: 'Energy Analyzer' },
    
    // Battery Chargers
    'VBC-1205': { file: 'VBC-1205.html', folder: 'BatteryCharger', name: 'VBC-1205', desc: '12V 5A Charger', category: 'Battery Charger' },
    'VBC-1205A': { file: 'VBC-1205A.html', folder: 'BatteryCharger', name: 'VBC-1205A', desc: '12V 5A Auto', category: 'Battery Charger' },
    'VBC-1210': { file: 'VBC-1210.html', folder: 'BatteryCharger', name: 'VBC-1210', desc: '12V 10A Charger', category: 'Battery Charger' },
    'VBC-1210A': { file: 'VBC-1210A.html', folder: 'BatteryCharger', name: 'VBC-1210A', desc: '12V 10A Auto', category: 'Battery Charger' },
    'VBC-2405': { file: 'VBC-2405.html', folder: 'BatteryCharger', name: 'VBC-2405', desc: '24V 5A Charger', category: 'Battery Charger' },
    'VBC-2405A': { file: 'VBC-2405A.html', folder: 'BatteryCharger', name: 'VBC-2405A', desc: '24V 5A Auto', category: 'Battery Charger' },
    'VBC-2410': { file: 'VBC-2410.html', folder: 'BatteryCharger', name: 'VBC-2410', desc: '24V 10A Charger', category: 'Battery Charger' },
    'VBC-A05': { file: 'VBC-A05.html', folder: 'BatteryCharger', name: 'VBC-A05', desc: 'Automatic Charger', category: 'Battery Charger' },
    
    // Power Supplies
    'PSU-2403': { file: 'PSU-2403.html', folder: 'PowerSupply', name: 'PSU-2403', desc: '24V Power Supply', category: 'Power Supply' },
    'PSU-2406': { file: 'PSU-2406.html', folder: 'PowerSupply', name: 'PSU-2406', desc: '24V 6A Power Supply', category: 'Power Supply' }
};

// Function to get current product info from page
function getCurrentProductInfo() {
    const productWrapper = document.querySelector('.product-details-wrapper');
    if (productWrapper) {
        return productWrapper.getAttribute('data-product') || '';
    }
    return '';
}

// Function to get all products in same category
function getRelatedProducts(currentProductId) {
    const currentProduct = productsDatabase[currentProductId];
    if (!currentProduct) return [];
    
    const currentCategory = currentProduct.category;
    const related = [];
    
    for (const [id, product] of Object.entries(productsDatabase)) {
        if (product.category === currentCategory && id !== currentProductId) {
            related.push({ id, ...product });
        }
    }
    
    // Sort alphabetically
    related.sort((a, b) => a.id.localeCompare(b.id));
    
    // Return only first 4
    return related.slice(0, 4);
}

// Function to load a product page
window.loadProduct = function(productId) {
    const product = productsDatabase[productId];
    if (product) {
        // Go up one directory then into the correct folder
        window.location.href = '../' + product.folder + '/' + product.file;
    } else {
        console.log('Product not found:', productId);
    }
};

// Function to generate related products HTML
window.renderRelatedProducts = function(currentProductId) {
    const relatedProducts = getRelatedProducts(currentProductId);
    const container = document.querySelector('.related-products .products-slider');
    const relatedSection = document.querySelector('.related-products');
    
    // Hide the entire section if no related products
    if (!container || relatedProducts.length === 0) {
        if (relatedSection) relatedSection.style.display = 'none';
        return;
    }
    
    // Show the section if we have products
    if (relatedSection) relatedSection.style.display = '';
    
    container.innerHTML = '';
    
    relatedProducts.forEach(product => {
        const card = document.createElement('div');
        card.className = 'related-product-card';
        card.onclick = () => window.loadProduct(product.id);
        
        card.innerHTML = `
            <div class="related-product-image">
                <img src="/vtekeimg/${product.category}s/${product.id}.png" 
                     alt="${product.name}" 
                     onerror="this.src='/vtekeimg/${product.category}s/ALL.png'">
            </div>
            <div class="related-product-info">
                <h4>${product.name}</h4>
                <p>${product.desc}</p>
                <a href="../${product.folder}/${product.file}" class="related-details-btn">More Details</a>
            </div>
        `;
        
        container.appendChild(card);
    });
};

document.addEventListener('DOMContentLoaded', function() {
    
    // ===== LANGUAGE TOGGLE =====
    const langButtons = document.querySelectorAll('.lang-btn');
    
    langButtons.forEach(btn => {
        btn.addEventListener('click', function() {
            langButtons.forEach(b => b.classList.remove('active'));
            this.classList.add('active');
            const lang = this.getAttribute('data-lang');
            toggleLanguage(lang);
        });
    });
    
    function toggleLanguage(lang) {
        document.querySelectorAll('[class*="-en"], [class*="-tr"]').forEach(el => {
            const className = el.className;
            if(className.includes('-en')) {
                el.style.display = (lang === 'en') ? 'inline' : 'none';
            }
            if(className.includes('-tr')) {
                el.style.display = (lang === 'tr') ? 'inline' : 'none';
            }
        });
        document.documentElement.lang = lang;
    }
    
    // ===== GALLERY IMAGE HANDLER (Click on thumbnails) =====
    const galleryImages = document.querySelectorAll('.gallery-image');
    
    galleryImages.forEach(thumb => {
        thumb.addEventListener('click', function() {
            galleryImages.forEach(img => img.classList.remove('active'));
            this.classList.add('active');
            
            const mainImg = document.getElementById('main-image');
            if(mainImg) {
                mainImg.style.opacity = '0.8';
                setTimeout(() => {
                    mainImg.src = this.src;
                    mainImg.alt = this.alt;
                    mainImg.style.opacity = '1';
                }, 150);
            }
        });
    });
    
    // ===== LIGHTBOX (Using existing HTML structure) =====
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightbox-img');
    
    window.openLightbox = function(wrapper) {
        const img = wrapper.querySelector('img');
        if(img && lightbox && lightboxImg) {
            lightboxImg.src = img.src;
            lightboxImg.alt = img.alt;
            lightbox.classList.add('active');
            document.body.style.overflow = 'hidden';
        }
    };
    
    window.closeLightbox = function(event) {
        if(!event || event.target === lightbox || event.target.classList.contains('lightbox-close') || event.target.closest('.lightbox-close')) {
            if(lightbox) {
                lightbox.classList.remove('active');
                document.body.style.overflow = '';
            }
        }
        if(event) event.stopPropagation();
    };
    
    document.addEventListener('keydown', function(e) {
        if(e.key === 'Escape' && lightbox && lightbox.classList.contains('active')) {
            window.closeLightbox();
        }
    });
    
    if(lightbox) {
        const lightboxContent = lightbox.querySelector('.lightbox-content');
        if(lightboxContent) {
            lightboxContent.addEventListener('click', function(e) {
                e.stopPropagation();
            });
        }
    }
    
    // ===== ACTION BUTTONS =====
    window.requestQuote = function() {
        const lang = document.querySelector('.lang-btn.active')?.getAttribute('data-lang') || 'en';
        const messages = {
            en: 'Thank you for your interest! Our sales team will contact you shortly.',
            tr: 'İlginiz için teşekkür ederiz! Satış ekibimiz sizi kısa süre içinde arayacak.'
        };
        alert(messages[lang] || messages.en);
    };
    
    window.downloadDatasheet = function() {
        const lang = document.querySelector('.lang-btn.active')?.getAttribute('data-lang') || 'en';
        const messages = {
            en: 'Preparing datasheet for download...',
            tr: 'Ürün bilgisi indirmek için hazırlanıyor...'
        };
        alert(messages[lang] || messages.en);
    };

    window.changeImage = function(element) {
        const mainImage = document.getElementById('main-image');
        if(mainImage) {
            mainImage.src = element.src;
            mainImage.alt = element.alt;
        }
        document.querySelectorAll('.gallery-image').forEach(img => {
            img.classList.remove('active');
        });
        element.classList.add('active');
    };
    
    // ===== SMOOTH SCROLL =====
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if(target) {
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });
    
    // ===== Render Related Products =====
    const currentProductId = getCurrentProductInfo();
    if (currentProductId) {
        renderRelatedProducts(currentProductId);
    }
});
