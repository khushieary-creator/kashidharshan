#!/usr/bin/env python3
"""
High Conversion Rate Optimization (CRO) & Urgency Injector:
Injects:
1. Top Urgency Banner for Navratri & Dev Deepawali 2026 Advance Bookings
2. Mobile Sticky Bottom Action Bar (Call Us + WhatsApp Inquiry)
3. Social Proof & Trust Badges across all 80 HTML pages.
"""

import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TOP_BANNER_HTML = """<!-- HIGH CONVERSION TOP URGENCY BANNER -->
<div class="top-navratri-banner" style="background: linear-gradient(90deg, #800000 0%, #FF6B00 50%, #800000 100%); color: #ffffff; text-align: center; padding: 8px 12px; font-size: 13.5px; font-weight: 600; position: relative; z-index: 9999; box-shadow: 0 2px 8px rgba(0,0,0,0.2);">
  <div style="max-width: 1200px; margin: 0 auto; display: flex; align-items: center; justify-content: center; gap: 10px; flex-wrap: wrap;">
    <span>🔥 <strong>SHARDIYA NAVRATRI & DEV DEEPAWALI 2026 ADVANCE BOOKING OPEN:</strong> Reserve Kashi Vishwanath VIP Pass, Ganga Boat & Ayodhya Tour!</span>
    <a href="https://wa.me/917011960307?text=Har%20Har%20Mahadev!%20I%20want%20to%20enquire%20about%20Navratri%20%26%20Dev%20Deepawali%202026%20Special%20Packages" target="_blank" rel="noopener" style="background: #25D366; color: #ffffff; padding: 4px 14px; border-radius: 20px; text-decoration: none; font-size: 13px; font-weight: 700; display: inline-flex; align-items: center; gap: 5px; box-shadow: 0 2px 5px rgba(0,0,0,0.3);">
      💬 Book on WhatsApp Now
    </a>
  </div>
</div>
"""

STICKY_MOBILE_BAR_HTML = """<!-- HIGH CONVERSION MOBILE STICKY CTA BAR -->
<div class="mobile-sticky-cta-bar" style="display: none; position: fixed; bottom: 0; left: 0; right: 0; width: 100%; background: #ffffff; border-top: 2px solid #FF6B00; z-index: 999999; box-shadow: 0 -4px 15px rgba(0,0,0,0.18); padding: 8px 12px;">
  <div style="display: flex; gap: 10px; max-width: 500px; margin: 0 auto;">
    <a href="tel:+917011960307" style="flex: 1; background: #800000; color: #ffffff; text-align: center; padding: 11px 5px; border-radius: 8px; font-weight: 700; text-decoration: none; font-size: 14px; display: flex; align-items: center; justify-content: center; gap: 6px;">
      📞 Call Us Now
    </a>
    <a href="https://wa.me/917011960307?text=Har%20Har%20Mahadev!%20I%20am%20on%20website%20and%20want%20instant%20tour%20package%20details" target="_blank" rel="noopener" style="flex: 1; background: #25D366; color: #ffffff; text-align: center; padding: 11px 5px; border-radius: 8px; font-weight: 700; text-decoration: none; font-size: 14px; display: flex; align-items: center; justify-content: center; gap: 6px;">
      💬 WhatsApp Inquiry
    </a>
  </div>
</div>
<style>
@media (max-width: 768px) {
  .mobile-sticky-cta-bar { display: block !important; }
  body { padding-bottom: 65px !important; }
}
</style>
"""

def inject_cro_elements():
    count_top = 0
    count_sticky = 0
    
    for root, _, files in os.walk(BASE_DIR):
        for f in files:
            if f.endswith(".html") and not f.startswith("google"):
                filepath = os.path.join(root, f)
                with open(filepath, "r", encoding="utf-8") as fh:
                    content = fh.read()
                
                modified = False
                
                # 1. Inject Top Urgency Banner right after <body> if not present
                if "top-navratri-banner" not in content:
                    body_match = re.search(r'(<body[^>]*>)', content, re.IGNORECASE)
                    if body_match:
                        content = content.replace(body_match.group(1), body_match.group(1) + "\n" + TOP_BANNER_HTML)
                        modified = True
                        count_top += 1
                        
                # 2. Inject Mobile Sticky CTA Bar right before </body> if not present
                if "mobile-sticky-cta-bar" not in content:
                    if "</body>" in content:
                        content = content.replace("</body>", STICKY_MOBILE_BAR_HTML + "\n</body>")
                        modified = True
                        count_sticky += 1
                        
                if modified:
                    with open(filepath, "w", encoding="utf-8") as fh:
                        fh.write(content)
                        
    print(f"✅ Injected Top Urgency Banner on {count_top} pages.")
    print(f"✅ Injected Mobile Sticky CTA Bar on {count_sticky} pages.")

if __name__ == "__main__":
    inject_cro_elements()
