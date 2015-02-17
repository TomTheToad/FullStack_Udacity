This project created by Victor Asselta for Udacity Full Stack
course project 1.

Version 1.0 Project 1 Movies Website:
*************************************
The Fresh Tomatoes Site is launched by way of the runApp.py file.
The files contained within untilize Python version 3.4.1. An internet
connection is necessary to run the http request to IMDBpy for the movie
content, links to CDNs for JQuery and Modernizr.

Know issues with version 1.0:
*****************************
1) The loading speed is somewhat slow thanks to the http request made to
IMDB.com through IMDBpy. The next version, after completion of the SQL course,
should utilize a local database to store the mostly dynamically created catalog.
2) In console there will also be a warning from IMDBpy if your system does not have
the lxml library installed.
3) There are currently two calls to JQuery(1.10.1 and 1.11.2). 1.11.2 and the
associated UI call are necessary for tooltip creation. This is probably
unnecessary and one should be dumped in version two. As is modernizr is being used
to asynchronously load JQuery 1.11.2 to help with speed.
4) Tooltip windows flicker in some browsers due to block href link in fresh_tomatoes.py
on line 151.

File Structure:
***************
P1_Movies
|
|__fresh_tomatoes.py
|__IMDBSearch.py
|__Media.py
|__readME.txt
|__runApp.py
|____css/
|		|__tomatoesStyle.css
|		|__tomatoesStyleIE.css
|
|
|____images/
|		|__ieTransparent.gif
|		|__IMDB-535x333.png
|		|__Tron_poster.jpg
|
|
|____scripts/
		|__modernizr.custom.68768.js
		|__tooltip.js	
		
