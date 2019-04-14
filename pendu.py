from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys
import os
import model.PenduModel

#################################################
#             Loading view                      #
#################################################

from_main, _ = loadUiType(os.path.join(os.path.dirname(__file__), "view/pendu.ui"))

#################################################
#               Class Main                      #
#################################################
class Main(QMainWindow, from_main):

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.btn_valider.clicked.connect(self.btn_valider_clicked)

    def btn_valider_clicked(self):

        letter = self.let_game.text()

        request = "SELECT nom INTO animal"

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
