from scraper import WebSite, Search
import sys

args = sys.argv[1:]

sites = [
["https://br.indeed.com", "https://br.indeed.com/empregos?q={}&l={}",
 "div.jobsearch-SerpJobCard", "a", False, "h2.title a", "span.company",
 "span.salaryText"],
["https://www.catho.com.br",
 "https://www.catho.com.br/vagas/&q={}&cidade={}",
 "article.Card__CardWrapper-om5cci-0",
 "a", True, "a", "", "div:nth-child(1) > div:nth-child(2) > div:nth-child(1)"],
 ["https://www.monster.com",
  "https://www.monster.com/jobs/search/?q={}&where={}&page={}",
  "section.card-content",
  "a", True, "h2.title a", "div.company span", ""]
 ]

websites = []
for site in sites:
    websites.append(WebSite(site[0], site[1], site[2], site[3],
                            site[4], site[5], site[6], site[7]))

linguagem, cidade = ["Python", "São Paulo"] if (len(args) != 2) else args

if (args and len(args) != 2):
    print(f'Usage: python {sys.argv[0]} [language] [city]')
    print(f'Defaults -> language: {linguagem}, city: {cidade}.\n')
else:
    for website in websites:
        contents = Search(linguagem, cidade).parse(website)
        for content in contents:
            print(content.dict())

