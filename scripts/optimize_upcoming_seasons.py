import os
import re

base_dir = "/Users/rishabhjaiswal/ayodhya-darshan"

# 1. Update Dev Deepawali Meta Tags & Callout
dev_file = os.path.join(base_dir, "blog-varanasi-dev-deepawali-guide.html")
if os.path.exists(dev_file):
    with open(dev_file, "r", encoding="utf-8") as f:
        dev_content = f.read()

    dev_content = dev_content.replace(
        '<meta name="keywords" content="Dev Deepawali Varanasi package, Dev Deepawali boat booking, Varanasi Dev Deepawali timings, Kartik Poornima Kashi yatra, Kashi ghat lighting">',
        '<meta name="keywords" content="Dev Deepawali 2026 boat booking, Dev Deepawali Varanasi package, Varanasi Dev Deepawali cruise price, Kartik Poornima Kashi yatra, Kashi 84 ghat lighting online booking, Dev Deepawali bajra booking">'
    )
    with open(dev_file, "w", encoding="utf-8") as f:
        f.write(dev_content)
    print("✅ Optimized blog-varanasi-dev-deepawali-guide.html for 2026 early-bird queries")

# 2. Update Ayodhya Deepotsav & Diwali Guide Meta Tags
diwali_file = os.path.join(base_dir, "blog-ayodhya-diwali-yatra-guide.html")
if os.path.exists(diwali_file):
    with open(diwali_file, "r", encoding="utf-8") as f:
        diwali_content = f.read()

    diwali_content = diwali_content.replace(
        '<meta name="keywords" content="Ayodhya Diwali tour package, Deepotsav Ayodhya booking, Ram Mandir Diwali yatra, Ayodhya Saryu Aarti Diwali, Diwali in Ayodhya 2026">',
        '<meta name="keywords" content="Ayodhya Deepotsav 2026 booking, Ayodhya Diwali Ram Mandir VIP pass, Ayodhya Diwali tour package, Ayodhya Saryu Aarti Diwali, Saryu ghat 25 lakh diya lighting, Ayodhya Diwali hotel booking">'
    )
    with open(diwali_file, "w", encoding="utf-8") as f:
        f.write(diwali_content)
    print("✅ Optimized blog-ayodhya-diwali-yatra-guide.html for Deepotsav 2026 queries")

# 3. Update Pind Daan Guide Meta Tags
pind_file = os.path.join(base_dir, "blog-varanasi-to-gaya-pind-daan-tour-guide.html")
if os.path.exists(pind_file):
    with open(pind_file, "r", encoding="utf-8") as f:
        pind_content = f.read()

    pind_content = pind_content.replace(
        '<meta name="keywords" content="varanasi to gaya tour package, kashi prayag gaya pind daan price, varanasi to gaya distance, vishnupad temple gaya pind daan cost, gaya pind daan tour package, varanasi to gaya taxi fare">',
        '<meta name="keywords" content="Pitru Paksha 2026 Gaya Pind Daan price, Kashi Prayag Gaya Shradh package, varanasi to gaya tour package, vishnupad temple gaya pind daan cost, gaya pind daan tour package, varanasi to gaya taxi fare">'
    )
    with open(pind_file, "w", encoding="utf-8") as f:
        f.write(pind_content)
    print("✅ Optimized blog-varanasi-to-gaya-pind-daan-tour-guide.html for Pitru Paksha queries")

print("\n🚀 Seasonal Peak Optimizations Completed!")
