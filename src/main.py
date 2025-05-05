from crewai.flow.flow import Flow, start, listen
from datetime import date
from litellm import completion
import os
from dotenv import load_dotenv

load_dotenv()


class MarketFlow(Flow):

    @start()
    def researcher(self):
        response = completion(
            api_key=os.getenv("GOOGLE_GEMINI_KEY"),
            model=os.getenv("GEMINI_MODEL"),
            messages=[
                {
                    "content": f"Buscar informações recentes e relevantes sobre o mercado de milho no Brasil e no mundo. Data de hoje: {date.today()}",
                    "role": "user",
                }
            ],
        )
        research_result = response["choices"][0]["message"]["content"]
        return research_result

    @listen("researcher")
    def writer(self, research_result):
        response = completion(
            api_key=os.getenv("GOOGLE_GEMINI_KEY"),
            model=os.getenv("GEMINI_MODEL"),
            messages=[
                {
                    "content": f"""A partir do conteúdo recebido, gere um relatório de análise de mercado, usando a formatação em HTML.\n 
                    Utilize apenas o conteúdo recebido e não acrescente nenhum conteúdo técnico a respeito do código, ou opinião própria,
                    mantendo o texto do relatório íntegro e relacionado apenas ao seu tema principal que é mercado de milho.
                    Ele deve conter apenas as seguintes sessões e nada além disso:\n
                    Título: 'Análise do Mercado de Milho - {date.today()}'\n
                    1. Cenário no Brasil\n
                    2. Cenário Global\n
                    3. Previsões de Mercado\n
                    \nConteúdo para utilizar no relatório: \n{research_result}""",
                    "role": "user",
                }
            ],
        )
        report_body = response["choices"][0]["message"]["content"]
        self.state["report_body"] = report_body

    @listen("writer")
    def save_report(self):
        with open(f"report-{date.today()}.html", "w", encoding="utf-8") as file:
            file.write(self.state["report_body"])
            return self.state["report_body"]


def kickoff():
    obj = MarketFlow()
    obj.kickoff()


if __name__ == "__main__":
    kickoff()
