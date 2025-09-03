# services/storage.py
import openpyxl
from datetime import datetime
from config import EXCEL_FILE

def load_workbook_and_sheet():
    try:
        workbook = openpyxl.load_workbook(EXCEL_FILE)
        sheet = workbook.active
    except FileNotFoundError:
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.append(["Data", "Descrição", "Valor", "Tipo", "Categoria"])
        workbook.save(EXCEL_FILE)
    return workbook, sheet

def add_record(workbook, sheet, linha, valor, tipo, categoria):
    sheet.append([datetime.now().strftime("%d/%m/%Y"), linha, valor, tipo, categoria])
    workbook.save(EXCEL_FILE)

def get_all_records(sheet):
    return list(sheet.iter_rows(min_row=2, values_only=True))

def update_record(workbook, sheet, idx, nova_categoria):
    row = list(sheet.iter_rows(min_row=2, max_row=idx+1, values_only=False))[-1]
    row[4].value = nova_categoria
    workbook.save(EXCEL_FILE)

def delete_records(workbook, sheet, indices):
    for idx in sorted(indices, reverse=True):
        sheet.delete_rows(idx+1)
    workbook.save(EXCEL_FILE)
