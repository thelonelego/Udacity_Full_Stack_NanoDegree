import urllib
import webbrowser

class Movie():
    """ This class, "Movie", provides a way to store movie related information """

    #class variable that all movies share
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    #initialization method that creates a movie object
    def __init__(self, movie_title, movie_story, movie_poster, movie_trailer):
        self.title = movie_title
        self.story = movie_story
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer

    #method that opens a web browser to show the current movie's trailer on YouTube
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
