import sys
import os
import exceldriver.excel_driver as driver
import pathlib 

# Relative paths to static folder containing data and template
STATIC_FOLDER = pathlib.Path(__file__).parent / "static"
TEMPLATE_PATH = STATIC_FOLDER / "template.tex"
DATA_PATH = STATIC_FOLDER / "data.xlsx"

#Load data and get the data
data = driver.Excel_Driver(DATA_PATH)
data.get_data()

#Use the data
print(data.data[:4])
#print(os.path.dirname(__file__))