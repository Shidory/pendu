from model.ConnectionDB import *

#################################################
#           Class PenduModel                    #
#################################################

cDb = ConnectionDB()

class PenduModel():

    def select_telephone(self):

        request = "SELECT marque FROM telephone"
        cDb.cursor.execute(request)
        result = cDb.cursor.fetchall()

        return result

    def select_fruit(self):

        request = "SELECT name FROM fruit"
        cDb.cursor.execute(request)
        result = cDb.cursor.fetchall()
