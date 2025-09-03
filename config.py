import os
from dotenv import load_dotenv

load_dotenv()  # carrega variáveis do arquivo .env

TOKEN = os.getenv("TELEGRAM_TOKEN")
EXCEL_FILE = "financas.xlsx"
CATEGORIAS_FILE = "categorias.json"
