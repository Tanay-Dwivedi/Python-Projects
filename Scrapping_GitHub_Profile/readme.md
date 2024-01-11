# Scraping GitHub Profile

This Python script uses the `requests` library to make an HTTP request to a specified URL and then uses `BeautifulSoup` from the `bs4` library to parse the HTML content of the page. The goal is to extract the source URL of a user's GitHub profile picture.

-----

## Installation

```
pip install beautifulsoup4
```
Firstly import the `pyspellChecker` library through the terminal that will help in the program.

-----

## Code Break:

```python
# Import necessary libraries
import requests
from bs4 import BeautifulSoup
```

These lines import the `requests` library for making HTTP requests and `BeautifulSoup` for parsing HTML content.

```python
# Specify the URL of the GitHub profile page
url = "https://github.com/Tanay-Dwivedi"
```

This line sets the URL to the GitHub profile page of the user "Tanay-Dwivedi."

```python
# Make an HTTP request to the specified URL
req = requests.get(url)
```

The `requests.get()` function is used to send an HTTP GET request to the specified URL, and the response is stored in the `req` variable.

```python
# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(req.content, "html.parser")
```

`BeautifulSoup` is used to parse the HTML content of the response (`req.content`). The parsed HTML content is stored in the `soup` variable.

```python
# Find the profile picture image element using its HTML class
pic_image = soup.find(
    "img", class_="avatar avatar-user width-full border color-bg-default"
)["src"]
```

The `find()` method is used to locate an `img` element with a specific combination of classes (`avatar`, `avatar-user`, `width-full`, `border`, and `color-bg-default`). The `["src"]` at the end extracts the value of the `src` attribute from the found `img` element, which represents the source URL of the profile picture.

```python
# Print the extracted profile picture URL
print(pic_image)
```

Finally, the script prints the extracted profile picture URL to the console. This URL can be the direct link to the user's GitHub profile picture.

-----