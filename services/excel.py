from openpyxl import Workbook
from datetime import datetime

def generate_report(*costs):
    date = datetime.now().strftime("%Y-%m-%d")
    time = datetime.now().strftime("%H-%M-%S")

    wb = Workbook()
    ws = wb.active
    ws['A1'] = 'Values'
    ws['A3'] = 'Bitcoin'
    ws['A4'] = 'Etherium'
    ws['A5'] = 'Litecoin'
    ws['B3'] = costs[0][0]
    ws['B4'] = costs[0][1]
    ws['B5'] = costs[0][2]

    wb.save(f"currency_{date}_{time}.xlsx")
