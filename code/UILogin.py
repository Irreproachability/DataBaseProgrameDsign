import sys
from PyQt5.QtWidgets import QApplication

from UILogin_frame import *
from PyQt5.QtWidgets import QFrame, QDialog
from PyQt5.Qt import QThread
from UIMyBase import UIMy_base
import time

from UIAdmini import UIAdmini
from UISearch import UISearch
from UISMMenu import UISMMenu
from UIMain import MyWindow

class  UILogin(QFrame, Ui_Frame_login_1, UIMy_base):
    def __init__(self, parent=None, x = 0, y = 0, xx = 1, yy = 1):
        super(UILogin, self).__init__()
        self.setupUi(self)
        self.time = 0

        self.win_main = MyWindow()
        self.win_main.show()
        self.my_layout(self.win_main, x, y, xx, yy)
        self.win_ad = None
        self.win_search = None
        self.win_smMenu = None

        # 统计点击间隔的
        self.perf_counter = time.perf_counter()
    def on_pushButton_login_released(self):

        QThread.msleep(200)
        login_type = self.login()
        if login_type != 0:
            print("登录成功")
            try:
                self.dialog_text("登录成功", "登录提示")
                if login_type == UILogin.WIN_EXTERN_ADMINI:
                    self.win_ad = UIAdmini(self.win_main, ano=self.username.text(),pushbutton=self)
                    self.win_ad.show()
                elif login_type == UILogin.WIN_EXTERN_SALEMAN:
                    self.win_smMenu = UISMMenu(self.win_main,0, 0, 1, 2, sMno=self.username.text(), pushButton=self)
                    self.win_smMenu.show()
            except TypeError:
                print("This Win is NO exist")
            except AttributeError:
                print("win Errow")
            finally:
                self.close()
        else:
            print("登录失败")
        QThread.msleep(200)

    def login(self):
        print("login")
        type = 0
        if self.time == 10:
            print("root")
            type = self.WIN_EXTERN_ROOT
        elif self.radioButton_Admini.isChecked():
            print("Admini")
            type = self.WIN_EXTERN_ADMINI
        elif self.radioButton_cust.isChecked():
            print("Salesman")
            type = self.WIN_EXTERN_SALEMAN

        username = self.username.text()
        password = self.password.text()

        if username == '' and password == '':
            self.time += 1
            self.label_warning.clear()
            if self.time == 5:
                self.pushButton_hide.setEnabled(True)
            elif self.time > 5:
                self.pushButton_hide.setEnabled(False)
                self.time = 0
            return 0
        # 连按处理
        import time
        counter =  time.perf_counter()
        space_time =  counter - self.perf_counter
        print(space_time)
        if space_time < 1.5:
            return 0

        self.perf_counter = counter
        import DbSelect
        Db = DbSelect.DbSelect()
        if type == self.WIN_EXTERN_ADMINI:
            # 管理员
            Db.select_administrator()

        elif type == self.WIN_EXTERN_SALEMAN:
            # 销售员
            Db.select_salesman()

        elif type == self.WIN_EXTERN_ROOT:
            # sa 帐户
            if username == 'sa' and password == '123':
                return type

        table_date = Db.cursor_data_to_list()
        for i in table_date:
            if i[0].strip() == username and i[3].strip() == password:
                self.label_warning.setText("登录成功")
                return type

        self.label_warning.setText("用户名或密码错误,请重新输入")
        self.time = 0
        return 0

    def on_pushButton_custer_released(self):
        self.win_search = UISearch(pushButton=self)
        self.win_search.my_layout(self.win_main,0, 0, 1, 1 )
        self.win_search.show()
        self.hide()

    def on_pushButton_hide_released(self):
        self.time += 1
        if self.time == 10:
            print("root")
        elif self.time > 10:
            self.time = 0

    def on_pushButton_quit_released(self):
        self.close()
        self.win_main.close()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    login = UILogin()
    sys.exit(app.exec_())

