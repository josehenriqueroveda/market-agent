# 🌽 Market Agent - Análise de Mercado de Grãos e Sementes

Este projeto usa **CrewAI**, **LangChain** e a LLM gratuita **Gemini 2.0 Flash** para realizar uma análise automatizada do mercado de grãos e de sementes.

## 🧠 Visão Geral

Dois agentes com tarefas distintas:

1. **Especialista em Mercado de Grãos**: coleta informações atuais sobre tendências, preços e produção.
2. **Gerador de Relatórios**: resume e formata os dados coletados em um relatório estratégico.

#### O relatório é gerado de forma modular, com os seguintes tópicos:

- Preços
- Mercado Brasil
- Mercado Global
- Tendências e Previsões

## 🗂️ Estrutura do Projeto

```
.
└── market-agent/
    ├── src/
    │   ├── __init__.py
    │   ├── agents.py
    │   ├── crew.py
    │   ├── main.py
    │   ├── tasks.py
    │   └── tools/
    │       ├── __init__.py
    │       └── search.py
    ├── README.md
    ├── .env
    ├── .gitignore
    ├── LICENSE
    ├── requirements.txt
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

### 4. Configure a chave da API Gemini

- Crie uma conta em https://aistudio.google.com/app/apikey
- Copie a chave e coloque em um arquivo `.env`:

```
GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL=choose_your_gemini_model
```

### 5. Execute

```bash
python src/main.py
```

Você verá o relatório final salvo na pasta raiz do projeto, como `report-yyyy-mm-dd.md`!

## 📌 Requisitos

- Python 3.10 ou superior
- Internet para acessar a API do Gemini

## 🔮 Ideias Futuras

- Exportar relatório em PDF
- Deploy com interface web (Streamlit)
- Agendamentos automáticos

---

### Gostou? Dê uma ⭐ no projeto.
