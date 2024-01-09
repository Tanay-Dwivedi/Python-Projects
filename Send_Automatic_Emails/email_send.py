import smtplib


def automatic_email_send():
    user = input("Enter your name: ")
    email = input("Enter your email ID: ")
    intro = f"Dear {user},"
    user_message = input("Enter the message you want to send: ")
    message = intro + "\n" + user_message
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login("<Your gmail account>", "<Your app password>")
    s.sendmail("<Sender's email>", email, message)
    s.quit()
    print("Email sent successfully!!")


automatic_email_send()
