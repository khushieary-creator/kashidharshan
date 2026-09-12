import os
from fpdf import FPDF

class PressReleasePDF(FPDF):
    def header(self):
        self.set_fill_color(255, 107, 0)
        self.rect(0, 0, 210, 4, 'F')
        self.set_font('Helvetica', 'B', 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, 'FOR IMMEDIATE RELEASE - PRESS RELEASE 2026', 0, 0, 'L')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', 0, 0, 'C')

def create_pr_pdf():
    pdf = PressReleasePDF()
    pdf.alias_nb_pages()
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.add_page()

    # Dateline & Title
    pdf.set_y(25)
    pdf.set_font('Helvetica', 'B', 10)
    pdf.set_text_color(255, 107, 0)
    pdf.cell(0, 6, 'OFFICIAL PRESS RELEASE', 0, 1, 'L')

    pdf.set_font('Helvetica', 'B', 18)
    pdf.set_text_color(128, 0, 0)
    pdf.multi_cell(0, 8, 'Ayodhya Dharshan Travels Launches All-Inclusive Ramayana Circuit & VIP Darshan Pilgrimage Packages for 2026')
    pdf.ln(4)

    pdf.set_font('Helvetica', 'B', 9.5)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(0, 6, 'AYODHYA, UTTAR PRADESH - AUGUST 31, 2026', 0, 1, 'L')

    pdf.set_draw_color(200, 200, 200)
    pdf.line(10, pdf.get_y() + 2, 200, pdf.get_y() + 2)
    pdf.ln(6)

    # Body
    pdf.set_font('Helvetica', '', 10)
    pdf.set_text_color(40, 40, 40)

    p1 = (
        "Ayodhya Dharshan travels, a premier registered pilgrimage tour operator in Uttar Pradesh, "
        "has officially announced the launch of its updated 2026 all-inclusive Ramayana Circuit yatra packages. "
        "Designed to offer a seamless, unhurried spiritual experience for families and senior citizens, "
        "the new packages cover Ayodhya Shri Ram Janmabhoomi, Kashi Vishwanath (Varanasi), Prayagraj (Triveni Sangam), "
        "and Mathura-Vrindavan."
    )
    pdf.multi_cell(0, 5.5, p1)
    pdf.ln(4)

    p2 = (
        "With millions of devotees traveling to Ayodhya following the historic consecration of the Shri Ram Janmabhoomi Mandir, "
        "navigating long queue times and local transport has become a key concern for pilgrims. "
        "Ayodhya Dharshan travels resolves this by providing complete yatra management including priority VIP Darshan (Sugam Darshan) "
        "pass assistance, dedicated private AC cabs (Dzire, Ertiga, Innova Crysta), and hand-picked corridor hotels close to temple gates."
    )
    pdf.multi_cell(0, 5.5, p2)
    pdf.ln(4)

    pdf.set_font('Helvetica', 'B', 11)
    pdf.set_text_color(128, 0, 0)
    pdf.cell(0, 6, 'Key Highlights of the 2026 Yatra Packages:', 0, 1, 'L')
    pdf.set_font('Helvetica', '', 10)
    pdf.set_text_color(40, 40, 40)

    highlights = (
        "- VIP Entry Pass Assistance: Sugam Darshan & Aarti slot bookings for Ram Mandir & Kashi Vishwanath.\n"
        "- Complete Logistics: Direct pickup from Lucknow/Varanasi airports, railway stations, and private highway transfers.\n"
        "- Specialized Regional Tours: Dedicated packages starting from major hubs including Bengaluru, Chennai, Mumbai, Delhi, and Hyderabad.\n"
        "- Luxury Varanasi Ganga Cruise & Pind Daan: Customized boat bookings for Ganga Aarti and certified Pujari coordination for Pind Daan at Gaya and Prayagraj."
    )
    pdf.multi_cell(0, 5.5, highlights)
    pdf.ln(4)

    p3 = (
        "Devotees can also utilize the newly launched online Ayodhya Yatra Cost Calculator on their website "
        "to compute real-time travel, accommodation, and cab budget estimates before booking."
    )
    pdf.multi_cell(0, 5.5, p3)
    pdf.ln(8)

    # About Section Box
    pdf.set_fill_color(249, 250, 251)
    pdf.set_draw_color(220, 220, 220)
    pdf.set_font('Helvetica', 'B', 10)
    pdf.set_text_color(128, 0, 0)
    pdf.cell(0, 6, ' About Ayodhya Dharshan Travels:', 0, 1, 'L', fill=True)
    
    pdf.set_font('Helvetica', '', 9.5)
    pdf.set_text_color(50, 50, 50)
    about_text = (
        "Ayodhya Dharshan travels is an IATA-compliant, Govt. registered pilgrimage tour operator based in Ayodhya, Uttar Pradesh. "
        "Having guided over 12,000+ devotees across Uttar Pradesh, the agency specializes in curated spiritual yatras, hotel stays, "
        "cabs, and VIP temple entry coordination.\n\n"
        "Media & Booking Contact:\n"
        "- Website: https://www.ayodhyadharshan.com/\n"
        "- Yatra Calculator: https://www.ayodhyadharshan.com/yatra-cost-calculator.html\n"
        "- Phone / WhatsApp: +91 92352 22399\n"
        "- Location: Ayodhya Dham, Uttar Pradesh, India"
    )
    pdf.multi_cell(0, 5.5, about_text, border=1, fill=True)

    output_path = "/Users/rishabhjaiswal/ayodhya-darshan/ayodhya_dharshan_press_release_2026.pdf"
    pdf.output(output_path)
    print(f"Press Release PDF generated at: {output_path}")

if __name__ == '__main__':
    create_pr_pdf()
