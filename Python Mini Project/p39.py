# Web Scraping to Create a Dataset using Python
# Scrapy
# Selenium
# BeautifulSoup
# Urlib.request
# All of the above Python libraries and modules are great for scraping data from websites.

# I searched for “comparison of programming languages” on Google and got this article as the first result.
# Let’s see how we can scrape data from this web page to create a dataset. Below is how we can use the 
# BeautifulSoup library in Python for the task of web scraping to create a dataset:


import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen(f"https://en.wikipedia.org/wiki/Comparison_of_programming_languages")
soup = BeautifulSoup(html,"html.parser")
table = soup.findAll("table",{"class" : "wikitable"})[0]
row = table.findAll('tr')
with open('language.csv','wt+',newline='')as f:
    writer = csv.writer(f)
    for i in row:
        row = []
        for cell in i.findAll(['td','th']):
            row.append(cell.get_text())
        writer.writerow(row)
        
import pandas as pd
a = pd.read_csv("language.csv")
print(a.head())



# import csv
# from urllib.request import urlopen
# from bs4 import BeautifulSoup

# html = urlopen("https://en.wikipedia.org/wiki/Comparison_of_programming_languages")
# soup = BeautifulSoup(html, "html.parser")
# table = soup.findAll("table", {"class":"wikitable"})[0]
# rows = table.findAll("tr")

# with open("language.csv", "wt+", newline="") as f:
#     writer = csv.writer(f)
#     for i in rows:
#         row = []
#         for cell in i.findAll(["td", "th"]):
#             row.append(cell.get_text())
#         writer.writerow(row)
   
  
# import pandas as pd
# a = pd.read_csv("language.csv")
# a.head()