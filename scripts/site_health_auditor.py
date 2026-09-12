import os
import re
import json
from urllib.parse import urlparse

def audit_html_files(root_dir):
    report = []
    html_files = [f for f in os.listdir(root_dir) if f.endswith('.html') and not f.startswith('google')]
    
    print(f"Scanning {len(html_files)} HTML files for SEO health...")
    
    for file_name in html_files:
        file_path = os.path.join(root_dir, file_name)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        file_issues = []
        
        # 1. Check Title Tag
        title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
        if not title_match:
            file_issues.append("Missing <title> tag")
        elif len(title_match.group(1).strip()) < 10:
            file_issues.append(f"Title too short: '{title_match.group(1)}'")
            
        # 2. Check Meta Description
        desc_match = re.search(r'<meta\s+name="description"\s+content="(.*?)"', content, re.IGNORECASE)
        if not desc_match:
            desc_match = re.search(r'<meta\s+content="(.*?)"\s+name="description"', content, re.IGNORECASE)
        if not desc_match:
            file_issues.append("Missing meta description")
            
        # 3. Check Headings hierarchy
        h1s = re.findall(r'<h1[^>]*>(.*?)</h1>', content, re.IGNORECASE)
        if len(h1s) == 0:
            file_issues.append("Missing <h1> tag")
        elif len(h1s) > 1:
            file_issues.append(f"Multiple <h1> tags detected (found {len(h1s)})")
            
        # 4. Check Images for alt tags
        img_tags = re.findall(r'<img\s+([^>]*?)>', content, re.IGNORECASE)
        for img in img_tags:
            if 'alt=' not in img.lower():
                src_match = re.search(r'src="([^"]*)"', img, re.IGNORECASE)
                src = src_match.group(1) if src_match else "unknown"
                file_issues.append(f"Image missing alt tag: src='{src}'")
                
        # 5. Check Schemas (JSON-LD)
        schemas = re.findall(r'<script\s+type="application/ld\+json">(.*?)</script>', content, re.DOTALL | re.IGNORECASE)
        for schema in schemas:
            try:
                # Remove carriage returns and leading/trailing whitespace
                clean_schema = schema.replace('\r', '').strip()
                json.loads(clean_schema)
            except json.JSONDecodeError as e:
                file_issues.append(f"JSON-LD Schema Syntax Error: {str(e)[:60]}")
                
        # 6. Check Local Links for 404s
        hrefs = re.findall(r'href="([^"]*?\.html)"', content, re.IGNORECASE)
        for href in hrefs:
            parsed = urlparse(href)
            if not parsed.netloc and not parsed.scheme:
                link_path = os.path.join(root_dir, href.split('#')[0])
                if not os.path.exists(link_path):
                    file_issues.append(f"Broken internal link: '{href}'")
                    
        if file_issues:
            report.append((file_name, file_issues))
            
    return report

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    issues = audit_html_files(current_dir)
    if issues:
        print("\nSEO Audit Results (Issues Found):")
        for filename, file_issues in issues:
            print(f"\n📄 {filename}:")
            for issue in file_issues:
                print(f"  ❌ {issue}")
    else:
        print("\n✅ All pages parsed. No SEO health errors found!")
