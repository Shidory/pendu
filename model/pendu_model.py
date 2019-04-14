#################################################
#           Class PenduModel                    #
#################################################
class PenduModel():

    def select_animal(self):

        request = "SELECT nom INTO animal"
        cursor.execute(request)