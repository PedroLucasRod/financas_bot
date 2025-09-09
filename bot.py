import os
from fastapi import FastAPI, Request
from telegram import Update, Bot
from telegram.ext import Dispatcher, MessageHandler, Filters
from config import TOKEN
from services.storage import load_workbook_and_sheet
from handlers.message_handler import receber_mensagem

# Carregar planilha
workbook, sheet = load_workbook_and_sheet()

# Bot e Dispatcher
bot = Bot(TOKEN)
dispatcher = Dispatcher(bot, None, workers=4)

# Handler principal
def handle(update, context):
    receber_mensagem(update, context, workbook, sheet)

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

# Executar app no Render
if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
