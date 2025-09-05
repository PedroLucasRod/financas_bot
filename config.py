#config.py
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
EXCEL_FILE = "financas.xlsx"
CATEGORIAS_FILE = "categorias.json"

# URL pública do seu serviço no Render, ex.: https://financas-bot.onrender.com
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
PORT = int(os.getenv("PORT", "8080"))
