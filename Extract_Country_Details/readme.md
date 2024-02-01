# Extract Country Details

Countryinfo is a Python module that helps to extract information about any country about the properties of that country, including ISO information, states, languages spoken, currencies, and various other information.

-----

## Installation

```
pip install countryinfo
```
Firstly import the `countryinfo` library through the terminal that will help in the program.

-----

## Code Break:

```python
from countryinfo import CountryInfo
```

This line imports the `CountryInfo` class from the `countryinfo` library.

```python
country = CountryInfo("India")
```

An instance of the `CountryInfo` class is created for the country "India."

```python
print(country.alt_spellings())
```

The `alt_spellings()` method is called to retrieve alternative spellings of the country's name and prints the result.

```python
print(country.capital())
```

The `capital()` method is called to retrieve the capital city of the country and prints the result.

```python
print(country.currencies())
```

The `currencies()` method is called to retrieve the currencies used in the country and prints the result.

```python
print(country.languages())
```

The `languages()` method is called to retrieve the languages spoken in the country and prints the result.

```python
print(country.borders())
```

The `borders()` method is called to retrieve the countries that share borders with the specified country and prints the result.

```python
data = country.info()
for i, j in data.items():
    print(f"{i}:>>{j}")
```

The `info()` method is called to retrieve general information about the country, and the result is stored in the `data` dictionary. A loop then iterates through the dictionary items, printing key-value pairs.

In summary, this script uses the `countryinfo` library to fetch and display various pieces of information about the country "India," including alternative spellings, capital, currencies, languages, borders, and general information.

-----