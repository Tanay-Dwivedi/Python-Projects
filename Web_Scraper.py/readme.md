# Web Scraper

Google News uses tags to create links to the various websites that make up the site. So in addition to some additional data, you’ll collect all the URLs of the articles that Google News displays. I will use the BeautifulSoup module to analyze the articles from Google News.

-----

## Installation

```
pip install beautifulsoup4
```
Firstly import the `beautifulsoup4` library through the terminal that will help in the program.

-----

## Code Break:

```python
import urllib.request
from bs4 import BeautifulSoup
```
We import necessary modules: `urllib.request` for making HTTP requests and `BeautifulSoup` for parsing HTML content.

```python
class Scraper:
    def __init__(self, site):
        self.site = site
```
We define a class `Scraper` with a constructor `__init__()` method. It initializes an instance of the class with a `site` attribute representing the target website URL.

```python
    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
```
We define a `scrape()` method within the class to perform the scraping operation. Inside this method:
  - We use `urllib.request.urlopen()` to open the target website URL (`self.site`) and assign the response to `r`.
  - We read the HTML content of the response using `r.read()` and assign it to the `html` variable.

```python
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
```
We define a parser variable to specify the HTML parser type as "html.parser".
We create a BeautifulSoup object `sp` by passing the HTML content (`html`) and the parser type (`parser`) as arguments.

```python
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "articles" in url:
                print("\n" + url)
```
We iterate over all `<a>` tags in the parsed HTML content using `sp.find_all("a")`.
For each `<a>` tag, we extract the value of the `href` attribute, which represents the URL of the link.
If the extracted URL contains the substring "articles", we print the URL.

```python
news = "https://news.google.com/"
Scraper(news).scrape()
```
We define a variable `news` containing the URL of Google News.
We create an instance of the `Scraper` class with the `news` URL as the argument and call the `scrape()` method on this instance to initiate the scraping process.

-----