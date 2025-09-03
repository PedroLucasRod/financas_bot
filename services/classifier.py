# services/classifier.py
import re
import unicodedata
import json
from config import CATEGORIAS_FILE

with open(CATEGORIAS_FILE, "r", encoding="utf-8") as f:
    categorias_dict = json.load(f)

def normalizar(texto):
    return unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII').lower()

def classificar_mensagem(mensagem):
    mensagem_norm = normalizar(mensagem)
    valor = None
    tipo = None
    categoria = None
    subcategoria = None
    encontrado = re.search(r"(\d+(?:,\d{2})?)", mensagem_norm)
    if encontrado:
        valor = float(encontrado.group(1).replace(",", "."))
    for cat, subs in categorias_dict.get("Gastos", {}).items():
        for subcat, palavras in subs.items():
            for palavra in palavras:
                palavra_norm = normalizar(palavra)
                if re.search(rf"\b{re.escape(palavra_norm)}\b", mensagem_norm):
                    categoria = cat
                    subcategoria = subcat
                    tipo = "Gasto"
                    break
            if categoria:
                break
        if categoria:
            break
    if not categoria:
        for subcat, palavras in categorias_dict.get("Ganhos", {}).items():
            for palavra in palavras:
                palavra_norm = normalizar(palavra)
                if re.search(rf"\b{re.escape(palavra_norm)}\b", mensagem_norm):
                    categoria = "Ganhos"
                    subcategoria = subcat
                    tipo = "Ganho"
                    break
            if categoria == "Ganhos":
                break
    return valor, tipo, categoria, subcategoria

def lista_categorias():
    texto = ""
    for cat, palavras in categorias_dict.items():
        texto += f"- {cat}: {', '.join(palavras)}\n"
    return texto
