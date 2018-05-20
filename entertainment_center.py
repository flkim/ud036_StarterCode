# This module creates instances of the Movie class
# and puts them in a list so that the corresponding
# movies can be displayed on a webpage.

import media
import fresh_tomatoes

# Create Movie instances
movie1 = media.Movie("A Quiet Place",
                     "https://ia.media-imdb.com/images/M/MV5BMjI0MDMzNTQ0M15BMl5BanBnXkFtZTgwMTM5NzM3NDM@._V1_SY1000_CR0,0,674,1000_AL_.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=p9wE8dyzEJE")

movie2 = media.Movie("Avengers: Infinity War",
                     "https://ia.media-imdb.com/images/M/MV5BMjMxNjY2MDU1OV5BMl5BanBnXkFtZTgwNzY1MTUwNTM@._V1_SY1000_CR0,0,674,1000_AL_.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

movie3 = media.Movie("Incredibles 2",
                     "https://ia.media-imdb.com/images/M/MV5BMTEzNzY0OTg0NTdeQTJeQWpwZ15BbWU4MDU3OTg3MjUz._V1_SY1000_CR0,0,674,1000_AL_.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=i5qOzqD9Rms")

# Compile Movie instances in a list
movieList = [movie1, movie2, movie3]

# Display movies in a webpage
fresh_tomatoes.open_movies_page(movieList)




