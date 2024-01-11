import requests
from bs4 import BeautifulSoup

url = "https://github.com/Tanay-Dwivedi"

req = requests.get(url)
soup = BeautifulSoup(req.content, "html.parser")

pic_image = soup.find(
    "img", class_="avatar avatar-user width-full border color-bg-default"
)["src"]

print(pic_image)
