from instabot import Bot

insta_bot = Bot()

insta_bot.login(username="Your Username", password="Your Password")

insta_bot.send_message("Your message", ["Receiver's Username"])
