from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.image("logo.jpg", 10, 8, 33)


pdf = PDF()


pdf.add_page()
pdf.set_font("Arial", "B", 16)
pdf.cell(40, 10, "Hello World!")
pdf.output("sample.pdf")