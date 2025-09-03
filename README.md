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
   git clone https://github.com/PedroLucasRod/financas_bot.git
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

🤖 Personal Finance Bot on Telegram
A Python + Telegram bot to record expenses and income directly from chat, save to Excel spreadsheet, and generate reports.

🚀 Features
Automatically record expenses and income.

Recognize categories and subcategories via keywords.

Generate financial summary reports.

View detailed transaction records.

Manually edit categories.

Remove unwanted records.

📂 Project Structure
text
financas_bot/
│── bot.py              # Entry point
│── handlers.py         # Message handling
│── services.py         # Business logic
│── storage.py          # Excel persistence
│── utils.py            # Helper functions
│── categorias.json     # Categories & keywords list
│── requirements.txt    # Dependencies
│── README.md           # Documentation
⚙️ Installation
Clone the repository:

text
git clone https://github.com/PedroLucasRod/financas_bot.git
cd financas_bot
Create and activate a virtual environment:

text
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
Install dependencies:

text
pip install -r requirements.txt
Add your Telegram Bot TOKEN in config.py or use environment variable.

▶️ How to run
Start the bot:

text
python bot.py
Send messages on Telegram:

Uber 35

Supermarket 250

Received salary 5000

Use commands:

visualizar → list all records

relatorio → show financial summary

categorias → list categories and keywords

alterar 2 Food>Restaurant → change category

remover 3 4 → delete records

🧠 Example Classification
Message:

text
Uber 35
Saved Result:

text
✅ Recorded: 35.0 - Expense - Transport > Uber
🏗️ Technologies Used
Python 3.12

python-telegram-bot

OpenPyXL

Matplotlib

📊 Sample Report
text
Income: R$ 5000.00  
Expenses by category:  
- Food > Restaurant: R$ 150.00  
- Transport > Uber: R$ 35.00
🤝 Contributing
Pull requests are welcome!
If you find bugs or have ideas, please open an issue.

📜 License
MIT License © 2025 - Pedro Lucas Rodrigues
