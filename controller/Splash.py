from PyQt5.QtCore import *
from controller.main import *
import time


from_splash, _ = loadUiType(os.path.join(os.path.dirname(__file__), "../view/splash.ui"))

class Splash(QMainWindow, from_splash):

    def __init__(self, parent=None):

        super(Splash, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        progress = Progress(self)
        progress.signal.connect(self.progress)
        progress.start()

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