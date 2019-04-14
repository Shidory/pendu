from model.ConnectionDB import *

#################################################
#           Class PenduModel                    #
#################################################

cDb = ConnectionDB()

class PenduModel():

    def select_animal(self):

        request = "SELECT nom INTO animal"
        cDb.cursor.execute(request)
        result = cDb.cursor.fetchall()

        return result