import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFrame
from UIMyBase import UIMy_base
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDateTime
from UIBackBook_frame import Ui_Frame_back_book
from DbBase import DbDesignBase

class UIBackBook(QFrame, UIMy_base, Ui_Frame_back_book):
    def __init__(self, parent=None, x=0, y=0, xx=1, yy=1, SMno = '', pushButton=None):
        super(UIBackBook, self).__init__()
        self.setupUi(self)
        self.my_layout(parent, x, y, xx, yy)
        self.sMno = SMno
        self.extern_button = pushButton
        self.init()

    def init(self):
        self.clear()
        self.show()

    def clear(self):
        self.lineEdit_brmno.setText('')
        self.lineEdit_brbno.setText('')
        self.lineEdit_brnum.setText('')
        self.lineEdit_brprice.setText('')

    def on_pushButton_clear_released(self):
        print("on_pushButton_clear_released")
        self.clear()


    def on_pushButton_ensure_released(self):
        print('on_pushButton_ensure_released')

        if self.lineEdit_brprice.text()!='' and self.lineEdit_brnum.text()!='' and self.lineEdit_brmno!='' and self.lineEdit_brbno!='':
            self.dbcur.select_run_exec("SELECT TOP 1 * FROM BackRecords order BY BRdate DESC")
            table = self.dbcur.select_cursor_data_to_list()
            last_date = table[0][0]
            crrurent_date = str(QDateTime.toPyDateTime(QDateTime.currentDateTime()).date())
            crrurent_time = str(QDateTime.toPyDateTime(QDateTime.currentDateTime()).time())
            print(crrurent_date,crrurent_time)
            if last_date == crrurent_date:
                brno = int(table[0][1])
                print("srno", brno)
                brno = brno + 1
                brno = '000000' + str(brno)
                brno = brno[len(brno) - 6:]
            else:
                brno = '000001'

            flag = self.dbcur.back_records_insert(brno,
                                           self.lineEdit_brbno.text(),
                                           self.lineEdit_brmno.text(),
                                           self.sMno,
                                           self.lineEdit_brprice.text(),
                                           self.lineEdit_brnum.text(),
                                           crrurent_time,
                                           crrurent_date)

            if flag:
                self.dialog_text('退货成功')
            else:
                self.dialog_text('退化失败 输入数据错误')
        else:
            pass

    def on_lineEdit_brmno_editingFinished(self):
        print('on_lineEdit_brmno_editingFinished')
        self.label_hint.setText('')

    def on_lineEdit_brbno_editingFinished(self):
        print('on_lineEdit_brbno_editingFinished')
        self.label_hint.setText('')

    def on_lineEdit_brprice_editingFinished(self):
        print('on_lineEdit_brprice_editingFinished')
        self.label_hint.setText('')

    def on_lineEdit_brnum_editingFinished(self):
        print('on_lineEdit_brnum_editingFinished')
        self.label_hint.setText('')

    def on_pushButton_back_released(self):
        print('on_puchButton_back_released')
        self.label_hint.setText('')
        self.close()
        try:
            self.extern_button.show()
        except AttributeError:
            print('NO Extern Button')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    buy = UIBackBook(SMno='4584445321')
    buy.show()
    sys.exit(app.exec_())