import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFrame
from UIMyBase import UIMy_base
from UIBecomeMember_frame import Ui_Frame_become_member
from PyQt5.QtCore import QDateTime

class UIBecomeMember(QFrame, UIMy_base, Ui_Frame_become_member):

    def __init__(self, parent=None, x=0, y=0, xx=1, yy=1, pushButton = None):

        super(UIBecomeMember, self).__init__()
        self.setupUi(self)
        self.my_layout(parent, x, y, xx, yy)
        self.extern_button = pushButton

    def on_lineEdit_mname_editingFinished(self):
        self.label_hint.setText('')
        print('on_lineEdit_mname_editingFinished')
        if self.dbcur.is_name(self.lineEdit_mname.text()):
            pass
        else:
            self.label_hint.setText("姓名格式有误")
            self.lineEdit_mname.setText('')

    def on_lineEdit_mtel_editingFinished(self):
        self.label_hint.setText('')
        print('on_lineedit_mtel_ditinFinished')
        if self.dbcur.is_tel(self.lineEdit_mtel.text()):
            pass
        else:
            self.label_hint.setText('电话号码格式有误')
            self.lineEdit_mtel.setText('')

    def on_pushButton_back_released(self):
        print('on_pubutthon_back_released')
        self.extern_button.show()
        self.hide()

    def on_pushButton_ensure_released(self):
        print('on_pushButthon_ensure_released')
        if self.lineEdit_mname.text() == '' or self.lineEdit_mtel.text() == '':
            return
        if self.dialog_yes_no("确写添加？"):
            self.add_member()
        else:
            pass

    def add_member(self):
        exec = "SELECT TOP 1 Mno FROM Member Order BY Mno Desc"
        self.dbcur.select_run_exec(exec)
        table =  self.dbcur.cursor_data_to_list()
        last_date = str(table[0][0])[1:9]
        current_date = str(QDateTime.toPyDateTime(QDateTime.currentDateTime()).date())

        x = current_date.split('-')
        current_date = x[0] + x[1] + x[2]
        if current_date == last_date:
            num = str(table[0][0])[9:]
            num = int(num)
            num = num + 1
            num = '000000' + str(num)
            num = num[len(num) - 6:]
        else:
            num = '000001'
        mno = 'V' + current_date + num
        if self.radioButton_man.isChecked():
            sex = '男'
        if self.radioButton_woman.isChecked():
            sex = '女'
        self.dbcur.member_insert(mno,
                                 self.lineEdit_mname.text(),
                                 sex,
                                 self.lineEdit_mtel.text(),
                                 str(self.dateEdit_mdate.text()),
                                 0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    bm = UIBecomeMember()
    bm.show()
    sys.exit(app.exec_())