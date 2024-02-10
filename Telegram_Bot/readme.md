# Telegram Bot

A bot is a software application programmed to perform certain tasks. The robots are automated, which means that they operate according to their instructions without a human user needing to start them. Bots often mimic or replace the behaviour of a human user.

-----

## Installation

```
pip install telegram requests json
```
Firstly import the `telegram requests json` libraries through the terminal that will help in the program.

-----

## Code Break:

```python
import telegram
import requests
import json
```
This part of the code imports necessary modules: `telegram` for interacting with the Telegram API, `requests` for making HTTP requests, and `json` for handling JSON data.

```python
bot = telegram.bot(token="TOKEN")  
```
This line attempts to create a Telegram bot instance using the provided token. The token should be replaced with the actual token string obtained from the Telegram BotFather.

```python
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
```
Here, specific modules and classes are imported from the `telegram.ext` package. These classes are needed to handle various aspects of bot functionality, like receiving updates, handling commands, and processing messages.

```python
updater = Updater(
    token="TOKEN", use_context=True
)
```
This creates an `Updater` object, which continuously fetches updates from Telegram servers. The `token` parameter should be replaced with the actual bot token obtained from BotFather. `use_context=True` indicates that the new context-based approach is used.

```python
dispatcher = updater.dispatcher
```
This line retrieves the dispatcher object from the updater. The dispatcher is responsible for handling different types of updates (e.g., messages, commands) by routing them to appropriate handlers.

```python
def hello(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, World")
```
This is a function definition for handling the `/hello` command. It sends a message "Hello, World" to the chat where the command was received.

```python
hello_handler = CommandHandler("hello", hello)
dispatcher.add_handler(hello_handler)
```
This creates a `CommandHandler` for the "/hello" command and associates it with the `hello` function. Then, it adds this handler to the dispatcher, so the bot knows how to respond to the "/hello" command.

```python
updater.start_polling()
```
This starts the polling mechanism, which continuously queries Telegram servers for new updates and passes them to the dispatcher for handling.

```python
def summary(update, context):
    response = requests.get("https://api.covid19api.com/summary")
    if response.status_code == 200:
        data = response.json()
        print(data["Global"])
        context.bot.send_message(chat_id=update.effective_chat.id, text=data["Global"])
    else:
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="Error, something went wrong."
        )
```
This function, `summary`, is defined to handle the `/summary` command. It makes a GET request to the COVID-19 API endpoint to fetch summary data. If the request is successful (status code 200), it extracts global data and sends it as a message. Otherwise, it sends an error message.

```python
corona_summary_handler = CommandHandler("summary", summary)
dispatcher.add_handler(corona_summary_handler)
```
Similar to the `/hello` command, this creates a `CommandHandler` for the "/summary" command and associates it with the `summary` function. Then, it adds this handler to the dispatcher to handle the "/summary" command.

```python
give code explanation line by line and code by code, dont give comments in the code, but give code breakdown line be line
```

-----