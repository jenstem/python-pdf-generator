from fpdf import FPDF
import csv


with open("countries.txt", encoding="utf-8") as csv_file:
    data = list(csv.reader(csv_file, delimiter=","))


pdf = FPDF()
pdf.set_font("Arial", size=14)


pdf.add_page()
with pdf.table() as table:
    for data_row in data:
        row = table.row()
        for data_cell in data_row:
            row.cell(data_cell)


pdf.output("table.pdf")