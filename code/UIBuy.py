import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFrame
from UIMyBase import UIMy_base
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDateTime
import time
from PyQt5.QtWidgets import QTableWidgetItem
from UIBuy_frame import Ui_Frame_Buy
import DbBase
class UIBuy(QFrame, UIMy_base, Ui_Frame_Buy):
    def __init__(self, parent=None, x=0, y=0, xx=1, yy=1, sMno = '', pushButton = None):
        super(UIBuy, self).__init__()
        self.setupUi(self)
        self.my_layout(parent, x, y, xx, yy)
        # print(self.buy_book)
        self.sMno = sMno
        exec =  self.dbcur.select_parmeter_deal('SalesMan', SMno=self.sMno)
        self.dbcur.select_run_exec(exec)
        table = self.dbcur.cursor_data_to_list()
        self.label_buy_smname.setText(table[0][1])
        self.extern_button = pushButton

        self.init()

    def init(self):
        self.buy_book = [[None, None, None, None] for i in range(50)]
        self.mno = ''
        self.discount = 10
        self.pushButton_buy_buy.setEnabled(False)
        self.mno = ''
        self.tableWidget_buy_info.clearContents()
        self.widget_buy_member_info.hide()
        self.widget_buy_book_info.hide()
        self.lineEdit_buy_member_input.setText('')
        self.pushButton_back.show()
    def set_book_info(self, table):
        if len(table) == 0:
            return False
        else:
            table = table[0]
            self.lineEdit_buy_bno.setText(str(table[0]))
            self.lineEdit_buy_bname.setText(str(table[1]))
            self.lineEdit_buy_bauthor.setText(str(table[2]))
            self.lineEdit_buy_bprice.setText(str(table[3]))
            self.comboBox_buy_btype.setCurrentText(str(table[4]))
            self.lineEdit_buy_publish.setText(str(table[5]))
            self.lineEdit_buy_bnum.setText(str(table[6]))
            return True

    def on_tableWidget_buy_info_cellDoubleClicked(self, i, j):
        print("on_tableWidget_buy_info_cellDoubleClicked", i, j)
        if self.tableWidget_buy_info.item(i, 0) is None:
            return
        else:
            item = self.tableWidget_buy_info.item(i, j)

    def on_checkBox_buy_is_member_stateChanged(self, state):
        print('on_checkBox_buy_is_member_stateChanged', state)
        if state == 2:
            self.widget_buy_member_info.show()
        elif state == 0:
            self.widget_buy_member_info.hide()

    def on_tableWidget_buy_info_cellClicked(self, i, j):
        print('on_tableWidget_buy_info_cellClicked', i, j)
        if j == 0:
            item = self.tableWidget_buy_info.item(i, j)
            if item is not None:
                bno = item.text()
                bno = self.dbcur.str_add_quotation(bno)
                exec  = self.dbcur.select_parmeter_deal('Book', Bno=bno)
                self.dbcur.select_run_exec(exec)
                table = self.dbcur.select_cursor_data_to_list()
                self.set_book_info(table)
                self.widget_buy_book_info.show()
            else:
                self.widget_buy_book_info.hide()

    def on_tableWidget_buy_info_currentCellChanged(self,i, j, m, n):
        # 0, 2, 0, 0
        print('on_tableWidget_buy_info_currentCellChanged', i, j, m, n)
        self.label_buy_input_hint.setText("")
        if m == -1:
            return

        if m != 0 :
            # 本行上一行数据为空  无法输入数据
            item = self.tableWidget_buy_info.item(m - 1, 0)
            if item is None or str(item.text()) == '':
                if self.tableWidget_buy_info.item(m, n) is not None:
                    self.tableWidget_buy_info.item(m, n).setText('')
                return
            elif item.text()=="":
                return
            # 本行第一列内容为空 无法输入数据
            item = self.tableWidget_buy_info.item(m, 0)
            if item is None or item.text().strip == '':
                if self.tableWidget_buy_info.item(m ,n) is not None:
                    self.tableWidget_buy_info.item(m, n).setText('')
                return

        item = self.tableWidget_buy_info.item(m, n)
        if item is None or item.text() == '':
            # self.dialog_text("未输入数据")
            self.label_buy_input_hint.setText("未输入数据")
            return

        if n == 0:
            # 书号
            if j == 0 or m != i:
                pass
            else:
                # 输入书号后输入
                bno = item.text()
                bno = self.dbcur.str_add_quotation(bno)
                print(bno)
                exec = self.dbcur.select_parmeter_deal('Book', Bno = bno)
                self.dbcur.run_exec(exec)
                table = self.dbcur.select_cursor_data_to_list()
                if len(table):
                    # 书号存在
                    # print(table)
                    for i in range(50):
                        item = self.tableWidget_buy_info.item(i, 0)
                        if item == None or item.text() == '' or i == m:
                            # 书籍未输入过
                            self.buy_book[m][0] = item.text()
                            bprice = float(table[0][3])
                            bprice = bprice * self.discount / 10
                            item = QtWidgets.QTableWidgetItem(str(bprice)) # 单价
                            self.tableWidget_buy_info.setItem(m, 1, item)
                            self.buy_book[m][1] = item.text()
                            item = QtWidgets.QTableWidgetItem('1')         # 数量
                            self.tableWidget_buy_info.setItem(m, 2, item)
                            self.buy_book[m][2] = item.text()
                            self.buy_book[m][3] = table[0][3]
                            break
                        elif str(item.text()).strip() == str(table[0][0]).strip():
                            print(item.text(), table[0][0])
                            # 本书已经输入过
                            bnum = int(self.tableWidget_buy_info.item(i, 2).text())
                            bnum = bnum + 1
                            self.tableWidget_buy_info.item(i, 2).setText(str(bnum))
                            self.tableWidget_buy_info.item(m, 0).setText('')
                            self.buy_book[i][2] = bnum
                            break
                else:
                    self.label_buy_input_hint.setText("该书不存在")
                    self.tableWidget_buy_info.item(m,n).setText('')
        elif n == 1:
            # 金额
            bprice = item.text()
            if self.dbcur.is_money(bprice):
                self.buy_book[m][n] = bprice
            else:
                self.label_buy_input_hint.setText("金额输入格式错误")
                item.setText('')
        elif n == 2:
            # 数量
            bnum = item.text()
            if self.dbcur.is_sale_num(bnum):
                self.buy_book[m][n] = bnum
            else:
                self.label_buy_input_hint.setText("数量格式错误或数量过大")
                item.setText('')
        # print(self.buy_book)
        money = self.cal_all_price()
        self.label_buy_allprice.setText(str("%.2f"%money))

    def cal_all_price(self):
        money = 0
        for i in self.buy_book:
            if i[0]:
                money += float(i[1]) * int(i[2])
        return money

    def on_pushButton_buy_book_info_hide_released(self):
        print('on_pushButton_buy_book_info_hide_released')
        self.widget_buy_book_info.hide()

    def on_lineEdit_buy_member_input_editingFinished(self):
        print('on_lineEdit_buy_member_input_editinFinished')
        mno_tel = self.lineEdit_buy_member_input.text().strip()
        mno_tel = self.dbcur.str_add_quotation(mno_tel)
        table = []
        if self.radioButton_buy_mno.isChecked():
            exec = self.dbcur.select_parmeter_deal("Member", Mno=mno_tel)
            self.dbcur.select_run_exec(exec)
            table = self.dbcur.select_cursor_data_to_list()
        elif self.radioButton_buy_mtel.isChecked():
            exec = self.dbcur.select_parmeter_deal("Member", Mtel=mno_tel)
            self.dbcur.select_run_exec(exec)
            table = self.dbcur.select_cursor_data_to_list()
        if len(table) == 0:
            self.dialog_text('会员不存在 请重新输入', '提示')
            self.label_buy_show_mname.setText('***')
            return
        else:
            self.label_buy_show_mname.setText(str(table[0][1]))
            self.mno = table[0][0]
            self.label_6.setText('9.8')
            self.discount = 9.8
            if int(table[0][5]) > 1000:
                self.label_6.setText('9')
                self.discount = 9
                self.label_buy_mi.setText('2')

    def on_lineEdit_buy_pay_money_editingFinished(self):
        self.label_buy_input_hint.setText('')
        text = self.lineEdit_buy_pay_money.text()
        print(text)
        if self.label_buy_allprice.text() == '':
            self.label_buy_input_hint.setText("无购买书籍")
        elif self.dbcur.is_money(text):
            money = float(self.lineEdit_buy_pay_money.text()) - float(self.label_buy_allprice.text())
            if money > 0:
                money = str("%.2f"%money)
                self.lineEdit_odd_change.setText(str(money))
                self.pushButton_buy_buy.setEnabled(True)
                datetime = QDateTime.currentDateTime()
                self.dateTimeEdit_buy.setDateTime(datetime)
            else:
                self.label_buy_input_hint.setText("金额不足")

        else:
            self.label_buy_input_hint.setText('金额输入格式有误')

    def on_pushButton_buy_buy_released(self):
        # self.buy_deal()
        print("on_pushButton_buy_buy_released")
        flag = self.dialog_yes_no("确认购买")
        if flag is True:
            self.dateTimeEdit_buy.setDateTime(QDateTime.currentDateTime())
            self.buy_deal()
            self.dialog_text("购买成功")
            self.pushButton_buy_buy.setEnabled(False)

    def buy_deal(self):
        self.dbcur.select_run_exec("SELECT  TOP 1 * FROM SalesRecords ORDER BY SRdate DESC")
        table = self.dbcur.cursor_data_to_list()
        crrurent_date = str(QDateTime.toPyDateTime(self.dateTimeEdit_buy.dateTime()).date())
        crrurent_time = str(QDateTime.toPyDateTime(self.dateTimeEdit_buy.dateTime()).time())
        last_data = table[0][0]

        if crrurent_date == last_data:
            # 当天存在记录
            srno = int(table[0][1])
            print("srno", srno)
            srno = srno + 1
            srno = '000000' + str(srno)
            srno = srno[len(srno) - 6:]
            mno = ''
            if self.checkBox_buy_is_member.isChecked():
                mno = self.mno
            else:
                x = crrurent_date.split('-')
                mno = 'C' + x[0] + x[1] + x[2] + srno
                print("mno", mno, srno)
                exec = "INSERT INTO Member VALUES ( '" + mno + "', NULL, NULL, NULL, NULL, NULL)"
                self.dbcur.insert("Member", exec)
        else:
            # 当前不存在
            srno = '000001'
            if self.checkBox_buy_is_member.isChecked():
                mno = self.mno
            else:
                x = crrurent_date.split('-')
                mno = 'C' + x[0] + x[1] + x[2] + srno
                exec = "INSERT INTO Member VALUES ( '" + mno + "', NULL, NULL, NULL, NULL, NULL)"
                self.dbcur.insert("Member", exec)
        for i in self.buy_book:
            if i[0]:
                self.dbcur.sales_records_insert(srno, i[0], mno, self.sMno, i[1], i[2], crrurent_time, crrurent_date,)

    def on_pushButton_back_released(self):
        print('on_puchButton_back_released')
        self.close()
        try :
            self.extern_button.show()
        except AttributeError:
            print("NO EXTERN BUTTON")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    buy = UIBuy(sMno='4584445321')
    buy.show()
    sys.exit(app.exec_())
