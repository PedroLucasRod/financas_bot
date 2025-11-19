import os
from fastapi import FastAPI, Request
from telegram import Update, Bot
from telegram.ext import Dispatcher, MessageHandler, Filters
from config import TOKEN, ALLOWED_USERS, SHEET_ID
from handlers.message_handler import receber_mensagem
from fastapi.responses import RedirectResponse

import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Bot e Dispatcher
bot = Bot(TOKEN)
dispatcher = Dispatcher(bot, None, workers=4)

# Handler principal
def handle(update, context):
    receber_mensagem(update, context, ALLOWED_USERS)

dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle))

# FastAPI app
app = FastAPI()

@app.on_event("startup")
async def startup():
    webhook_url = os.getenv("WEBHOOK_URL")
    if webhook_url:
        url = f"{webhook_url}/{TOKEN}"
        success = bot.set_webhook(url)
        print(f"✅ Webhook configurado ({success}): {url}")
    else:
        print("⚠️ Nenhuma WEBHOOK_URL configurada!")


@app.post(f"/{TOKEN}")
async def webhook(request: Request):
    """Recebe atualizações do Telegram"""
    data = await request.json()
    update = Update.de_json(data, bot)
    dispatcher.process_update(update)
    return {"ok": True}

@app.get("/")
async def home():
    return {"status": "🤖 Bot rodando via webhook!"}

@app.get("/download")
async def download_excel():
    # Link direto para exportar como Excel do Google Sheets
    url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=xlsx"
    return RedirectResponse(url)

@app.get("/test")
async def test():
    return {"status": "funcionando"}

# Executar app no Render
if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
