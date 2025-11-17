
# 🤖 Personal Finance Bot (Web + Telegram)

A modern solution to track your **expenses and income** via Telegram *and* a web dashboard — all built with Python. Data is securely saved and always accessible through automated reports.

**Live App:** [https://financas-bot.onrender.com](https://financas-bot.onrender.com/)

---

## ✨ Features

* Register expenses or income instantly (Telegram or Web)
* Smart category and subcategory recognition
* Detailed records and friendly summaries
* Manual category adjustment and deletion
* Data stored in Excel files for easy export
* Fast, lightweight interface

---

## 🖥️ Project Access

* **Telegram Bot:** Use Telegram to chat with your bot and quickly record new transactions.
* **Web Dashboard:** View, filter, and manage your finances anytime at
  [https://financas-bot.onrender.com](https://financas-bot.onrender.com/)

---

## 🚀 Quickstart

1. **Clone the repository (if you want local setup):**
   <pre class="not-prose w-full rounded font-mono text-sm font-extralight"><div class="codeWrapper text-light selection:text-super selection:bg-super/10 my-md relative flex flex-col rounded-lg font-mono text-sm font-normal bg-subtler"><div class="translate-y-xs -translate-x-xs bottom-xl mb-xl flex h-0 items-start justify-end md:sticky md:top-[calc(var(--header-height)+var(--size-xs))]"><div class="overflow-hidden rounded-full border-subtlest ring-subtlest divide-subtlest bg-base"><div class="border-subtlest ring-subtlest divide-subtlest bg-subtler"></div></div></div><div class="-mt-xl"><div><div data-testid="code-language-indicator" class="text-quiet bg-subtle py-xs px-sm inline-block rounded-br rounded-tl-lg text-xs font-thin">bash</div></div><div><span><code><span><span class="token token">git</span><span> clone https://github.com/PedroLucasRod/financas_bot.git
   </span></span><span><span></span><span class="token token">cd</span><span> financas_bot
   </span></span><span></span></code></span></div></div></div></pre>
2. **Install dependencies:**
   <pre class="not-prose w-full rounded font-mono text-sm font-extralight"><div class="codeWrapper text-light selection:text-super selection:bg-super/10 my-md relative flex flex-col rounded-lg font-mono text-sm font-normal bg-subtler"><div class="translate-y-xs -translate-x-xs bottom-xl mb-xl flex h-0 items-start justify-end md:sticky md:top-[calc(var(--header-height)+var(--size-xs))]"><div class="overflow-hidden rounded-full border-subtlest ring-subtlest divide-subtlest bg-base"><div class="border-subtlest ring-subtlest divide-subtlest bg-subtler"></div></div></div><div class="-mt-xl"><div><div data-testid="code-language-indicator" class="text-quiet bg-subtle py-xs px-sm inline-block rounded-br rounded-tl-lg text-xs font-thin">bash</div></div><div><span><code><span><span>pip </span><span class="token token">install</span><span> -r requirements.txt
   </span></span><span></span></code></span></div></div></div></pre>
3. **Set your Telegram Bot token in `bot.py`:**
   <pre class="not-prose w-full rounded font-mono text-sm font-extralight"><div class="codeWrapper text-light selection:text-super selection:bg-super/10 my-md relative flex flex-col rounded-lg font-mono text-sm font-normal bg-subtler"><div class="translate-y-xs -translate-x-xs bottom-xl mb-xl flex h-0 items-start justify-end md:sticky md:top-[calc(var(--header-height)+var(--size-xs))]"><div class="overflow-hidden rounded-full border-subtlest ring-subtlest divide-subtlest bg-base"><div class="border-subtlest ring-subtlest divide-subtlest bg-subtler"></div></div></div><div class="-mt-xl"><div><div data-testid="code-language-indicator" class="text-quiet bg-subtle py-xs px-sm inline-block rounded-br rounded-tl-lg text-xs font-thin">python</div></div><div><span><code><span><span>TOKEN </span><span class="token token operator">=</span><span></span><span class="token token">"YOUR_TELEGRAM_BOT_TOKEN"</span><span>
   </span></span><span></span></code></span></div></div></div></pre>
4. **Run locally:**
   <pre class="not-prose w-full rounded font-mono text-sm font-extralight"><div class="codeWrapper text-light selection:text-super selection:bg-super/10 my-md relative flex flex-col rounded-lg font-mono text-sm font-normal bg-subtler"><div class="translate-y-xs -translate-x-xs bottom-xl mb-xl flex h-0 items-start justify-end md:sticky md:top-[calc(var(--header-height)+var(--size-xs))]"><div class="overflow-hidden rounded-full border-subtlest ring-subtlest divide-subtlest bg-base"><div class="border-subtlest ring-subtlest divide-subtlest bg-subtler"></div></div></div><div class="-mt-xl"><div><div data-testid="code-language-indicator" class="text-quiet bg-subtle py-xs px-sm inline-block rounded-br rounded-tl-lg text-xs font-thin">bash</div></div><div><span><code><span><span>python bot.py
   </span></span><span></span></code></span></div></div></div></pre>

Or, simply try the live demo at [https://financas-bot.onrender.com](https://financas-bot.onrender.com/).

---

## 💬 How to Use

* **In Telegram:**
  * Send a message like `Uber 35` or `Supermercado 250`
  * Receive instant confirmation and summary
  * Use commands for more control:
    * `visualizar` → List records
    * `relatorio` → See a financial overview
    * `categorias` → Show categories
    * `alterar 2 Alimentação>Restaurante` → Change a record's category
    * `remover 3 4` → Remove records
* **On the Web:**
  * Register, view, and manage all your finances through an intuitive dashboard.

---

## 💡 Example

* **Message sent:**
  `Uber 35`
* **Saved as:**
  ✔️ 35.00 - Expense: Transport > Uber

---

## 🛠️ Tech Highlights

* Python 3.12, FastAPI or Flask
* python-telegram-bot
* OpenPyXL for Excel integration
* Render.com for cloud hosting
* Simple, maintainable codebase

---

## 🤝 Contributing

Pull requests are very welcome!
Found a bug or have new ideas? Open an issue.

---

## 📜 License

MIT License © 2025 - Pedro Lucas Rodrigues

---

---

# 🤖 Bot de Finanças Pessoais (Web + Telegram)

Uma solução moderna para gerenciar **gastos e ganhos** via Telegram *e* um painel web — tudo feito em Python. Seus dados ficam salvos, prontos para relatórios automáticos e acesso seguro a qualquer momento.

**App Online:** [https://financas-bot.onrender.com](https://financas-bot.onrender.com/)

---

## ✨ Funcionalidades

* Registrar gastos e ganhos pelo Telegram ou Web
* Reconhecimento automático de categorias/subcategorias
* Relatórios e extratos detalhados
* Permite alterar ou apagar registros manualmente
* Dados exportáveis em Excel
* Interface leve, rápida e fácil de usar

---

## 🖥️ Como acessar

* **Bot no Telegram:**
  Use o Telegram para cadastrar transações rapidinho com mensagens simples.
* **Painel Web:**
  Gerencie suas finanças sempre que quiser pelo painel em
  [https://financas-bot.onrender.com](https://financas-bot.onrender.com/)

---

## 🚀 Para começar

1. **Clone o repositório (para uso local):**
   <pre class="not-prose w-full rounded font-mono text-sm font-extralight"><div class="codeWrapper text-light selection:text-super selection:bg-super/10 my-md relative flex flex-col rounded-lg font-mono text-sm font-normal bg-subtler"><div class="translate-y-xs -translate-x-xs bottom-xl mb-xl flex h-0 items-start justify-end md:sticky md:top-[calc(var(--header-height)+var(--size-xs))]"><div class="overflow-hidden rounded-full border-subtlest ring-subtlest divide-subtlest bg-base"><div class="border-subtlest ring-subtlest divide-subtlest bg-subtler"></div></div></div><div class="-mt-xl"><div><div data-testid="code-language-indicator" class="text-quiet bg-subtle py-xs px-sm inline-block rounded-br rounded-tl-lg text-xs font-thin">bash</div></div><div><span><code><span><span class="token token">git</span><span> clone https://github.com/PedroLucasRod/financas_bot.git
   </span></span><span><span></span><span class="token token">cd</span><span> financas_bot
   </span></span><span></span></code></span></div></div></div></pre>
2. **Instale as dependências:**
   <pre class="not-prose w-full rounded font-mono text-sm font-extralight"><div class="codeWrapper text-light selection:text-super selection:bg-super/10 my-md relative flex flex-col rounded-lg font-mono text-sm font-normal bg-subtler"><div class="translate-y-xs -translate-x-xs bottom-xl mb-xl flex h-0 items-start justify-end md:sticky md:top-[calc(var(--header-height)+var(--size-xs))]"><div class="overflow-hidden rounded-full border-subtlest ring-subtlest divide-subtlest bg-base"><div class="border-subtlest ring-subtlest divide-subtlest bg-subtler"></div></div></div><div class="-mt-xl"><div><div data-testid="code-language-indicator" class="text-quiet bg-subtle py-xs px-sm inline-block rounded-br rounded-tl-lg text-xs font-thin">bash</div></div><div><span><code><span><span>pip </span><span class="token token">install</span><span> -r requirements.txt
   </span></span><span></span></code></span></div></div></div></pre>
3. **Coloque seu token do Bot Telegram no `bot.py`:**
   <pre class="not-prose w-full rounded font-mono text-sm font-extralight"><div class="codeWrapper text-light selection:text-super selection:bg-super/10 my-md relative flex flex-col rounded-lg font-mono text-sm font-normal bg-subtler"><div class="translate-y-xs -translate-x-xs bottom-xl mb-xl flex h-0 items-start justify-end md:sticky md:top-[calc(var(--header-height)+var(--size-xs))]"><div class="overflow-hidden rounded-full border-subtlest ring-subtlest divide-subtlest bg-base"><div class="border-subtlest ring-subtlest divide-subtlest bg-subtler"></div></div></div><div class="-mt-xl"><div><div data-testid="code-language-indicator" class="text-quiet bg-subtle py-xs px-sm inline-block rounded-br rounded-tl-lg text-xs font-thin">python</div></div><div><span><code><span><span>TOKEN </span><span class="token token operator">=</span><span></span><span class="token token">"SEU_TOKEN_AQUI"</span><span>
   </span></span><span></span></code></span></div></div></div></pre>
4. **Rode o bot localmente:**
   <pre class="not-prose w-full rounded font-mono text-sm font-extralight"><div class="codeWrapper text-light selection:text-super selection:bg-super/10 my-md relative flex flex-col rounded-lg font-mono text-sm font-normal bg-subtler"><div class="translate-y-xs -translate-x-xs bottom-xl mb-xl flex h-0 items-start justify-end md:sticky md:top-[calc(var(--header-height)+var(--size-xs))]"><div class="overflow-hidden rounded-full border-subtlest ring-subtlest divide-subtlest bg-base"><div class="border-subtlest ring-subtlest divide-subtlest bg-subtler"></div></div></div><div class="-mt-xl"><div><div data-testid="code-language-indicator" class="text-quiet bg-subtle py-xs px-sm inline-block rounded-br rounded-tl-lg text-xs font-thin">bash</div></div><div><span><code><span><span>python bot.py
   </span></span><span></span></code></span></div></div></div></pre>

Ou apenas acesse a versão online em [https://financas-bot.onrender.com](https://financas-bot.onrender.com/).

---

## 💬 Como usar

* **No Telegram:**
  * Mande mensagens, exemplo: `Uber 35`, `Supermercado 250`
  * Veja confirmação instantânea e resumo
  * Use comandos:
    * `visualizar` → Listar lançamentos
    * `relatorio` → Resumo financeiro
    * `categorias` → Ver categorias
    * `alterar 2 Alimentação>Restaurante` → Alterar categoria
    * `remover 3 4` → Apagar registros
* **No site:**
  * Cadastre, consulte e edite todas as transações pelo painel moderno e intuitivo

---

## 💡 Exemplo

* **Mensagem enviada:**
  `Uber 35`
* **Registro salvo:**
  ✔️ 35,00 - Gasto: Transporte > Uber

---

## 🛠️ Tecnologias

* Python 3.12, FastAPI ou Flask
* python-telegram-bot
* OpenPyXL (Excel)
* Hospedagem cloud na Render.com
* Código enxuto e fácil de manter

---

## 🤝 Contribua

Pull requests são bem-vindos!
Sugestões ou bugs? Só abrir uma issue.

---

## 📜 Licença

MIT License © 2025 - Pedro Lucas Rodrigues

---
