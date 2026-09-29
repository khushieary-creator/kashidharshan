#!/usr/bin/env python3
"""
EMD (Exact Match Domain) Kashi Darshan Booster:
Adds alternateName entity tags for "Kashi Darshan" & "Kashi Dharshan" to Schema JSON-LD
and prioritizes EMD keywords in meta tags on main Kashi/Varanasi pages.
"""

import os
import re

def boost_emd():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    target_files = [
        'index.html',
        'varanasi-tour-package.html',
        'varanasi-guide.html',
        'blog.html',
        'blog-varanasi-kashi-vishwanath-vip-darshan-guide.html'
    ]

    emd_keywords = ["Kashi Darshan", "Kashi Dharshan", "Kashi Vishwanath VIP Darshan", "Kashi Tour Package", "Kashi Yatra Package"]

    for fname in target_files:
        fpath = os.path.join(root_dir, fname)
        if not os.path.exists(fpath):
            continue

        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. Add alternateName to WebSite / TravelAgency Schema if missing
        if '"alternateName"' not in content:
            alt_names_str = '"alternateName": ["Kashi Darshan", "Kashi Dharshan", "Kashi Vishwanath VIP Darshan", "Kashi Tour Package"],'
            content = content.replace(
                '"name": "Kashi Dharshan",',
                f'"name": "Kashi Dharshan",\n      {alt_names_str}',
                1
            )
            print(f"Added alternateName schema to {fname}")

        # 2. Prioritize EMD keywords at beginning of meta keywords
        meta_match = re.search(r'<meta\s+name="keywords"\s+content="([^"]*)"', content, re.IGNORECASE)
        if meta_match:
            existing_kw_list = [k.strip() for k in meta_match.group(1).split(',') if k.strip()]
            new_kw_list = list(emd_keywords)
            seen = {k.lower() for k in emd_keywords}
            for k in existing_kw_list:
                if k.lower() not in seen:
                    seen.add(k.lower())
                    new_kw_list.append(k)

            new_meta_str = ', '.join(new_kw_list)
            content = re.sub(
                r'<meta\s+name="keywords"\s+content="[^"]*"',
                f'<meta name="keywords" content="{new_meta_str}"',
                content,
                flags=re.IGNORECASE
            )
            print(f"Prioritized EMD keywords in meta tag on {fname}")

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)

if __name__ == '__main__':
    boost_emd()
