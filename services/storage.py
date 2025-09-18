import os
import json
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
from config import SHEET_ID

# Configuração Google Sheets
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# Lê as credenciais do Render (variável de ambiente)
creds_json = os.getenv("GOOGLE_CREDENTIALS")

if not creds_json:
    raise RuntimeError("❌ Variável de ambiente GOOGLE_CREDENTIALS não encontrada")

creds_dict = json.loads(creds_json)
creds = Credentials.from_service_account_info(creds_dict, scopes=SCOPES)

client = gspread.authorize(creds)
sheet = client.open_by_key(SHEET_ID).sheet1  # primeira aba

def add_record(linha, valor, tipo, categoria):
    nova_linha = [datetime.now().strftime("%d/%m/%Y"), linha, valor, tipo, categoria]
    sheet.append_row(nova_linha)
    print(f"✅ Linha adicionada: {nova_linha}")

def get_all_records():
    return sheet.get_all_values()[1:]  # ignora cabeçalho

def update_record(idx, nova_categoria):
    # Google Sheets é 1-based (primeira linha = 1)
    linha = idx + 1  # +1 porque primeira linha é cabeçalho
    sheet.update_cell(linha, 5, nova_categoria)  # coluna 5 = Categoria

def delete_records(indices):
    for idx in sorted(indices, reverse=True):
        linha = idx + 1
        sheet.delete_rows(linha)
