from bottle import run
from services import *

__author__ = 'Aishwarya Sharma'


run(server="cherrypy", host="localhost", port=8080, debug=True)
