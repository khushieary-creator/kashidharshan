import os
from fpdf import FPDF

class BacklinkPDF(FPDF):
    def header(self):
        # Draw a top saffron border bar
        self.set_fill_color(255, 107, 0)
        self.rect(0, 0, 210, 4, 'F')
        
        self.set_font('Helvetica', 'B', 8)
        self.set_text_color(150, 150, 150)
        # Using simple ASCII dash "-"
        self.cell(0, 10, 'AYODHYA DHARSHAN TRAVELS - INTERNAL SEO TEAM DOCUMENT', 0, 0, 'L')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', 0, 0, 'C')

def create_backlink_pdf():
    pdf = BacklinkPDF()
    pdf.alias_nb_pages()
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.add_page()
    
    # ── TITLE PAGE / SECTION ──
    pdf.set_y(25)
    pdf.set_font('Helvetica', 'B', 22)
    pdf.set_text_color(128, 0, 0) # Maroon
    pdf.cell(0, 12, 'Backlink Campaign 2026', 0, 1, 'L')
    
    pdf.set_font('Helvetica', 'B', 14)
    pdf.set_text_color(212, 175, 55) # Saffron/Gold
    pdf.cell(0, 8, 'Step-by-Step Execution Guide & Action Plan', 0, 1, 'L')
    
    pdf.set_y(pdf.get_y() + 5)
    pdf.set_draw_color(200, 200, 200)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.set_y(pdf.get_y() + 8)
    
    # Intro
    pdf.set_font('Helvetica', '', 10.5)
    pdf.set_text_color(40, 40, 40)
    intro_text = (
        "This guide outlines the exact copy-pasteable bio descriptions, directory submission templates, "
        "and anchor text rules to build high-authority backlinks for ayodhyadharshan.com. "
        "Please follow the priorities below in order."
    )
    pdf.multi_cell(0, 6, intro_text)
    pdf.ln(6)
    
    # Important Note Box
    pdf.set_fill_color(254, 243, 199) # Light Saffron/Yellow box
    pdf.set_draw_color(212, 175, 55)
    pdf.set_text_color(120, 53, 4)
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(0, 6, ' CRITICAL RULE: ANCHOR TEXT DISTRIBUTION', 0, 1, 'L', fill=True)
    pdf.set_font('Helvetica', '', 9.5)
    rule_desc = (
        "Do NOT link only to the homepage. Distribute backlinks to your target package pages "
        "using the exact keyword as the link text. This drives targeted search ranking jumps."
    )
    pdf.multi_cell(0, 5.5, rule_desc, border='L', fill=True)
    pdf.ln(8)
    
    # ── SECTION 1: GITHUB PAGES ──
    pdf.set_font('Helvetica', 'B', 13)
    pdf.set_text_color(128, 0, 0)
    pdf.cell(0, 7, '1. The GitHub Pages authority Hack (DR 96)', 0, 1, 'L')
    pdf.set_font('Helvetica', '', 10)
    pdf.set_text_color(40, 40, 40)
    github_desc = (
        "Since our source code is hosted on GitHub, enabling GitHub Pages is the fastest way to get a "
        "DR 96 backlink that automatically crawl-indexes all our pages.\n\n"
        "Instructions to Enable:\n"
        "1. Go to repository: https://github.com/ayodhyadharsha-max/Ayodhya-Darshan\n"
        "2. Click on 'Settings' (top menu bar).\n"
        "3. In the left sidebar menu, click 'Pages'.\n"
        "4. Under 'Build and deployment' -> 'Source', select 'Deploy from a branch'.\n"
        "5. Under 'Branch', click the dropdown, select 'main' and '/ (root)', then click 'Save'.\n"
        "6. Once deployed, the live URL will be: https://ayodhyadharsha-max.github.io/Ayodhya-Darshan/\n"
        "   (This URL passes massive link equity back to our domain)."
    )
    pdf.multi_cell(0, 5.5, github_desc)
    pdf.ln(8)
    
    # ── SECTION 2: PROFILE BACKLINKS ──
    pdf.set_font('Helvetica', 'B', 13)
    pdf.set_text_color(128, 0, 0)
    pdf.cell(0, 7, '2. High-DR Profile Backlinks (DR 90 - 91)', 0, 1, 'L')
    
    pdf.set_font('Helvetica', '', 10)
    pdf.set_text_color(40, 40, 40)
    pdf.multi_cell(0, 5.5, "Create accounts on these platforms, and add our site details to the profile website section:")
    pdf.ln(2)
    
    # Details Box
    pdf.set_fill_color(249, 250, 251) # Light gray
    pdf.set_draw_color(220, 220, 220)
    pdf.set_text_color(50, 50, 50)
    
    # Bio details
    details = (
        "Website Name: Ayodhya Dharshan travels\n"
        "Target URL: https://www.ayodhyadharshan.com/\n"
        "Short Tagline: Soulful, fully-managed pilgrimages and custom tour packages to Ayodhya Ram Mandir, Varanasi, and Prayagraj.\n\n"
        "Full Bio / Description:\n"
        "Ayodhya Dharshan travels is a registered premium pilgrimage tour operator offering completely managed yatra packages to the holy cities of Uttar Pradesh, including Ayodhya, Varanasi (Kashi), Prayagraj, and Chitrakoot. We coordinate end-to-end travel including flights/trains bookings, premium hotel stays, private AC cab transfers, and VIP Darshan entry passes for the grand Shri Ram Janmabhoomi Mandir and Kashi Vishwanath temple."
    )
    pdf.set_font('Helvetica', '', 9.5)
    pdf.multi_cell(0, 5.5, details, border=1, fill=True)
    pdf.ln(4)
    
    # Profiles list
    pdf.set_font('Helvetica', '', 10)
    pdf.set_text_color(40, 40, 40)
    profiles = (
        "- Buy Me a Coffee (DR 90) -> Create creator page, add website link.\n"
        "- G2 (DR 91) -> Create company listing in Travel Agencies category.\n"
        "- ProvenExpert (DR 91) -> Create professional business profile.\n"
        "- Reclaim.ai (DR 81) -> Create free account, add site in profile settings.\n"
        "- Modal.com (DR 76) -> Add link to user account bio section."
    )
    pdf.multi_cell(0, 5.5, profiles)
    pdf.ln(8)
    
    # ── SECTION 3: DIRECTORY SUBMISSIONS ──
    pdf.set_font('Helvetica', 'B', 13)
    pdf.set_text_color(128, 0, 0)
    pdf.cell(0, 7, '3. Product & Tool Directories (DR 49 - 75)', 0, 1, 'L')
    
    pdf.set_font('Helvetica', '', 10)
    pdf.set_text_color(40, 40, 40)
    pdf.multi_cell(0, 5.5, "Submit our interactive Yatra Budget Planner to the following product directories:")
    pdf.ln(2)
    
    # Submission details
    sub_details = (
        "Product Name: Ayodhya Yatra Cost Calculator & Planner\n"
        "Target URL: https://www.ayodhyadharshan.com/yatra-cost-calculator.html\n"
        "Category: Travel Tools / Personal Finance / Calculators\n\n"
        "Short Description:\n"
        "An interactive budget planner that computes travel, hotel stays, local taxi transfers, and VIP darshan pass prices for the Ayodhya & Kashi pilgrimage in real-time.\n\n"
        "Full Pitch:\n"
        "Planning a pilgrimage to Ayodhya or Kashi often involves unpredictable taxi costs and hotel rates. The Ayodhya Yatra Cost Calculator simplifies this by letting devotees choose their starting city, hotel category, and travel modes to get an instant cost estimate with direct WhatsApp enquiry integration."
    )
    pdf.set_font('Helvetica', '', 9.5)
    pdf.multi_cell(0, 5.5, sub_details, border=1, fill=True)
    pdf.ln(4)
    
    # Directories list
    pdf.set_font('Helvetica', '', 10)
    pdf.set_text_color(40, 40, 40)
    dirs = (
        "- index.dodopayments.com (DR 75) -> Submit tool link.\n"
        "- Uneed.best (DR 74) -> Submit under Travel Utilities.\n"
        "- whatlaunched.today (DR 55) -> Submit launch details.\n"
        "- betterlaunch.co (DR 54) -> List as travel startup/app.\n"
        "- ctralt.cc (DR 49) -> Submit under web utilities.\n"
        "- nicklaunches.com (DR 30) / abacklaunch.com (DR 26) -> Free startup listing."
    )
    pdf.multi_cell(0, 5.5, dirs)
    pdf.ln(8)
    
    # ── SECTION 4: NICHE LINKS & DIRECTORIES ──
    pdf.set_font('Helvetica', 'B', 13)
    pdf.set_text_color(128, 0, 0)
    pdf.cell(0, 7, '4. Niche & Directory Links (DR 33 - 76)', 0, 1, 'L')
    pdf.set_font('Helvetica', '', 10)
    niche_text = (
        "- grokipedia.com (DR 76) -> Submit / suggest the article:\n"
        "  * Title: How to Book Ram Mandir VIP Darshan Pass Online\n"
        "  * Link: https://www.ayodhyadharshan.com/blog-ram-mandir-vip-pass-booking-guide.html\n"
        "- auraplusplus.com (DR 69) -> Submit request to add tool.\n"
        "- domainaio.com (DR 43) -> Submit domain lookup.\n"
        "- useneedle.net (DR 33) -> Add to agency directory listings."
    )
    pdf.multi_cell(0, 5.5, niche_text)
    pdf.ln(8)
    
    # ── SECTION 5: TARGET DISTRIBUTION SHEET ──
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 13)
    pdf.set_text_color(128, 0, 0)
    pdf.cell(0, 7, '5. Target Keyword Link Distribution Sheet', 0, 1, 'L')
    pdf.set_font('Helvetica', '', 10.5)
    pdf.set_text_color(40, 40, 40)
    pdf.multi_cell(0, 5.5, "When doing submissions, use these exact keywords as Anchor Texts (clickable text) linking to the specific pages:")
    pdf.ln(4)
    
    # Table headers
    pdf.set_fill_color(255, 107, 0) # Saffron
    pdf.set_text_color(255, 255, 255)
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(85, 8, 'Target Keyword (Anchor)', 1, 0, 'L', fill=True)
    pdf.cell(105, 8, 'Target Landing Page URL', 1, 1, 'L', fill=True)
    
    # Table rows
    pdf.set_fill_color(255, 255, 255)
    pdf.set_text_color(40, 40, 40)
    pdf.set_font('Helvetica', '', 9)
    
    rows = [
        ("Delhi to Ayodhya tour package", "https://www.ayodhyadharshan.com/delhi-to-ayodhya-tour-package.html"),
        ("Ram Mandir VIP Pass Price", "https://www.ayodhyadharshan.com/blog-ram-mandir-vip-pass-booking-guide.html"),
        ("Kashi Vishwanath VIP Darshan", "https://www.ayodhyadharshan.com/blog-kashi-vishwanath-sawan-vip-darshan-guide.html"),
        ("Varanasi Ganga Cruise Booking", "https://www.ayodhyadharshan.com/blog-varanasi-ganga-cruise-booking-guide.html"),
        ("Mathura Vrindavan Tour Package", "https://www.ayodhyadharshan.com/mathura-vrindavan-tour-package.html")
    ]
    
    toggle = True
    for kw, url in rows:
        if toggle:
            pdf.set_fill_color(249, 250, 251) # Light gray alternate row
        else:
            pdf.set_fill_color(255, 255, 255)
        pdf.cell(85, 8, f' {kw}', 1, 0, 'L', fill=True)
        pdf.cell(105, 8, f' {url}', 1, 1, 'L', fill=True)
        toggle = not toggle
        
    pdf.ln(8)
    pdf.set_font('Helvetica', 'I', 9.5)
    pdf.set_text_color(100, 100, 100)
    pdf.multi_cell(0, 5, "Confidential internal SEO document created for Ayodhya Dharshan marketing execution.")

    output_path = "/Users/rishabhjaiswal/ayodhya-darshan/backlink_campaign_2026.pdf"
    pdf.output(output_path)
    print(f"PDF successfully generated at: {output_path}")

if __name__ == '__main__':
    create_backlink_pdf()
