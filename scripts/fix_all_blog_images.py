import os
import re
import glob

ROOT_DIR = '/Users/rishabhjaiswal/.gemini/antigravity/scratch/kashidharshan'

def fix_blog_html():
    fpath = os.path.join(ROOT_DIR, 'blog.html')
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    # 1. Replace broken kashi-temple.jpg with assets/destinations/kashi-temple.webp
    c = c.replace('assets/reviews/kashi-temple.jpg', 'assets/destinations/kashi-temple.webp')
    
    # 2. Replace sarnath.webp with assets/destinations/kashi-temple.webp
    c = c.replace('assets/destinations/sarnath.webp', 'assets/destinations/kashi-temple.webp')

    # 3. Replace all 403 Unsplash URLs with local verified assets
    unsplash_replacements = [
        ('https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?auto=format&fit=crop&w=700&q=80', 'assets/destinations/kashi-temple.webp'),
        ('https://images.unsplash.com/photo-1540555700478-4be289fbecef?auto=format&fit=crop&w=700&q=80', 'assets/destinations/ram-mandir.webp'),
        ('https://images.unsplash.com/photo-1546833999-b9f581a1996d?auto=format&fit=crop&w=700&q=80', 'assets/reviews/ayodhya-family.jpg'),
    ]

    for unsplash_url, local_img in unsplash_replacements:
        c = c.replace(unsplash_url, local_img)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)
    print("blog.html: All broken and external 403 images replaced with local WebP/JPG assets!")

def fix_individual_unsplash_blogs():
    files_to_fix = [
        ('blog-ayodhya-diwali-yatra-guide.html', 'https://images.unsplash.com/photo-1540555700478-4be289fbecef?auto=format&fit=crop&w=1200&q=80', 'assets/reviews/ayodhya-night.jpg'),
        ('blog-ayodhya-food-guide-sattvic-cuisine.html', 'https://images.unsplash.com/photo-1546833999-b9f581a1996d?auto=format&fit=crop&w=1200&q=80', 'assets/reviews/ayodhya-family.jpg'),
        ('blog-ayodhya-to-varanasi-vande-bharat-train-guide.html', 'https://images.unsplash.com/photo-1540555700478-4be289fbecef?auto=format&fit=crop&w=1200&q=80', 'assets/lucknow_ayodhya_highway.webp'),
        ('blog-ayodhya-tour-cost-budget-planner.html', 'https://images.unsplash.com/photo-1540555700478-4be289fbecef?auto=format&fit=crop&w=1200&q=80', 'assets/destinations/ram-mandir.webp'),
    ]

    for fname, old_url, new_img in files_to_fix:
        fpath = os.path.join(ROOT_DIR, fname)
        if not os.path.exists(fpath):
            continue
        with open(fpath, 'r', encoding='utf-8') as f:
            c = f.read()
        if old_url in c:
            c = c.replace(old_url, new_img)
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(c)
            print(f"Fixed Unsplash 403 in {fname} -> {new_img}")

def inject_featured_images_to_empty_blogs():
    # Mapping of files that need featured images
    blog_image_map = {
        # Money pages
        'kashi-vishwanath-sugam-darshan-vip-pass.html': ('assets/destinations/kashi-temple.webp', 'Shri Kashi Vishwanath Dham Sugam Darshan VIP Pass'),
        'varanasi-ganga-aarti-boat-booking-cost.html': ('assets/destinations/ganga-aarti.webp', 'Dashashwamedh Ghat Evening Ganga Aarti Private Boat Booking'),
        'mangla-aarti-kashi-vishwanath-booking-guide.html': ('assets/destinations/kashi-temple.webp', 'Shri Kashi Vishwanath Mangla Aarti Garbhagriha Seva'),
        'varanasi-airport-to-kashi-vishwanath-taxi-fare.html': ('assets/lucknow_ayodhya_highway.webp', 'Varanasi Lal Bahadur Shastri Airport to Kashi Vishwanath AC Cab'),
        
        # Blog pages with 0 images
        'blog-varanasi-kashi-vishwanath-vip-darshan-guide.html': ('assets/destinations/kashi-temple.webp', 'Kashi Vishwanath VIP Sugam Darshan Guide'),
        'blog-varanasi-dev-deepawali-boat-booking-guide.html': ('assets/destinations/ganga-aarti.webp', 'Varanasi Dev Deepawali Ghat Illumination and Boat Booking'),
        'blog-varanasi-dev-deepawali-2026-vip-boat-booking-guide.html': ('assets/destinations/ganga-aarti.webp', 'Varanasi Dev Deepawali 2026 VIP Boat Booking'),
        'blog-varanasi-ganga-aarti-vip-boat-booking.html': ('assets/destinations/ganga-aarti.webp', 'Varanasi Dashashwamedh Ghat Ganga Aarti VIP Boat Booking'),
        'blog-varanasi-local-sightseeing-tour-package.html': ('assets/destinations/kashi-temple.webp', 'Varanasi Local Sightseeing Tour Package and Sarnath Guide'),
        'blog-kashi-vishwanath-corridor-tourist-guide.html': ('assets/destinations/kashi-temple.webp', 'Kashi Vishwanath Corridor Tourist and Darshan Guide'),
        'blog-kashi-vishwanath-mangla-aarti-online-booking-guide-2026.html': ('assets/destinations/kashi-temple.webp', 'Kashi Vishwanath Mangla Aarti Online Booking 2026'),
        'blog-kashi-vishwanath-sparsh-darshan-booking-rules-2026.html': ('assets/destinations/kashi-temple.webp', 'Kashi Vishwanath Sparsh Darshan Booking Rules 2026'),
        'blog-kashi-vishwanath-vip-darshan-booking-guide.html': ('assets/destinations/kashi-temple.webp', 'Kashi Vishwanath VIP Darshan Booking Guide'),
        'blog-kashi-vishwanath-vip-pass-booking-online.html': ('assets/destinations/kashi-temple.webp', 'Kashi Vishwanath VIP Pass Online Booking'),
        'blog-kashi-vishwanath-vip-pass-online-booking-price-guide.html': ('assets/destinations/kashi-temple.webp', 'Kashi Vishwanath VIP Pass Online Booking Price Guide'),
        'blog-prayagraj-sangam-tour-guide.html': ('assets/destinations/triveni-sangam.webp', 'Prayagraj Triveni Sangam Holy Snan and Boat Ride'),
        'blog-chitrakoot-ram-vanvas-tour-guide.html': ('assets/destinations/mandakini-river.webp', 'Chitrakoot Ramghat and Mandakini River Pilgrimage'),
        'blog-naimisharanya-chakra-tirth-guide.html': ('assets/destinations/ram-mandir.webp', 'Naimisharanya Chakra Tirth and Lalita Devi Temple'),
        'blog-vindhyachal-trikon-parikrama-guide.html': ('assets/vindhyachal.webp', 'Vindhyachal Dham Maa Vindhyavasini Trikon Parikrama'),
        'blog-ayodhya-deepotsav-kashi-dev-deepawali-tour-package-2026.html': ('assets/reviews/ayodhya-night.jpg', 'Ayodhya Deepotsav and Kashi Dev Deepawali Festival Package'),
    }

    for fname, (img_src, alt_text) in blog_image_map.items():
        fpath = os.path.join(ROOT_DIR, fname)
        if not os.path.exists(fpath):
            continue
        with open(fpath, 'r', encoding='utf-8') as f:
            c = f.read()

        # Check if already has destination/review img (other than logo)
        imgs = re.findall(r'<img[^>]+src=[\"\']([^\s\"\'>]+)[\"\']', c)
        non_logo = [img for img in imgs if 'logo' not in img]
        if len(non_logo) > 0:
            print(f"Skipping {fname}: already has {len(non_logo)} images ({non_logo[0]})")
            continue

        img_block = f'''
    <div class="featured-image-container" style="margin: 24px 0 32px; border-radius: 14px; overflow: hidden; box-shadow: 0 8px 24px rgba(0,0,0,0.12); border: 1px solid rgba(212,175,55,0.25);">
      <img width="900" height="480" src="{img_src}" alt="{alt_text}" style="width: 100%; height: auto; max-height: 440px; object-fit: cover; display: block;" loading="lazy" decoding="async">
    </div>
'''
        # Strategy 1: In money pages, insert right before or inside <main class="section">
        if '<main class="section">' in c:
            c = c.replace('<main class="section">', '<main class="section">\n' + img_block)
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(c)
            print(f"Injected featured image into money page {fname} -> {img_src}")
            continue

        # Strategy 2: In blog pages with <article ...>, insert right after the subtitle/lead or after <h1>
        # Look for the introductory text box or subtitle
        if '<div style="background:#f9fafb; border-left:4px solid #d97706;' in c:
            c = c.replace('<div style="background:#f9fafb; border-left:4px solid #d97706;', img_block + '\n    <div style="background:#f9fafb; border-left:4px solid #d97706;')
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(c)
            print(f"Injected featured image into article {fname} -> {img_src}")
            continue

        # Strategy 3: Look for <main ...> or </header>
        if '</header>' in c and '<main' in c:
            c = re.sub(r'(</header>\s*<main[^>]*>)', r'\1\n' + img_block, c)
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(c)
            print(f"Injected featured image into header/main {fname} -> {img_src}")
            continue

        # Strategy 4: Look for <h1 ...></h1>
        if '</h1>' in c:
            c = re.sub(r'(</h1>\s*(?:<p[^>]*>.*?</p>)?)', r'\1\n' + img_block, c, count=1)
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(c)
            print(f"Injected featured image after H1 in {fname} -> {img_src}")
            continue

        print(f"Could not find insertion point for {fname}")

def main():
    print("Fixing blog images...")
    fix_blog_html()
    fix_individual_unsplash_blogs()
    inject_featured_images_to_empty_blogs()
    print("All blog image optimizations completed successfully!")

if __name__ == '__main__':
    main()
