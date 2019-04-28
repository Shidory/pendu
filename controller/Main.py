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

        #self.cbx_choice_action()
        #self.btn_n.clicked.connect(self.btn_n_clicked)
        #self.btn_n.clicked.connect(self.pendu)
        self.pendu()

    """Method who return telephone choices"""
    def telephone(self):

        selectWord = pm.select_telephone()
        choiceWord = choice(selectWord)
        wordGame = choiceWord[0]

        return wordGame

    def get_letter(self):

        letterN = self.btn_n.text().lower()

        return letterN

    def hash_choice_game(self, mysteriousWord, letterWin):

        """newt = ""
        telephone = self.telephone()
        l = len(telephone)
        hash = "*"

        for leter in range(l):

            t = telephone[leter]
            newt += hash

            self.lbl_pendu.setText(newt)

        return telephone"""
        hash = "*"
        wordHash = ""

        for letter in mysteriousWord:
            if letter in letterWin:
                wordHash += letter
            else:
                wordHash += hash
        self.lbl_pendu.setText(wordHash)

        return wordHash

    def pendu(self):

        letter = self.get_letter()
        mysteriousWord = self.telephone()
        letterWin = []
        wordWin = self.hash_choice_game(mysteriousWord, letterWin)

        if letter in mysteriousWord:
            letterWin.append(letter)
            self.hash_choice_game(mysteriousWord, letterWin)

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
