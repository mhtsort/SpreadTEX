from pathlib import Path
from openpyxl import load_workbook


class Excel_Driver():
    def __init__(self, path:Path) -> None:
        self.path=path
        self.data=[]
    def __str__(self) -> str:
        return str(self.data)
    def __repr__(self) -> str:
        return str(self.data[0])
    def getdata(self):
        # Load the workbook
        workbook = load_workbook(filename=self.path)
        # Select a worksheet
        sheet = workbook.active  # This will select the first sheet as active

        # Or select by name
        # sheet = workbook['Sheet1']
        sheet.iter_rows()
        # Iterate through the rows and read the values
        for row in sheet.iter_rows(values_only=True):
            print(row)
            self.data.append(row)