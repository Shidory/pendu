from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from model.
import sys
import os


#################################################
#             Loading view                      #
#################################################

from_main, _ = loadUiType(os.path.join(os.path.dirname(__file__), "../view/pendu.ui"))

#################################################
#               Class Main                      #
#################################################
class Main(QMainWindow, from_main):

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.btn_valider.clicked.connect(self.btn_valider_clicked)

    def btn_valider_clicked(self):

        #pm means pendu model
        pm = Pendu
        letter = self.let_game.text()

        """for i in range (len(result)):
            pass"""

# main function
def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()


if __name__ == '__main__':

    try:
        main()

    except Exception as e:
        print(e)
