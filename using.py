from scraper import WebSite, Search

sites = [
["https://br.indeed.com", "https://br.indeed.com/empregos?q={}&l={}&start={}",
 "div.jobsearch-SerpJobCard", "a", False, "h2.title a", "span.company",
  "span.salaryText"]
]

websites = []
for site in sites:
    websites.append(WebSite(site[0], site[1], site[2], site[3],
                            site[4], site[5], site[6], site[7]))

contents = Search("Python", "São Paulo").parse(websites[0])
for content in contents:
    print(content.dict())
