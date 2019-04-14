import sqlite3

#################################################
#       Connection to DB                        #
#################################################

connection = sqlite3.connect("../pendu_db.db")
cursor = connection.cursor()