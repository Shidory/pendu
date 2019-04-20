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

        print(self.lbl_pendu.text()[2])

        self.cbx_choice_action()
        self.btn_a.clicked.connect(self.btn_a_clicked)
        self.btn_n.clicked.connect(self.btn_n_clicked)

    def telephone(self):
        #print(self.btn_a.text().lower())
        wordGame = pm.select_telephone()
        choiceRandom = choice(wordGame)
        choiceGame = choiceRandom[0]

        self.lbl_pendu.setText(choiceGame)
        return choiceGame

    def btn_a_clicked(self):


        """if self.button.text().upper == "a":
            print("bouton b appuié")"""

    def btn_n_clicked(self):
        pass

    def btn_valider_clicked(self):

        letter = self.let_game.text()

        """for i in range(len(choiceRamdom)):
            pass"""

    def cbx_choice_action(self):

        if self.cbx_choice.currentText() == "Telephone":

            self.hash_choice_game()

    def hash_choice_game(self):
        newt = ""
        telephone = self.telephone()
        l = len(telephone)
        hash = "*"

        for leter in range(l):

            t = telephone[leter]
            newt += hash

            self.lbl_pendu.setText(newt)

        return telephone

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
