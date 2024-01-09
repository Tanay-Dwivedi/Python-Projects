# Send Automatic Email

This Python code is designed for sending automated emails using the *Simple Mail Transfer Protocol (SMTP)*. Users are prompted to input their name, email address, and a custom message. The script then constructs an email with a personalized greeting and the user-provided message. It uses Gmail's SMTP server to send the email, requiring authentication with a Gmail account and an app password. The use case for this code is a simple automated email sender, potentially useful for tasks like sending personalized messages or notifications programmatically.

-----

## Pre-Requisites:

For this program, you must first generate a [google app password](https://myaccount.google.com/apppasswords) for your Gmail account. If you don’t know how to generate it, you can learn more from the [video](https://youtu.be/ndxUgivCszE).

It is very important to generate a Google app password for your Gmail account, as you will be sending automatic emails using Python through your Gmail account. Once you’ve generated your Google app password, you can proceed with the program

-----

## Code Break: 

```python
# Import necessary modules
import smtplib
```

This line imports the required `smtplib` module for sending emails using the Simple Mail Transfer Protocol.

```python
# Define the function for automatic email sending
def automatic_email_send():
```

This line begins the definition of the function named `automatic_email_send`.

```python
    # Prompt the user to enter their name and email
    user = input("Enter your name: ")
    email = input("Enter your email ID: ")
```

Here, the user is prompted to enter their name and email address, and the input is stored in the variables `user` and `email`.

```python
    # Compose the email message
    intro = f"Dear {user},"
    user_message = input("Enter the message you want to send: ")
    message = intro + "\n" + user_message
```

This part constructs the email message with a personalized greeting and the user's input message.

```python
    # Set up the SMTP server
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login("<Your gmail account>", "<Your app password>")
```

Here, it creates an SMTP object and connects to the Gmail SMTP server using the `starttls()` method to enable encryption. It then logs in to the Gmail account using the provided Gmail account and app password.

```python
    # Send the email
    s.sendmail("<Sender's email>", email, message)
```

This line sends the email using the `sendmail` method. The sender's email address is set to `<Sender's email>`, and the recipient's email address is set to the user-provided email. The composed message is used as the body of the email.

```python
    # Close the SMTP connection
    s.quit()
```

After sending the email, the connection to the SMTP server is closed.

```python
    # Print a success message
    print("Email sent successfully!!")
```

Finally, a message is printed to indicate that the email has been sent successfully.

```python
# Call the function to execute the email sending process
automatic_email_send()
```

This line calls the `automatic_email_send()` function to execute the email sending process when the script is run.

-----