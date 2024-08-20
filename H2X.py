# Importing pandas
import pandas as pd
  
def html_add_2_excel(html, excel_file_name):
    print('Writing information on Excel file\n')
    table = pd.read_html(html)[0]
    table.to_excel(excel_file_name + '.xlsx')
    print('The information was written on an Excel file\n\n')