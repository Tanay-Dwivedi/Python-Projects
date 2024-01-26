# Scrape IMDb

[IMDb](https://www.imdb.com/) is an online database that contains data about Movies, TV Shows, Streaming Shows, Video Games, Reviews, Ratings, and all other entertainment related data. Being an online database, it provides an API so that we can collect data from IMDb for various data science tasks.

-----

## Installation

```
pip install IMDbPY
```
Firstly import the `IMDbPY` library through the terminal that will help in the program.

-----

## Code Break:

```python
from imdb import IMDb

# Create an IMDb object and get information for a specific movie with ID "012346"
movie = IMDb().get_movie("012346")
print(movie)

# Print the directors of the movie
for director in movie["directors"]:
    print(director)
```

In this section, the code imports the IMDbPY library and creates an instance of the IMDb class. It then retrieves information for a specific movie with the IMDb ID "012346" using the `get_movie` method. The details of the movie, such as title, year, cast, directors, etc., are printed. Additionally, a loop iterates through the directors of the movie, printing each director.

```python
movies = IMDb().get_top250_movies()

# Print information for each movie in the top 250 list
for movie in movies:
    print(movie)
```

In this part of the code, it uses the `get_top250_movies` function to obtain a list of the top 250 movies on IMDb based on their ratings. Subsequently, a loop iterates through the list of movies, printing information about each movie.

The IMDbPY library is leveraged in this code to interact with IMDb's database programmatically, allowing users to access detailed information about movies, TV shows, and celebrities. It's important to note that IMDb's website structure or policies may change, affecting the functionality of web scraping libraries like IMDbPY. Checking the library documentation for updates or changes is advisable.

-----