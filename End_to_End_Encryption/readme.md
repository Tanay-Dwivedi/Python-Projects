# End-to-End Encryption

End-to-end encryption is a system that ensures that only the users involved in the communication can understand and read the messages.

-----

## Code Break:

```python
def is_even(number):
    return number % 2 == 0
```
This function checks whether a given number is even.

```python
def get_even_letters(message):
    even_letters = []
    for counter in range(0, len(message)):
        if is_even(counter):
            even_letters.append(message[counter])
    return even_letters
```
This function retrieves the letters at even indices from the input message.

```python
def get_odd_letters(message):
    odd_letters = []
    for counter in range(0, len(message)):
        if not is_even(counter):
            odd_letters.append(message[counter])
    return odd_letters
```
This function retrieves the letters at odd indices from the input message.

```python
def swap_letters(message):
    letter_list = []
    if not is_even(len(message)):
        message = message + "x"
    even_letters = get_even_letters(message)
    odd_letters = get_odd_letters(message)
    for counter in range(0, int(len(message) / 2)):
        letter_list.append(odd_letters[counter])
        letter_list.append(even_letters[counter])
    new_message = "".join(letter_list)
    return new_message
```
This function swaps the letters at odd and even indices in the input message. If the length of the message is odd, it adds an 'x' at the end to ensure an even length.

```python
user = "My name is Tanay Dwivedi."
print(swap_letters(user))
```
This prints the result of swapping letters in the given user message using the `swap_letters` function.

-----