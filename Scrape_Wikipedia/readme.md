# Scrape Wikipedia

Wikipedia is one of those largest platforms which provides almost every information for free. From your kindergarten till today, you must have visited this platform atleast once to get any information from school presentations to professional research, Wikipedia helps everybody.

-----

## Installation

```
pip install wikipedia
```
Firstly import the `wikipedia` library through the terminal that will help in the program.

-----

## Code Break:

```python
import wikipedia as wiki
```
This imports the `wikipedia` library, which allows you to access Wikipedia content programmatically.

```python
print(wiki.search("Python"))
```
The `search()` function is used to search Wikipedia for articles related to the keyword "Python". It returns a list of titles of articles that match the search query.

```python
print(wiki.suggest("Pyth"))
```
The `suggest()` function is used to provide suggestions for a search query. It returns a suggested search query based on the input. Here, it suggests "Python" based on the input "Pyth".

```python
print(wiki.summary("Python"))
```
The `summary()` function retrieves a summary of the Wikipedia article for the given topic. In this case, it prints a summary of the article on "Python".

```python
wiki.set_lang("fr")
print(wiki.summary("Python"))
```
`set_lang()` function is used to set the language for subsequent Wikipedia queries. Here, it sets the language to French ("fr"). Then, it prints a summary of the article on "Python" in French.

```python
wiki.set_lang("en")
p = wiki.page("Python")
```
The `page()` function is used to fetch a Wikipedia page by its title. Here, it fetches the page titled "Python" and assigns it to the variable `p`.

```python
print(p.title)
print(p.url)
print(p.content)
print(p.images)
print(p.links)
```
Various attributes of the Wikipedia page object `p` are accessed and printed:
- `title`: The title of the Wikipedia page.
- `url`: The URL of the Wikipedia page.
- `content`: The full content of the Wikipedia page.
- `images`: A list of URLs of images associated with the Wikipedia page.
- `links`: A list of titles of Wikipedia pages linked from the current page.

-----