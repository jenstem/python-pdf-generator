from fpdf import FPDF


class PDF(FPDF):
    """
    Custom PDF class that extends FPDF to create structured PDF documents
    with headers, footers, and chapters.
    """
    def header(self):
        """
        Define the header for the PDF document.
        Sets the font, colors, and layout for the title.
        """
        self.set_font("Arial", "B", 18)
        width = self.get_string_width(self.title) + 6
        self.set_x((210 - width) / 2)
        self.set_draw_color(0, 80, 180)
        self.set_fill_color(230, 230, 0)
        self.set_text_color(220, 50, 50)
        self.set_line_width = 1
        self.cell(width, 9, self.title, new_x="LMARGIN", new_y="NEXT", align="C", fill=True)
        self.ln(10)

    def footer(self):
        """
        Define the footer for the PDF document.
        Sets the page number at the bottom center of the page.
        """
        self.set_y(-15)
        self.set_font("Arial", "I", 12)
        self.set_text_color(128)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def chapter_title(self, num, label):
        """
        Create a chapter title.

        Args:
            num (int): Chapter number.
            label (str): Chapter title.
        """
        self.set_font("Arial", "B", 16)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 6, f"Chapter {num} : {label}", new_x = "LMARGIN", new_y = "NEXT", align = "L", fill = True)

    def chapter_body(self, filepath):
        """
        Read and format the body of the chapter from a file.

        Args:
            filepath (str): Path to the text file containing chapter content.
        """
        with open(filepath, "rb") as fh:
            txt = fh.read().decode("latin-1")
        self.set_font("Arial", size=12)
        self.multi_cell(0, 5, txt)
        self.ln()
        self.set_font(style = "I")
        self.cell(0, 5, "(End of excerpt)")

    def print_chapter(self, num, title, filepath):
        """
        Print a chpater in the PDF document.

        Args:
            num (int): Chapter number.
            title (str): Chapter title.
            filepath (str): Path to the text file containing chapter content.
        """
        self.add_page()
        self.chapter_title(num, title)
        self.chapter_body(filepath)


pdf = PDF()
pdf.set_title("Programming Guide")
pdf.set_author("John Doe")
pdf.print_chapter(1, "Getting Started with Programming", "para.txt")
pdf.print_chapter(2, "Which Programming Language to Learn", "para.txt")

pdf.add_page()
pdf.set_font("Arial", size=20)
pdf.image("logo.jpg", 10, 10, 50, 0, "", "https://www.google.com")
pdf.set_left_margin(60)
pdf.write_html("<h1>Links</h1>")
pdf.write_html(""" <br>
                <p> External Link - will take you to Google.com </p>
                <a href="https://www.google.com">Link to Google</a>
                <br>
                <br>
                <p> Internal Link - will take you to page 2 </p>
                <br>
                """)
pdf.write(5, "To find out what's new in tutorial, click ")
pdf.set_font(style="U")
link = pdf.add_link(page=2)
pdf.write(5, "here", link)


pdf.output("new-pdf.pdf")
