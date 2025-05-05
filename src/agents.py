import os
from dotenv import load_dotenv
from crewai import Agent, LLM
from datetime import date

from tools.search import news_tool

load_dotenv()

llm = LLM(api_key=os.environ["GEMINI_API_KEY"], model=os.environ["GEMINI_MODEL"])

searcher = Agent(
    role="Especialista em pesquisa de mercado de milho",
    goal=f"Buscar informações recentes e relevantes sobre o mercado de milho no Brasil e no mundo. A data de hoje é {date.today()}.",
    backstory="""
            Você é especialista em agronegócio com foco em tendências de mercado agrícola de sementes e de milho.
            Você vai conduzir busca online de notícias recentes sobre milho e sementes, coletar e agrupar as informações.
            Seu trabalho servirá de base para o Escritor de Relatório.
    """,
    llm=llm,
    verbose=True,
    allow_delegation=False,
    tools=[news_tool],
)

writer = Agent(
    role="Redator de relatório de inteligência de mercado",
    goal="Gerar um relatório claro, objetivo e estratégico com base nos dados fornecidos de mercado de milho e sementes",
    backstory="""
    Você é um profissional de comunicação com experiência em agronegócio.
    Sua tarefa é criar um relatório das principais e mais recentes notícias do mercado de milho e sementes brasileiro e global,
    utilizando os dados gerados pelo Especialista em pesquisa de mercado de milho como referência.
    O conteúdo do relatório deve ser informativo, preciso e bem escrito.
    """,
    tools=[news_tool],
    llm=llm,
    verbose=True,
)
