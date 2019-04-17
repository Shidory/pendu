from controller.Main import *

from_choose, _ = loadUiType(os.path.join(os.path.dirname(__file__), "../view/choose.ui"))

class Choose(QMainWindow, from_choose):

    def __init__(self, parent = None):

        super(Choose, self).__init__(parent)
        self.setupUi(self)

        #self.setWindowFlags(Qt.FramelessWindowHint)

        size_screen = QDesktopWidget().screenGeometry()
        size_window = self.geometry()
        self.move((size_screen.width() - size_window.width()) / 2,
                  (size_screen.height() - size_window.height()) / 2)

        self.btn_telephone.clicked.connect(self.btn_telephone_clicked)

    def btn_telephone_clicked(self):

        main = Main(self)
        main.show()