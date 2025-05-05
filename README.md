# 🌽 Market Agent - Análise de Mercado de Milho e Sementes

Este projeto usa **CrewAI**, **LangChain** e a LLM gratuita **Gemini 2.0 Flash** para realizar uma análise automatizada do mercado de milho e da concorrência em sementes de milho.

## 🧠 Visão Geral

Três agentes com tarefas distintas:

1. **Especialista em Mercado de Milho**: coleta informações atuais sobre tendências, preços e produção.
2. **Analista de Concorrência**: identifica os principais concorrentes no setor de sementes de milho.
3. **Gerador de Relatórios**: resume e formata os dados coletados em um relatório estratégico.

## 🗂️ Estrutura do Projeto

```
market-agent/
├── src/
│   ├── __init__.py
│   ├── agents.py
│   ├── tasks.py
│   └── main.py
├── .env
├── README.md
├── .gitignore
└── venv/
```

## 🚀 Como Rodar o Projeto

### 1. Clone o repositório e entre na pasta

```bash
git clone https://github.com/seu-usuario/market-agent.git
cd market-agent
```

### 2. Crie o ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate    # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

Crie o arquivo `requirements.txt` com:

```
crewai
langchain
google-generativeai
python-dotenv
```

### 4. Configure a chave da API Gemini

- Crie uma conta em https://aistudio.google.com/app/apikey
- Copie a chave e coloque em um arquivo `.env`:

```
GOOGLE_API_KEY=your_gemini_api_key
```

### 5. Execute

```bash
python src/main.py
```

Você verá o relatório final no terminal!

## 📌 Requisitos

- Python 3.9 ou superior
- Internet para acessar a API do Gemini

## 🔮 Ideias Futuras

- Exportar relatório em PDF
- Deploy com interface web (Streamlit)
- Agendamentos automáticos

---

Feito com ❤️ para análises inteligentes no agro.