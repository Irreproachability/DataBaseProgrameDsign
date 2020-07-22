import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFrame
from UIMyBase import UIMy_base
from UIAdminiInfo_frame import Ui_Frame_admini_info


class UIAdminiInfo(QFrame, UIMy_base, Ui_Frame_admini_info):
    def __init__(self, parent=None, x=0, y=0, xx=1, yy=1, admini = '', pushButton=None):
        super(UIAdminiInfo, self).__init__()
        self.setupUi(self)
        self.my_layout(parent, x, y, xx, yy)
        self.ano = admini
        self.extern_button = pushButton
        self.tabel = []
        self.init()
        self.lineEdit_ano.setText(str(self.tabel[0][0]))
        self.lineEdit_aname.setText(str(self.tabel[0][1]))
        self.lineEdit_asex.setText(str(self.tabel[0][2]))

    def init(self, ano = None):
        if ano is not None:
            self.ano = ano
        self.clear()
        exec = self.dbcur.select_parmeter_deal('Administrator', Ano=self.ano)
        self.dbcur.select_run_exec(exec)
        self.tabel = self.dbcur.select_cursor_data_to_list()
        self.pushButton_ensure.hide()
        self.widget_password_change.hide()
        self.pushButton_cancel.hide()

    def clear(self):
        self.lineEdit_new1.setText('')
        self.lineEdit_new2.setText('')
        self.lineEdit_old.setText('')

    def on_pushButton_ensure_released(self):
        print('on_pushButton_ensure_released')
        if self.lineEdit_new1.text()!=self.lineEdit_new2.text():
            self.dialog_text('再次输入密码不一样')
            return

        elif self.lineEdit_old.text()!=self.tabel[0][3]:
            self.dialog_text('旧密码错误')
            return


        else:
            if self.dialog_yes_no("确认修改？"):
                exec = self.dbcur.updata_parmeter_deal('Administrator',
                                           {'Apassword':self.lineEdit_new1.text()},
                                            {'Ano':self.tabel[0][0]})
                if self.dbcur.update_run_exec(exec):
                    self.dialog_text("修改成功")
                    self.init()
                else:
                    self.dialog_text('修改失败')
            else:
                pass

    def on_pushButton_change_password_released(self):
        print('on_pushButton_password_change_released')
        self.widget_password_change.show()
        self.pushButton_ensure.show()
        self.pushButton_cancel.show()
    def on_pushButton_back_released(self):
        self.close()
        try:
            self.extern_button.show()
        except AttributeError:
            print("NO extern WIN")

    def on_pushButton_cancel_released(self):
        print('on_pushButton_cancel_released')
        self.init()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    buy = UIAdminiInfo(admini='4752123597')
    buy.show()
    sys.exit(app.exec_())