import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFrame, QDialog
from UIMyBase import UIMy_base

from UIBookManage_frame import Ui_Frame_BookManage
from DbMyClass import *
class  UIBookManage(QFrame, Ui_Frame_BookManage , UIMy_base):
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
        super(UIBookManage, self).__init__()
        self.setupUi(self)
        self.time = 0
        self.connect_to_db()
        self.my_layout(parent, x, y, xx, yy)
        self.extern_button = pushButton
        self.mode = mode
        self.pushButton_pre_view_cancel.hide()

        if mode == self.MODE_ADD:
            self.label_bno.hide()
            self.pushButton_choose.hide()
            self.pushButton_del.hide()
            self.pushButton_change.hide()
            self.widget_3.hide()
            self.widget_2.hide()
            self.lineEdit_bno_choose.hide()
            self.pushButton_add.setEnabled(False)
            self.pushButton_add.setEnabled(False)

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
            self.label_table_name.setText('修改后的书籍信息')

    def on_pushButton_back_released(self):
        print("返回")
        self.close()
        try:
            self.extern_button.show()
            del(self)
        except AttributeError:
            print("no EXtern show")

    def on_pushButton_choose_released(self):
        print("book chose pushButton is prsed")
        bno = self.lineEdit_bno_choose.text()
        exec = self.dbcur.select_parmeter_deal("Book", Bno = DbSelect.str_add_quotation(bno))
        self.dbcur.run_exec(exec)
        list = self.dbcur.cursor_data_to_list()
        if len(list) == 0:
            self.pushButton_choose.setEnabled(False)
            self.dialog_text("该书号不存在", "提示")
            self.pushButton_choose.setEnabled(True)
            return
        else:
            self.lineEdit_bno_3.setText(str(bno))
            self.lineEdit_bname_3.setText(str(list[0][1]))
            self.lineEdit_bauthor_3.setText(str(list[0][2]))
            self.lineEdit_bprice_3.setText(str(list[0][3]))
            self.comboBox_btype_3.setCurrentText(str(list[0][4]))
            self.lineEdit_bpublish_3.setText(str(list[0][5]))
            self.lineEdit_bnum_3.setText(str(list[0][6]))
            self.pushButton_del.setEnabled(True)
            self.data_copy_widget1_to_widget3()

    def data_copy_widget1_to_widget3(self):
        self.lineEdit_bno.setText(str(self.lineEdit_bno_3.text().strip()))
        self.lineEdit_bname.setText(str(self.lineEdit_bname_3.text().strip()))
        self.lineEdit_bauthor.setText(str(self.lineEdit_bauthor_3.text().strip()))
        self.lineEdit_bprice.setText(str(self.lineEdit_bprice_3.text().strip()))
        self.comboBox_btype.setCurrentText(str(self.comboBox_btype_3.currentText().strip()))
        self.lineEdit_bpublish.setText(str(self.lineEdit_bpublish_3.text().strip()))
        self.lineEdit_bnum.setText(str(self.lineEdit_bnum_3.text().strip()))

    def data_clear_widget(self):
        self.lineEdit_bno.clear()
        self.lineEdit_bname.clear()
        self.lineEdit_bauthor.clear()
        self.lineEdit_bprice.clear()
        self.lineEdit_bpublish.clear()
        self.lineEdit_bnum.clear()
        self.comboBox_btype.setCurrentText("无")
    def data_clear_widget_3(self):
        self.lineEdit_bno_3.clear()
        self.lineEdit_bname_3.clear()
        self.lineEdit_bauthor_3.clear()
        self.lineEdit_bprice_3.clear()
        self.comboBox_btype_3.setCurrentText("无")
        self.lineEdit_bpublish_3.clear()
        self.lineEdit_bnum_3.clear()

    def on_pushButton_del_released(self):
        print('on_pushButton_del_released')
        bno = self.lineEdit_bno_3.text()
        if bno == '':
            return
        self.pushButton_del.setEnabled(False)
        flag = self.dialog_yes_no("是否删除？", "确认")
        if flag is True:
            if self.dbcur.delete_book(bno):
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
            flag = self.dbcur.book_insert(
                self.lineEdit_bno.text().strip(),
                self.lineEdit_bname.text().strip(),
                self.lineEdit_bauthor.text().strip(),
                self.lineEdit_bprice.text().strip(),
                self.comboBox_btype.currentText().strip(),
                self.lineEdit_bpublish.text().strip(),
                self.lineEdit_bnum.text().strip(),
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
        if self.check_add_book() is True:
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
            if self.dialog_yes_no("确认修改", "确认") is True:
                updata = self.dbcur.updata_parmeter_deal('Book', set, {'Bno':self.lineEdit_bno.text().strip()})
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
        if self.lineEdit_bno_3.text().strip() == self.lineEdit_bno.text().strip():
            pass
        else:
            set['Bno'] = self.lineEdit_bno.text().strip()
        if self.lineEdit_bname_3.text().strip() == self.lineEdit_bname.text().strip():
            pass
        else:
            set['Bname'] = self.lineEdit_bname.text().strip()
        if self.lineEdit_bauthor_3.text().strip() == self.lineEdit_bauthor.text().strip():
            pass
        else:
            set['Bauthor'] = self.lineEdit_bauthor.text().strip()
        if self.lineEdit_bprice_3.text().strip() == self.lineEdit_bprice.text().strip():
            pass
        else:
            set['Bprice'] = self.lineEdit_bprice.text().strip()
        if self.comboBox_btype.currentText().strip() == self.comboBox_btype.currentText().strip():
            pass
        else:
            set['Btype'] = self.comboBox_btype.currentText().strip()
        if self.lineEdit_bpublish_3.text().strip() == self.lineEdit_bpublish.text().strip():
            pass
        else:
            set['Bpublish'] = self.lineEdit_bpublish.text().strip()
        if self.lineEdit_bnum_3.text().strip() == self.lineEdit_bnum.text().strip():
            pass
        else:
            set['Bnum'] = self.lineEdit_bnum.text().strip()
        return set

    def check_add_book(self):
        flag =  DbInsert.insert_data_check_book(
            self.lineEdit_bno.text().strip(),
            self.lineEdit_bname.text().strip(),
            self.lineEdit_bauthor.text().strip(),
            self.lineEdit_bprice.text().strip(),
            self.comboBox_btype.currentText().strip(),
            self.lineEdit_bpublish.text().strip(),
            self.lineEdit_bnum.text().strip(),
            )
        if flag == DbInsert.BOOK_INSERT_OK:
            return True
        else:
            return False


    MODE_ADD = 1
    MODE_DEL = 2
    MODE_CHANGE = 3

if __name__ == '__main__':
    app = QApplication(sys.argv)
    book_choose = UIBookManage()
    book_choose.show()
    sys.exit(app.exec_())