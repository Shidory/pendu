from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys
import os

from_main, _ = loadUiType(os.path.join(os.path.dirname(__file__), "pendu.ui"))
#################################################
#               Class Main                      #
#################################################
class Main(QMainWindow, from_main):

    def __init__(self, parent=None):

        super(Main, self).__init__(parent)
        self.setupUi(self)

class GameInteligence():
    pass

#main function
def main():

    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()

if __name__=='__main__':

    try:
        main()

    except Exception as e:
        print(e)