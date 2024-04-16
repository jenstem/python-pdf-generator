from fpdf import FPDF

pdf = FPDF()

pdf.add_page()
pdf.set_font("Arial", size=20)
pdf.write(5, "To find out what's new in tutorial, click ")
pdf.set_font(style="U")
link = pdf.add_link(page=2)
pdf.write(5, "here", link)


pdf.add_page()
pdf.image("logo.jpg", 10, 10, 50, 0, "", "https://www.google.com")


pdf.output("link.pdf")