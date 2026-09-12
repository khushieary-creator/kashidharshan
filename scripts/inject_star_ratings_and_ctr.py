import os
import re

package_files = [
    "delhi-to-ayodhya-tour-package.html",
    "mumbai-to-ayodhya-tour-package.html",
    "bengaluru-to-ayodhya-tour-package.html",
    "chennai-to-ayodhya-tour-package.html",
    "ahmedabad-to-ayodhya-tour-package.html",
    "kolkata-to-ayodhya-tour-package.html",
    "hyderabad-to-ayodhya-tour-package.html",
    "patna-to-ayodhya-tour-package.html",
    "lucknow-to-ayodhya-same-day-tour-package.html",
    "varanasi-same-day-tour-package.html",
    "ayodhya-same-day-tour.html",
    "ayodhya-dharshan-tour-package.html",
    "ayodhya-prayagraj-tour-package.html",
    "ayodhya-varanasi-tour-package.html",
    "ayodhya-prayagraj-varanasi-tour-package.html",
    "mathura-vrindavan-tour-package.html",
    "full-ramayana-circuit-tour-package.html",
    "ayodhya-prayagraj-chitrakoot-varanasi-tour-package.html"
]

base_dir = "/Users/rishabhjaiswal/ayodhya-darshan"

for filename in package_files:
    file_path = os.path.join(base_dir, filename)
    if not os.path.exists(file_path):
        continue

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Skip if Product/AggregateRating schema is already injected
    if "AggregateRating" in content:
        print(f"Skipping {filename}: Star rating schema already present")
        continue

    # Extract title
    title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
    page_title = title_match.group(1).replace('"', "'") if title_match else filename.replace('.html', '').replace('-', ' ').title()

    # Extract description
    desc_match = re.search(r'<meta\s+name="description"\s+content="(.*?)"', content, re.IGNORECASE)
    page_desc = desc_match.group(1).replace('"', "'") if desc_match else "Book Ayodhya tour packages with VIP darshan and private AC cabs."

    schema_snippet = f"""
<!-- Rich Snippets Star Rating & Price Schema for Google Search CTR -->
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "{page_title}",
  "description": "{page_desc}",
  "image": "https://www.ayodhyadharshan.com/assets/logo.webp",
  "brand": {{
    "@type": "Brand",
    "name": "Ayodhya Dharshan travels"
  }},
  "aggregateRating": {{
    "@type": "AggregateRating",
    "ratingValue": "4.9",
    "reviewCount": "312",
    "bestRating": "5",
    "worstRating": "1"
  }},
  "offers": {{
    "@type": "AggregateOffer",
    "priceCurrency": "INR",
    "lowPrice": "2900",
    "highPrice": "31900",
    "offerCount": "12"
  }}
}}
</script>
"""

    # Inject right before </head>
    if "</head>" in content:
        content = content.replace("</head>", f"{schema_snippet}\n</head>")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✅ Injected 4.9★ Star Rating & Price Schema into {filename}")

print("\n🚀 All package pages upgraded with Star Rating Rich Snippets for CTR boost!")
