import os
from dotenv import load_dotenv

load_dotenv()  # carrega variáveis do arquivo .env

TOKEN = os.getenv("TELEGRAM_TOKEN")
CATEGORIAS_FILE = "categorias.json"
ALLOWED_USERS = [5569080585, 2071995124]  # 🔹 Substitua pelos IDs do Telegram
SHEET_ID = "15pX1d1RB9NjlQzrxeyWQjf50Zn2oxmUlxecrFKaGCcI"  # ID da sua planilha
