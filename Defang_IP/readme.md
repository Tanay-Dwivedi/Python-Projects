# Defang IP Address

A user’s IP address is defanged to prevent the user from clicking on a malicious link. Solving the problem of changing an IP address is only based on the concepts of replacing and join.
To convert an IP address to a defanged IP address, we need to replace “.” with “[.]”.

-----

## Code Break:

```python
# Define a function to convert an IP address format
def ip_address(address):
```

This line declares a function named `ip_address` that takes a single parameter `address`, representing an IP address.

```python
    # Initialize an empty string to store the modified IP address
    new_ip_address = ""
```

This line initializes an empty string `new_ip_address` to store the modified IP address.

```python
    # Split the input IP address into a list using dots as separators
    split_ip_address = address.split(".")
```

Here, the input IP address is split into a list of strings using the `split()` method with a dot (`.`) as the separator. For example, `"123.131.237.101"` becomes `['123', '131', '237', '101']`.

```python
    # Define a custom separator (in this case, "[.]")
    ip_separator = "[.]"
```

This line defines a custom separator `ip_separator`, which is set to "[.]" in this case.

```python
    # Use the join method to concatenate the list elements with the custom separator
    new_ip_address = ip_separator.join(split_ip_address)
```

Here, the `join()` method is used to concatenate the elements of the `split_ip_address` list into a string, with the custom separator `ip_separator`. This creates a new string where dots are replaced with "[.]". For example, `['123', '131', '237', '101']` becomes `"123[.]131[.]237[.]101"`.

```python
    # Return the modified IP address
    return new_ip_address
```

The modified IP address is returned from the function.

```python
# Example usage of the function
ipAddress = ip_address("123.131.237.101")
```

The function is called with an example IP address ("123.131.237.101"), and the result is stored in the variable `ipAddress`.

```python
print(ipAddress)
```

Finally, the modified IP address is printed.

-----