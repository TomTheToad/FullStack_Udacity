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
    
    # Fields
    title = None
    year = None
    cast = None
    briefCast = None
    summary = None
    plot = None
    movieID = None
    movie = None
    
    def __init__(self, movieID):
        i = imdb.IMDb(accessSystem='http')
        self.movie = i.get_movie(movieID)
        
    def getID(self):
        return self.movieID
    
    def getTitle(self):
        self.title = self.movie['title']
        return self.title
    
    def getYear(self):
        self.year = str(self.movie['year'])
        return self.year
    
    def getCast(self):
        self.cast = self.movie['cast']
        return self.cast
    
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
    
    def getSummary(self):
        self.summary = self.movie.summary()
        return self.summary
    
    def getPlot(self):
        self.plot = self.movie['plot']
        
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
            
