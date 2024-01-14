# Send Instagram Messages

By using a third-party application or API to manage the functionality of an application, you are automating the application. If you send messages, post photos or videos, or follow someone without opening your Instagram directly, that means you are automating Instagram.

-----

## Installation

```python
pip install instabot
```
To send Instagram message using Python, you need to have an Instagram account and the `instabot` library installed in your python virtual environment

-----

## Code Break:

```python
from instabot import Bot
```

This line imports the `Bot` class from the `instabot` module. The `instabot` library is a Python wrapper for the Instagram Private API, allowing users to interact with Instagram programmatically.

```python
insta_bot = Bot()
```

An instance of the `Bot` class is created and assigned to the variable `insta_bot`.

```python
insta_bot.login(username="Your Username", password="Your Password")
```

The `login` method of the `Bot` instance is called to log in to an Instagram account. You should replace "Your Username" and "Your Password" with your actual Instagram account credentials.

```python
insta_bot.send_message("Your message", ["Receiver's Username"])
```

The `send_message` method is used to send a direct message on Instagram. You should replace "Your message" with the actual message you want to send, and ["Receiver's Username"] with the username of the person to whom you want to send the message.

-----

***Keep in mind that using automation tools like Instabot may violate Instagram's terms of service, and it's essential to use such tools responsibly to avoid potential consequences such as account suspension or banning. Additionally, always ensure that you are complying with Instagram's policies and guidelines when interacting with the platform programmatically.***

-----