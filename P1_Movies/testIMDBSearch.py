#=============================================================================
#    Pyton 3.4.2 Document
#    Written by Victor Asselta
#    for Full Stack Udacity NanoDegree
#    Project 1 Movies
#
#    
#    2-9-2015
#=============================================================================

import imdb

i = imdb.IMDb(accessSystem='http')
movie = i.get_movie('0049223')
print(movie['plot'])