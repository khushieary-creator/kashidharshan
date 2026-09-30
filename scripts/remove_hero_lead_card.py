#!/usr/bin/env python3
"""
Removes hero-lead-card completely from index.html and any other HTML file.
"""

import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def remove_hero_card():
    removed_count = 0
    
    for root, _, files in os.walk(BASE_DIR):
        for f in files:
            if f.endswith(".html") and not f.startswith("google"):
                filepath = os.path.join(root, f)
                with open(filepath, "r", encoding="utf-8") as fh:
                    content = fh.read()
                    
                if "hero-lead-card" in content:
                    # Match from <!-- HERO LEAD CAPTURE FORM --> or <div class="hero-lead-card"... down to closing div
                    new_content = re.sub(
                        r'<!-- HERO LEAD CAPTURE FORM -->\s*<div class="hero-lead-card".*?</form>\s*</div>',
                        '',
                        content,
                        flags=re.DOTALL
                    )
                    
                    if "hero-lead-card" in new_content:
                        new_content = re.sub(
                            r'<div class="hero-lead-card".*?</form>\s*</div>',
                            '',
                            new_content,
                            flags=re.DOTALL
                        )
                        
                    if new_content != content:
                        with open(filepath, "w", encoding="utf-8") as fh:
                            fh.write(new_content)
                        removed_count += 1
                        
    print(f"✅ Removed hero-lead-card from {removed_count} HTML pages!")

if __name__ == "__main__":
    remove_hero_card()
