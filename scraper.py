import requests
from bs4 import BeautifulSoup

class WebSite:

    def __init__(self, url, search_url, result_list,
                 linkjob, absolute_url, title, company, salary):
        self.url = url
        self.search_url = search_url
        self.result_list = result_list
        self.linkjob = linkjob
        self.absolute_url = absolute_url
        self.title = title
        self.company = company
        self.salary = salary

class Content:
    def __init__(self, title, company, linkjob, salary):
        self.title = title
        self.company = company
        self.linkjob = linkjob
        self.salary = salary

    def dict(self):
        dict = {"Title":self.title,
                "Company":self.company,
                "Link":self.linkjob,
                "Salary":self.salary
        }
        return dict

class Search:

    def __init__(self, keyword, location):
        self.keyword = keyword
        self.location = location

    def get(self, website):
        try:
            req = requests.get(
            website.search_url.format(self.keyword, self.location))
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(req.text, "html.parser")


    def safeget(self, pageObj, selector):
        childObj = pageObj.select(selector)
        if childObj is not None and len(childObj) > 0:
            return childObj[0].get_text().replace("\n", "")
        else:
            return "NA"

    def parse(self, website):
        titles = []
        companies = []
        links = []
        salaries = []

        soup = self.get(website)
        results = soup.select(website.result_list)
        for div in results:
            titles.append(self.safeget(div, website.title))
            companies.append(self.safeget(div, website.company))
            salaries.append(self.safeget(div, website.salary))

            if website.absolute_url == False:
                links.append(website.url + div.select(website.linkjob)[0]["href"])
            else:
                links.append(div.select(website.linkjob)[0]["href"])

        content = Content(titles, companies, links, salaries)
        return content

sites = [
["https://br.indeed.com", "https://br.indeed.com/empregos?q={}&l={}",
 "div.jobsearch-SerpJobCard", "a", False, "h2.title a", "span.company",
  "span.salaryText"]
]

websites = []
for site in sites:
    websites.append(WebSite(site[0], site[1], site[2], site[3],
                            site[4], site[5], site[6], site[7]))

content = Search("Python", "São Paulo").parse(websites[0])
print(content.dict())
