# bot.py
import os
from telegram.ext import Updater, MessageHandler, Filters
from config import TOKEN, WEBHOOK_URL, PORT
from services.storage import load_workbook_and_sheet
from handlers.message_handler import receber_mensagem

# FastAPI apenas para healthcheck
from fastapi import FastAPI
app = FastAPI()

workbook, sheet = load_workbook_and_sheet()

def handle(update, context):
    receber_mensagem(update, context, workbook, sheet)

def run():
    if not TOKEN:
        raise RuntimeError("TELEGRAM_TOKEN não definido.")

    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle))

    if WEBHOOK_URL:  
        # PRODUÇÃO → Render
        updater.start_webhook(
            listen="0.0.0.0",
            port=PORT,
            url_path=TOKEN
        )
        updater.bot.setWebhook(f"{WEBHOOK_URL}/{TOKEN}")
        print(f"🤖 Bot rodando em webhook: {WEBHOOK_URL}/{TOKEN} (PORT={PORT})")
    else:  
        # LOCAL → Polling
        updater.start_polling()
        print("🤖 Bot rodando em polling (local)")

    updater.idle()

@app.get("/")
def health():
    return {"status": "ok", "service": "telegram-bot"}

if __name__ == "__main__":
    run()
