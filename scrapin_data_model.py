class ResultDataModel:
    def __init__(self, title, company, location, link):
        self.title = title.text.strip()
        self.company = company.text.strip()
        self.location = location.text.strip()
        self.link = link[1]["href"]

    def print_scraping_result(self):
        print(self.title)
        print(self.company)
        print(self.location)
        print(self.link)
        print("\n")
