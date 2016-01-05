import pymysql
from pymysql import cursors

__author__ = "Aishwarya Sharma"


class Connection:
    def __init__(self):
        self.connection = pymysql.connect(host="localhost", port=3306, user="test", password="test", db="weirdo_blog",
                                          cursorclass=cursors.DictCursor)

    def get_connection(self):
        return self.connection
