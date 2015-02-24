#=============================================================================
#    Pyton 3.4.2 Document
#    Written by Victor Asselta
#    for Full Stack Udacity NanoDegree
#    Project 1 Movies
#    
#    version 1.0
#    Use this file to create the movie catalog and launch
#    the Fresh Tomatoes Site.
# 
#    2-11-2015
#=============================================================================

import Media
import fresh_tomatoes

# Field variable to hold Movie content.
movieList = None
    
# This method configures the movie content library by calling the Media class 
# and returns a list of entries. This method takes no arguments.
# Movie entries require IMDB id numbers, links to poster art and youtube trailers.
# See the Media.py class for full movie entry information.
def configureApp():
    print("Running IMDBpy Http query.....")
    
    forbiddenPlanet = Media.Movie("0049223",
                    "http://upload.wikimedia.org/wikipedia/commons/5/50/Forbiddenplanetposter.jpg",
                    "http://www.youtube.com/watch?v=8y4crGU7dkg")
    print(forbiddenPlanet.showAddMovieInfo())

    tron = Media.Movie("0084827",
                   "images/Tron_poster.jpg", #Using local source, links have been unreliable
                   "http://youtu.be/3efV2wqEjEY")
    print(tron.showAddMovieInfo())

    hackers = Media.Movie("0113243",
                    "http://upload.wikimedia.org/wikipedia/en/6/67/Hackersposter.jpg",
                    "http://www.youtube.com/watch?v=Ql1uLyuWra8")
    print(hackers.showAddMovieInfo())
    
    movieList = [forbiddenPlanet, tron, hackers]
    
    return movieList
 
# The runApp() method calls the configureApp() method to first build
# the content library for the Fresh Tomatoes site and then calls the
# Fresh Tomatoes open_movies_page to initiate the build of the site.
# This method does not take any arguments.   
def runApp():
    movies = configureApp()
    fresh_tomatoes.open_movies_page(movies)

# Launch Application - This is starting point for the application. 
runApp()
    
