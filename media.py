class Movie:
    """This class stores info for a movie for display on a webpage"""

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """Initializes a movie instance"""
        # The movie title
        self.title = title
        # A link to an image of the movie poster
        self.poster_image_url = poster_image_url
        # A link to the youtube trailer for the movie
        self.trailer_youtube_url = trailer_youtube_url