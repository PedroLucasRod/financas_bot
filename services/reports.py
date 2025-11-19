# services/reports.py
# services/reports.py

import matplotlib
matplotlib.use('Agg')  # ⚠️ IMPORTANTE: Usar backend sem interface gráfica
import matplotlib.pyplot as plt
from io import BytesIO
from services.storage import sheet
import logging

def gerar_relatorio(tipo_grafico=None, update=None):
    try:
        logging.info("🔍 Iniciando geração de relatório...")
        
        dados = sheet.get_all_values()[1:]  # ignora cabeçalho
        
        if not dados:
            return "📋 Nenhum registro encontrado para gerar relatório."
        
        gastos = {}
        ganhos = 0
        total_gastos = 0
        
        for row in dados:
            try:
                data, desc, valor_str, tipo, categoria = row
                
                # Remove vírgulas e espaços, converte para float
                valor_str = valor_str.replace(',', '.').replace(' ', '')
                valor = float(valor_str)
                
                if tipo == "Gasto":
                    gastos[categoria] = gastos.get(categoria, 0) + valor
                    total_gastos += valor
                elif tipo == "Ganho":
                    ganhos += valor
                    
            except (ValueError, IndexError) as e:
                logging.warning(f"⚠️ Linha ignorada (erro de formato): {row} - {e}")
                continue
        
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
            
            # Gera gráfico se solicitado
            if update and tipo_grafico in ["pizza", "barra"]:
                try:
                    fig, ax = plt.subplots(figsize=(7, 5))
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
                    logging.info(f"✅ Gráfico {tipo_grafico} enviado com sucesso")
                    
                except Exception as graph_error:
                    logging.error(f"❌ Erro ao gerar gráfico: {graph_error}")
                    texto += "\n⚠️ Não foi possível gerar o gráfico."
        else:
            texto += "Nenhum gasto registrado ainda ✅"
        
        logging.info("✅ Relatório gerado com sucesso")
        return texto
        
    except Exception as e:
        logging.error(f"❌ Erro ao gerar relatório: {e}")
        return f"❌ Erro ao gerar relatório: {str(e)}"
