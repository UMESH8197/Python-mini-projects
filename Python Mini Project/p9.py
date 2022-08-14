# Scraping GitHub Profile using Python
import requests
from bs4 import BeautifulSoup as bs

github_profile = "https://github.com/UMESH8197"
req = requests.get(github_profile)
scraper = bs(req.content,'html.parser')
github_profile = scraper.find('img',{'alt':'Avatar'})['src']
print(github_profile)