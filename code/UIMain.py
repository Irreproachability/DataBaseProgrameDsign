import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from UIMainWindow import Ui_MainWindow
from UIMyBase import UIMy_base


class MyWindow(QMainWindow, Ui_MainWindow, UIMy_base):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    buy = MyWindow()
    buy.show()
    sys.exit(app.exec_())