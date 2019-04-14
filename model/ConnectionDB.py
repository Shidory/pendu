import sqlite3

#################################################
#       Connection to DB                        #
#################################################

class ConnectionDB():

    connection = sqlite3.connect("../pendu_db.db")
    cursor = connection.cursor()
