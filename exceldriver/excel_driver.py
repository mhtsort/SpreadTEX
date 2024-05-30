from pathlib import Path
from openpyxl import load_workbook

class Excel_Driver:
    def __init__(self, path: Path) -> None:
        if self.file_exists(path):
            self.path = path
            self.data = []
            print(f"Excel Driver created for {self.path}")
        else:
            raise FileExistsError("The file does not exist in Path")

    def __str__(self) -> str:
        return str(self.data)

    def __repr__(self) -> str:
        return f"Excel_Driver({self.path})"

    def get_data(self):
        # Load the workbook
        workbook = load_workbook(filename=self.path)
        # Select a worksheet
        sheet = workbook.active  # This will select the first sheet as active

        # Iterate through the rows and read the values
        for row in sheet.iter_rows(values_only=True):
            self.data.append(row)

    def file_exists(self, path: Path) -> bool:
        """
        Check if the Excel file exists at the specified path.

        Returns:
        - bool: True if the file exists, False otherwise.
        """
        return path.exists() and path.is_file()
    def read(self):
        self.data = []
        self.get_data()
        return self.data
    
    def select(self, selection_strategy = None):
        if selection_strategy is not None:
            return selection_strategy(self.data)
        else:
            return self.data
if __name__ == '__main__':
    
    def strategy(mylist):
        return [x for x in mylist[1:] if x[2]>50210]
    print("START")
    static_dir = Path(__file__).resolve().parent.parent / 'static'
    path = static_dir / 'data.xlsx'
    try:
        driver = Excel_Driver(path)
    except FileExistsError as e:
        print(e)
    driver.read()
    driver.select()
    
    print(driver.select(strategy))