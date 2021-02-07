# python libraries
from fpdf import FPDF
from datetime import datetime, timedelta
import os

WIDTH = 210
HEIGHT = 297

TEST_DATE = "2020-12-25"

def create_title(day, pdf):
    pdf.set_font('Arial', '', 24)  
    pdf.ln(60)
    pdf.write(5, f"Sales Analytics Report")
    pdf.ln(10)
    pdf.set_font('Arial', '', 16)
    pdf.write(4, f'{day}')
    pdf.ln(5)

def create_sales_analytics_report(day=TEST_DATE, filename="report.pdf"):
    pdf = FPDF() #A4 (210x297 mm)

    ''' First Page '''
    pdf.add_page()
    pdf.image("./resources/pdf-header.png", 0, 0, WIDTH)
    create_title(day, pdf)

    ''' Second Page '''

    ''' Third Page '''

    pdf.output(filename, 'F')

if __name__ == '__main__':
    yesterday = (datetime.today() - timedelta(days=1)).strftime("%m/%d/%y").replace("/0","/").lstrip("0")
    yesterday = "2020-12-25" # Uncomment line for testing

    create_sales_analytics_report(yesterday)
