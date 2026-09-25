import glob
import re

blog_target_packages = {
    # Varanasi
    "blog-varanasi-local-sightseeing-tour-package.html": ("varanasi-tour-package.html", "📋 Book Varanasi Sightseeing Package"),
    "blog-varanasi-same-day-tour-package.html": ("varanasi-tour-package.html", "📋 Book Varanasi Same Day Package"),
    "blog-varanasi-kashi-vishwanath-vip-darshan-guide.html": ("varanasi-tour-package.html", "📋 Book Kashi Vishwanath VIP Package"),
    "blog-varanasi-dev-deepawali-boat-booking-guide.html": ("varanasi-tour-package.html", "📋 Book Dev Deepawali Boat Package"),
    "blog-varanasi-dev-deepawali-guide.html": ("varanasi-tour-package.html", "📋 Enquire for Dev Deepawali Package"),
    "blog-varanasi-ganga-aarti-vip-boat-booking.html": ("varanasi-tour-package.html", "📋 Book Ganga Aarti VIP Boat Package"),
    "blog-varanasi-ganga-cruise-booking-guide.html": ("varanasi-tour-package.html", "📋 Book Varanasi Cruise Package"),
    "blog-kashi-vishwanath-corridor-tourist-guide.html": ("varanasi-tour-package.html", "📋 Book Kashi Vishwanath Corridor Package"),
    "blog-kashi-vishwanath-sawan-vip-darshan-guide.html": ("varanasi-tour-package.html", "📋 Book Sawan Kashi Vishwanath Package"),
    "blog-kashi-vishwanath-vip-darshan-booking-guide.html": ("varanasi-tour-package.html", "📋 Book VIP Sugam Darshan Package"),
    "blog-kashi-vishwanath-vip-pass-booking-online.html": ("varanasi-tour-package.html", "📋 Book Kashi VIP Pass Package"),
    "blog-varanasi-to-gaya-pind-daan-tour-guide.html": ("varanasi-tour-package.html", "📋 Book Varanasi Gaya Pind Daan Package"),

    # Ayodhya
    "blog-ayodhya-dharshan-tour-package.html": ("ayodhya-dharshan-tour-package.html", "📋 Book Ayodhya Dharshan Package"),
    "blog-ayodhya-diwali-yatra-guide.html": ("ayodhya-dharshan-tour-package.html", "📋 Book Ayodhya Deepotsav Package"),
    "blog-ayodhya-food-guide-sattvic-cuisine.html": ("ayodhya-dharshan-tour-package.html", "📋 Book Ayodhya Food & Temple Tour"),
    "blog-ayodhya-same-day-tour-itinerary.html": ("ayodhya-dharshan-tour-package.html", "📋 Book Ayodhya Same Day Tour Package"),
    "blog-ayodhya-tour-cost-budget-planner.html": ("ayodhya-dharshan-tour-package.html", "📋 Book Ayodhya Budget Yatra Package"),
    "blog-ayodhya-tour-package-from-delhi-cost.html": ("ayodhya-dharshan-tour-package.html", "📋 Book Delhi to Ayodhya Tour Package"),
    "blog-best-time-to-visit-ayodhya.html": ("ayodhya-dharshan-tour-package.html", "📋 Book Ayodhya Yatra Package"),
    "blog-ram-mandir-vip-pass-booking-guide.html": ("ayodhya-dharshan-tour-package.html", "📋 Book Ram Mandir VIP Darshan Package"),
    "blog-vip-darshan-ayodhya-ram-mandir.html": ("ayodhya-dharshan-tour-package.html", "📋 Book Ram Mandir VIP Pass Package"),
    "blog-lucknow-to-ayodhya-travel-guide-taxi.html": ("ayodhya-dharshan-tour-package.html", "📋 Book Lucknow to Ayodhya Cab Package"),

    # Prayagraj
    "blog-prayagraj-sangam-tour-guide.html": ("prayagraj-tour-package.html", "📋 Book Prayagraj Sangam Package"),
    "blog-ayodhya-to-prayagraj-distance-travel-guide.html": ("prayagraj-tour-package.html", "📋 Book Ayodhya Prayagraj Tour Package"),

    # Vindhyachal
    "blog-vindhyachal-trikon-parikrama-guide.html": ("vindhyachal-tour-package.html", "📋 Book Vindhyachal Trikon Parikrama Package"),

    # Chitrakoot
    "blog-chitrakoot-ram-vanvas-tour-guide.html": ("chitrakoot-tour-package.html", "📋 Book Chitrakoot Ram Vanvas Package"),

    # Naimisharanya
    "blog-naimisharanya-chakra-tirth-guide.html": ("naimisharanya-tour-package.html", "📋 Book Naimisharanya Chakra Tirth Package"),

    # Mathura / Vrindavan
    "blog-mathura-vrindavan-vip-darshan-guide.html": ("mathura-tour-package.html", "📋 Book Mathura Vrindavan Tour Package"),

    # Multi-city
    "blog-ayodhya-kashi-vip-darshan-complete-guide.html": ("ayodhya-prayagraj-varanasi-tour-package.html", "📋 Book Kashi Ayodhya Combo Package"),
    "blog-ayodhya-prayagraj-tour-package.html": ("ayodhya-prayagraj-tour-package.html", "📋 Book Ayodhya Prayagraj Tour Package"),
    "blog-ayodhya-prayagraj-varanasi-tour-package.html": ("ayodhya-prayagraj-varanasi-tour-package.html", "📋 Book 3-City Sacred Circuit Package"),
    "blog-ayodhya-to-varanasi-distance-travel-guide.html": ("ayodhya-varanasi-tour-package.html", "📋 Book Ayodhya to Varanasi Cab Package"),
    "blog-ayodhya-to-varanasi-taxi-fare-cab-booking.html": ("ayodhya-varanasi-tour-package.html", "📋 Book Ayodhya Varanasi Taxi Package"),
    "blog-ayodhya-to-varanasi-vande-bharat-train-guide.html": ("ayodhya-varanasi-tour-package.html", "📋 Book Ayodhya Varanasi Yatra Package"),
    "blog-ayodhya-varanasi-ganga-aarti-guide.html": ("ayodhya-varanasi-tour-package.html", "📋 Book Ayodhya Varanasi Aarti Package"),
    "blog-ayodhya-varanasi-tour-package.html": ("ayodhya-varanasi-tour-package.html", "📋 Book Ayodhya Varanasi Tour Package"),
    "blog-sawan-yatra-vip-darshan-guide.html": ("varanasi-tour-package.html", "📋 Book Sawan Yatra VIP Package")
}

updated_files = 0
updated_links = 0

for blog_file, (target_pkg, btn_label) in blog_target_packages.items():
    try:
        with open(blog_file, "r", encoding="utf-8") as f:
            content = f.read()

        # Replace buttons/links pointing to contact.html in CTA blocks or body text
        # Pattern 1: <a href="contact.html" ...>...Book...</a> or similar
        # We replace href="contact.html" with href="{target_pkg}" when it is an enquiry/booking CTA button
        new_content = content
        
        # 1. High Conversion CTA Box link: href="contact.html" -> href="target_pkg"
        # Search for: <a href="contact.html" class="btn"...>📋 Book Online Enquiry</a>
        new_content = re.sub(
            r'<a\s+href=["\']contact\.html["\'](\s+class=["\']btn["\'][^>]*)>📋 Book Online Enquiry</a>',
            f'<a href="{target_pkg}"\\1>{btn_label}</a>',
            new_content
        )

        # 2. Any CTA button in blog body linking to contact.html
        new_content = re.sub(
            r'<a\s+href=["\']contact\.html["\'](\s+class=["\']btn[^"\']*["\'][^>]*)>(.*?)</a>',
            f'<a href="{target_pkg}"\\1>\\2</a>',
            new_content
        )

        if new_content != content:
            with open(blog_file, "w", encoding="utf-8") as f:
                f.write(new_content)
            updated_files += 1
            print(f"Updated {blog_file} -> CTA points to {target_pkg}")
    except Exception as e:
        print(f"Error processing {blog_file}: {e}")

print(f"\nTotal blog files updated: {updated_files}")
