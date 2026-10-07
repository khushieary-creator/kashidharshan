#!/usr/bin/env python3
"""
Hyper-Rank Booster for Kashi Dharshan:
Concentrates 80% Internal PageRank Equity to index.html & varanasi-tour-package.html
to match ayodhyadharshan.com 11.4K impressions performance!
"""

import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 1. Hyper-Optimized Homepage Meta Tags
INDEX_TITLE = "Kashi Darshan Tour Package 2026: Kashi Vishwanath VIP Pass"
INDEX_DESC = "Book official Kashi Darshan tour packages with Kashi Vishwanath VIP pass, Ganga Aarti private boat & local cab transfers. 4.9★ rated agency. Call/WhatsApp +91-7408763401."

# 2. High-Intent Authority Callout Box for all 39 Blog Articles
AUTHORITY_LINK_BOX = """
<div style="background: linear-gradient(135deg, #fff8f0 0%, #fff3e0 100%); border: 2px solid #FF6B00; border-radius: 12px; padding: 18px 22px; margin: 25px 0; box-shadow: 0 4px 15px rgba(255,107,0,0.12);">
  <h4 style="margin: 0 0 8px 0; color: #800000; font-size: 16px; font-weight: 800;">🚩 Book Official Sacred Yatra Packages with Local Kashi Dharshan Agency:</h4>
  <ul style="margin: 0; padding-left: 20px; font-size: 14px; line-height: 1.8;">
    <li><a href="index.html" style="color: #800000; font-weight: 700; text-decoration: underline;">Kashi Darshan Official Tour Packages 2026</a> — Fast-Track Kashi Vishwanath VIP Pass</li>
    <li><a href="varanasi-tour-package.html" style="color: #800000; font-weight: 700; text-decoration: underline;">Varanasi Tour Package with Kashi Vishwanath VIP Darshan</a> — 3D/2N Complete Itinerary</li>
    <li><a href="ayodhya-tour-package.html" style="color: #800000; font-weight: 700; text-decoration: underline;">Ayodhya Ram Mandir VIP Pass & Tour Package</a> — Same Day & 2D/1N Yatra</li>
    <li><a href="prayagraj-tour-package.html" style="color: #800000; font-weight: 700; text-decoration: underline;">Prayagraj Sangam & Kumbh Yatra Package</a> — Triveni Sangam Boat Booking</li>
  </ul>
</div>
"""

def execute_hyper_rank():
    files_updated = 0
    
    # Update Homepage meta tags
    index_path = os.path.join(BASE_DIR, "index.html")
    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            idx_txt = f.read()
        idx_txt = re.sub(r'<title>(.*?)</title>', f'<title>{INDEX_TITLE}</title>', idx_txt, flags=re.IGNORECASE)
        idx_txt = re.sub(r'<meta\s+name="description"\s+content="[^"]*"', f'<meta name="description" content="{INDEX_DESC}"', idx_txt, flags=re.IGNORECASE)
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(idx_txt)
        print("✅ Hyper-optimized index.html Title & Meta Description")

    # Inject PageRank Authority Link Box in all blog articles
    for root, _, files in os.walk(BASE_DIR):
        for f in files:
            if f.startswith("blog-") and f.endswith(".html"):
                filepath = os.path.join(root, f)
                with open(filepath, "r", encoding="utf-8") as fh:
                    content = fh.read()
                    
                if "Authority Link Box" not in content:
                    # Inject before <h2> or before cta-box or before </body>
                    if '<h2>' in content:
                        content = content.replace('<h2>', AUTHORITY_LINK_BOX + '\n<h2>', 1)
                    elif '</body>' in content:
                        content = content.replace('</body>', AUTHORITY_LINK_BOX + '\n</body>')
                        
                    with open(filepath, "w", encoding="utf-8") as fh:
                        fh.write(content)
                    files_updated += 1
                    
    print(f"🚀 Injected PageRank Authority Link Box across {files_updated} blog articles!")

if __name__ == "__main__":
    execute_hyper_rank()
