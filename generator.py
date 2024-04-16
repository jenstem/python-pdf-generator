from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        pass

    def footer(self):
        pass

    def chapter_title(self, num, label):
        self.set_font("Arial", "B", 16)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 6, f"Chapter {num} : {label}", new_x = "LMARGIN", new_y = "NEXT", align = "L", fill = True)

    def chapter_body(self, filepath):
        with open(filepath, "rb") as fh:
            txt = fh.read().decode("latin-1")
        self.set_font("Arial", size=12)
        self.multi_cell(0, 5, txt)
        self.ln()
        self.set_font(style = "I")
        self.cell(0, 5, "(End of excerpt)")

    def print_chapter(self, num, title, filepath):
        self.add_page()
        self.chapter_title(num, title)
        self.chapter_body(filepath)


pdf = PDF()
pdf.print_chapter(1, "Getting Started with Programming", "para.txt")
pdf.output("sample2.pdf")
