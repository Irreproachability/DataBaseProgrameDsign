import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFrame, QDialog
from UIMyBase import UIMy_base

from UISalesManManage_frame import Ui_Frame_salesman_manage
from DbMyClass import *
class  UISanlesManManage(QFrame, Ui_Frame_salesman_manage , UIMy_base):
    def __init__(self, parent=None, x = 0, y = 0, xx = 1, yy = 1, mode = None, pushButton = None):
        """

        :param parent: 父窗口
        :param x: X位置
        :param y: Y位置
        :param xx: 占高度
        :param yy: 占宽度
                布局管理， 咱也不太明白怎么回事
        :param mode:模式  MODE_ADD MODE_DEL MODE_CHANGE 三种
        :param pushButton: 按本返回键后要显示的内容，不一定要是pushButtonButton
        """
        super(UISanlesManManage, self).__init__()
        self.setupUi(self)
        self.time = 0
        self.connect_to_db()
        self.my_layout(parent, x, y, xx, yy)
        self.extern_button = pushButton
        self.mode = mode
        self.pushButton_pre_view_cancel.hide()
        if mode == self.MODE_ADD:
            self.label_SMno.hide()
            self.pushButton_choose.hide()
            self.pushButton_del.hide()
            self.pushButton_change.hide()
            self.widget_3.hide()
            self.widget_2.hide()
            self.lineEdit_SMno_choose.hide()
            self.pushButton_add.setEnabled(False)
            # self.pushButton_add.setEnabled(False)

        elif mode == self.MODE_DEL:
            self.pushButton_change.hide()
            self.pushButton_add.hide()
            self.pushButton_del.setEnabled(False)
            self.widget.hide()
            self.widget_4.hide()

        elif mode == self.MODE_CHANGE:
            self.pushButton_del.hide()
            self.pushButton_add.hide()
            self.pushButton_change.setEnabled(False)
            self.label_table_name.setText('修改后的人员信息')

    def on_pushButton_back_released(self):
        print("on_pushButton_back_released")
        try:
            self.close()
        except AttributeError:
            return
        try:
            self.extern_button.show()
        except AttributeError:
            print("no EXtern show")


    def on_pushButton_choose_released(self):
        print("book chose pushButton is prsed")
        SMno = self.lineEdit_SMno_choose.text()
        exec = self.dbcur.select_parmeter_deal("SalesMan", Bno = DbSelect.str_add_quotation(SMno))
        self.dbcur.run_exec(exec)
        list = self.dbcur.cursor_data_to_list()
        if len(list) == 0:
            self.pushButton_choose.setEnabled(False)
            self.dialog_text("该书号不存在", "提示")
            self.pushButton_choose.setEnabled(True)
            return
        else:
            self.lineEdit_SMno_3.setText(str(SMno))
            self.lineEdit_SMname_3.setText(str(list[0][1]))
            self.comboBox_Smsex_3.setCurrentText(str(list[0][3]))
            self.lineEdit_SMpassword_3.setText(str(list[0][2]))

            self.pushButton_del.setEnabled(True)
            self.data_copy_widget1_to_widget3()

    def data_copy_widget1_to_widget3(self):
        self.lineEdit_SMno.setText(str(self.lineEdit_SMno_3.text().strip()))
        self.lineEdit_SMname.setText(str(self.lineEdit_SMname_3.text().strip()))
        self.comboBox_SMsex.setCurrentText(str(self.comboBox_Smsex_3.currentText().strip()))
        self.lineEdit_SMpassword.setText(str(self.lineEdit_SMpassword_3.text().strip()))

    def data_clear_widget(self):
        self.lineEdit_SMno.clear()
        self.lineEdit_SMname.clear()
        self.comboBox_SMsex.clear()
        self.lineEdit_SMpassword.clear()

    def data_clear_widget_3(self):
        self.lineEdit_SMno_3.clear()
        self.lineEdit_SMname_3.clear()
        self.comboBox_SMsex_3.setCurrentText("无")
        self.lineEdit_SMpassword_3.clear()

    def on_pushButton_del_released(self):
        print('on_pushButton_del_released')
        smno = self.lineEdit_SMno_3.text()
        if smno == '':
            return
        self.pushButton_del.setEnabled(False)
        flag = self.dialog_yes_no("是否删除？", "确认")
        if flag is True:
            if self.dbcur.delete_salesMan(smno):
                self.dialog_text("删除成功","提示窗")
                self.data_clear_widget_3()
                self.pushButton_del.setEnabled(False)
            else:
                self.dialog_text("删除失败 可能存在外键限制","提示窗")

    def on_pushButton_add_released(self):
        print("on_pushButton_add_released")
        self.pushButton_add.setEnabled(False)
        flag = self.dialog_yes_no("是否添加","提示")
        if flag is True:
            flag = self.dbcur.salesman_insert(
                self.lineEdit_SMno.text().strip(),
                self.lineEdit_SMname.text().strip(),
                self.comboBox_SMsex.currentText().strip(),
                self.lineEdit_SMpassword.text().strip()
            )
            if flag is True:
                self.dialog_text("添加成功", "提示")
                self.widget_3.setEnabled(True)
            else:
                self.dialog_text("添回失败 可能主键冲突", "提示")
        else:
            self.pushButton_add.setEnabled(True)

    def on_pushButton_pre_view_released(self):

        print("on_pushButton_pre_view_released")
        if self.check_add_selasMan() is True:
            self.widget.setEnabled(False)
            self.pushButton_pre_view_cancel.show()
            self.pushButton_pre_view.hide()
            self.pushButton_add.setEnabled(True)
            self.pushButton_change.setEnabled(True)
        else:
            self.pushButton_pre_view.setEnabled(False)
            self.dialog_text("输入模式有误 请检查看重新输入", "提示")
            self.pushButton_pre_view.setEnabled(True)

    def on_pushButton_pre_view_cancel_released(self):
        self.widget.setEnabled(True)
        self.pushButton_pre_view_cancel.hide()
        self.pushButton_pre_view.show()
        self.pushButton_add.setEnabled(False)
        self.pushButton_change.setEnabled(False)

    def on_pushButton_cancel_released(self):
        print('on_pushButton_cancel_released')
        self.data_clear_widget_3()
        self.data_clear_widget()
        self.pushButton_del.setEnabled(False)
        self.pushButton_change.setEnabled(False)

    def on_pushButton_change_released(self):
        print('on_puchButton_change_released')
        self.pushButton_change.setEnabled(False)
        set = self.get_set_parmeter()
        print(set)
        if len(set) == 0:
            self.dialog_text("内容未做变更", '提示')
        else:
            if self.dialog_yes_no("确认修改？", "确认") is True:
                updata = self.dbcur.updata_parmeter_deal('SalesMan', set, {'SMno':self.lineEdit_SMno.text().strip()})
                # print(updata)
                if self.dbcur.update_run_exec(updata):
                    self.dialog_text("修改成功", '提示')
                else:
                    self.dialog_text("修改失败", '提示')
            else:
                self.widget.setEnabled(True)
                self.pushButton_pre_view.show()
                self.pushButton_pre_view_cancel.hide()

    def get_set_parmeter(self):
        set = {}
        if self.lineEdit_SMno_3.text().strip() == self.lineEdit_SMno.text().strip():
            pass
        else:
            set['SMno'] = self.lineEdit_SMno.text().strip()

        if self.lineEdit_SMname_3.text().strip() == self.lineEdit_SMname.text().strip():
            pass
        else:
            set['SMname'] = self.lineEdit_SMname.text().strip()

        if self.lineEdit_SMpassword_3.text().strip() == self.lineEdit_SMpassword.text().strip():
            pass
        else:
            set['SMpassword'] = self.lineEdit_SMpassword.text().strip()

        if self.comboBox_Smsex_3.currentText().strip() == self.comboBox_SMsex.currentText().strip():
            pass
        else:
            set['SMsex'] = self.comboBox_SMsex.currentText().strip()

        return set

    def check_add_selasMan(self):
        flag =  DbInsert.insert_data_check_salesMan(
            self.lineEdit_SMno.text().strip(),
            self.lineEdit_SMname.text().strip(),
            self.comboBox_SMsex.currentText().strip(),
            self.lineEdit_SMpassword.text().strip(),
            )
        if flag == DbInsert.INSERT_OK:
            return True
        else:
            return False


    MODE_ADD = 1
    MODE_DEL = 2
    MODE_CHANGE = 3

if __name__ == '__main__':
    app = QApplication(sys.argv)
    SMManage = UISanlesManManage()
    SMManage.show()
    sys.exit(app.exec_())