# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication

from UITableEmpty_frame import *
from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QTableWidgetItem
from UIMyBase import UIMy_base
from DbMyClass import DbMyClass
class UiTable(QFrame, Ui_Frame_table_empty, UIMy_base):
    def __init__(self, parent=None, x = 0, y = 0, xx = 1, yy = 1, pushButton = None):
        super(UiTable, self).__init__()
        self.setupUi(self)
        self.table = []
        self.table_i = 0
        self.dbcur = DbMyClass()
        self.extern_button = pushButton
        n = self.tableWidget.columnCount()
        for i in range(n):
            self.tableWidget.setHorizontalHeaderItem(i, QTableWidgetItem(''))

        self.my_layout(parent,x,y,xx,yy)

    def setTableName(self, table_name="Table name"):
        """

        :param table_name: 设置表名
        :return:
        """
        self.lable_table_name.setText(table_name)

    def setHorizontalHeader(self, *args):
        """
        设置表头
        :param args: 表头名
        :return:
        """
        n = self.tableWidget.columnCount()
        for i in range(n):
            self.tableWidget.setHorizontalHeaderItem(i, QTableWidgetItem(''))

        if isinstance(args[0], list) or isinstance(args[0], tuple):
            args = args[0]
        i = -1

        n = self.tableWidget.size()

        for table_head in args:
            i = i + 1
            self.tableWidget.setHorizontalHeaderItem(i, QTableWidgetItem(table_head))

    def setTableDate(self, list):
        x = len(list)
        y = len(list[0])

        for i in range(x):
            for j in range(y):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(list[i][j])))

    def add_table_data(self, list3):
        self.table = list3
        self.spinBox.setMaximum(len(list3))
        x = '共' + str(len(list3)) + '页'
        self.label_page.setText(x)
        self.setTableDate(self.table[0])

    def clear_table_data(self):
        self.table = []
        self.table_i = 0

    def clear_table(self):
        self.tableWidget.clearContents()
        self.setHorizontalHeader('','','','','','','','','','','','','','','')

    def on_spinBox_valueChanged(self, value):
        print('on_spinBox_valueChanged')
        value = int(value)
        if self.table_i == value:
            return
        #　print(self.table[value-1])
        self.tableWidget.clearContents()
        self.setTableDate(self.table[value - 1])

    def on_pushButton_hide_released(self):
        self.close()
        try:
            self.extern_button.show()
        except AttributeError:
            print("NO EXTERON BUTTON")

if __name__ == '__main__':
    from UItestMain import *

    app = QApplication(sys.argv)
    # win = MyWindow()
    win = UiTable()
    win.dbcur.select_book()
    list3 = win.dbcur.cursor_data_to_list_all()
    #　print(list3)
    win.add_table_data(list3)
    win.show()
    # win.show()
    sys.exit(app.exec_())



