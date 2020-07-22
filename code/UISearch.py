import sys
from PyQt5.QtWidgets import QApplication

from UISearch_frame import *
from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.Qt import QThread
import UIMyBase
from UITable import UiTable
from PyQt5.QtCore import QDateTime

class UISearch(QFrame, Ui_Frame_search, UIMyBase.UIMy_base):
    def __init__(self, parent=None, x = 0, y = 0, xx = 1, yy = 1, pushButton = None):
        super(UISearch, self).__init__()
        self.setupUi(self)
        self.extern_button = pushButton
        self.connect_to_db()
        self.win_table = UiTable()
        self.pushButton_weak.hide()
        x = ['图书编号', '书名', '作者', '价格', '种类', '出版社', '库存量', '销量']
        n = self.tableWidget.columnCount()
        for i in range(n):
            self.tableWidget.setHorizontalHeaderItem(i, QTableWidgetItem(''))

        self.my_layout(parent, x, y, xx, yy)
        self.win_table.setHorizontalHeader(x)
        self.win_table.setTableName("书籍查找")
        self.setHorizontalHeader(x)

    def setHorizontalHeader(self, *args):
        """

        :param args: 表头名
        :return:
        """
        if isinstance(args[0], list) or isinstance(args[0], tuple):
            args = args[0]
        i = -1

        n = self.tableWidget.size()

        for table_head in args:
            i = i + 1

            self.tableWidget.setHorizontalHeaderItem(i, QTableWidgetItem(table_head))

    def setTableDate(self, list):
        try:
            x = len(list)
            y = len(list[0])
        except IndexError:
            print("data is NULL")
            return
        self.tableWidget.clearContents()
        for i in range(x):
            for j in range(y):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(list[i][j])))

    def on_pushButton_clear_released(self):

        self.lineEdit_search_data.clear()
        self.tableWidget.clearContents()
        self.comboBox_btype.setCurrentIndex(0)
        self.radioButton_bname.setChecked(True)

    def on_pushButton_find_released(self):
        book_type = self.comboBox_btype.currentText()
        search_type = ''
        if self.radioButton_bno.isChecked():
            search_type = ' Bno = '
        elif self.radioButton_bname.isChecked():
            search_type = ' Bname = '
        elif self.radioButton_bauthor.isChecked():
            search_type = ' Bauthor = '
        elif self.radioButton_pubulish.isChecked():
            search_type = ' Bpublish = '
        text = self.lineEdit_search_data.text()

        exec = ''

        if book_type == '无' and text != '':
            exec = "SELECT * FROM Book WHERE " + search_type + "'" + text + "'"
        elif book_type =='无' and text == '':
            exec = "SELECT * FROM Book"
        elif book_type != '无' and text == '':
            exec = "SELECT * FROM Book WHERE Btype = " + "'" + book_type + "'"
        elif book_type != '无' and text != '':
            exec = "SELECT * FROM Book WHERE " + search_type + "'" + text + "'" +'AND Btype = ' + "'" + book_type + "'"

        self.dbcur.run_exec(exec)
        table = self.dbcur.cursor_data_to_list_all()
        self.tableWidget.clearContents()
        if len(table):
            self.setTableDate(table[0])
            self.win_table.add_table_data(table)
        else:
            self.dialog_text('无数据')

    def on_pushButton_back_released(self):
        QThread.msleep(200)
        self.setVisible(False)
        try:
            self.extern_win[self.WIN_EXTERN_LOGIN].show()
        except TypeError:
            print("This Win is NO exist")
        except AttributeError:
            print("win Errow")

        try:
            self.extern_button.show()
            self.close()
            del(self.dbcur)
            del(self)
        except AttributeError:
            print('NO Button')

        QThread.msleep(200)

    def on_pushButton_show_all_released(self):
        print('on_pushButton_show_all_released')
        self.win_table.show()


    def on_pushButton_month_released(self):
        date = str(QDateTime.toPyDateTime(QDateTime.currentDateTime()))
        date = date[0:7]
        print(date)
        exec = ("select TOP 10 Book.Bno, Bname, Bauthor, Bprice, Btype, Bpublish,Bnum, sum(SRnum) "
                "from SalesRecords,Book " +
                "where SalesRecords.Bno=Book.Bno " +
                "and SRdate like '%s%%' " % (date) +
                "group by Book.Bno, Bname, Bauthor, Bprice, Btype, Bpublish,Bnum order by sum(SRnum) desc")
        self.dbcur.select_run_exec(exec)
        list2 = self.dbcur.select_cursor_data_to_list()
        if len(list2):
           #  self.setHorizontalHeader("书名", "书号", "销量")
            self.setTableDate(list2)
        else:
            self.dialog_text('当月无销售')

    def on_pushButton_day_released(self):
        date = str(QDateTime.toPyDateTime(QDateTime.currentDateTime()))
        date = date[0:10]
        exec = ("select TOP 10 Book.Bno, Bname, Bauthor, Bprice, Btype, Bpublish,Bnum, sum(SRnum) "
        "from SalesRecords,Book " +
        "where SalesRecords.Bno=Book.Bno " +
        "and SRdate like '%s%%' "% (date) +
        "group by Book.Bno, Bname, Bauthor, Bprice, Btype, Bpublish,Bnum order by sum(SRnum) desc" )
        self.dbcur.select_run_exec(exec)
        list2 = self.dbcur.select_cursor_data_to_list()
        if len(list2):
            self.setTableDate(list2)
        else:
            self.dialog_text('当日无销售')




if __name__ == '__main__':
    import UIMain
    import UILogin

    app = QApplication(sys.argv)
    login = UILogin.UILogin()
    win = UIMain.MyWindow()
    search = UISearch()
    search.my_set_exten_win(win, 1, 2, 3, 4, login, 6)
    search.show()
    # win.show()
    sys.exit(app.exec_())
