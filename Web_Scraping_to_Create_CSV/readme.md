# Web Scraping to Create CSV

Web Scraping means to collect data from the Internet. As a beginner in data science, you must have seen CSV files on the Internet distributed by some popular websites like Kaggle and other govt websites. The data is prepared by either collecting and writing using standard methods or by scraping it from the Internet.

-----

## Installation

```
pip install beautifulsoup4 urllib3
```
Firstly import the `beautifulsoup4 urllib3` libraries through the terminal that will help in the program.

-----

## Code Break:

This script scrapes product information (product name, price, and ratings) from Flipkart's search results page for Samsung mobiles.

```python
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
```
Imports necessary modules from BeautifulSoup (`soup`) and `urlopen` from `urllib.request`.

```python
my_url = "https://www.flipkart.com/search?q=samsung+mobiles&amp;sid=tyy%2C4io&amp;as=on&amp;as-show=on&amp;otracker=AS_QueryStore_HistoryAutoSuggest_0_2&amp;otracker1=AS_QueryStore_HistoryAutoSuggest_0_2&amp;as-pos=0&amp;as-type=HISTORY&amp;as-searchtext=sa"
```
Sets the URL of the Flipkart search results page for Samsung mobiles.

```python
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
```
Opens a connection to the URL using `urlopen`, reads the HTML content, and then closes the connection.

```python
page_soup = soup(page_html, "html.parser")
```
Parses the HTML content of the page using BeautifulSoup and stores it in `page_soup`.

```python
containers = page_soup.findAll("div", {"class": "_3O0U0u"})
print(len(containers))
```
Finds all div containers with the class "_3O0U0u", which typically contain information about each product, and prints the total number of containers found.

```python
print(soup.prettify(containers[0]))
```
Prints the prettified HTML content of the first container for better readability.

```python
container = containers[0]
print(container.div.img["alt"])
```
Selects the first container and extracts the product name from the "alt" attribute of the image tag within the container.

```python
price = container.findAll("div", {"class": "col col-5-12 _2o7WAb"})
print(price[0].text)
```
Finds all div containers with the class "col col-5-12 _2o7WAb", which typically contain the price information, and prints the price of the first product.

```python
ratings = container.findAll("div", {"class": "niH0FQ"})
print(ratings[0].text)
```
Finds all div containers with the class "niH0FQ", which typically contain the ratings information, and prints the ratings of the first product.

```python
filename = "products.csv"
f = open(filename, "w")
headers = "Product_Name, Pricing, Ratings \n"
f.write(headers)
```
Creates a CSV file named "products.csv", opens it in write mode, writes the headers for the columns, and then starts writing product information to the file.

```python
for container in containers:
    product_name = container.div.img["alt"]
    price_container = container.findAll("div", {"class": "col col-5-12 _2o7WAb"})
    price = price_container[0].text.strip()

    rating_container = container.findAll("div", {"class": "niH0FQ"})
    rating = rating_container[0].text

    print("Product_Name:" + product_name)
    print("Price: " + price)
    print("Ratings:" + rating)

    f.write(product_name.replace(",", "|") + "," + price + "," + rating + "\n")
```
Loops through each container, extracts the product name, price, and ratings, prints them to the console, and writes them to the CSV file. The `replace(",", "|")` is used to avoid any conflicts with the comma used as the delimiter in CSV files.

This script effectively scrapes product information from Flipkart's search results page for Samsung mobiles and saves it to a CSV file for further analysis.

-----