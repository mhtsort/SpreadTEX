from excel_driver import Excel_Driver
from pathlib import Path
#Relative path to static folder
path = Path(r"C:\Users\mhtso\OneDrive\Desktop1\SpreadTEX\app\SpreadTEX\")

file = Excel_Driver(path)
file.get_data() 

for row in file.data[:5]:
    print(row)

print(Path.cwd())