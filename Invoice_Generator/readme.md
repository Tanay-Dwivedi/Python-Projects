# Invoice Generator

An invoice is a bill that serves as proof of a transaction between a buyer and a seller.

-----

## Code Break:

```python
product1_name, product1_price = "Books", 50.95
product2_name, product2_price = "Computer", 598.99
product3_name, product3_price = "Monitor", 156.89
```

These lines define variables for three products, each with a name and price.

```python
company_name = "Thecleverprogrammer, inc."
company_address = "144 Kalka ji."
company_city = "New Delhi"
```

These lines define variables for the company's name, address, and city.

```python
message = "Thanks for shopping with us today!"
```

This line defines a variable for a thank-you message.

```python
# create a top border
print("*" * 50)
```

This line prints a top border made of asterisks.

```python
print("\t\t{}".format(company_name.title()))
print("\t\t{}".format(company_address.title()))
print("\t\t{}".format(company_city.title()))
```

These lines print the formatted company information with proper indentation.

```python
# print a line between sections
print("=" * 50)
```

This line prints a line made of equal signs to separate sections in the receipt.

```python
print("\tProduct Name\tProduct Price")
```

This line prints a header for the product details section.

```python
# create a print statement for each item
print("\t{}\t\t${}".format(product1_name.title(), product1_price))
print("\t{}\t${}".format(product2_name.title(), product2_price))
print("\t{}\t\t${}".format(product3_name.title(), product3_price))
```

These lines print the product details, including names and prices, with proper formatting.

```python
print("=" * 50)
```

This line prints another line of equal signs to separate sections.

```python
# print out header for section of total
print("\t\t\tTotal")
```

This line prints a header for the total cost section.

```python
# calculate total price and print out
total = product1_price + product2_price + product3_price
print("\t\t\t${}".format(total))
```

These lines calculate the total price by summing the prices of the three products and then print the total with proper formatting.

```python
# print a line between sections
print("=" * 50)
```

This line prints another line of equal signs to separate sections.

```python
print("\n\t{}\n".format(message))
```

This line prints the thank-you message with proper formatting and a newline character for spacing.

-----