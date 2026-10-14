import os
import re
import glob
import json

print("Starting Task 1, Task 2 & Task 5: Eliminating 308 Redirect Loop, Sanitizing Keywords & Generating Clean Sitemap...")

# ----------------------------------------------------------------------
# 1. UPDATE VERCEL.JSON
# ----------------------------------------------------------------------
vercel_config = {
    "cleanUrls": True,
    "trailingSlash": False
}

with open("vercel.json", "w", encoding="utf-8") as f:
    json.dump(vercel_config, f, indent=2)

print("Updated vercel.json with cleanUrls: true and trailingSlash: false!")

# ----------------------------------------------------------------------
# 2. COLLECT ALL HTML FILES
# ----------------------------------------------------------------------
all_html_files = sorted(glob.glob("*.html"))
# Exclude google verification
target_html_files = [f for f in all_html_files if f != "google0dc20d35f8fb3bcd.html"]
print(f"Total HTML files to process: {len(target_html_files)}")

# Build list of base names (without .html)
slugs = {f: f[:-5] for f in target_html_files}

# ----------------------------------------------------------------------
# 3. HELPER FUNCTION TO SANITIZE META KEYWORDS (TASK 5)
# ----------------------------------------------------------------------
def get_clean_keywords(filename, content):
    base = filename[:-5]
    if filename == "index.html":
        return "Kashi tour package, Kashi Vishwanath VIP darshan, Varanasi pilgrimage tour, Varanasi Ganga Aarti boat booking, Sarnath tour package"
    elif "kashi-vishwanath-sugam-darshan" in base:
        return "Kashi Vishwanath Sugam Darshan booking, VIP pass price, Gate 4 queue-less darshan, Kashi VIP darshan ticket, Varanasi temple VIP entry"
    elif "varanasi-ganga-aarti-boat-booking" in base:
        return "Dashashwamedh Ghat Ganga Aarti boat booking, private bajra boat price, motorboat sharing rates, Varanasi boat ride cost, evening aarti boat booking"
    elif "mangla-aarti-kashi-vishwanath" in base:
        return "Kashi Vishwanath Mangla Aarti booking time, 3:00 AM pass, ticket quota, Mangla aarti price, Kashi morning aarti booking online"
    elif "varanasi-airport-to-kashi-vishwanath" in base:
        return "Varanasi airport to temple cab fare, Lal Bahadur Shastri airport taxi to Godowlia, Varanasi airport taxi rate, Kashi Vishwanath airport cab booking"
    elif "kashi-vishwanath-tour-package" in base:
        return "Kashi Vishwanath tour package, Kashi VIP darshan pass, Varanasi 3 day tour, Dashashwamedh Ganga Aarti boat, Sarnath yatra"
    elif "varanasi-tour-package" in base or "varanasi-same-day" in base:
        return "Varanasi tour package 2026, Kashi darshan tour, Varanasi local sightseeing, Kashi Vishwanath darshan, Ganga Aarti boat ride"
    elif "ayodhya-tour-package" in base or "ayodhya-same-day" in base:
        return "Varanasi to Ayodhya tour package, Ram Mandir VIP darshan, Ayodhya same day cab, Purvanchal Expressway tour, Saryu Aarti"
    elif "prayagraj-varanasi" in base or "ayodhya-prayagraj" in base:
        return "Kashi Prayagraj Ayodhya tour package, 3-Dham UP yatra, Triveni Sangam snan, Ram Mandir VIP pass, Kashi Vishwanath darshan"
    elif "prayagraj-tour-package" in base:
        return "Prayagraj tour package, Triveni Sangam holy dip, Lete Hanuman darshan, Sangam boat booking, Anand Bhawan tour"
    elif "mathura" in base or "vrindavan" in base:
        return "Mathura Vrindavan tour package, Bankey Bihari VIP darshan, Shri Krishna Janmabhoomi, Prem Mandir light show"
    elif "chitrakoot" in base:
        return "Chitrakoot tour package, Ram Ghat Mandakini Aarti, Kamadgiri Parikrama, Hanuman Dhara, Gupt Godavari"
    elif "vindhyachal" in base:
        return "Vindhyachal tour package, Maa Vindhyavasini VIP darshan, Trikon Parikrama, Kali Khoh, Ashtabhuja Devi"
    elif "naimisharanya" in base:
        return "Naimisharanya tour package, Chakra Tirth holy dip, Vyas Gaddi, Lalita Devi Shaktipeeth, 88000 Rishi Tapasthali"
    elif "services" in base:
        return "Kashi tour package prices, Varanasi car rental rates, VIP darshan assistance, Ganga boat booking, hotel stays"
    elif "destinations" in base:
        return "Varanasi spiritual destinations, Kashi temples, Ayodhya Ram Mandir, Prayagraj Sangam, UP pilgrimage cities"
    elif "about" in base or "contact" in base:
        return "Kashi Dharshan tour operator, Varanasi travel agency, Kashi yatra booking contact, authentic pilgrimage tour guide"
    elif filename.startswith("blog-"):
        # Generate clean keywords from title or slug
        title_match = re.search(r'<title>(.*?)</title>', content, re.I)
        if title_match:
            raw_title = title_match.group(1).split('|')[0].split('—')[0].split(':')[0].strip()
            return f"{raw_title}, Varanasi yatra guide, Kashi pilgrimage tips, UP tour guide"
        clean_slug = base.replace("blog-", "").replace("-", " ")
        return f"{clean_slug}, Kashi yatra guide, Varanasi travel tips"
    else:
        return "Kashi Dharshan, Varanasi tour package, Kashi Vishwanath darshan, spiritual yatra Uttar Pradesh"

# ----------------------------------------------------------------------
# 4. PROCESS EVERY HTML FILE: CANONICAL, OG:URL, SCHEMAS, LINKS, KEYWORDS
# ----------------------------------------------------------------------
canonical_updates = 0
link_updates = 0
keywords_sanitized = 0

for filename in target_html_files:
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    orig_content = content
    base = filename[:-5]

    # --- A. FIX CANONICAL TAG ---
    if filename == "index.html":
        clean_canonical = "https://www.kashidharshan.com/"
    else:
        clean_canonical = f"https://www.kashidharshan.com/{base}"

    # Replace existing canonical tag
    if re.search(r'<link[^>]*rel=[\"\']canonical[\"\'][^>]*href=[\"\'].*?[\"\']', content, re.I):
        content = re.sub(
            r'<link[^>]*rel=[\"\']canonical[\"\'][^>]*href=[\"\'].*?[\"\'][^>]*>',
            f'<link rel="canonical" href="{clean_canonical}" />',
            content,
            flags=re.I
        )
    else:
        # If not present, inject before </head>
        content = content.replace("</head>", f'<link rel="canonical" href="{clean_canonical}" />\n</head>')

    # --- B. FIX OG:URL TAG ---
    if re.search(r'<meta[^>]*property=[\"\']og:url[\"\'][^>]*content=[\"\'].*?[\"\']', content, re.I):
        content = re.sub(
            r'<meta[^>]*property=[\"\']og:url[\"\'][^>]*content=[\"\'].*?[\"\'][^>]*>',
            f'<meta property="og:url" content="{clean_canonical}">',
            content,
            flags=re.I
        )

    # --- C. FIX OG:SITE_NAME ---
    content = re.sub(
        r'<meta[^>]*property=[\"\']og:site_name[\"\'][^>]*content=[\"\'].*?[\"\'][^>]*>',
        '<meta property="og:site_name" content="Kashi Dharshan">',
        content,
        flags=re.I
    )

    # --- D. FIX SCHEMA URLS IN JSON-LD ---
    # Replace https://www.kashidharshan.com/index.html -> https://www.kashidharshan.com/
    content = content.replace("https://www.kashidharshan.com/index.html", "https://www.kashidharshan.com/")
    # Replace https://www.kashidharshan.com/<slug>.html -> https://www.kashidharshan.com/<slug>
    content = re.sub(r'https://www\.kashidharshan\.com/([a-zA-Z0-9_\-]+)\.html', r'https://www.kashidharshan.com/\1', content)

    # --- E. SANITIZE META KEYWORDS (TASK 5) ---
    clean_kws = get_clean_keywords(filename, content)
    if re.search(r'<meta[^>]*name=[\"\']keywords[\"\'][^>]*content=[\"\'].*?[\"\']', content, re.I):
        content = re.sub(
            r'<meta[^>]*name=[\"\']keywords[\"\'][^>]*content=[\"\'].*?[\"\'][^>]*>',
            f'<meta name="keywords" content="{clean_kws}">',
            content,
            flags=re.I
        )
        keywords_sanitized += 1
    else:
        content = content.replace("</head>", f'<meta name="keywords" content="{clean_kws}">\n</head>')
        keywords_sanitized += 1

    # --- F. FIX INTERNAL ANCHOR LINKS (TASK 1) ---
    # 1. href="index.html" or href="./index.html" or href="/index.html" -> href="/"
    content = re.sub(r'href=[\"\'](?:\./|/)?index\.html(#.*?)?[\"\']', r'href="/\1"', content)
    # Fix if href="/#" or href="/"
    content = content.replace('href="/""', 'href="/"').replace('href="/#"', 'href="/#')
    
    # 2. Convert all local page links: href="foo.html" -> href="foo"
    # Match href="foo.html" or href="./foo.html" or href="/foo.html" (with optional #anchor)
    def clean_href(match):
        prefix = match.group(1) # e.g. href=" or href='
        path = match.group(2)   # e.g. services, about, blog-something
        anchor = match.group(3) or "" # e.g. #timeline or empty
        quote = match.group(4)
        
        # Don't touch external or assets
        if path.startswith("http://") or path.startswith("https://") or path.startswith("//"):
            return match.group(0)
        
        # Strip leading ./
        if path.startswith("./"):
            path = path[2:]
        
        return f'{prefix}{path}{anchor}{quote}'

    # Pattern matching href="something.html"
    content = re.sub(
        r'(href=[\"\'])(?!https?://|//)([a-zA-Z0-9_\-]+)\.html(#[-a-zA-Z0-9_]+)?([\"\'])',
        clean_href,
        content
    )
    
    # 3. Fix form actions and window.location
    content = content.replace('action="thankyou.html"', 'action="thankyou"')
    content = content.replace("window.location.href = 'thankyou.html'", "window.location.href = 'thankyou'")
    content = content.replace('window.location.href = "thankyou.html"', 'window.location.href = "thankyou"')

    # Write file if modified
    if content != orig_content:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        canonical_updates += 1

print(f"Cleaned canonicals, og:url, schemas, and internal links across {canonical_updates} HTML files!")
print(f"Sanitized meta keywords across {keywords_sanitized} HTML files!")

# ----------------------------------------------------------------------
# 5. OVERHAUL SITEMAP.XML TO 100% CLEAN 200 OK ENDPOINTS (TASK 2)
# ----------------------------------------------------------------------
print("\n--- Overhauling sitemap.xml to 100% clean extension-less endpoints ---")

# Core money pages get 0.9 priority & daily changefreq
core_money_pages = {
    "kashi-vishwanath-tour-package",
    "varanasi-tour-package",
    "kashi-vishwanath-sugam-darshan-vip-pass",
    "varanasi-ganga-aarti-boat-booking-cost",
    "mangla-aarti-kashi-vishwanath-booking-guide",
    "varanasi-airport-to-kashi-vishwanath-taxi-fare",
    "ayodhya-tour-package",
    "ayodhya-prayagraj-varanasi-tour-package",
    "prayagraj-tour-package",
    "mathura-tour-package",
    "vrindavan-tour-package",
    "chitrakoot-tour-package",
    "vindhyachal-tour-package",
    "naimisharanya-tour-package",
    "varanasi-same-day-tour-package",
    "full-ramayana-circuit-tour-package"
}

sitemap_entries = []

# Add Homepage first (priority 1.0)
sitemap_entries.append("""  <url>
    <loc>https://www.kashidharshan.com/</loc>
    <lastmod>2026-10-14</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>""")

# Add all other pages
for filename in target_html_files:
    if filename == "index.html":
        continue
    slug = filename[:-5]
    
    if slug in core_money_pages or "tour-package" in slug:
        priority = "0.9"
        changefreq = "daily"
    elif slug.startswith("blog-") or "guide" in slug:
        priority = "0.8"
        changefreq = "weekly"
    elif slug in ["services", "destinations", "yatra-cost-calculator"]:
        priority = "0.8"
        changefreq = "weekly"
    else:
        priority = "0.7"
        changefreq = "monthly"

    entry = f"""  <url>
    <loc>https://www.kashidharshan.com/{slug}</loc>
    <lastmod>2026-10-14</lastmod>
    <changefreq>{changefreq}</changefreq>
    <priority>{priority}</priority>
  </url>"""
    sitemap_entries.append(entry)

clean_sitemap_xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
""" + "\n".join(sitemap_entries) + "\n</urlset>\n"

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(clean_sitemap_xml)

print(f"Successfully generated clean sitemap.xml with {len(sitemap_entries)} clean URLs (all without .html)!")
print("\nTasks 1, 2, and 5 completed successfully!")
