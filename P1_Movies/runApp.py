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

# Fields
movieList = None
    
# Create Movie Catalog
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
 
# Call to configure app by http query and then run the app after load is complete.   
def runApp():
    movies = configureApp()
    fresh_tomatoes.open_movies_page(movies)

# Launch Application
runApp()
    
