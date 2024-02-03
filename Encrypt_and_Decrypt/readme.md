# Encrypt and Decrypt

Cryptography means changing the text of a message so that people who don’t know your secret never understand your message.

-----

## Installation

```
pip install tkinter
```
Firstly import the `tkinter` library through the terminal that will help in the program.

-----

## Code Break:

```python
from tkinter import messagebox, simpledialog, Tk
```

Imports necessary functions and classes from the `tkinter` library.

```python
def is_even(number):
    return number % 2 == 0
```

Defines a function `is_even` that checks if a given number is even.

```python
def get_even_letters(message):
    # ... (Function to get even-positioned letters from the message)
```

Defines a function `get_even_letters` that retrieves even-positioned letters from the given message.

```python
def get_odd_letters(message):
    # ... (Function to get odd-positioned letters from the message)
```

Defines a function `get_odd_letters` that retrieves odd-positioned letters from the given message.

```python
def swap_letters(message):
    # ... (Function to swap even and odd-positioned letters in the message)
```

Defines a function `swap_letters` that swaps even and odd-positioned letters in the given message.

```python
def get_task():
    # ... (Function to get the task (encrypt or decrypt) from the user)
```

Defines a function `get_task` that prompts the user to input the task (encrypt or decrypt).

```python
def get_message():
    # ... (Function to get the secret message from the user)
```

Defines a function `get_message` that prompts the user to input the secret message.

```python
root = Tk()
while True:
    task = get_task()
    if task == "encrypt":
        message = get_message()
        encrypted = swap_letters(message)
        messagebox.showinfo("Ciphertext of the secret message is:", encrypted)
    elif task == "decrypt":
        message = get_message()
        decrypted = swap_letters(message)
        messagebox.showinfo("Plaintext of the secret message is:", decrypted)
    else:
        break
root.mainloop()
```

Creates the main Tkinter window (`root`) and enters a loop where the user is prompted to choose between encryption and decryption tasks. The chosen task is then performed based on user input, and the result is displayed using message boxes. The loop continues until the user chooses to exit the program.

-----