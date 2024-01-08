# Password Authentication

This Python code implements a simple authentication system. It prompts the user to input a username and a password using the getpass module for enhanced security. It checks if the entered username exists in a predefined database. If the username is found, it enters a loop asking the user to input the correct password. The loop continues until the correct password is entered.

-----

## Code Break:

This Python code is a basic authentication system that prompts the user to enter a username and password. It uses the `getpass` module to securely input the password without displaying it on the screen. Let's go through the code line by line:

```python
# Import the getpass module
import getpass
```

This line imports the `getpass` module, which provides a method for securely entering passwords without displaying them on the screen.

```python
# Define a dictionary called 'database' with username-password pairs
database = {
    "Tanay Dwivedi": "837219",
    "Anurag Singh": "604831",
    "Shrey Srivastava": "195024",
    "Rohan Sharma": "763508",
    "Sarthak Mishra": "321975",
    "Priyansh Rastogi": "489623",
}
```

Here, a dictionary named `database` is defined, containing username-password pairs.

```python
# Prompt the user to enter a username
username = input("Enter Your Username : ")
```

The user is prompted to enter their username, and the input is stored in the variable `username`.

```python
# Prompt the user to enter a password (securely using getpass)
password = getpass.getpass("Enter Your Password : ")
```

The user is prompted to enter their password securely using the `getpass.getpass()` function.

```python
# Loop through the usernames in the database
for i in database.keys():
    # Check if the entered username matches any in the database
    if username == i:
        # If a match is found, enter a loop to check the password
        while password != database.get(i):
            # If the entered password is incorrect, prompt the user to enter it again
            password = getpass.getpass("Enter Your Password Again : ")
        # Break out of the loop if the password is correct
        break
```

This part of the code checks if the entered username matches any in the database. If a match is found, it enters a loop to check the entered password against the stored password in the database. If the entered password is incorrect, the user is prompted to enter it again until it matches the stored password.

```python
# Print "Verified" once the username and password are successfully verified
print("Verified")
```

Finally, if both the username and password are successfully verified, it prints "Verified" to indicate successful authentication.

-----