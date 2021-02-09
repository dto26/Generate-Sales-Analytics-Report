# python libraries
from fpdf import FPDF
from datetime import datetime, timedelta, date
import os
import analysis

WIDTH = 210
HEIGHT = 297

TEST_DATE = date.today()

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

    # Generate plots
    # plot_world_sales()
    # plot_monthly_sales()
    # plot_country_sales()
    # plot_product_sales()
    # plot_orders_vs_price()

    # Add figures to pdf
    pdf.image('./resources/world_sales.png', 12, 95, WIDTH-20)
    pdf.image('./resources/monthly_sales_plot.png', 5, 200, WIDTH/2-10)
    pdf.image('./resources/orders_vs_price.png', WIDTH/2, 200, WIDTH/2-10)

    ''' Second Page '''

    ''' Third Page '''

    pdf.output(filename, 'F')

if __name__ == '__main__':
    create_sales_analytics_report(TEST_DATE)
    print('Sales Analysis Report created successfully')
