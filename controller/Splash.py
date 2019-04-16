from PyQt5.QtCore import *
from controller.main import *


from_splash, _ = loadUiType(os.path.join(os.path.dirname(__file__), "../view/splash.ui"))

class Splash(QMainWindow, from_splash):
    pass

class Progress(QThread):

    signal = pyqtSignal(int)

    def __init__(self, parent=None):

        QThread.__init__(self, parent)

    def run(self):
        pass