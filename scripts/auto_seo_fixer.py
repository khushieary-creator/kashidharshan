#!/usr/bin/env python3
"""
Auto SEO Fixer Script:
1. Fixes missing meta keywords, OpenGraph tags, canonicals & Schema JSON-LD on city guides:
   - ayodhya-guide.html
   - varanasi-guide.html
   - prayagraj-guide.html
   - chitrakoot-guide.html
   - naimisharanya-guide.html
   - vindhyachal-guide.html
   - mathura-guide.html
   - vrindavan-guide.html
   - about.html
   - feedback.html
   - thankyou.html
2. Regenerates sitemap.xml & rss_feed.xml to include all HTML pages (except Google verification file).
"""

import os
import glob
import re
from datetime import datetime

def fix_city_guides():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    city_configs = {
        'varanasi-guide.html': {
            'title': 'Varanasi City Guide 2026 - Kashi Vishwanath VIP Darshan & Ghats',
            'desc': 'Complete Varanasi travel guide 2026. Explore Kashi Vishwanath Dham VIP Sugam Darshan booking, Dashashwamedh Ganga Aarti boat rides, Sarnath Buddhist tour & heritage walking routes.',
            'kw': 'Varanasi travel guide 2026, Kashi Vishwanath VIP Sugam Darshan booking, Dashashwamedh Ghat Ganga Aarti, Sarnath tour package, Varanasi local sightseeing taxi, Banarasi saree shopping, Kashi Yatra guide',
            'schema_type': 'TravelGuide',
            'name': 'Varanasi Travel & Sightseeing Guide 2026'
        },
        'ayodhya-guide.html': {
            'title': 'Ayodhya City Guide 2026 - Ram Mandir VIP Darshan & Saryu Aarti',
            'desc': 'Complete Ayodhya travel guide 2026. Includes Ram Janmabhoomi VIP pass booking, Hanuman Garhi temple timings, Kanak Bhawan sightseeing & Saryu River evening Aarti.',
            'kw': 'Ayodhya travel guide 2026, Ram Mandir VIP Darshan pass booking, Hanuman Garhi temple timings, Kanak Bhawan Ayodhya, Saryu Aarti boat ride, Ayodhya Dham railway station taxi',
            'schema_type': 'TravelGuide',
            'name': 'Ayodhya Ram Janmabhoomi Travel Guide 2026'
        },
        'prayagraj-guide.html': {
            'title': 'Prayagraj City Guide 2026 - Triveni Sangam Snan & Kumbh Mela',
            'desc': 'Complete Prayagraj travel guide 2026. Sangam boat charges, Triveni Sangam holy dip rituals, Lete Hue Hanuman Ji temple, Alopi Devi Shaktipeeth & Anand Bhawan tour.',
            'kw': 'Prayagraj travel guide 2026, Triveni Sangam boat ride charges, Lete Hanuman Ji Mandir prayagraj, Alopi Devi Shaktipeeth, Anand Bhawan museum, Prayagraj Kumbh Mela tour',
            'schema_type': 'TravelGuide',
            'name': 'Prayagraj Triveni Sangam Travel Guide 2026'
        },
        'chitrakoot-guide.html': {
            'title': 'Chitrakoot City Guide 2026 - Kamadgiri Parikrama & Ramghat Aarti',
            'desc': 'Complete Chitrakoot travel guide 2026. Kamadgiri 5km parikrama route, Ramghat Mandakini evening Aarti, Gupt Godavari caves, Hanuman Dhara waterfall & Sati Anusuya ashram.',
            'kw': 'Chitrakoot travel guide 2026, Kamadgiri parikrama route distance, Ramghat Mandakini Aarti, Gupt Godavari caves tour, Hanuman Dhara ropeway, Sati Anusuya ashram Chitrakoot',
            'schema_type': 'TravelGuide',
            'name': 'Chitrakoot Dham Ram Vanvas Travel Guide 2026'
        },
        'naimisharanya-guide.html': {
            'title': 'Naimisharanya City Guide 2026 - Chakra Tirth Snan & Lalita Devi',
            'desc': 'Complete Naimisharanya travel guide 2026. Chakra Tirth holy snan, Maa Lalita Devi Shaktipeeth darshan, Maharishi Ved Vyas Gaddi, Dadhichi Kund & 84 Kos Parikrama route.',
            'kw': 'Naimisharanya travel guide 2026, Chakra Tirth holy snan, Maa Lalita Devi Shaktipeeth darshan, Maharishi Ved Vyas Gaddi, Dadhichi Kund, Naimisharanya 84 Kos Parikrama',
            'schema_type': 'TravelGuide',
            'name': 'Naimisharanya Dham Travel Guide 2026'
        },
        'vindhyachal-guide.html': {
            'title': 'Vindhyachal City Guide 2026 - Maa Vindhyavasini & Trikon Parikrama',
            'desc': 'Complete Vindhyachal travel guide 2026. Maa Vindhyavasini Shaktipeeth VIP darshan, Kali Khoh temple, Ashtabhuja Devi mandir & Trikon Parikrama circuit route.',
            'kw': 'Vindhyachal travel guide 2026, Maa Vindhyavasini Shaktipeeth darshan, Kali Khoh temple Mirzapur, Ashtabhuja Devi mandir, Vindhyachal Trikon Parikrama route',
            'schema_type': 'TravelGuide',
            'name': 'Vindhyachal Dham Travel Guide 2026'
        },
        'mathura-guide.html': {
            'title': 'Mathura City Guide 2026 - Shri Krishna Janmabhoomi & Vishram Ghat',
            'desc': 'Complete Mathura travel guide 2026. Shri Krishna Janmabhoomi temple darshan, Dwarkadhish Mandir timings, Vishram Ghat Yamuna Aarti & Mathura Peda shopping guide.',
            'kw': 'Mathura travel guide 2026, Shri Krishna Janmabhoomi darshan timing, Dwarkadhish Temple Mathura, Vishram Ghat Yamuna Aarti boat ride, Mathura famous Peda shops',
            'schema_type': 'TravelGuide',
            'name': 'Mathura Shri Krishna Janmabhoomi Travel Guide 2026'
        },
        'vrindavan-guide.html': {
            'title': 'Vrindavan City Guide 2026 - Banke Bihari & Prem Mandir Light Show',
            'desc': 'Complete Vrindavan travel guide 2026. Shri Banke Bihari Mandir VIP darshan timing, Prem Mandir evening light show, ISKCON temple, Nidhivan mystery & Govardhan parikrama.',
            'kw': 'Vrindavan travel guide 2026, Banke Bihari Mandir VIP darshan timing, Prem Mandir light show timing, ISKCON Vrindavan, Nidhivan mystery, Govardhan Parikrama distance',
            'schema_type': 'TravelGuide',
            'name': 'Vrindavan Dham Travel Guide 2026'
        },
        'about.html': {
            'title': 'About Us - Kashi Dharshan Sacred Yatra & Pilgrimage Experts',
            'desc': 'Learn about Kashi Dharshan, your trusted spiritual travel operator for Uttar Pradesh sacred yatras, VIP darshan passes, private cab rentals & customized pilgrimage packages.',
            'kw': 'About Kashi Dharshan, UP pilgrimage tour operator, Kashi Vishwanath VIP darshan agency, Ayodhya Ram Mandir tour booking company, Varanasi tour operator',
            'schema_type': 'AboutPage',
            'name': 'About Kashi Dharshan Yatra Travel Services'
        },
        'feedback.html': {
            'title': 'Customer Feedback & Reviews - Kashi Dharshan Pilgrimage Tours',
            'desc': 'Read authentic reviews and travel experiences from pilgrims who booked Kashi Vishwanath VIP darshan, Ayodhya Ram Mandir packages & UP sacred yatra tours with Kashi Dharshan.',
            'kw': 'Kashi Dharshan reviews, Varanasi tour feedback, Ayodhya Ram Mandir yatra reviews, UP pilgrimage tour agency rating, pilgrim testimonials',
            'schema_type': 'WebPage',
            'name': 'Kashi Dharshan Pilgrim Reviews & Feedback'
        },
        'thankyou.html': {
            'title': 'Thank You - Booking Enquiry Received | Kashi Dharshan',
            'desc': 'Thank you for submitting your booking enquiry with Kashi Dharshan. Our travel experts will reach out to you within 30 minutes with your customized itinerary.',
            'kw': 'Kashi Dharshan booking confirmation, thank you page, tour request confirmation',
            'schema_type': 'WebPage',
            'name': 'Kashi Dharshan Booking Confirmation'
        }
    }

    for filename, cfg in city_configs.items():
        filepath = os.path.join(root_dir, filename)
        if not os.path.exists(filepath):
            continue

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        page_url = f"https://www.kashidharshan.com/{filename}"

        # 1. Title
        content = re.sub(r'<title>.*?</title>', f'<title>{cfg["title"]}</title>', content, flags=re.IGNORECASE | re.DOTALL)

        # 2. Meta description
        if 'name="description"' in content:
            content = re.sub(r'<meta\s+name="description"\s+content="[^"]*"', f'<meta name="description" content="{cfg["desc"]}">', content, flags=re.IGNORECASE)
        else:
            content = content.replace('</head>', f'  <meta name="description" content="{cfg["desc"]}">\n</head>', 1)

        # 3. Meta keywords
        if 'name="keywords"' in content:
            content = re.sub(r'<meta\s+name="keywords"\s+content="[^"]*"', f'<meta name="keywords" content="{cfg["kw"]}">', content, flags=re.IGNORECASE)
        else:
            content = content.replace('</head>', f'  <meta name="keywords" content="{cfg["kw"]}">\n</head>', 1)

        # 4. Canonical
        if 'rel="canonical"' in content:
            content = re.sub(r'<link\s+rel="canonical"\s+href="[^"]*"', f'<link rel="canonical" href="{page_url}">', content, flags=re.IGNORECASE)
        else:
            content = content.replace('</head>', f'  <link rel="canonical" href="{page_url}">\n</head>', 1)

        # 5. OpenGraph Tags
        og_tags = f'''  <meta property="og:locale" content="en_US">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{cfg['title']}">
  <meta property="og:description" content="{cfg['desc']}">
  <meta property="og:url" content="{page_url}">
  <meta property="og:site_name" content="Kashi Dharshan">
  <meta property="og:image" content="https://www.kashidharshan.com/images/og-main.jpg">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{cfg['title']}">
  <meta name="twitter:description" content="{cfg['desc']}">
  <meta name="twitter:image" content="https://www.kashidharshan.com/images/og-main.jpg">'''

        if 'property="og:title"' in content:
            content = re.sub(r'<meta\s+property="og:title"\s+content="[^"]*"', f'<meta property="og:title" content="{cfg["title"]}">', content, flags=re.IGNORECASE)
            content = re.sub(r'<meta\s+property="og:description"\s+content="[^"]*"', f'<meta property="og:description" content="{cfg["desc"]}">', content, flags=re.IGNORECASE)
            content = re.sub(r'<meta\s+property="og:url"\s+content="[^"]*"', f'<meta property="og:url" content="{page_url}">', content, flags=re.IGNORECASE)
        else:
            content = content.replace('</head>', f'{og_tags}\n</head>', 1)

        # 6. JSON-LD Schema
        schema_json = f'''
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "{cfg['schema_type']}",
  "name": "{cfg['name']}",
  "description": "{cfg['desc']}",
  "url": "{page_url}",
  "publisher": {{
    "@type": "Organization",
    "name": "Kashi Dharshan",
    "url": "https://www.kashidharshan.com/"
  }}
}}
</script>'''

        if '<script type="application/ld+json">' not in content:
            content = content.replace('</head>', f'{schema_json}\n</head>', 1)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"Fixed SEO tags on {filename}")

def update_sitemap():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sitemap_path = os.path.join(root_dir, 'sitemap.xml')

    html_files = sorted(glob.glob(os.path.join(root_dir, '*.html')))
    today_str = datetime.now().strftime('%Y-%m-%d')

    url_entries = []
    for filepath in html_files:
        filename = os.path.basename(filepath)
        if filename.startswith('google') or filename == 'search.html':
            continue

        loc = f"https://www.kashidharshan.com/{filename}"
        priority = "0.80"
        freq = "weekly"

        if filename == 'index.html':
            loc = "https://www.kashidharshan.com/"
            priority = "1.00"
            freq = "daily"
        elif filename in ['destinations.html', 'packages.html', 'blog.html']:
            priority = "0.90"
            freq = "daily"
        elif filename.endswith('-tour-package.html') or filename.endswith('-guide.html'):
            priority = "0.85"
            freq = "daily"

        url_entries.append(f'''  <url>
    <loc>{loc}</loc>
    <lastmod>{today_str}</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>{priority}</priority>
  </url>''')

    sitemap_xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(url_entries)}
</urlset>'''

    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(sitemap_xml.strip())

    print(f"Updated sitemap.xml with {len(url_entries)} URLs!")

def main():
    fix_city_guides()
    update_sitemap()

if __name__ == '__main__':
    main()
