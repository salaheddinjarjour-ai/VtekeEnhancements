#!/usr/bin/env python3
"""
Script to add translation attributes to HTML category pages.
This script adds data-lang-en and data-lang-tr attributes to:
- Hero sections (h1.hero-title, p.hero-subtitle)
- Product names (h2.product-name)
- Product descriptions (p.product-desc)
- View Details buttons
"""

import os
import re

# Translation data for each category page
TRANSLATIONS = {
    "Current Transformer.html": {
        "hero_title": ("Current Transformers", "Akım Transformatörleri"),
        "hero_subtitle": (
            "Premium current transformers for measurement and protection applications. IEC 61869 certified with accuracy classes from 0.2 to 5P20.",
            "Ölçüm ve koruma uygulamaları için premium akım transformatörleri. 0.2'den 5P20'a kadar doğruluk sınıflarına sahip IEC 61869 sertifikalı."
        ),
        "products": [
            {
                "code": "CK20",
                "name_suffix": (" - Measuring Current Transformer", " - Ölçüm Akım Transformatörü"),
                "desc_en": "The CK20 Series Window Type Current Transformer is a compact CT for 40-300A applications, with 1A or 5A secondary output, accuracy classes 0.5, 1, and 3, up to 2.5 VA power, and a 20 mm window diameter.",
                "desc_tr": "CK20 Serisi Pencere Tipi Akım Transformatörü, 40-300A uygulamaları için kompakt bir CT olup, 1A veya 5A ikincil çıkış, 0.5, 1 ve 3 doğruluk sınıfları, 2.5 VA'ya kadar güç ve 20 mm pencere çapına sahiptir."
            },
            {
                "code": "TK30N",
                "name_suffix": (" - Measuring Current Transformer", " - Ölçüm Akım Transformatörü"),
                "desc_en": "The TK30N Series Window Type Current Transformer is a compact CT for 40-600A applications, with 1A or 5A secondary output, accuracy classes 0.5, 1, 3, and 5, up to 3.75 VA power, and a 30X10 mm window size.",
                "desc_tr": "TK30N Serisi Pencere Tipi Akım Transformatörü, 40-600A uygulamaları için kompakt bir CT olup, 1A veya 5A ikincil çıkış, 0.5, 1, 3 ve 5 doğruluk sınıfları, 3.75 VA'ya kadar güç ve 30X10 mm pencere boyutuna sahiptir."
            },
            {
                "code": "TK30",
                "name_suffix": (" - Measuring Current Transformer", " - Ölçüm Akım Transformatörü"),
                "desc_en": "The TK30 Series Window Type Current Transformer is a compact CT for 40-600A applications, with 1A or 5A secondary output, accuracy classes 0.5S, 0.5, 1, and 3, up to 10 VA power, and a 30X10 mm window size.",
                "desc_tr": "TK30 Serisi Pencere Tipi Akım Transformatörü, 40-600A uygulamaları için kompakt bir CT olup, 1A veya 5A ikincil çıkış, 0.5S, 0.5, 1 ve 3 doğruluk sınıfları, 10 VA'ya kadar güç ve 30X10 mm pencere boyutuna sahiptir."
            },
            {
                "code": "TK30A",
                "name_suffix": (" - Measuring Current Transformer", " - Ölçüm Akım Transformatörü"),
                "desc_en": "The TK30A Series Window Type Current Transformer is a compact CT for 25-600A applications, with 1A or 5A secondary output, accuracy classes 0.2S, 0.5S, 0.1, 0.2, 0.5, and 1, up to 30 VA power, and a 30X10 mm window size.",
                "desc_tr": "TK30A Serisi Pencere Tipi Akım Transformatörü, 25-600A uygulamaları için kompakt bir CT olup, 1A veya 5A ikincil çıkış, 0.2S, 0.5S, 0.1, 0.2, 0.5 ve 1 doğruluk sınıfları, 30 VA'ya kadar güç ve 30X10 mm pencere boyutuna sahiptir."
            },
            {
                "code": "TK40",
                "name_suffix": (" - Measuring Current Transformer", " - Ölçüm Akım Transformatörü"),
                "desc_en": "The TK40 Series Window Type Current Transformer is a compact CT for 200-800A applications, with 1A or 5A secondary output, accuracy classes 0.2S, 0.5S, 0.2, 0.5, and 1, up to 10 VA power, and a 40X10 mm window size.",
                "desc_tr": "TK40 Serisi Pencere Tipi Akım Transformatörü, 200-800A uygulamaları için kompakt bir CT olup, 1A veya 5A ikincil çıkış, 0.2S, 0.5S, 0.2, 0.5 ve 1 doğruluk sınıfları, 10 VA'ya kadar güç ve 40X10 mm pencere boyutuna sahiptir."
            },
            {
                "code": "TK40A",
                "name_suffix": (" - Measuring Current Transformer", " - Ölçüm Akım Transformatörü"),
                "desc_en": "The TK40A Series Window Type Current Transformer is a compact CT for 100-800A applications, with 1A or 5A secondary output, accuracy classes 0.2S, 0.2, 0.5S, 0.5, 1, 3, and 5, up to 20 VA power, and a 40X10 mm window size.",
                "desc_tr": "TK40A Serisi Pencere Tipi Akım Transformatörü, 100-800A uygulamaları için kompakt bir CT olup, 1A veya 5A ikincil çıkış, 0.2S, 0.2, 0.5S, 0.5, 1, 3 ve 5 doğruluk sınıfları, 20 VA'ya kadar güç ve 40X10 mm pencere boyutuna sahiptir."
            },
            {
                "code": "TK60",
                "name_suffix": (" - Measuring Current Transformer", " - Ölçüm Akım Transformatörü"),
                "desc_en": "The TK60 Series Window Type CT is a compact transformer for 400-1250A applications, with 1A or 5A secondary output, accuracy classes 0.1, 0.2S, 0.2, 0.5S, 0.5 and 1, up to 15 VA power, and a 60X10 mm window size.",
                "desc_tr": "TK60 Serisi Pencere Tipi CT, 400-1250A uygulamaları için kompakt bir transformatör olup, 1A veya 5A ikincil çıkış, 0.1, 0.2S, 0.2, 0.5S, 0.5 ve 1 doğruluk sınıfları, 15 VA'ya kadar güç ve 60X10 mm pencere boyutuna sahiptir."
            },
            {
                "code": "TK60D",
                "name_suffix": (" - Protection Current Transformer", " - Koruma Akım Transformatörü"),
                "desc_en": "The TK60D Series Window Type CT is a compact transformer for 500-2000A applications, with 1A or 5A secondary output, accuracy classes 0.5 and 1, up to 30 VA power, and a 30X60 mm window size.",
                "desc_tr": "TK60D Serisi Pencere Tipi CT, 500-2000A uygulamaları için kompakt bir transformatör olup, 1A veya 5A ikincil çıkış, 0.5 ve 1 doğruluk sınıfları, 30 VA'ya kadar güç ve 30X60 mm pencere boyutuna sahiptir."
            },
            {
                "code": "TK80",
                "name_suffix": (" - Measuring Current Transformer", " - Ölçüm Akım Transformatörü"),
                "desc_en": "The TK80 Series Window Type CT is a compact transformer for 800-2000A applications, with 1A or 5A secondary output, accuracy classes 0.1, 0.2S, 0.2, 0.5S, 0.5 and 1, up to 30 VA power, and an 80X10 mm window size.",
                "desc_tr": "TK80 Serisi Pencere Tipi CT, 800-2000A uygulamaları için kompakt bir transformatör olup, 1A veya 5A ikincil çıkış, 0.1, 0.2S, 0.2, 0.5S, 0.5 ve 1 doğruluk sınıfları, 30 VA'ya kadar güç ve 80X10 mm pencere boyutuna sahiptir."
            }
        ]
    },
    "protection relay.html": {
        "hero_title": ("Protection Relays", "Koruma Röleleri"),
        "hero_subtitle": (
            "Advanced protection relays for phase, voltage, and current monitoring. Ensure electrical system safety with reliable fault detection and prevention.",
            "Faz, gerilim ve akım izleme için gelişmiş koruma röleleri. Güvenilir arıza tespiti ve önlemesi ile elektrik sistemi güvenliğini sağlayın."
        )
    },
    "timers.html": {
        "hero_title": ("Timers", "Zamanlayıcılar"),
        "hero_subtitle": (
            "Professional timing relays and controllers for industrial automation. Features on-delay, off-delay, star-delta, staircase, and multi-function timers with adjustable time ranges from 0.1 seconds to 100 hours.",
            "Endüstriyel otomasyon için profesyonel zamanlama röleleri ve kontrolörleri. 0.1 saniyeden 100 saate kadar ayarlanabilir zaman aralıklarına sahip açma gecikmesi, kapama gecikmesi, yıldız-üçgen, merdiven ve çok fonksiyonlu zamanlayıcılar."
        )
    },
    "digital meters.html": {
        "hero_title": ("Digital Meters", "Dijital Sayaçlar"),
        "hero_subtitle": (
            "Advanced digital panel meters for precise measurement of voltage, current, and energy. Features RTU RS485 communication and multiple panel sizes for versatile industrial applications.",
            "Gerilim, akım ve enerji hassas ölçümü için gelişmiş dijital panel sayaçları. Çok yönlü endüstriyel uygulamalar için RTU RS485 iletişimi ve birden fazla panel boyutu."
        )
    },
    "analog meters.html": {
        "hero_title": ("Analog Meters", "Analog Sayaçlar"),
        "hero_subtitle": (
            "Professional analog panel meters for precise measurement of current, voltage, and frequency. Available in 72x72mm and 96x96mm sizes with Class 1.5 accuracy.",
            "Akım, gerilim ve frekans hassas ölçümü için profesyonel analog panel sayaçları. Sınıf 1.5 doğrulukla 72x72mm ve 96x96mm boyutlarında mevcuttur."
        )
    },
    "energy analyzer.html": {
        "hero_title": ("Energy Analyzers", "Enerji Analizörleri"),
        "hero_subtitle": (
            "Advanced energy analyzers for comprehensive power quality monitoring. Features energy measurement, power factor analysis, harmonics detection, and communication capabilities for smart grid applications.",
            "Kapsamlı güç kalitesi izleme için gelişmiş enerji analizörleri. Akıllı şebeke uygulamaları için enerji ölçümü, güç faktörü analizi, harmonik tespiti ve iletişim yetenekleri."
        )
    },
    "power factor controller.html": {
        "hero_title": ("Power Factor Controllers", "Güç Faktörü Kontrolörleri"),
        "hero_subtitle": (
            "Advanced power factor controllers for automatic capacitor bank switching. Optimize power factor, reduce energy costs, and improve electrical system efficiency with intelligent control and multiple programming options.",
            "Otomatik kapasitör bankası anahtarlama için gelişmiş güç faktörü kontrolörleri. Akıllı kontrol ve çoklu programlama seçenekleriyle güç faktörünü optimize edin, enerji maliyetlerini azaltın ve elektrik sistemi verimliliğini artırın."
        )
    },
    "control relay.html": {
        "hero_title": ("Control Relays", "Kontrol Röleleri"),
        "hero_subtitle": (
            "Advanced control relays for automated system control including photocell relays, liquid level control relays, and pump alternation controllers. Reliable automation solutions for industrial and commercial applications.",
            "Fotoelektrik röleler, sıvı seviye kontrol röleleri ve pompa alternatif kontrolörleri dahil otomatik sistem kontrolü için gelişmiş kontrol röleleri. Endüstriyel ve ticari uygulamalar için güvenilir otomasyon çözümleri."
        )
    },
    "battery charger.html": {
        "hero_title": ("Battery Chargers", "Akü Şarj Cihazları"),
        "hero_subtitle": (
            "Intelligent battery chargers for 12V and 24V systems. Advanced charging algorithms with multi-stage protection for extended battery life and reliable backup power.",
            "12V ve 24V sistemler için akıllı akü şarj cihazları. Uzun pil ömrü ve güvenilir yedek güç için çok aşamalı korumalı gelişmiş şarj algoritmaları."
        )
    },
    "power supply.html": {
        "hero_title": ("Power Supply", "Güç Kaynağı"),
        "hero_subtitle": (
            "Reliable switching power supplies for industrial automation and control systems. Features wide input voltage range, stable 24V DC output, and compact design for panel mounting.",
            "Endüstriyel otomasyon ve kontrol sistemleri için güvenilir anahtamalı güç kaynakları. Panel montajı için geniş giriş gerilimi aralığı, kararlı 24V DC çıkışı ve kompakt tasarım."
        )
    }
}

def add_translations_to_file(filepath):
    """Add translation attributes to a single HTML file."""
    print(f"Processing: {filepath}")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    filename = os.path.basename(filepath)

    if filename in TRANSLATIONS:
        trans = TRANSLATIONS[filename]
        if "hero_title" in trans:
            title_en, title_tr = trans["hero_title"]
            subtitle_en, subtitle_tr = trans["hero_subtitle"]
            
            # Check if hero title has data-lang attribute by checking the hero section
            hero_match = re.search(r'<h1 class="hero-title"[^>]*data-lang-en', content)
            if not hero_match:
                # Replace hero title
                content = re.sub(
                    r'(<h1 class="hero-title")>([^<]+)</h1>',
                    rf'\1 data-lang-en="{title_en}" data-lang-tr="{title_tr}">\2</h1>',
                    content
                )
                print(f"  - Added hero title translation")
            
            # Check hero subtitle
            hero_sub_match = re.search(r'<p class="hero-subtitle"[^>]*data-lang-en', content)
            if not hero_sub_match:
                content = re.sub(
                    r'(<p class="hero-subtitle")>([^<]+)</p>',
                    rf'\1 data-lang-en="{subtitle_en}" data-lang-tr="{subtitle_tr}">\2</p>',
                    content
                )
                print(f"  - Added hero subtitle translation")
            
            if hero_match and hero_sub_match:
                print(f"  - Hero translations already exist")

    # Check if translation JavaScript already exists
    if '// Apply translations on page load' not in content:
        # Add translation script before </body>
        translation_script = '''
    <script>
    // Apply translations on page load
    (function() {
      const lang = localStorage.getItem('vteke_language') || 'en';
      document.querySelectorAll('[data-lang-en]').forEach(el => {
        const translation = el.getAttribute('data-lang-' + lang);
        if (translation) {
          el.textContent = translation;
        }
      });
      // Handle product name spans
      document.querySelectorAll('h2.product-name span[data-lang-en]').forEach(el => {
        const translation = el.getAttribute('data-lang-' + lang);
        if (translation) {
          el.textContent = translation;
        }
      });
    })();
    </script>
'''
        content = content.replace('</body>', translation_script + '\n</body>')
        print(f"  - Added translation script")
    else:
        print(f"  - Translation script already exists")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  - Done")

def main():
    """Main function to process all HTML files."""
    base_path = "/Users/marwaghalayini/Salaheddin's Work/Websites/vteke_Upgrades"

    files_to_process = [
        "Current Transformer.html",
        "protection relay.html",
        "timers.html",
        "digital meters.html",
        "analog meters.html",
        "energy analyzer.html",
        "power factor controller.html",
        "control relay.html",
        "battery charger.html",
        "power supply.html"
    ]

    for filename in files_to_process:
        filepath = os.path.join(base_path, filename)
        if os.path.exists(filepath):
            add_translations_to_file(filepath)
        else:
            print(f"File not found: {filepath}")

if __name__ == "__main__":
    main()
