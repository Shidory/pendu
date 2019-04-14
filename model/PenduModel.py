"""from model.ConnectionDB import *

#################################################
#           Class PenduModel                    #
#################################################

cDb = ConnectionDB()"""
import sqlite3
connection = sqlite3.connect("pendu.db")
cursor = connection.cursor()
class PenduModel():

    def select_animal(self):

        request = "SELECT nom FROM animal"
        cursor.execute(request)
        result = cursor.fetchall()

        #return result