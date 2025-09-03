# services/reports.py
import matplotlib.pyplot as plt
from io import BytesIO

def gerar_relatorio(sheet, tipo_grafico=None, update=None):
    gastos = {}
    ganhos = 0
    total_gastos = 0
    for row in sheet.iter_rows(min_row=2, values_only=True):
        data, desc, valor, tipo, categoria = row
        if tipo == "Gasto":
            gastos[categoria] = gastos.get(categoria, 0) + valor
            total_gastos += valor
        elif tipo == "Ganho":
            ganhos += valor
    saldo = ganhos - total_gastos
    texto = "📊 *Relatório Financeiro*\n\n"
    texto += f"💰 *Ganhos:* R$ {ganhos:.2f}\n"
    texto += f"💸 *Gastos:* R$ {total_gastos:.2f}\n"
    texto += f"⚖️ *Saldo:* {'🟢' if saldo >= 0 else '🔴'} R$ {saldo:.2f}\n\n"
    if gastos:
        texto += "*📂 Gastos por categoria:*\n"
        for cat, total in sorted(gastos.items(), key=lambda x: x[1], reverse=True):
            porcent = (total / total_gastos * 100) if total_gastos > 0 else 0
            barra = "█" * int(porcent // 5)
            texto += f"- {cat}: R$ {total:.2f} ({porcent:.1f}%) {barra}\n"
        if update and tipo_grafico in ["pizza", "barra"]:
            fig, ax = plt.subplots(figsize=(7,5))
            categorias = list(gastos.keys())
            valores = list(gastos.values())
            if tipo_grafico == "barra":
                ax.bar(categorias, valores)
                ax.set_title("Gastos por Categoria", fontsize=14)
                ax.set_ylabel("Valor (R$)")
                ax.set_xlabel("Categorias")
                plt.xticks(rotation=30, ha="right")
            elif tipo_grafico == "pizza":
                ax.pie(valores, labels=categorias, autopct='%1.1f%%', startangle=140)
                ax.set_title("Distribuição de Gastos", fontsize=14)
            buf = BytesIO()
            plt.savefig(buf, format="png", bbox_inches="tight")
            buf.seek(0)
            plt.close(fig)
            update.message.reply_photo(photo=buf)
    else:
        texto += "Nenhum gasto registrado ainda ✅"
    return texto
