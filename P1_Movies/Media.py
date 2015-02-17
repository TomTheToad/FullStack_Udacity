#=============================================================================
#    Pyton 3.4.2 Document
#    Written by Victor Asselta
#    for Full Stack Udacity NanoDegree
#    Project 1 Movies
#
#    version 1.0
#    Creates a class which allows the creation of
#    movie media objects with simple get and set methods.
#    
#    2-9-2015
#=============================================================================

import webbrowser
import IMDBSearch

class Movie():
    
    #Fields
    IMDBid = None
    title = None
    storyline = None
    cast = None
    plotSummary = None
    poster_image_url = None
    trailer_youtube_url = None
    tooltipHTMLContent = None
    
    
    # Constructor
    def __init__(self, imdb_id_number, poster_image, trailer_youtube):
        self.IMDBid = imdb_id_number
        
        self.searchResults = IMDBSearch.searchIMDB(self.IMDBid)
        
        self.title = self.searchResults.getTitle()
        self.year = self.searchResults.getYear()
        self.storyline = self.searchResults.getPlot()
        self.briefCast = self.searchResults.getBriefCast()
        self.plotSummary = self.searchResults.getPlotSummary()
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
        self.tooltipHTMLContent = "<image src='images/IMDB-535x333.png' width='235' height='133' alt='IMDB Logo' id='IMDBLogo'><h4>" +self.title+" ("+self.year+")" + "</h4><h4>Cast:</h4>" +self.briefCast+ "<h4>Plot:</h4>" +self.plotSummary+ "<br><em>Powered by IMDB.com</em>"
        
    def showTrailer(self):
        webbrowser.open(self.trailer_youtube_url)
    
    # Getters
    def getUniqueCatID(self):
        return self.uniqueCatID
    def getTitle(self):
        return self.title
    def getStoryLine(self):
        return self.storyline
    def getPosterImageURL(self):
        return self.poster_image_url
    def getTrailerURL(self):
        return self.trailer_youtube_url
    def getTooltipHTMLContent(self):
        return self.tooltipHTMLContent
        
    # "Show movie info added successfully"
    def showAddMovieInfo(self):
        movieInfo = "Movie Title: "+self.title+"\nCatalog ID: "+self.IMDBid+"\nAdded to Catalog\n"
        return movieInfo