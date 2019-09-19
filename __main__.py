import UILogin
import sys
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = UILogin.UILogin()
    sys.exit(app.exec_())
