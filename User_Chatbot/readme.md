# Chatbot

A Chatbot is an application that interacts with users like a human. Chatbots are typically used to resolve the most common queries that a business receives from its customers daily.

-----

## Installation

```
pip install nltk
```
Firstly import the `nltk` library through the terminal that will help in the program.

-----

## Code Break:

```python
from nltk.chat.util import Chat, reflections
```

Imports the `Chat` class and `reflections` from the `nltk.chat.util` module.

```python
# Pairs is a list of patterns and responses.
pairs = [
    [
        r"(.*)my name is (.*)",
        [
            "Hello %2, How are you today ?",
        ],
    ],
    # ... (other pairs)
    [r"quit", ["Bye for now. See you soon :) ", "It was nice talking to you. See you soon :)"]],
    [r"(.*)", ["That is nice to hear"]],
]
```

Defines a list named `pairs` containing patterns and corresponding responses. Each pair consists of a regular expression pattern and a list of possible responses.

```python
# default message at the start of chat
print(
    "Hi, I'm Tanay Dwivedi and I like to chat.\nPlease type lowercase English language to start a conversation. Type quit to leave "
)
```

Prints a welcome message at the beginning of the chat.

```python
# Create Chat Bot
chat = Chat(pairs, reflections)
# Start conversation
chat.converse()
```

Creates an instance of the `Chat` class with the provided `pairs` and `reflections`. Then, it starts the conversation using the `converse` method.

In summary, this script defines a set of patterns and responses for the chatbot. The chatbot interacts with the user based on the entered patterns and responds accordingly. The conversation continues until the user types "quit." The NLTK library is used to facilitate this chatbot implementation.

-----