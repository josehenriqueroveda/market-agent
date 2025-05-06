import agents
from datetime import date
from crewai import Task


search = Task(
    description=f"""
            1. Pesquisar e coletar informações relevantes sobre o mercado de grãos e sementes, incluindo preços, tendências e previsões para o ano de {date.today().year}.\n
            2. Identificar o cenário competitivo, perspectivas futuras e mapeamento de oportunidades/ameaças.\n
            3. Identificar os movimentos acionáveis.\n
            4. Utilizar fontes confiáveis e atualizadas, como notícias, relatórios de mercado e dados de preços. \n
            5. Certificar-se de que as informações coletadas sejam relevantes e úteis para o usuário. \n
            6. Fornecer uma análise de mercado completa e totalmente modular que inclua uma visão geral do mercado de grãos e sementes brasileiro e global, cenário competitivo, segmentação de público, mapeamento de oportunidades/ameaças e estratégias acionáveis.\n
            7. Certificar-se de que todas as descobertas sejam verificadas pela Internet.\n
            8. Fornecer uma narrativa estratégica sólida que identifique as maiores oportunidades do usuário e as vantagens do primeiro movimento.\n
            9. Realizar previsões de mercado e identificar oportunidades de negócios.\n
            10. Interpretação crítica dos negócios: Vá além dos relatórios, interprete o que os dados e o cenário competitivo implicam para a ação do usuário.\n
    """,
    agent=agents.searcher,
    expected_output=f"""
            Os resultados da pesquisa devem incluir os seguintes tópicos:\n
            1. Resumo executivo:\n
            - Objetivo: o Resumo Executivo fornece uma síntese de alto nível de todo o relatório de mercado, destacando as principais conclusões e oportunidades imediatas. Ele define o tom para os tomadores de decisão e garante que eles entendam os insights mais importantes em um piscar de olhos.\n
            - Visão geral curta (3 a 5 frases) que resume as descobertas e as maiores oportunidades identificadas.\n
            - Inclua uma breve recomendação para as “primeiras ações” com base na análise.\n
            2. Visão geral do setor:\n
            - Objetivo: Compreender o cenário atual do mercado de grãos e sementes, descrevendo as principais tendências e trajetórias futuras, fundamentais para o planejamento estratégico.\n
            - Tendências atuais:\n
            -- Principais tendências que estão moldando o mercado de grãos e sementes, como mudanças climáticas, inovações tecnológicas, regulamentações governamentais e mudanças nas preferências dos consumidores.\n
            -- Como essas tendências estão impactando a produção, distribuição e consumo de grãos e sementes.\n
            - Previsões de crescimento:\n
            -- Previsões de crescimento do mercado de grãos e sementes para o ano de {date.today().year}.\n
            -- Como essas previsões podem influenciar na produção, distribuição e consumo.\n
            -- Cenário competitivo:\n
            -- Principais players do mercado de grãos e sementes, incluindo empresas líderes, novos entrantes e startups.\n
            - Perspectivas futuras:\n
            -- O que esperar do mercado de grãos e sementes nos próximos anos, incluindo tendências emergentes e oportunidades de crescimento.\n
            3. Oportunidades de mercado e ameaças:\n
            - Objetivo: Identificar oportunidades e ameaças no mercado de grãos e sementes, ajudando os tomadores de decisão a entender onde concentrar seus esforços.\n
            - Fornecer suporte estratégico para os negócios, com visão de futuro baseada na realidade, não na esperança.\n
            - Oportunidades de mercado:\n
            -- Principais oportunidades de crescimento no mercado de grãos e sementes, incluindo novas tendências, novos players e novos produtos.\n
            - Ameaças no mercado:\n
            -- Principais ameaças no mercado de grãos e sementes, incluindo baixas na produção, baixas na distribuição e baixas no consumo.\n
            6. Movimentos acionáveis:\n
            - Objetivo: transformar os insights em decisões comerciais táticas e imediatas. Proporcionar uma ponte direta entre a pesquisa e a implementação, oferecendo ao usuário estratégias específicas baseadas nas descobertas.\n
            - 3 a5 Recomendações estratégicas:
            * Cada uma delas escrita claramente como uma ação (por exemplo, “Desenvolva o recurso X visando o público Y”).
            - Evidências de apoio:
            * Associe cada recomendação a descobertas específicas de sua pesquisa.
            - Priorização:
            * Observe quais ações são “vitórias rápidas” de alta prioridade versus ações de longo prazo.
    """,
)

write = Task(
    description="""
            1. A partir dos dados coletados pelo Especialista em pesquisa de mercado de grãos, criar um relatório claro, objetivo e estratégico.\n
            2. Garantir que o conteúdo do relatório seja informativo, preciso e bem escrito, utilizando os dados gerados pelo Especialista em pesquisa de mercado de grãos como referência.\n
            3. Utilizar o idioma português brasileiro e garantir que o conteúdo esteja bem escrito.\n
            4. Montar o relatório de forma modular, com os seguintes tópicos:\n
            - Resumo executivo.\n
            - Visão geral do setor.\n
            - Oportunidades de mercado e ameaças.\n
            - Movimentos acionáveis.\n
            5. Garantir que o relatório tenha ZERO alucinações, todas as informações devem ser reais, verificadas e atualizadas.\n
            6. Utilizar uma linguagem clara e incisiva. Evite divagações acadêmicas ou jargões excessivos.\n
    """,
    agent=agents.writer,
    expected_output="""
            1. Um relatório markdown profissional com os dados mais recentes e relevantes do mercado de grãos do Brasil e do mundo\n
            2. Modularidade rigorosa: Cada seção deve ser estruturada de forma independente e ser fácil para os usuários reutilizarem ou se aprofundarem conforme necessário.\n
            3. Estrutura do relatório:\n
            - Resumo executivo.\n
            - Visão geral do setor.\n
            - Oportunidades de mercado e ameaças.\n
            - Movimentos acionáveis.\n
            4. Texto no formato Markdown, com formatação adequada para cada seção do relatório.\n
            5. Sem alucinações: Nenhuma estatística, alegação ou detalhe inventado. Cada insight deve ser fundamentado em uma fonte real e atualizada.\n
            6. Redação abrangente, mas pronta para os negócios: Linguagem clara e incisiva. Evite divagações acadêmicas e, ao mesmo tempo, ofereça uma cobertura completa e estratégica.\n
    """,
)
