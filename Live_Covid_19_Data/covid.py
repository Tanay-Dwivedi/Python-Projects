import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen(
    "https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data#covid-19-pandemic-data"
)
soup = BeautifulSoup(html, "html.parser")
table = soup.findAll("table", {"class": "wikitable"})[0]
rows = table.findAll("tr")

with open("Dataset.csv", "wt+", newline="") as f:
    writer = csv.writer(f)
    for i in rows:
        row = []
        for cell in i.findAll(["td", "th"]):
            row.append(cell.get_text())
        writer.writerow(row)
import pandas as pd

data = pd.read_csv("Dataset.csv")
data.head()

data = data.drop(labels="Ref.\n", axis=1)
data.columns = ["Location", "Cases", "Deaths", "Recovered"]
data.head()
