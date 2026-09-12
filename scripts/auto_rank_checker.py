import os
import urllib.request
import urllib.parse
import re
import csv
from datetime import datetime

KEYWORDS = [
    "Delhi to Ayodhya tour package",
    "Mumbai to Ayodhya tour package",
    "Ahmedabad to Ayodhya tour package",
    "ayodhya to varanasi distance",
    "lucknow to ayodhya same day tour"
]

TARGET_DOMAIN = "ayodhyadharshan.com"

def get_google_rank(keyword, domain):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    query = urllib.parse.quote_plus(keyword)
    # Search top 50 results
    url = f"https://www.google.com/search?q={query}&num=50"
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            html = response.read().decode('utf-8', errors='ignore')
            
        # Parse search results
        # Look for links containing href="/url?q=... or direct links <a href="...
        links = re.findall(r'href=["\']/url\?q=(https?://[^&"\']+)', html)
        if not links:
            links = re.findall(r'<a[^>]+href=["\'](https?://[^"\']+)["\']', html)
            
        rank = -1
        seen_domains = set()
        
        position = 1
        for link in links:
            parsed_url = urllib.parse.urlparse(link)
            netloc = parsed_url.netloc.lower()
            
            # Clean up subdomain prefix (e.g. www.)
            domain_name = netloc.replace("www.", "")
            
            if not domain_name or "google" in domain_name or domain_name in seen_domains:
                continue
                
            seen_domains.add(domain_name)
            
            if domain in domain_name:
                rank = position
                break
                
            position += 1
            if position > 50:
                break
                
        return rank
    except Exception as e:
        print(f"  ⚠️ Error fetching search results for '{keyword}': {str(e)}")
        return -2 # Indicates error/blocked

def check_and_log_rankings(root_dir):
    csv_path = os.path.join(root_dir, 'seo_rank_history.csv')
    date_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    print("Checking keyword ranks on Google...")
    results = []
    
    import time
    import random
    
    for kw in KEYWORDS:
        print(f"  🔍 Checking rank for: '{kw}'...")
        rank = get_google_rank(kw, TARGET_DOMAIN)
        rank_str = "Not in top 50" if rank == -1 else ( "Blocked/Error" if rank == -2 else f"Rank {rank}" )
        print(f"    ➡️ {rank_str}")
        results.append({
            'date': date_str,
            'keyword': kw,
            'rank': rank
        })
        # Add a random delay to prevent Google from blocking requests
        time.sleep(random.uniform(6, 12))
        
    # Write to CSV
    file_exists = os.path.exists(csv_path)
    with open(csv_path, 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['date', 'keyword', 'rank']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        if not file_exists:
            writer.writeheader()
            
        for row in results:
            writer.writerow(row)
            
    print(f"✅ Ranks updated in: {csv_path}")

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    check_and_log_rankings(current_dir)
