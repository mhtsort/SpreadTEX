import sys
import exceldriver.excel_driver as driver

TEMPLATE_PATH =r"C:\Users\mhtso\OneDrive\Desktop1\SpreadTEX\app\SpreadTEX\static\template.tex"
DATA_PATH = r"C:\Users\mhtso\OneDrive\Desktop1\SpreadTEX\app\SpreadTEX\static\data.xlsx"
data=driver.Excel_Driver(DATA_PATH)
data.getdata()
print(data.data[:4])
