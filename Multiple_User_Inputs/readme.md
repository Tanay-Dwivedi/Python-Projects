# Multiple User Inputs

The `input()` function of Python help us to give a user input while writing a program.

-----

## Code Break:

```python
while True:
    reply = input("Enter Text: ")
    if reply == "stop":
        break
    print(reply)
```

This code snippet initiates an infinite loop (`while True:`) that keeps running until the user enters "stop". Inside the loop:

- `reply = input("Enter Text: ")` prompts the user to input text, and the input is stored in the variable `reply`.
- `if reply == "stop":` checks if the entered text is "stop". If it is, the `break` statement is executed, which terminates the loop.
- `print(reply)` is executed if the user did not enter "stop", and it prints the entered text.

The loop continues to prompt the user for input until "stop" is entered.

-----