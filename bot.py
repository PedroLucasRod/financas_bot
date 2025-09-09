import os
from fastapi import FastAPI, Request, HTTPException
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

from fastapi.responses import FileResponse

EXCEL_FILE = "financas.xlsx"
ALLOWED_USERS = [5569080585, 2071995124]  # 🔹 Substitua pelos IDs do Telegram

@app.get("/download")
async def download_excel(request: Request):
    # Verifica se veio user_id como query param
    user_id = request.query_params.get("user_id")
    if not user_id or int(user_id) not in ALLOWED_USERS:
        raise HTTPException(status_code=403, detail="Acesso negado 🚫")

    if not os.path.exists(EXCEL_FILE):
        raise HTTPException(status_code=404, detail="Arquivo não encontrado")

    return FileResponse(
        EXCEL_FILE,
        filename="financas_atual.xlsx",
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
