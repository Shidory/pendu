from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys
import os

from_main, _ = loadUiType()
#################################################
#               Class Main                      #
#################################################
class Main:
    pass

#main function
def main():

    app = QApplication(sys.argv)

if __name__=='__main__':

    try:
        main()

    except Exception as e:
        print(e)