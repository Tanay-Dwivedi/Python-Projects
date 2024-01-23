# Email Slicer

An Email slicer is a very useful program for separating the username and domain name of an email address.

-----

# Code Break:

This script takes an email address as input, extracts the username and domain name, and then prints a formatted message displaying the extracted information. Let's break down the code:

```python
email = input("Enter Your Email: ").strip()
```

This line prompts the user to input their email address and uses the `strip()` method to remove any leading or trailing whitespace.

```python
username = email[: email.index("@")]
```

This line extracts the username from the email. It uses slicing to get the substring from the beginning of the email up to (but not including) the "@" symbol.

```python
domain_name = email[email.index("@") + 1 :]
```

This line extracts the domain name from the email. It uses slicing to get the substring starting from the character immediately after the "@" symbol until the end of the email.

```python
format_ = f"Your user name is '{username}' and your domain is '{domain_name}'"
```

This line uses an f-string to format a message that includes the extracted username and domain name.

```python
print(format_)
```

This line prints the formatted message, displaying the user's username and domain name.

So, for example, if the user enters "example_user@example.com", the output might be:

```
Your user name is 'example_user' and your domain is 'example.com'
```

-----