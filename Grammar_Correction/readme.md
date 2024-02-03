# Grammar Correction

There are so many applications that help you to correct your grammatical mistakes while writing. Grammarly is one of the best examples of such applications. It can correct every error while writing and helps you to complete your articles, emails, or any piece of writing without any errors.

-----

## Installation

```
pip install gingerit
```
Firstly import the `gingerit` library through the terminal that will help in the program.

-----

## Code Break:

```python
from gingerit.gingerit import GingerIt
```

Imports the `GingerIt` class from the `gingerit` module.

```python
text = input("Enter a sentence >>: ")
```

Prompts the user to enter a sentence through the command line.

```python
corrected_text = GingerIt().parse(text)
```

Creates an instance of the `GingerIt` class and uses the `parse` method to correct the input sentence. The corrected result is stored in the `corrected_text` variable.

```python
print(corrected_text["result"])
```

Prints the corrected text obtained from the `result` key of the `corrected_text` dictionary.

In summary, this script utilizes the `GingerIt` library to correct grammatical errors in a user-entered sentence. The corrected text is then displayed.

-----