import agents
from datetime import date
from crewai import Task


search = Task(
    description=f"""
            Tendo como base a data de hoje, {date.today()}, você deve:\n
            1. Priorizar as notícias mais recentes e relevantes do mercado de milho do Brasil e do mundo.
            2. Destacar tendências, preço e informações de produção de milho e sementes.
            3. Incluir notícias recentes de empresas produtoras de sementes de milho.
    """,
    agent=agents.searcher,
    expected_output="Dados de preços e tópicos atualizados retirados de notícias sobre o mercado de milho, sementes de milho e empresas do setor.",
)

write = Task(
    description="""
            1. Elaborar um relatório profissional sobre as notícias mais recentes e relevantes do mercado de milho do Brasil e do mundo.
            2. Separar o relatório nos seguintes tópicos: Preços, Mercado Brasil, Mercado Global e Tendências.
            3. Estruturar o relatório deixando-o pronto para o usuario leitor final.
    """,
    agent=agents.writer,
    expected_output="Um relatório sumarizado com os tópicos e insights estratégicos de posicionamento no mercado.",
)
