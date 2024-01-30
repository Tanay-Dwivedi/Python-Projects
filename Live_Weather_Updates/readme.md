# Live Weather Updates

If you are using weather APIs provided by any platform, you need to connect to their paid services to work with the weather APIs. But if you use your web scraping skills, it will be free.

-----

## Installation

```
pip install beautifulsoup4 requests
```
Firstly import the `beautifulsoup4 requests` libraries through the terminal that will help in the program.

-----

## Code Break:

The given Python script utilizes the BeautifulSoup and requests libraries to scrape weather information from Google for a specified city. Let's break down the code line by line:

```python
from bs4 import BeautifulSoup
import requests
```
These lines import the necessary libraries. BeautifulSoup is used for parsing HTML content, and requests is used for making HTTP requests.

```python
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
```
Here, a user-agent header is defined to mimic a web browser. This is often necessary to prevent websites from blocking or providing different content based on the user agent.

```python
def weather(city):
    city = city.replace(" ", "+")
    res = requests.get(
        f"https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8",
        headers=headers,
    )
    print("Searching......\n")
    soup = BeautifulSoup(res.text, "html.parser")
    location = soup.select("#wob_loc")[0].getText().strip()
    time = soup.select("#wob_dts")[0].getText().strip()
    info = soup.select("#wob_dc")[0].getText().strip()
    weather = soup.select("#wob_tm")[0].getText().strip()
    print(location)
    print(time)
    print(info)
    print(weather + "°C")
```
The `weather` function is defined to retrieve and display weather information for a given city. It takes the city name as input, replaces spaces with '+' for the URL, sends a GET request to the Google weather search page, and parses the HTML content using BeautifulSoup.

The `select` method is used to extract information from specific HTML elements with corresponding IDs (`#wob_loc`, `#wob_dts`, `#wob_dc`, and `#wob_tm`). The extracted data includes location, time, weather information, and temperature.

```python
city = input("Enter the Name of Any City >>  ")
city = city + " weather"
weather(city)
```
The script prompts the user to input the name of a city, appends "weather" to the city name for more accurate search results, and then calls the `weather` function with the specified city. The weather information is printed to the console.

-----