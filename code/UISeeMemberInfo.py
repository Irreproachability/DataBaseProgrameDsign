import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFrame
from UIMyBase import UIMy_base
from UISeeMemberInfo_frame import Ui_Frame_see_member_info
from PyQt5.QtCore import QDateTime

class UISeeMemberInfo(QFrame, UIMy_base, Ui_Frame_see_member_info):

    def __init__(self, parent=None, x=0, y=0, xx=1, yy=1, pushButton = None):
        super(UISeeMemberInfo, self).__init__()
        self.setupUi(self)
        self.my_layout(parent, x, y, xx, yy)
        self.extern_button = pushButton
        self.table = []

    def on_pushButton_see_released(self):
        print('on_pushButton_see_released')
        self.label_hint.setText('')
        self.info_clear()
        self.pushButton_change.setEnabled(False)
        self.lineEdit_mtel.setEnabled(False)
        text = self.lineEdit_seach_text.text()
        text = self.dbcur.str_add_quotation(text)
        if text == '':
            return
        if self.radioButton_mname.isChecked():
            exec = self.dbcur.select_parmeter_deal("Member", Mname = text)
        elif self.radioButton_mno.isChecked():
            exec = self.dbcur.select_parmeter_deal("Member", Mno = text)
        elif self.radioButton_mtel.isChecked():
            exec = self.dbcur.select_parmeter_deal("Member", Mtel = text)
        else:
            return

        self.dbcur.select_run_exec(exec)
        table = self.dbcur.cursor_data_to_list()
        print(table)
        if len(table):
            self.lineEdit_mno.setText(str(table[0][0]))
            self.lineEdit_manme.setText(str(table[0][1]))
            self.lineEdit_msex.setText(str(table[0][2]))
            self.lineEdit_mtel.setText(str(table[0][3]))
            self.lineEdit_mbirth.setText(str(table[0][4]))
            self.lineEdit_minte.setText(str(table[0][5]))

            self.pushButton_change.setEnabled(True)
            self.table = table[0]

        else:
            self.label_hint.setText("会员不存在")
            self.lineEdit_seach_text.setText("")

    def on_pushButton_change_released(self):
        print('on_puchButton_change_released')
        self.lineEdit_mtel.setEnabled(True)

    def on_lineEdit_mtel_editingFinished(self):
        print('on_lineEdit_mtel_editingFinished')
        if self.dbcur.is_tel(self.lineEdit_mtel.text()):
            self.pushButton_ensure.setEnabled(True)
        else:
            self.label_hint.setText("电话号码输入格式有误")

    def info_clear(self):
        self.lineEdit_mno.setText('')
        self.lineEdit_manme.setText('')
        self.lineEdit_msex.setText('')
        self.lineEdit_mtel.setText('')
        self.lineEdit_mbirth.setText('')
        self.lineEdit_minte.setText('')

    def on_pushButton_ensure_released(self):
        print('on_puchButton_change_released')
        if self.table[3] == self.lineEdit_mtel.text():
            self.label_hint.setEnabled('信息未做修改')
            return
        else:
            exec = self.dbcur.updata_parmeter_deal('Member', {"Mtel":self.lineEdit_mtel.text()}, {'Mno':self.table[0]})
            if self.dbcur.update_run_exec(exec):
                self.dialog_text("修改成功")
                self.pushButton_ensure.setEnabled(False)
                # self.pushButton_change.setEnabled(False)
                self.lineEdit_mtel.setEnabled(False)
                self.lineEdit_seach_text.setText('')
            else:
                self.dialog_text("修改失败")

    def on_pushButton_back_released(self):
        print('on_pushButton_back_released')
        self.close()
        try:
            self.extern_button.show()
        except AttributeError:
            print("NO EXTERN WIN")




if __name__ == '__main__':
    app = QApplication(sys.argv)
    semi= UISeeMemberInfo()
    semi.show()
    sys.exit(app.exec_())