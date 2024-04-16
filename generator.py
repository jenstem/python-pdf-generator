from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.image("logo.jpg", 10, 8, 33)
        self.set_font("Arial", "B", 16)
        self.cell(80)
        self.cell(40, 10, "Hello World!", border = 1, align = "C")


pdf = PDF()


pdf.add_page()
pdf.output("sample.pdf")