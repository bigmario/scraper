class ResultDataModel:
    def __init__(self, title, company, location, link):
        self.title = title.text.strip()
        self.company = company.text.strip()
        self.location = location.text.strip()
        self.link = link[1]["href"]

    def scraping_result(self):
        result = {
            "title": self.title,
            "company": self.company,
            "location": self.location,
            "link": self.link,
        }
        return result
