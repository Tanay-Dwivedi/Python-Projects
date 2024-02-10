# Scraping Twitter

Scraping Twitter with Python without API using the twint module, and I’ll also analyze some relationships based on followings and mentions among a group of Twitter users.

-----

## Installation

```
pip install twint pandas
```
Firstly import the `twint pandas` libraries through the terminal that will help in the program.

-----

## Code Break:

```python
import twint
import pandas as pd
from collections import Counter
```
This part of the code imports necessary modules: `twint` for accessing Twitter data without using their API, `pandas` for data manipulation and analysis, and `Counter` for counting hashable objects.

```python
users = [
    "shakira",
    "KimKardashian",
    "rihanna",
    "jtimberlake",
    "KingJames",
    "neymarjr",
]
```
A list named `users` is created, containing the usernames of Twitter accounts.

```python
def get_followings(username):

    c = twint.Config()
    c.Username = username
    c.Pandas = True

    twint.run.Following(c)
    list_of_followings = twint.storage.panda.Follow_df

    return list_of_followings["following"][username]
```
A function named `get_followings` is defined to retrieve the list of users a given Twitter user follows. It utilizes the `twint` library to fetch the following list for a given username.

```python
followings = {}
following_list = []
for person in users:
    print("#####\nStarting: " + person + "\n#####")
    try:
        followings[person] = get_followings(person)
        following_list = following_list + followings[person]
    except KeyError:
        print("IndexError")
```
A loop iterates through each user in the `users` list. For each user, it attempts to retrieve their followings using the `get_followings` function and stores the result in the `followings` dictionary. Additionally, it aggregates all followings into the `following_list` list.

```python
Counter(following_list).most_common(10)
```
This line creates a Counter object from the `following_list` and retrieves the ten most common elements (users) along with their counts.

```python
follow_relations = {}
for following_user in followings.keys():
    follow_relation_list = []
    for followed_user in followings.keys():
        if followed_user in followings[following_user]:
            follow_relation_list.append(True)
        else:
            follow_relation_list.append(False)
    follow_relations[following_user] = follow_relation_list
```
A loop iterates through each user in the `followings` dictionary. For each user, it checks whether they follow each user in the `followings` dictionary. It then stores the result (True if they follow, False if not) in the `follow_relation_list`, which is then stored in the `follow_relations` dictionary.

```python
following_df = pd.DataFrame.from_dict(
    follow_relations, orient="index", columns=followings.keys()
)
following_df
```
This code converts the `follow_relations` dictionary into a pandas DataFrame where each row represents a user and each column represents whether the corresponding user follows that user. Finally, it displays the DataFrame.

-----