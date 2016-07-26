import media
import fresh_tomatoes


toy_story = media.Movie(
    # title
    "Toy Story",
    #synopsis
    "A story of a boy and his toys that come to life",
    #poster
    "http://vignette4.wikia.nocookie.net/disney/images/4/4c/Toy-story-movie-posters-4.jpg/revision/latest?cb=20140816182710",
    #YouTube trailer
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie(
    "Avatar",
    "Guy goes to other planet, lives in blue body -- it's basically 'Dances with Wolves' tbh,",
    "http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp",
    "www.youtube.com/watch?v=uZNHIU3uHT4")

the_big_lebowski = media.Movie(
    "The Big Lebowski",
    "Guy tries to get his rug back, drinks white russians, encounters white Germans",
    "http://goo.gl/2cxt3f",
    "https://www.youtube.com/watch?v=cd-go0oBF4Y")

back_to_the_future = media.Movie(
    "Back to the Future",
    "Guy kisses his mom in car, gross. Watch if you like Rick and Morty",
    "http://goo.gl/IxgBni",
    "https://www.youtube.com/watch?v=yosuvf7Unmg")

time_bandits = media.Movie(
    "Time Bandits",
    "I think god comes in at some point and there's a villain with kitchen wrap as an outfit",
    "http://goo.gl/yndMxB",
    "https://www.youtube.com/watch?v=Yd4DBq8a2y0")

fight_club = media.Movie(
    "Fight Club",
    "Brad Pitt got dem abs, yo. Edward Norton can't sleep, yo. Don't do steroids, brah.",
    "http://goo.gl/BR5nIh",
    "https://www.youtube.com/watch?v=SUXWAEX2jlg")

#create an array of movie objects
movies = [toy_story, avatar, the_big_lebowski, back_to_the_future, time_bandits, fight_club]

fresh_tomatoes.open_movies_page(movies)

#experimenting with __doc__, __name__, and __module__
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)

