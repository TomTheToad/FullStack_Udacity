This project created by Victor Asselta for Udacity Full Stack
course project 1.

Version 1.0 Project 1 Movies Website:
*************************************
The Fresh Tomatoes Site is launched by way of the runApp.py file.
The files contained within were written mostly with Python version 3.4.1 syntax
but have been tested with 2.7 successfully. An internet
connection is necessary to run the http request to IMDBpy for the movie
content, links to CDNs for JQuery and Modernizr. IMDBpy is required as listed
below but is also included in the virtual environment.

Requirements
*****************************
Python 2.7
IMDBpy
	which requires(SQLObject or SQLAlchemy included with the PiP install)
python-lxml
The included virtual environment is built with virtualEnv.

Know Issues with Version 1.0
****************************
1) Browser consoles may show a syntax error something akin to this: (Unexpected token',')
This appears to be an issue utilizing modernizr within a js template utilizing bootstrap 3.0.
It seems to be treating the script as a css marker.
2) There maybe an "unexpected css token" in bootstrap 3.0 files due to custom css?
3) When a user clicks on the link for the youtube trailer, the console records many html5 player error messages.
This seems to be related to the manner in which the method within fresh_tomatoes.py accesses the youtube link?


File Structure:
***************
P1_Movies
|
|__fresh_tomatoes.py
|__IMDBSearch.py
|__Media.py
|__readME.txt
|__runApp.py
|
|____activate/* virtualenv files including python 2.7 (too many to list)
|
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
|		|__modernizr.custom.68768.js
|		|__tooltip.js	
|
|____venv/* again virtualevn files
