from fpdf import FPDF
import pandas as pd

df = pd.read_csv("topics.csv")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font("Arial", style="B", size=25)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(200, 10, txt=f"{row['Topic']} : {row['Pages']}", ln=1, align="L")

    # set the lines
    a = 21
    for i in range(20, 298, 10):
        pdf.line(10, i, 200, i)
        a = a + 10

    # Set the footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # Set the footer
        pdf.ln(265)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

        # set the lines
        for i in range(20, 298, 10):
            pdf.line(10, i, 200, i)
            a = a + 10

pdf.output("op1.pdf")
