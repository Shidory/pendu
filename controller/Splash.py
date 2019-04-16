from PyQt5.QtCore import *
from controller.main import *
import time


from_splash, _ = loadUiType(os.path.join(os.path.dirname(__file__), "../view/splash.ui"))

class Splash(QMainWindow, from_splash):

    def __init__(self, parent=None):

        super(Splash, self).__init__(parent)

class Progress(QThread):

    signal = pyqtSignal(int)

    def __init__(self, parent=None):

        QThread.__init__(self, parent)

    def run(self):

        i = 0
        while i < 101:
            time.sleep(0.1)
            self.signal.emit(i)
            i += 1