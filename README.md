# 🤖 Bot de Finanças Pessoais no Telegram

Um bot em **Python + Telegram** para registrar **gastos e ganhos** diretamente do chat, salvar em planilha Excel e gerar relatórios.

---

## 🚀 Funcionalidades

- Registrar **gastos** e **ganhos** automaticamente.
- Reconhecer categorias e subcategorias via palavras-chave.
- Gerar relatórios com resumo financeiro.
- Visualizar registros detalhados.
- Alterar categorias manualmente.
- Remover registros indesejados.

---

## 📂 Estrutura do Projeto

financas_bot/
│── bot.py # Ponto de entrada
│── handlers.py # Tratamento das mensagens
│── services.py # Lógica de negócios
│── storage.py # Persistência em Excel
│── utils.py # Funções auxiliares
│── categorias.json # Lista de categorias e palavras-chave
│── requirements.txt # Dependências
│── README.md # Documentação


---

## ⚙️ Instalação

## 1.1 Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/financas_bot.git
   cd financas_bot

## 1.2 Crie um ambiente virtual e ative:

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

## 1.3 Instale as dependências:

pip install -r requirements.txt

## 1.4 Adicione seu TOKEN do Telegram Bot no arquivo bot.py:

TOKEN = "SEU_TOKEN_AQUI"

## 2.1 Inicie o bot:

python bot.py

## 2.2 No Telegram, envie mensagens como:

Uber 35

Supermercado 250

Recebi salário 5000

## 2.3 Use comandos:

visualizar → Lista registros

relatorio → Mostra resumo financeiro

categorias → Lista categorias e palavras-chave

alterar 2 Alimentação>Restaurante → Alterar categoria

remover 3 4 → Remove registros

## 🧠 Exemplo de Classificação

Mensagem:

Uber 35


Resultado salvo:

✅ Registrado: 35.0 - Gasto - Transporte > Uber

## 🏗️ Tecnologias

Python 3.12

python-telegram-bot

OpenPyXL

## 📊 Demonstração do Relatório
## 📊 Relatório

Ganhos: R$ 5000.00

Gastos por categoria:
- Alimentação > Restaurante: R$ 150.00
- Transporte > Uber: R$ 35.00

## 🤝 Contribuindo

Pull requests são bem-vindos!
Se encontrar bugs ou tiver ideias, abra uma issue.

📜 Licença

MIT License © 2025 - Pedro Lucas Rodrigues
