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
#    Utilizes the custom IMDBSearch.py Class
#    
#    2-9-2015
#=============================================================================

import webbrowser
import IMDBSearch

class Movie():
    
    #Fields: Class variables for various movie parameters.
    IMDBid = None
    title = None
    storyline = None
    cast = None
    plotSummary = None
    poster_image_url = None
    trailer_youtube_url = None
    tooltipHTMLContent = None
    
    
    # Constructor:
    # This constructor takes supplied movie parameters and utilizes those to
    # initialize an IMDB search, using IMDBSearch.py, and populate instance fields.
    def __init__(self, imdb_id_number, poster_image, trailer_youtube):
        self.IMDBid = imdb_id_number
        
        # IMDB instance search declaration using IMDBSearch.py
        self.searchResults = IMDBSearch.searchIMDB(self.IMDBid)
        
        # Movie Title:
        self.title = self.searchResults.getTitle()
        # Movie Year:
        self.year = self.searchResults.getYear()
        # Movie Story line:
        self.storyline = self.searchResults.getPlot()
        # Truncated Cast list:
        self.briefCast = self.searchResults.getBriefCast()
        # IMDB generated plot summary including cast
        self.plotSummary = self.searchResults.getPlotSummary()
        # URL Poster link:
        self.poster_image_url = poster_image
        # youtube.com trailer link:
        self.trailer_youtube_url = trailer_youtube
        
        # Build tooltip window information:
        self.tooltipHTMLContent = "<image src='images/IMDB-535x333.png' width='235' height='133' alt='IMDB Logo' id='IMDBLogo'><h4>" +self.title+" ("+self.year+")" + "</h4><h4>Cast:</h4>" +self.briefCast+ "<h4>Plot:</h4>" +self.plotSummary+ "<br><em>Powered by IMDB.com</em>"
        
    # A method call to show the current instance movie trailer.
    # This is for the second, portfolio version, of this site.
    def showTrailer(self):
        webbrowser.open(self.trailer_youtube_url)
    
    # Getters
    # Getter functionality for second, portfolio version, of this site.
    # May need to add setter versions as well.
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
        
    # "Show movie info added successfully" to console output for data check
    # and trouble shooting.
    def showAddMovieInfo(self):
        movieInfo = "Movie Title: "+self.title+"\nCatalog ID: "+self.IMDBid+"\nAdded to Catalog\n"
        return movieInfo