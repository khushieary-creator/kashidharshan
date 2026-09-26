import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
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
    pdf.cell(0, 6, 'OFFICIAL PRESS RELEASE', new_x="LMARGIN", new_y="NEXT")

    pdf.set_font('Helvetica', 'B', 18)
    pdf.set_text_color(128, 0, 0)
    pdf.multi_cell(0, 8, 'Kashi Dharshan Travels Launches All-Inclusive Ramayana Circuit & VIP Darshan Pilgrimage Packages for 2026')
    pdf.ln(4)

    pdf.set_font('Helvetica', 'B', 9.5)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(0, 6, 'VARANASI, UTTAR PRADESH - AUGUST 31, 2026', new_x="LMARGIN", new_y="NEXT")

    pdf.set_draw_color(200, 200, 200)
    pdf.line(10, pdf.get_y() + 2, 200, pdf.get_y() + 2)
    pdf.ln(6)

    # Body
    pdf.set_font('Helvetica', '', 10)
    pdf.set_text_color(40, 40, 40)

    p1 = (
        "Kashi Dharshan Travels, a premier registered pilgrimage tour operator in Uttar Pradesh, "
        "has officially announced the launch of its updated 2026 all-inclusive Ramayana Circuit yatra packages. "
        "Designed to offer a seamless, unhurried spiritual experience for families and senior citizens, "
        "the new packages cover Kashi Vishwanath (Varanasi), Ayodhya Shri Ram Janmabhoomi, Prayagraj (Triveni Sangam), "
        "and Mathura-Vrindavan."
    )
    pdf.multi_cell(0, 5.5, p1)
    pdf.ln(4)

    p2 = (
        "With millions of devotees traveling to Kashi and Ayodhya following the historic consecration of the Shri Ram Janmabhoomi Mandir and Kashi Vishwanath Corridor, "
        "navigating long queue times and local transport has become a key concern for pilgrims. "
        "Kashi Dharshan Travels resolves this by providing complete yatra management including priority VIP Darshan (Sugam Darshan) "
        "pass assistance, dedicated private AC cabs (Dzire, Ertiga, Innova Crysta), and hand-picked corridor hotels close to temple gates."
    )
    pdf.multi_cell(0, 5.5, p2)
    pdf.ln(4)

    pdf.set_font('Helvetica', 'B', 11)
    pdf.set_text_color(128, 0, 0)
    pdf.cell(0, 6, 'Key Highlights of the 2026 Yatra Packages:', new_x="LMARGIN", new_y="NEXT")
    pdf.set_font('Helvetica', '', 10)
    pdf.set_text_color(40, 40, 40)

    highlights = (
        "- VIP Entry Pass Assistance: Sugam Darshan & Aarti slot bookings for Kashi Vishwanath & Ram Mandir.\n"
        "- Complete Logistics: Direct pickup from Varanasi/Lucknow airports, railway stations, and private highway transfers.\n"
        "- Specialized Regional Tours: Dedicated packages starting from major hubs including Bengaluru, Chennai, Mumbai, Delhi, and Hyderabad.\n"
        "- Luxury Varanasi Ganga Cruise & Pind Daan: Customized boat bookings for Ganga Aarti and certified Pujari coordination for Pind Daan at Gaya and Prayagraj."
    )
    pdf.multi_cell(0, 5.5, highlights)
    pdf.ln(4)

    p3 = (
        "Devotees can also utilize the newly launched online Yatra Cost Calculator on their website "
        "to compute real-time travel, accommodation, and cab budget estimates before booking."
    )
    pdf.multi_cell(0, 5.5, p3)
    pdf.ln(8)

    # About Section Box
    pdf.set_fill_color(249, 250, 251)
    pdf.set_draw_color(220, 220, 220)
    pdf.set_font('Helvetica', 'B', 10)
    pdf.set_text_color(128, 0, 0)
    pdf.cell(0, 6, ' About Kashi Dharshan Travels:', fill=True, new_x="LMARGIN", new_y="NEXT")
    
    pdf.set_font('Helvetica', '', 9.5)
    pdf.set_text_color(50, 50, 50)
    about_text = (
        "Kashi Dharshan Travels is an IATA-compliant, Govt. registered pilgrimage tour operator based in Varanasi, Uttar Pradesh. "
        "Having guided over 12,000+ devotees across Uttar Pradesh, the agency specializes in curated spiritual yatras, hotel stays, "
        "cabs, and VIP temple entry coordination.\n\n"
        "Media & Booking Contact:\n"
        "- Website: https://www.kashidharshan.com/\n"
        "- Yatra Calculator: https://www.kashidharshan.com/yatra-cost-calculator.html\n"
        "- Phone / WhatsApp: +91 70119 60307\n"
        "- Location: Godowlia, Varanasi, Uttar Pradesh, India"
    )
    pdf.multi_cell(0, 5.5, about_text, border=1, fill=True)

    output_path = os.path.join(BASE_DIR, "kashi_dharshan_press_release_2026.pdf")
    pdf.output(output_path)
    print(f"Press Release PDF generated at: {output_path}")

if __name__ == '__main__':
    create_pr_pdf()
