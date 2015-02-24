#=============================================================================
#    Pyton 3.4.2 Document
#    Written by Victor Asselta
#    for Full Stack Udacity NanoDegree
#    Project 1 Movies
#    
#    version 1.0
#    CLass that allows access to IMDBpy module
#    with simple get arguments.
#
#    for more information and copyright information
#    on IMDBpy see http://imdbpy.sourceforge.net
#
#    2-11-2015
#=============================================================================

import imdb

class searchIMDB():
    
    # Fields for instance movie data returned from IMDB.
    title = None
    year = None
    cast = None
    briefCast = None
    summary = None
    plot = None
    movieID = None
    movie = None
    
    # Constructor:
    # This constructor takes an IMDB movie ID and initializes IMDB http access and fetches
    # the movie data.
    def __init__(self, movieID):
        i = imdb.IMDb(accessSystem='http')
        self.movie = i.get_movie(movieID)
        
    # Returns movie ID class variable for current movie instance:
    def getID(self):
        return self.movieID
    
    # Returns title for current movie instance from IMDB search results:
    def getTitle(self):
        self.title = self.movie['title']
        return self.title
    
    # Returns year for current movie instance from IMDB search results:
    def getYear(self):
        self.year = str(self.movie['year'])
        return self.year
    
    # Returns cast list for current movie instance from IMDB search results:
    def getCast(self):
        self.cast = self.movie['cast']
        return self.cast
    
    # Retrieves and truncates a cast list for current movie IMDB search results:
    def getBriefCast(self):
        longCast = self.movie['cast']
        content = " "
        itemCount = 0
        # Convert list query from IMDB to a string and shorten.
        for item in longCast:
            content += str(item) + ","
            itemCount += 1
            if(itemCount > 5):
                content+= "  ... "
                return content
        return content
    
    # Returns an IMDB prepared summary for current movie instance from IMDB search results:
    def getSummary(self):
        self.summary = self.movie.summary()
        return self.summary
    
    # Returns plot for current movie instance from IMDB search results:
    def getPlot(self):
        self.plot = self.movie['plot']
     
    # Returns a truncated plot summary from IMDB search results:   
    def getPlotSummary(self):
        longPlot = self.movie['plot']
        # Convert query from IMDB to a string and shorten.
        str(longPlot)
        plotSummary = " "
        for c in longPlot:
            plotSummary += c
            if(c > 50):
                plotSummary += "  ..."
                return plotSummary
        print(plotSummary)
        return plotSummary
            
