from controller.main import *

from_choose, _ = loadUiType(os.path.join(os.path.dirname(__file__), "../view/choose.ui"))

class Choose(QMainWindow, from_choose):

    def __init__(self, parent = None):

        super(Main, self).__init__(parent)
        self.setupUi(self)