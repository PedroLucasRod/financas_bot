# handlers/message_handler.py
from telegram import Update
from telegram.ext import CallbackContext
from services.classifier import classificar_mensagem, lista_categorias
from services.storage import add_record, get_all_records, update_record, delete_records
from services.reports import gerar_relatorio

def processar_linhas(workbook, sheet, texto):
    respostas = []
    for linha in texto.splitlines():
        if not linha.strip():
            continue
        valor, tipo, categoria, subcategoria = classificar_mensagem(linha)
        if valor and tipo and categoria and subcategoria:
            add_record(workbook, sheet, linha, valor, tipo, f"{categoria} > {subcategoria}")
            respostas.append(f"✅ Registrado: {valor} - {tipo} - {categoria} > {subcategoria}")
        elif valor:
            respostas.append(f"❌ Categoria não reconhecida para '{linha}'.\nCategorias disponíveis:\n{lista_categorias()}")
        else:
            respostas.append(f"❌ Não entendi o valor em: '{linha}'")
    return "\n".join(respostas)

def boas_vindas(update, context):
    texto = ("👋 Olá! Bem-vindo ao seu bot de finanças!\n\n"
        "Você pode:\n"
        "- Visualizar registros: escreva 'visualizar'\n"
        "- Ver relatório: escreva 'relatorio' ou 'relatorio barra'/'relatorio pizza'\n"
        "- Alterar categoria: escreva 'alterar <número> <nova_categoria>'\n"
        "- Remover registros: escreva 'remover <número(s)>'\n"
        "Para registrar gastos/ganhos, envie a descrição normalmente (pode ser várias linhas).\n"
        "Categorias: escreva 'categorias'")
    update.message.reply_text(texto)

def receber_mensagem(update, context, workbook, sheet):
    msg = update.message.text.strip()
    args = msg.split()
    comando = args[0].lower()
    tipo_grafico = args[1].lower() if len(args) > 1 else None
    if comando == "visualizar":
        registros = get_all_records(sheet)
        texto = "📋 *Registros:*\n"
        for i, row in enumerate(registros, start=1):
            data, desc, valor, tipo, categoria = row
            texto += f"{i}. {data} | {desc} | R$ {valor:.2f} | {tipo} | {categoria}\n"
        update.message.reply_text(texto, parse_mode="Markdown")
    elif comando == "relatorio":
        texto = gerar_relatorio(sheet, tipo_grafico, update)
        update.message.reply_text(texto, parse_mode="Markdown")
    elif comando == "alterar":
        try:
            idx = int(args[1])
            nova_categoria = args[2]
            update_record(workbook, sheet, idx, nova_categoria)
            update.message.reply_text(f"✅ Categoria alterada para {nova_categoria} no registro {idx}.")
        except Exception:
            update.message.reply_text("❌ Use: alterar <número> <nova_categoria>")
    elif comando == "remover":
        try:
            indices = [int(i) for i in args[1:]]
            delete_records(workbook, sheet, indices)
            update.message.reply_text(f"✅ Registros removidos: {', '.join(map(str, indices))}")
        except Exception:
            update.message.reply_text("❌ Use: remover <número(s)> (ex: remover 1 2 3)")
    elif comando == "categorias":
        update.message.reply_text(f"Categorias disponíveis:\n{lista_categorias()}")
    elif comando in ["oi", "olá", "inicio", "start"]:
        boas_vindas(update, context)
    else:
        resposta = processar_linhas(workbook, sheet, msg)
        update.message.reply_text(resposta)
