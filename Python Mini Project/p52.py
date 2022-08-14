# Get Live Covid-19 Data using Python

import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://bit.ly/3jpMFRW")
soup = BeautifulSoup(html, "html.parser")
table = soup.findAll("table", {"class":"wikitable"})[0]
rows = table.findAll("tr")

with open("Dataset.csv", "wt+", newline="") as f:
    writer = csv.writer(f)
    for i in rows:
        row = []
        for cell in i.findAll(["td", "th"]):
            row.append(cell.get_text())
        writer.writerow(row)
import pandas as pd
data = pd.read_csv("Dataset.csv", encoding= 'latin-1')

# data = data.drop(labels="Ref.\n", axis=1)
data.columns = ["Location", "Cases", "Deaths", "Recovered"]
print(data.head())