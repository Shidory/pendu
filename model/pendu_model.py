import model.connection_db

#################################################
#           Class PenduModel                    #
#################################################
class PenduModel():

    def select_animal(self):

        request = "SELECT nom INTO animal"
        self.cursor.execute(request)
        result = self.cursor.fetchall()