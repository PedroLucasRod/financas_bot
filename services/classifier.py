# services/classifier.py
import re
import unicodedata
import json
from config import CATEGORIAS_FILE


with open(CATEGORIAS_FILE, "r", encoding="utf-8") as f:
    categorias_dict = json.load(f)


def normalizar(texto: str) -> str:
    """
    Remove acentos, deixa minúsculo e converte para ASCII.
    Ex.: 'Farmácia' -> 'farmacia'
    """
    return (
        unicodedata.normalize("NFKD", texto)
        .encode("ASCII", "ignore")
        .decode("ASCII")
        .lower()
    )


def classificar_mensagem(mensagem):
    """
    Retorna: valor (float), tipo ("Gasto"/"Ganho"), categoria, subcategoria.
    Usa o dicionário categorias_dict (Gastos / Ganhos) do categorias.json.
    """
    mensagem_norm = normalizar(mensagem)

    valor = None
    tipo = None
    categoria = None
    subcategoria = None

    # 1) Extrair valor numérico (ex: 10, 10,50, 79,29)
    encontrado = re.search(r"(\d+(?:,\d{1,2})?)", mensagem_norm)
    if encontrado:
        valor = float(encontrado.group(1).replace(",", "."))

    # 2) Tentar classificar como Gasto primeiro
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

    # 3) Se não encontrou categoria de Gasto, tenta Ganho
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
    """
    Gera uma listagem amigável de categorias e subcategorias,
    baseada na estrutura do categorias.json.
    """
    linhas = []

    # Gastos
    gastos = categorias_dict.get("Gastos", {})
    if gastos:
        linhas.append("📉 *Categorias de Gastos*")
        for cat, subs in gastos.items():
            linhas.append(f"\n• {cat}")
            for subcat in subs.keys():
                linhas.append(f"   └ {subcat}")

    # Ganhos
    ganhos = categorias_dict.get("Ganhos", {})
    if ganhos:
        linhas.append("\n💰 *Categorias de Ganhos*")
        for subcat in ganhos
