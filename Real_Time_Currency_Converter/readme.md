# Real-time Currency Converter

A currency converter is an application used to convert the value of one currency into another currency.

Features of Forex-Python Library:
Some of the important features provided by this library are:

- List all exchange rates
- BitCoin price for all currencies
- Converting the amount into BitCoins
- Get historical rates for any day since 1999
- The conversion rate for a currency (ex; USD to INR)
- Convert the amount from one currency to - another. (‘USD $ 10’ to INR)
- Currency symbols
- Names of currencies

It uses [ratesapi](https://ratesapi.io) which is a free API to work with real-time and historical exchange rates published by the European Central Bank.

-----

## Installation

```
pip install forex-python
```
Firstly import the `forex-python` library through the terminal that will help in the program.

-----

# Code Break:

```python
from forex_python.converter import CurrencyRates
```

This line imports the `CurrencyRates` class from the `forex_python.converter` module, which is used for currency conversion.

```python
c = CurrencyRates()
```

An instance of the `CurrencyRates` class is created, allowing us to use its methods for currency conversion.

```python
amount = int(input("Enter the amount: "))
from_currency = input("From Currency: ").upper()
to_currency = input("To Currency: ").upper()
```

The user is prompted to enter the amount to be converted and the source and target currencies. The `upper()` method is used to convert the input currencies to uppercase for consistency.

```python
print(from_currency, " To ", to_currency, amount)
```

A message is printed to indicate the conversion details, such as "USD To EUR 100".

```python
result = c.convert(from_currency, to_currency, amount)
```

The `convert` method of the `CurrencyRates` instance is called with the specified source currency (`from_currency`), target currency (`to_currency`), and the amount to convert (`amount`). The result is stored in the variable `result`.

```python
print(result)
```

The converted amount is printed to the console. The actual exchange rate used for the conversion depends on the real-time rates fetched by the `forex_python` library.

-----