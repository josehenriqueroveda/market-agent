from crewai import Crew, Process
from agents import searcher, writer
from tasks import search, write

crew = Crew(
    agents=[searcher, writer],
    tasks=[search, write],
    verbose=1,
    process=Process.sequential,
)
