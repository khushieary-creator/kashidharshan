#!/usr/bin/env python3
"""
Replicates the exact winning SEO Architecture, Meta Tags, Schema @graph, 
Robots tags, and Keyword density from ayodhyadharshan.com directly into kashidharshan.com
to shoot impressions from 395 to 11.4K+ and clicks to 130+!
"""

import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 1. Exact Winning Robots Tag from ayodhyadharshan.com
WINNING_ROBOTS_TAG = '<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">'

# 2. Exact Winning Title Tags for Core Pages
WINNING_TITLES = {
    "index.html": "Kashi Vishwanath & Varanasi Darshan Tour Packages 2026",
    "varanasi-tour-package.html": "Varanasi Tour Package 2026: Kashi Vishwanath VIP Darshan",
    "ayodhya-tour-package.html": "Ayodhya Ram Mandir & Darshan Tour Packages 2026",
    "prayagraj-tour-package.html": "Prayagraj Sangam & Kumbh Yatra Tour Packages 2026",
    "mathura-tour-package.html": "Mathura Vrindavan Krishna Darshan Tour Packages 2026"
}

# 3. Exact Winning Keywords List (Comprehensive 150+ High-Volume Keywords)
WINNING_KEYWORDS_KASHI = "Kashi Tour Packages, Kashi travel package, Kashi trip package, Kashi pilgrimage tour, Kashi temple tour, Kashi weekend tour, Kashi tour cost, Kashi darshan tour, Varanasi Ayodhya Tour Package, Varanasi Prayagraj Ayodhya Tour Package, Ayodhya Kashi tour package, Kashi Vishwanath darshan package, sugam yatra kashi, vip darshan kashi vishwanath, tour and travel agency in varanasi, kashi vishwanath darshan booking online, best tour packages for varanasi, tour and travels in varanasi, varanasi tour packages for couple, varanasi local sightseeing tour package, best travel agency in varanasi, kashi dharshan tour package, kashi vishwanath package, best places to stay in varanasi with family, varanasi tour package from mumbai, varanasi tour packages from nagpur, varanasi to ayodhya tour package, kashi ayodhya prayagraj tour package, varanasi tours and travel, irctc tour packages varanasi, trip to varanasi and ayodhya, places to visit varanasi, online booking of kashi vishwanath darshan, kashi vishwanath booking, varanasi ayodhya prayagraj bodhgaya tour package, kashi trip packages, good hotels in varanasi near kashi vishwanath, trip plan for varanasi, chennai to varanasi package, kashi vishwanath vip darshan, varanasi and ayodhya, kashi vishwanath corridor, up tourism online booking, varanasi temple visit, varanasi tour from ahmedabad, varanasi and ayodhya package, uttar pradesh tour packages, varanasi sightseeing tour, room booking in varanasi, best places to stay at varanasi, how many days required to visit varanasi dham, varanasi temple tour package, varanasi tour packages from mumbai, varanasi package from bangalore, stay in varanasi, places to visit varanasi dham, bangalore to varanasi package, varanasi kashi vishwanath ticket online booking, dharamshala booking varanasi, varanasi tour packages from chennai, varanasi itinerary for 2 days from delhi, banaras ayodhya tour plan, kolkata to varanasi kashi vishwanath tour guide, up tour package, varanasi itinerary for 3 days, varanasi trip, varanasi trip package from mumbai, varanasi darshan for senior citizens, kashi vishwanath visit, kashi vishwanath darshan booking, bangalore to varanasi tour package, varanasi ticket, shri kashi vishwanath temple varanasi, kolkata to varanasi tour package, kashi vishwanath sugam darshan, kashi ayodhya tour package from bangalore, varanasi tourism places, kashi vishwanath mandir vip darshan, varanasi 3 day itinerary, famous temples to visit in varanasi, mumbai to varanasi ayodhya tour package, varanasi trip itinerary, tours to varanasi, varanasi yatra package, varanasi tour package for family, hotels at varanasi, varanasi kashi prayagraj tour package, tour packages for varanasi, darshan at kashi vishwanath temple, prayagraj ayodhya varanasi tour package, varanasi ayodhya tour package from mumbai, varanasi ayodhya 4 days itinerary, varanasi ayodhya tour package from hyderabad, irctc package for varanasi, vip darshan at kashi vishwanath, delhi to varanasi tour, best places to stay in varanasi, kashi vishwanath shri ram darshan, places to see in varanasi in 1 day, varanasi tour plan for 2 days, delhi to varanasi tourist places, 2 days varanasi tour package, kashi vishwanath temple darshan online booking, varanasi booking online, 3 star hotels in varanasi near kashi vishwanath, how to go to varanasi from chennai, hyderabad to varanasi package, varanasi mandir tour package, surat to varanasi tour package, kashi vishwanath trip package, 1 night 2 days varanasi itinerary, 2 day itinerary varanasi, ahmedabad to varanasi package, ahmedabad to varanasi tour package, kashi darshan 1 day tour, kashi darshan 2 day itinerary, kashi and naimisharanya tour package, kashi and prayagraj tour package, kashi and varanasi tour, kashi banaras trip, kashi booking darshan, kashi booking online, kashi city tour, kashi darshan, kashi darshan booking, kashi darshan booking online, kashi darshan for senior citizens, kashi darshan guide, kashi darshan how much time, kashi darshan online, kashi darshan online booking, kashi darshan package, kashi darshan pass, kashi darshan ticket, kashi darshan tour and travels, kashi darshan tour package, kashi darshan vip, kashi darshanam, kashi day tour, kashi dham darshan, kashi dham darshan booking, kashi dham darshan time, kashi dham online booking, kashi dham places to visit"

# 4. Winning Schema @graph for Kashi Dharshan
WINNING_SCHEMA_GRAPH = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "TravelAgency",
      "datePublished": "2026-01-01",
      "dateModified": "2026-10-07",
      "@id": "https://www.kashidharshan.com/#org",
      "name": "Kashi Dharshan",
      "alternateName": ["Kashi Dharshan Teerth Yatra", "Kashi Darshan", "Kashi Vishwanath VIP Darshan"],
      "url": "https://www.kashidharshan.com/",
      "logo": "https://www.kashidharshan.com/assets/logo.png",
      "image": "https://www.kashidharshan.com/assets/reviews/kashi-temple.jpg",
      "description": "Guided, fully-managed pilgrimage tour packages across Varanasi (Kashi), Ayodhya, Prayagraj, Chitrakoot, Naimisharanya, Vindhyachal, Mathura and Vrindavan.",
      "telephone": "+91-7408763401",
      "priceRange": "₹₹",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "Dashashwamedh Ghat Road, Godowlia",
        "addressLocality": "Varanasi",
        "addressRegion": "Uttar Pradesh",
        "postalCode": "221001",
        "addressCountry": "IN"
      },
      "areaServed": ["Varanasi","Ayodhya","Prayagraj","Chitrakoot","Naimisharanya","Vindhyachal","Mathura","Vrindavan"],
      "sameAs": [
        "https://www.instagram.com/",
        "https://www.facebook.com/",
        "https://wa.me/917408763401?text=Har%20Har%20Mahadev!%20I%20want%20to%20enquire%20about%20Kashi%20Dharshan%20tour%20packages."
      ],
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "4.9",
        "reviewCount": "1280"
      }
    },
    {
      "@type": "ItemList",
      "name": "Kashi Yatra Tour Packages",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "item": { "@type": "TouristTrip", "name": "Kashi Vishwanath VIP Darshan Package", "description": "Quick 1-day yatra covering Kashi Vishwanath Sugam Darshan VIP entry, Ganga Aarti boat ride, and Sarnath.", "touristType": "Pilgrimage", "offers": { "@type": "Offer", "price": "2900", "priceCurrency": "INR" } } },
        { "@type": "ListItem", "position": 2, "item": { "@type": "TouristTrip", "name": "Varanasi Kashi Dharshan Tour Package", "description": "3 days / 2 nights Varanasi darshan covering Kashi Vishwanath, Ganga Aarti, Subah-e-Banaras and Sarnath.", "touristType": "Pilgrimage", "offers": { "@type": "Offer", "price": "7900", "priceCurrency": "INR" } } },
        { "@type": "ListItem", "position": 3, "item": { "@type": "TouristTrip", "name": "Varanasi Ayodhya Combined Tour Package", "description": "4 days / 3 nights covering Varanasi Kashi Vishwanath and Ayodhya Ram Mandir with Saryu Aarti.", "touristType": "Pilgrimage", "offers": { "@type": "Offer", "price": "12900", "priceCurrency": "INR" } } },
        { "@type": "ListItem", "position": 4, "item": { "@type": "TouristTrip", "name": "Varanasi Ayodhya Prayagraj Circuit Tour Package", "description": "5 days / 4 nights covering Kashi Vishwanath, Ayodhya Ram Mandir, and Prayagraj Triveni Sangam.", "touristType": "Pilgrimage", "offers": { "@type": "Offer", "price": "17500", "priceCurrency": "INR" } } },
        { "@type": "ListItem", "position": 5, "item": { "@type": "TouristTrip", "name": "Varanasi Prayagraj Chitrakoot Ayodhya Tour Package", "description": "6 days / 5 nights across Varanasi, Prayagraj, Chitrakoot and Ayodhya.", "touristType": "Pilgrimage", "offers": { "@type": "Offer", "price": "23900", "priceCurrency": "INR" } } },
        { "@type": "ListItem", "position": 6, "item": { "@type": "TouristTrip", "name": "Full Ramayana Circuit Tour Package", "description": "8 days / 7 nights across Varanasi, Naimisharanya, Prayagraj, Chitrakoot, Ayodhya and Vindhyachal.", "touristType": "Pilgrimage", "offers": { "@type": "Offer", "price": "31900", "priceCurrency": "INR" } } }
      ]
    },
    {
      "@type": "WebSite",
      "name": "Kashi Dharshan",
      "url": "https://www.kashidharshan.com/",
      "potentialAction": {
        "@type": "SearchAction",
        "target": "https://www.kashidharshan.com/?s={search_term_string}",
        "query-input": "required name=search_term_string"
      }
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        { "@type": "Question", "name": "How to book VIP Darshan or Sugam Darshan at Kashi Vishwanath Temple?", "acceptedAnswer": { "@type": "Answer", "text": "Official Sugam Darshan (VIP Pass) or Aarti passes can be booked online on the official portal. Alternatively, our Kashi Dharshan tour packages include complete VIP darshan booking assistance, making entry comfortable for senior citizens and families." } },
        { "@type": "Question", "name": "How much does a Kashi Dharshan tour package cost?", "acceptedAnswer": { "@type": "Answer", "text": "A Kashi Dharshan tour package starts from ₹7,900 per person for a 3-day / 2-night trip, including hotel stays, private AC travel, local guide and darshan assistance." } },
        { "@type": "Question", "name": "How many days are needed for Varanasi Kashi darshan?", "acceptedAnswer": { "@type": "Answer", "text": "2 nights / 3 days is ideal for visiting Kashi Vishwanath Temple, Ganga Aarti at Dashashwamedh, Sarnath, and morning boat ride. Add 2–3 days to cover Ayodhya, Prayagraj or Vindhyachal." } },
        { "@type": "Question", "name": "How far is Ayodhya from Varanasi, and how many days are needed?", "acceptedAnswer": { "@type": "Answer", "text": "Varanasi is about 200–230 km from Ayodhya — roughly 4–5 hours by road or Vande Bharat train. A combined Varanasi–Ayodhya tour package is comfortable in 4 days / 3 nights." } }
      ]
    }
  ]
}
</script>"""

# 5. Winning Govt & Trust Badge Hero HTML
WINNING_GOVT_BADGE_HTML = """
<div class="govt-badge" style="display: inline-flex; align-items: center; gap: 8px; background: rgba(4, 120, 87, 0.08); border: 1px solid rgba(4, 120, 87, 0.3); border-radius: 100px; padding: 6px 14px; margin-bottom: 15px;">
  <span style="width: 6px; height: 6px; border-radius: 50%; background: #047857; display: inline-block;"></span>
  <span style="color: #047857; font-size: 11px; font-weight: 600; letter-spacing: 0.05em; text-transform: uppercase;">Govt. Registered UP Yatra Agency (GSTIN: 09CJPPJ6346G1ZR)</span>
</div>
"""

def replicate_winning_architecture():
    updated = 0
    
    for root, _, files in os.walk(BASE_DIR):
        for f in files:
            if f.endswith(".html") and not f.startswith("google"):
                filepath = os.path.join(root, f)
                with open(filepath, "r", encoding="utf-8") as fh:
                    content = fh.read()
                    
                orig_content = content
                
                # A. Replace Title Tag if in WINNING_TITLES
                if f in WINNING_TITLES:
                    content = re.sub(r'<title>(.*?)</title>', f'<title>{WINNING_TITLES[f]}</title>', content, flags=re.IGNORECASE)
                    
                # B. Inject Winning Robots Tag
                if 'name="robots"' in content:
                    content = re.sub(r'<meta\s+name="robots"\s+content="[^"]*"[^>]*>', WINNING_ROBOTS_TAG, content, flags=re.IGNORECASE)
                else:
                    if '</head>' in content:
                        content = content.replace('</head>', WINNING_ROBOTS_TAG + '\n</head>')
                        
                # C. Replace Meta Keywords with 150+ Winning Keyword List
                meta_kw_tag = f'<meta name="keywords" content="{WINNING_KEYWORDS_KASHI}">'
                if 'name="keywords"' in content:
                    content = re.sub(r'<meta\s+name="keywords"\s+content="[^"]*"[^>]*>', meta_kw_tag, content, flags=re.IGNORECASE)
                else:
                    if '</head>' in content:
                        content = content.replace('</head>', meta_kw_tag + '\n</head>')
                        
                # D. Inject Schema @graph into index.html, varanasi-tour-package.html, ayodhya-tour-package.html
                if f in ['index.html', 'varanasi-tour-package.html', 'ayodhya-tour-package.html']:
                    if 'https://schema.org' in content:
                        # Replace existing schema scripts with WINNING_SCHEMA_GRAPH
                        content = re.sub(r'<script type="application/ld\+json">.*?</script>', '', content, flags=re.DOTALL)
                        if '</head>' in content:
                            content = content.replace('</head>', WINNING_SCHEMA_GRAPH + '\n</head>')
                            
                # E. Inject Govt Trust Badge on index.html
                if f == 'index.html' and 'Govt. Registered UP Yatra Agency' not in content:
                    if '<h1' in content:
                        content = re.sub(r'(<h1[^>]*>)', WINNING_GOVT_BADGE_HTML + r'\1', content, flags=re.IGNORECASE)
                        
                if content != orig_content:
                    with open(filepath, "w", encoding="utf-8") as fh:
                        fh.write(content)
                    updated += 1
                    
    print(f"🔥 Successfully replicated ayodhyadharshan.com's winning SEO Architecture across {updated} HTML files!")

if __name__ == "__main__":
    replicate_winning_architecture()
