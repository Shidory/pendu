import sqlite3

#################################################
#       Connection to DB                        #
#################################################

class ConnectionDB():

    def __init__(self):

        connection = sqlite3.connect("../pendu_db.db")
        cursor = connection.cursor()
