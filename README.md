# Udacity_Full_Stack_NanoDegree

Author: John Patrick Lewis
Submission #1 Date: 07-26-2016
Udacity Full Stack Web Design Nanodegree +

Assignment: Movie Trailer Website

-- Purpose -- This assignment promotes basic practice in classes, imports, and functions.

-- Output -- At completion, the code creates a basic web page featuring movie names as
well as their respective poster and YouTube trailer.

code snippets:
-------------------------------------------------------------------------------
    -- Below is the Movie class, from which all Movie objects are created --

    class Movie():
    """ This class, "Movie", provides a way to store movie related information """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_story, movie_poster, movie_trailer):
        self.title = movie_title
        self.story = movie_story
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer

    def show_trailer(self):
        #urllib.urlopen(self.trailer)
        webbrowser.open(self.trailer_youtube_url)

-------------------------------------------------------------------------------

    -- The following code demonstrates the initialization of a Movie object. --
    -- In this case the movie is "The Big Lebowski" --

    the_big_lebowski = media.Movie(
    "The Big Lebowski",
    "Guy tries to get his rug back, drinks white russians, encounters white Germans",
    "http://goo.gl/2cxt3f",
    "https://www.youtube.com/watch?v=cd-go0oBF4Y")
    
-------------------------------------------------------------------------------    
    
    HOW TO RUN: 
    1) Make sure all requisiste files are in the appropriate directory.
    2) double-click the fresh_tomatoes.html file with a valid web broswer application (I recommend Google Chrome).
    

-------------------------------------------------------------------------------
