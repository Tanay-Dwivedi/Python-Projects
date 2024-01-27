# Message Encryption

Message Encryption means keeping the message secret. In simple words, Message Encryption means putting the message in a secret box that only the receiver can open.

Before implementing Message Encryption using Python, let’s look at the process of Message Encryption. Here’s the complete process of Message Encryption that messaging apps follow:

- First, choose a secret key that to encrypt the message. This key is a password only the person supposed to read the message knows.
- Then take the message and scramble it using the key. It means turning the message into a secret code like a jumble of letters or numbers.
- Once the message is scrambled, it is delivered to the person who is supposed to read it. But if anyone else tries to read it, they’ll see a jumble of letters or numbers that don’t make sense.

So, Message Encryption is like having a secret code that only the person who is supposed to read the message can understand.

-----

## Installation

```
pip install cryptography
```
Firstly import the `cryptography` library through the terminal that will help in the program.

-----

## Code Break:

```python
message_data = {
    "Aman": [
        {"message": "Hey Divyansha, how's it going?", "time": "2023-03-21 10:30:00"},
        {"message": "Not too bad, just working on some coding projects. Did you hear about the new encryption algorithm?", "time": "2023-03-21 10:35:00"},
        {"message": "It's called AES256 and it's supposed to be really secure. Want to give it a try with our messages?", "time": "2023-03-21 10:40:00"},
    ],
    "Divyansha": [
        {"message": "Good, thanks! How about you?", "time": "2023-03-21 10:32:00"},
        {"message": "No, what's that?", "time": "2023-03-21 10:37:00"},
        {"message": "Sure, let's do it!", "time": "2023-03-21 10:42:00"},
    ],
}
```
A dictionary `message_data` contains messages exchanged between users ("Aman" and "Divyansha") along with timestamps.

```python
shared_secret_key = os.urandom(32)
```
A shared secret key of 32 bytes (256 bits) is generated using `os.urandom()`.

```python
def encrypt_message(message, key):
    # Function to encrypt a message using AES256
    ...

def decrypt_message(ciphertext, key):
    # Function to decrypt a message using AES256
    ...
```
Two functions, `encrypt_message` and `decrypt_message`, are defined for encrypting and decrypting messages using the AES256 algorithm.

```python
for person, messages in message_data.items():
    for message in messages:
        encrypted_message = encrypt_message(message["message"], shared_secret_key)
        message["message"] = encrypted_message.hex()
```
The code iterates through the `message_data` dictionary, encrypts each message using the `encrypt_message` function, and updates the original message with the hexadecimal representation of the encrypted message.

```python
print("Encrypted message_data dictionary:")
print(message_data)
```
The code prints the updated `message_data` dictionary, now containing the encrypted messages.

Please note that this is a simplified example, and in a real-world scenario, additional considerations such as secure key exchange and proper handling of initialization vectors (IVs) would be necessary for a secure communication system.

-----