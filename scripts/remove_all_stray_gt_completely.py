#!/usr/bin/env python3
"""
Removes all stray '/>>' and '">>' across all 80 HTML files completely.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def cleanup_all():
    fixed = 0
    for root, _, files in os.walk(BASE_DIR):
        for f in files:
            if f.endswith(".html") and not f.startswith("google"):
                filepath = os.path.join(root, f)
                with open(filepath, "r", encoding="utf-8") as fh:
                    content = fh.read()
                    
                new_content = content.replace('/>>', '/>').replace('">>', '">')
                
                if new_content != content:
                    with open(filepath, "w", encoding="utf-8") as fh:
                        fh.write(new_content)
                    fixed += 1
                    
    print(f"🎉 Cleaned up stray '>>' from {fixed} HTML files!")

if __name__ == "__main__":
    cleanup_all()
