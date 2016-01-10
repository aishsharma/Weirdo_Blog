from bottle import run
from services import *
import database.alchemy_tables as tbls

__author__ = 'Aishwarya Sharma'


# Starting Server
run(server="cherrypy", host="localhost", port=8080, debug=True)
