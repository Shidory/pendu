from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys
import os

from_main, _ = loadUiType(os.path.join(os.path.dirname(__file__), "main.ui"))
#################################################
#               Class Main                      #
#################################################
class Main(QMainWindow, from_main):
    pass

#main function
def main():

    app = QApplication(sys.argv)

if __name__=='__main__':

    try:
        main()

    except Exception as e:
        print(e)