from PyQt5.QtCore import QSize
from PyQt5.uic import loadUiType
import sys
import os
from_choose, _ = loadUiType(os.path.join(os.path.dirname(__file__), "../view/splash.ui"))

class Splash():
    pass