from model.ConnectionDB import *

#################################################
#           Class PenduModel                    #
#################################################

cDb = ConnectionDB()

class PenduModel():

    def select_animal(self):

        request = "SELECT marque FROM telephone"
        cDb.cursor.execute(request)
        result = cDb.cursor.fetchall()

        return result