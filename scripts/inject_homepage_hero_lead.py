import re

INDEX_PATH = '/Users/rishabhjaiswal/.gemini/antigravity/scratch/kashidharshan/index.html'

with open(INDEX_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

HERO_WIDGET = """<!-- HERO INSTANT TOUR QUOTE & ITINERARY WIDGET -->
<div class="hero-instant-quote container" style="max-width: 1100px; margin: 20px auto 30px; position: relative; z-index: 10;">
  <div style="background: #ffffff; border: 2px solid #b45309; border-radius: 16px; padding: 24px 28px; box-shadow: 0 12px 36px rgba(180, 83, 9, 0.16);">
    <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px; margin-bottom: 16px; border-bottom: 1px solid #fef3c7; padding-bottom: 12px;">
      <div>
        <h2 style="color: #78350f; margin: 0; font-size: 1.35rem; font-family: var(--font-display); display: flex; align-items: center; gap: 8px;">
          🚩 Get Instant Yatra Plan &amp; Lowest Price Quote
        </h2>
        <p style="margin: 4px 0 0; color: #4b5563; font-size: 0.9rem;">
          ⚡ Directly connect with certified Varanasi &amp; Ayodhya Yatra experts. Instant response within 5 minutes on WhatsApp!
        </p>
      </div>
      <div style="display: flex; align-items: center; gap: 6px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; padding: 4px 12px; font-size: 0.82rem; color: #065f46; font-weight: 700;">
        <span style="width: 8px; height: 8px; background: #10b981; border-radius: 50%; display: inline-block;"></span> 24×7 Local Guides Online
      </div>
    </div>

    <form id="heroLeadForm" onsubmit="return submitYatraFormToWhatsApp(event, 'Homepage Hero Instant Quote')" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px; align-items: end;">
      <div>
        <label style="display: block; font-size: 0.82rem; font-weight: 700; color: #374151; margin-bottom: 4px;">Devotee Name *</label>
        <input type="text" name="fullname" placeholder="Your Name" required style="width: 100%; padding: 11px 12px; border: 1.5px solid #d1d5db; border-radius: 8px; font-size: 0.95rem; box-sizing: border-box;">
      </div>
      <div>
        <label style="display: block; font-size: 0.82rem; font-weight: 700; color: #374151; margin-bottom: 4px;">WhatsApp Number *</label>
        <input type="tel" name="mobile" placeholder="10-digit Mobile Number" required style="width: 100%; padding: 11px 12px; border: 1.5px solid #d1d5db; border-radius: 8px; font-size: 0.95rem; box-sizing: border-box;">
      </div>
      <div>
        <label style="display: block; font-size: 0.82rem; font-weight: 700; color: #374151; margin-bottom: 4px;">Select Sacred Destination</label>
        <select name="package" style="width: 100%; padding: 11px 12px; border: 1.5px solid #d1d5db; border-radius: 8px; font-size: 0.95rem; background: #fff; box-sizing: border-box;">
          <option value="Kashi Darshan &amp; Varanasi Tour Package (3D/2N)">Kashi Darshan &amp; Varanasi (3D/2N)</option>
          <option value="1-Day Kashi Darshan Tour Package">1-Day Kashi Same Day Yatra</option>
          <option value="Ayodhya Ram Mandir VIP Darshan Tour">Ayodhya Ram Mandir VIP Yatra</option>
          <option value="Kashi &amp; Ayodhya Combined Tour (4D/3N)">Kashi + Ayodhya Tour (4D/3N)</option>
          <option value="Kashi, Prayagraj &amp; Ayodhya Mahayatra (5D/4N)">Kashi + Prayagraj + Ayodhya (5D/4N)</option>
          <option value="Kashi Vishwanath VIP Sugam Darshan Pass">Kashi Vishwanath VIP Sugam Pass</option>
          <option value="Varanasi Ganga Aarti Private Boat Booking">Ganga Aarti Private Boat Booking</option>
        </select>
      </div>
      <div>
        <label style="display: block; font-size: 0.82rem; font-weight: 700; color: #374151; margin-bottom: 4px;">Travel Date</label>
        <input type="text" name="travel_date" placeholder="e.g. 28 Nov or Dec" style="width: 100%; padding: 11px 12px; border: 1.5px solid #d1d5db; border-radius: 8px; font-size: 0.95rem; box-sizing: border-box;">
      </div>
      <div>
        <button type="submit" style="width: 100%; background: linear-gradient(135deg, #25D366 0%, #128C7E 100%); color: #ffffff; border: none; padding: 12px 14px; border-radius: 8px; font-size: 1rem; font-weight: 800; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 8px; box-shadow: 0 4px 14px rgba(37,211,102,0.35); transition: transform 0.2s;">
          💬 Get Free Quote
        </button>
      </div>
    </form>
    <div style="display: flex; gap: 20px; flex-wrap: wrap; margin-top: 12px; font-size: 0.8rem; color: #6b7280;">
      <span>🔒 100% Privacy</span>
      <span>⏱️ 5-Minute WhatsApp Quote</span>
      <span>⭐ 4.9/5 Rating (12,000+ Yatris)</span>
      <span>🚕 Cabs + Hotels + VIP Darshan</span>
    </div>
  </div>
</div>
"""

# Check if already injected
if 'id="heroLeadForm"' not in content:
    # Insert right before <!-- ===== DESTINATIONS ===== -->
    target = '<!-- ===== DESTINATIONS ===== -->'
    if target in content:
        content = content.replace(target, HERO_WIDGET + '\n\n' + target, 1)
        with open(INDEX_PATH, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully injected Hero Lead Capture form on index.html!")
    else:
        print("Target not found on index.html")
else:
    print("Hero form already present on index.html")
