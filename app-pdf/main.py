from fpdf import FPDF
import pandas as pd


df = pd.read_csv("topics.csv")

pdf = FPDF(orientation="P", unit="mm", format="A4")


for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font("Arial", style="B", size=25)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(200, 10, txt=f"{row['Topic']} : {row['Pages']}", ln=1, align="L")
    pdf.line(10, 21, 200, 21)


pdf.output("op1.pdf")