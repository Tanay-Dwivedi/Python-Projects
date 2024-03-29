import instaloader

bot = instaloader.Instaloader()

profile = instaloader.Profile.from_username(bot.context, "aman.kharwal")

print(type(profile))

print("Username: ", profile.username)
print("User ID: ", profile.userid)
print("Number of Posts: ", profile.mediacount)
print("Followers: ", profile.followers)
print("Followees: ", profile.followees)
print("Bio: ", profile.biography, profile.external_url)

bot.login(user="your username", passwd="your password")

bot.interactive_login("your username")

followers = [follower.username for follower in profile.get_followers()]

followees = [followee.username for followee in profile.get_followees()]
print(followers)

profile = instaloader.Profile.from_username(bot.context, "wwe")

posts = profile.get_posts()

for index, post in enumerate(posts, 1):
    bot.download_post(post, target=f"{profile.username}_{index}")
