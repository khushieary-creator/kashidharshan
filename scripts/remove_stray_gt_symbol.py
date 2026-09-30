#!/usr/bin/env python3
"""
Removes stray '>' symbol (">>" -> ">") from head/meta tags across all 80 HTML pages.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def remove_stray_gt():
    fixed_count = 0
    
    for root, _, files in os.walk(BASE_DIR):
        for f in files:
            if f.endswith(".html") and not f.startswith("google"):
                filepath = os.path.join(root, f)
                with open(filepath, "r", encoding="utf-8") as fh:
                    content = fh.read()
                    
                if '">>' in content:
                    new_content = content.replace('">>', '">')
                    
                    if new_content != content:
                        with open(filepath, "w", encoding="utf-8") as fh:
                            fh.write(new_content)
                        fixed_count += 1
                        
    print(f"🎉 Successfully removed stray '>' symbol from {fixed_count} HTML pages!")

if __name__ == "__main__":
    remove_stray_gt()
