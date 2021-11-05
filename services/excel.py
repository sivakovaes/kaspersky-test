from openpyxl import Workbook
from datetime import datetime

def generate_report(*costs):
    date = datetime.now().strftime("%Y-%m-%d")
    time = datetime.now().strftime("%H-%M-%S")

    wb = Workbook()
    ws = wb.active
    ws['A1'] = 'Values'
    ws.append(['Bitcoin', costs[0]])
    ws.append(['Etherium', costs[1]])
    ws.append(['TiLitecoinme', costs[2]])

    wb.save(f"currency_{date}_{time}.xlsx")
