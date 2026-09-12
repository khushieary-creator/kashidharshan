import os
import re

targets = {
    "bengaluru-to-ayodhya-tour-package.html": {
        "keywords": [
            "ayodhya package from bangalore by train",
            "ayodhya flight package from bangalore",
            "bangalore to ayodhya package",
            "ayodhya trip package from bangalore",
            "ayodhya tour packages from bangalore by train"
        ],
        "injections": [
            (
                '<p class="lead">Book a direct pilgrimage tour from Bengaluru to Ayodhya. Includes direct flights support, comfortable hotel accommodations, private AC cab, and VIP entry passes at Ram Mandir.</p>',
                '<p class="lead">Book the best <strong>bangalore to ayodhya tour package</strong> with direct flight assistance or <strong>ayodhya package from bangalore by train</strong>. Our all-inclusive <strong>ayodhya trip package from bangalore</strong> includes comfortable hotels, private AC cabs, local sightseeing, and VIP darshan passes at the Ram Janmabhoomi temple.</p>'
            )
        ]
    },
    "chennai-to-ayodhya-tour-package.html": {
        "keywords": [
            "ayodhya tour packages from chennai",
            "ayodhya package from chennai",
            "ayodhya trip from chennai",
            "chennai to ayodhya package"
        ],
        "injections": [
            (
                '<p class="lead">Book a direct pilgrimage tour from Chennai to Ayodhya. Includes direct flights support, comfortable hotel accommodations, private AC cab, and VIP entry passes at Ram Mandir.</p>',
                '<p class="lead">Book the best <strong>chennai to ayodhya tour package</strong> with direct flight booking assistance. Our customized <strong>ayodhya tour packages from chennai</strong> and family-friendly <strong>ayodhya trip from chennai</strong> include comfortable hotel stays, private AC cabs for sightseeing, and VIP darshan passes for the Ram Mandir.</p>'
            )
        ]
    },
    "blog-ram-mandir-vip-pass-booking-guide.html": {
        "keywords": [
            "ayodhya ram mandir ticket online booking",
            "ramlala vip darshan",
            "sugam darshan ayodhya",
            "ayodhya ram mandir mangla aarti booking",
            "online booking of ram mandir darshan"
        ],
        "injections": [
            (
                '<p>Ever since the historic consecration (Pran Pratishtha) of Ram Lalla, the Shri Ram Janmabhoomi Mandir in Ayodhya has been receiving millions of pilgrims weekly. Standing in the general public queues can take anywhere between 1.5 to 3 hours, depending on the season and time of day. To experience a comfortable yatra, securing a <strong>Ram Mandir VIP Pass (Sugam Darshan)</strong> is the smartest decision. This guide outlines everything you need to know about official slot bookings, timings, and priority queue coordination.</p>',
                '<p>Ever since the historic consecration of Ram Lalla, the Shri Ram Janmabhoomi Mandir in Ayodhya has been receiving millions of pilgrims. Standing in general public queues can take hours. To experience a comfortable yatra, securing a <strong>Ram Mandir VIP Pass</strong> for <strong>sugam darshan ayodhya</strong> is the smartest decision. If you are planning an <strong>ayodhya ram mandir ticket online booking</strong> or looking for <strong>ayodhya ram mandir mangla aarti booking</strong> slots, read this guide to learn how to schedule your <strong>ramlala vip darshan</strong> and complete the <strong>online booking of ram mandir darshan</strong> safely.</p>'
            )
        ]
    },
    "ayodhya-dharshan-tour-package.html": {
        "keywords": [
            "ayodhya chhapaiya tour package"
        ],
        "injections": [
            (
                '<p class="lead">An unhurried, spiritual yatra exploring the ancient temples and ghats of Lord Ram\'s holy birthplace. VIP darshan assistance, comfortable accommodation close to temples, and private local travel included.</p>',
                '<p class="lead">An unhurried, spiritual yatra exploring the ancient temples of Lord Ram\'s holy birthplace. Ask for our specialized <strong>ayodhya chhapaiya tour package</strong> for Swaminarayan temple visits. VIP darshan assistance, comfortable accommodations close to temples, and private local travel are fully included.</p>'
            )
        ]
    },
    "index.html": {
        "keywords": [
            "ayodhya tour packages for couple",
            "ayodhya local sightseeing tour package",
            "best travel agency in ayodhya"
        ],
        "injections": [
            (
                '<p class="lead">From Shri Ram\'s Ayodhya to the eternal ghats of Kashi — we craft soulful, fully-managed pilgrimages across the holiest cities of Uttar Pradesh. You walk the path; we carry every detail.</p>',
                '<p class="lead">From Shri Ram\'s Ayodhya to the eternal ghats of Kashi — as the <strong>best travel agency in ayodhya</strong>, we offer custom <strong>ayodhya tour packages for couple</strong>, <strong>ayodhya local sightseeing tour package</strong>, and fully-managed pilgrimages across the holiest cities of Uttar Pradesh.</p>'
            )
        ]
    }
}

base_dir = "/Users/rishabhjaiswal/ayodhya-darshan"

for filename, data in targets.items():
    file_path = os.path.join(base_dir, filename)
    if not os.path.exists(file_path):
        print(f"Skipping {filename}: File not found")
        continue

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Meta Keywords Replacement / Appending
    meta_pattern = re.compile(r'<meta\s+name="keywords"\s+content="([^"]*)"', re.IGNORECASE)
    match = meta_pattern.search(content)
    if match:
        existing_kws = match.group(1)
        # Avoid duplicate keywords
        added = [kw for kw in data["keywords"] if kw.lower() not in existing_kws.lower()]
        if added:
            new_kws = existing_kws + ", " + ", ".join(added)
            content = meta_pattern.sub(f'<meta name="keywords" content="{new_kws}"', content)
            print(f"✅ Appended meta keywords for {filename}")
    else:
        print(f"⚠️ Meta keywords tag not found in {filename}")

    # Text Injections
    for target_str, replacement_str in data["injections"]:
        if target_str in content:
            content = content.replace(target_str, replacement_str)
            print(f"✅ Injected keyword content into {filename}")
        else:
            print(f"⚠️ Target text block not found in {filename}")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print("\n🚀 All search term keyword injections completed!")
