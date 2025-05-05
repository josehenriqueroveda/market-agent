from datetime import date
from crew import crew


def save_report(report_body):
    with open(f"report-{date.today()}.md", "w", encoding="utf-8") as file:
        file.write(report_body)
        return report_body


if __name__ == "__main__":
    result = crew.kickoff()
    save_report(result.raw)
