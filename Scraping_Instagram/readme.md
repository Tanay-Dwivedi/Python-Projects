# Scraping Instagram

To scrap Instagram, we will use a library know as instaloader which provides us with an API for scraping Instagram. You can install this library by using the pip method in your terminal – `pip install instaloader`.

-----

## Installation

```
pip install instaloader
```
Firstly import the `instaloader` library through the terminal that will help in the program.

-----

## Code Break:

```python
import instaloader
```
Imports the `instaloader` library.

```python
bot = instaloader.Instaloader()
```
Initializes an `Instaloader` instance named `bot` to interact with the Instagram API.

```python
profile = instaloader.Profile.from_username(bot.context, "aman.kharwal")
```
Retrieves the profile information of the Instagram user "aman.kharwal" using the `Profile.from_username()` method.

```python
print(type(profile))
```
Prints the type of the `profile` object to confirm it's an instance of `Profile`.

```python
print("Username: ", profile.username)
print("User ID: ", profile.userid)
print("Number of Posts: ", profile.mediacount)
print("Followers: ", profile.followers)
print("Followees: ", profile.followees)
print("Bio: ", profile.biography, profile.external_url)
```
Prints various details about the profile such as username, user ID, number of posts, followers, followees, biography, and external URL.

```python
bot.login(user="your username", passwd="your password")
```
Logs in to Instagram using the provided username and password. (Replace `"your username"` and `"your password"` with your actual Instagram credentials.)

```python
bot.interactive_login("your username")
```
Interactive login prompt for password. (Replace `"your username"` with your actual Instagram username.)

```python
followers = [follower.username for follower in profile.get_followers()]
```
Retrieves the usernames of followers of the profile.

```python
followees = [followee.username for followee in profile.get_followees()]
```
Retrieves the usernames of accounts followed by the profile.

```python
print(followers)
```
Prints the list of followers.

```python
profile = instaloader.Profile.from_username(bot.context, "wwe")
```
Retrieves the profile information of the Instagram user "wwe".

```python
posts = profile.get_posts()

for index, post in enumerate(posts, 1):
    bot.download_post(post, target=f"{profile.username}_{index}")
```
Iterates through the user's posts and downloads each post. The `target` parameter specifies the directory where the posts will be saved, with the filename format `{profile.username}_{index}`.

-----