from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from model.PenduModel import *
from controller.Splash import *
from random import choice
import sys
import os


#################################################
#             Loading view                      #
#################################################

from_main, _ = loadUiType(os.path.join(os.path.dirname(__file__), "../view/pendu.ui"))

#################################################
#               Class Main                      #
#################################################

#pm means pendu model
pm = PenduModel()

class Main(QMainWindow, from_main):

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        size_screen = QDesktopWidget().screenGeometry()
        size_window = self.geometry()
        self.move((size_screen.width() - size_window.width()) / 2,
                  (size_screen.height() - size_window.height()) / 2)
        self.btn_a.clicked.connect(self.telephone)
        """if btn_telephone.clicked():

            telephone()

        self.btn_valider.clicked.connect(self.btn_valider_clicked)"""

    def telephone(self):
        print(self.btn_a.text().lower())
        wordGame = pm.select_animal()
        choiceRandom = choice(wordGame)

    def btn_letter_clicked(self):
    def btn_valider_clicked(self):

        letter = self.let_game.text()

        """for i in range(len(choiceRamdom)):
            pass"""

# main function
def main():
    app = QApplication(sys.argv)
    window = Splash()
    window.show()
    app.exec_()


if __name__ == '__main__':

    try:
        main()

    except Exception as e:
        print(e)
