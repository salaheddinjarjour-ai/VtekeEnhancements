/* ========================================
   VTEKE - Product Page Scripts (FIXED)
   ======================================== */

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
    
    // ✅ تم تعريف الدالة على window لتكون متاحة لـ onclick في HTML
    window.openLightbox = function(wrapper) {
        const img = wrapper.querySelector('img');
        if(img && lightbox && lightboxImg) {
            lightboxImg.src = img.src;
            lightboxImg.alt = img.alt;
            lightbox.classList.add('active');
            document.body.style.overflow = 'hidden'; // منع التمرير في الخلفية
        }
    };
    
    // ✅ دالة الإغلاق متاحة عالمياً
    window.closeLightbox = function(event) {
        // إذا كان الحدث فارغاً (تم الاستدعاء يدوياً) أو تم الضغط على الخلفية أو زر الإغلاق
        if(!event || event.target === lightbox || event.target.classList.contains('lightbox-close') || event.target.closest('.lightbox-close')) {
            if(lightbox) {
                lightbox.classList.remove('active');
                document.body.style.overflow = '';
            }
        }
        if(event) event.stopPropagation();
    };
    
    // إغلاق اللايت بوكس عند ضغط زر Escape
    document.addEventListener('keydown', function(e) {
        if(e.key === 'Escape' && lightbox && lightbox.classList.contains('active')) {
            window.closeLightbox();
        }
    });
    
    // منع إغلاق اللايت بوكس عند الضغط على الصورة نفسها
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

    // ✅ دالة تغيير الصورة متاحة عالمياً لأكواد HTML
    window.changeImage = function(element) {
        const mainImage = document.getElementById('main-image');
        if(mainImage) {
            mainImage.src = element.src;
            mainImage.alt = element.alt;
        }
        // تحديث الكلاس النشط
        document.querySelectorAll('.gallery-image').forEach(img => {
            img.classList.remove('active');
        });
        element.classList.add('active');
    };

    // دالة تحميل منتج آخر
    window.loadProduct = function(productId) {
        console.log('Loading product:', productId);
        // window.location.href = '/products/' + productId; // مثال للتوجيه
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
});