# bot.py
from telegram.ext import Updater, MessageHandler, Filters
from config import TOKEN
from services.storage import load_workbook_and_sheet
from handlers.message_handler import receber_mensagem

workbook, sheet = load_workbook_and_sheet()

def handle(update, context):
    receber_mensagem(update, context, workbook, sheet)

updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle))

print("🤖 Bot rodando...")
updater.start_polling()
updater.idle()
