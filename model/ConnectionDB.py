import sqlite3

#################################################
#       Connection to DB                        #
#################################################

class ConnectionDB():

    connection = sqlite3.connect("../pendu.db")
    cursor = connection.cursor()
