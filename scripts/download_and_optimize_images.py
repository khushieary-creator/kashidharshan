import os
import urllib.request
import urllib.parse
from PIL import Image

# Directory setup
DEST_DIR = "/Users/rishabhjaiswal/ayodhya-darshan/assets/destinations"
os.makedirs(DEST_DIR, exist_ok=True)

# Images to download, convert to webp, and resize to max-width 800px
images_map = {
    "ram-mandir.webp": "https://commons.wikimedia.org/wiki/Special:FilePath/Ram_Mandir%2C_Ayodhya.png",
    "ganga-aarti.webp": "https://commons.wikimedia.org/wiki/Special:FilePath/Evening_Ganga_Aarti_at_Dashashwamedh_Ghat.JPG",
    "triveni-sangam.webp": "https://commons.wikimedia.org/wiki/Special:FilePath/Triveni_Sangam.JPG",
    "mandakini-river.webp": "https://commons.wikimedia.org/wiki/Special:FilePath/Mandakini_River.jpg",
    "kashi-temple.webp": "https://commons.wikimedia.org/wiki/Special:FilePath/Kashi_Vishwanath_temple.jpg",
    "prem-mandir.webp": "https://commons.wikimedia.org/wiki/Special:FilePath/Prem_Mandir%2C_Vrindavan.jpg",
    "vishram-ghat.webp": "https://commons.wikimedia.org/wiki/Special:FilePath/Vishram_Ghat.jpg"
}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

import time
import random

for filename, url in images_map.items():
    dest_path = os.path.join(DEST_DIR, filename)
    if os.path.exists(dest_path):
        print(f"File {filename} already exists, skipping...")
        continue
        
    temp_path = dest_path + ".tmp"
    
    # Retry loop
    for attempt in range(5):
        print(f"Downloading {url} (Attempt {attempt+1}/5) ...")
        try:
            req = urllib.request.Request(
                url, 
                headers={
                    'User-Agent': 'AyodhyaDharshanBot/1.0 (https://www.ayodhyadharshan.com/; yatra@ayodhyadharshan.com) Pillow/9.0',
                    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8'
                }
            )
            with urllib.request.urlopen(req) as response:
                with open(temp_path, 'wb') as out_file:
                    out_file.write(response.read())
            
            # Optimize using Pillow
            with Image.open(temp_path) as img:
                img = img.convert('RGB')
                max_width = 800
                if img.width > max_width:
                    height = int((max_width / img.width) * img.height)
                    img = img.resize((max_width, height), Image.Resampling.LANCZOS)
                    print(f"Resized {filename} to {max_width}x{height}")
                img.save(dest_path, "WEBP", quality=82, method=6)
                print(f"Saved optimized webp to {dest_path} (size: {os.path.getsize(dest_path)} bytes)")
            
            if os.path.exists(temp_path):
                os.remove(temp_path)
            break # Success, break attempt loop
            
        except urllib.error.HTTPError as e:
            if e.code == 429:
                sleep_time = (5 * (attempt + 1)) + random.random() * 5
                print(f"Rate limited (429). Sleeping for {sleep_time:.2f}s...")
                time.sleep(sleep_time)
            else:
                print(f"HTTP Error {e.code}: {e.reason}")
                break
        except Exception as e:
            print(f"Error processing {filename}: {e}")
            break
            
    # Sleep between images to avoid triggering rate limit
    time.sleep(5 + random.random() * 3)

print("Image optimization complete.")
