import requests
from pprint import pprint
from bs4 import BeautifulSoup

from scrapin_data_model import ResultDataModel


URL = "https://realpython.github.io/fake-jobs/"


def _get_data(elements):
    result = []
    for item in elements:
        result.append(
            ResultDataModel(
                title=item.find("h2", class_="title"),
                company=item.find("h3", class_="company"),
                location=item.find("p", class_="location"),
                link=item.find_all("a", class_="card-footer-item"),
            )
        )
    for item in result:
        item.print_scraping_result()


def _scrape(url, session):
    page = session.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("div", attrs={"id": "ResultsContainer"})
    job_elemants = results.find_all("div", attrs={"class": "card-content"})

    python_jobs = results.find_all("h2", string=lambda text: "python" in text.lower())

    python_jobs_elements = [
        h2_element.parent.parent.parent for h2_element in python_jobs
    ]

    print("***ALL JOBS***", end="\n")
    _get_data(job_elemants)

    print("***PYTHON JOBS***", end="\n")
    _get_data(python_jobs_elements)


def main():
    try:
        with requests.Session() as session:
            _scrape(URL, session)
    except Exception as error:
        print(f"An Error occurred: {error}")


if __name__ == "__main__":
    main()
