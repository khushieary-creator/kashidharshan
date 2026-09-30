#!/usr/bin/env python3
"""
Removes top-navratri-banner from all 80 HTML pages cleanly.
"""

import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def remove_banner():
    removed_count = 0
    
    for root, _, files in os.walk(BASE_DIR):
        for f in files:
            if f.endswith(".html") and not f.startswith("google"):
                filepath = os.path.join(root, f)
                with open(filepath, "r", encoding="utf-8") as fh:
                    content = fh.read()
                    
                if "top-navratri-banner" in content:
                    # Remove top-navratri-banner block
                    new_content = re.sub(
                        r'<!-- HIGH CONVERSION TOP URGENCY BANNER -->\s*<div class="top-navratri-banner".*?</div>\s*</div>',
                        '',
                        content,
                        flags=re.DOTALL
                    )
                    
                    if "top-navratri-banner" in new_content:
                        new_content = re.sub(
                            r'<div class="top-navratri-banner".*?</div>\s*</div>',
                            '',
                            new_content,
                            flags=re.DOTALL
                        )
                        
                    if "top-navratri-banner" in new_content:
                        # Fallback regex for unclosed inner div
                        new_content = re.sub(
                            r'<div class="top-navratri-banner"[^>]*>.*?Book on WhatsApp Now\s*</a>\s*</div>\s*</div>',
                            '',
                            new_content,
                            flags=re.DOTALL
                        )
                        
                    if new_content != content:
                        with open(filepath, "w", encoding="utf-8") as fh:
                            fh.write(new_content)
                        removed_count += 1
                        
    print(f"✅ Removed top banner from {removed_count} HTML pages!")

if __name__ == "__main__":
    remove_banner()
