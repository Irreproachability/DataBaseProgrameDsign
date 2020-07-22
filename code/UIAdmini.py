
import sys
from PyQt5.QtWidgets import QApplication
from UIAdmini_frame import Ui_Frame_admini
from PyQt5.QtWidgets import QFrame
from PyQt5.Qt import QThread
from UIMyBase import UIMy_base
from UIBookManage import UIBookManage
from UISalesManManage import UISanlesManManage
from PyQt5.QtCore import QDateTime

from UISearch import UISearch
from DbMyClass import DbMyClass
from UIAdminiInfo import UIAdminiInfo
from UITable import UiTable
class UIAdmini(QFrame, Ui_Frame_admini, UIMy_base):
    def __init__(self, parent=None, x = 0, y = 0, xx = 1, yy = 1, ano = '',pushbutton=None):
        super(UIAdmini, self).__init__()
        self.setupUi(self)
        self.time = 0
        self.my_layout(parent, x, y, xx, yy)
        self.connect_to_db()
        self.ano = ano
        self.extern_button = pushbutton

        self.book_manage_change = UIBookManage(mode=UIBookManage.MODE_CHANGE, pushButton=self.widget)
        self.gridLayout_7.addWidget(self.book_manage_change, 1, 0, 1, 1)
        self.book_manage_change.hide()

        self.book_manage_add = UIBookManage(mode=UIBookManage.MODE_ADD, pushButton=self.widget)
        self.gridLayout_7.addWidget(self.book_manage_add, 1, 0, 1, 1)
        self.book_manage_add.hide()


        self.book_manage_del = UIBookManage(mode=UIBookManage.MODE_DEL, pushButton=self.widget)
        self.gridLayout_7.addWidget(self.book_manage_del, 1, 0, 1, 1)
        self.book_manage_del.hide()

        self.sM_manage_change = UISanlesManManage(mode=UISanlesManManage.MODE_CHANGE, pushButton=self.widget_3_button)
        self.gridLayout_salesMan.addWidget(self.sM_manage_change, 1, 0, 1, 1)
        self.sM_manage_change.hide()

        self.sM_manage_del = UISanlesManManage(mode=UISanlesManManage.MODE_DEL, pushButton=self.widget_3_button)
        self.gridLayout_salesMan.addWidget(self.sM_manage_del, 1, 0, 1, 1)
        self.sM_manage_del.hide()

        self.sM_manage_add = UISanlesManManage(mode=UISanlesManManage.MODE_ADD, pushButton=self.widget_3_button)
        self.gridLayout_salesMan.addWidget(self.sM_manage_add, 1, 0, 1, 1)
        self.sM_manage_add.hide()

        self.win_sM_view = UiTable(pushButton=self.pushButton_3_SM_view)
        self.dbcur.select_salesman()
        table = self.dbcur.cursor_data_to_list_all()
        self.win_sM_view.add_table_data(table)
        self.win_sM_view.setHorizontalHeader('售货员编号','姓名','性别','密码')
        self.gridLayout_salesMan.addWidget(self.win_sM_view, 0, 1, 2, 2)
        self.win_sM_view.hide()

        self.win_data_see = UiTable()
        self.gridLayout_date_see.addWidget(self.win_data_see, 1, 0, 1, 1)
        self.win_data_see.show()
        self.win_data_see.pushButton_hide.hide()
        self.win_data_see.setTableName('')

        admini = UIAdminiInfo(admini=self.ano)
        self.gridLayout_admini_info.addWidget(admini, 0, 0, 1, 1)

        self.win_book_search = UISearch(pushButton=self.pushButton_2_search_see)
        self.gridLayout_7.addWidget(self.win_book_search, 0, 1, 2, 2)
        self.win_book_search.hide()

    def on_tabWidget_admini_tabBarClicked(self, tab):
        print(tab)

    def on_pushButton_2_book_change_released(self):
        self.book_manage_change.show()
        self.widget.hide()

    def on_pushButton_2_book_add_released(self):
        self.book_manage_add.show()
        self.widget.hide()

    def on_pushButton_2_book_del_released(self):
        self.book_manage_del.show()
        self.widget.hide()

    def on_pushButton_2_search_see_released(self):
        """
        图书查看键，可以进入图书查看面板
        :return:
        """
        self.win_book_search.show()
        self.pushButton_2_search_see.hide()

    def on_pushButton_3_SM_change_released(self):
        print("on_pushButton_3_SM_change_released")
        self.widget_3_button.hide()
        self.sM_manage_change.show()

    def on_pushButton_3_SM_add_released(self):
        print("on_pushButton_3_SM_add_released")
        self.widget_3_button.hide()
        self.sM_manage_add.show()

    def on_pushButton_3_SM_del_released(self):
        print("on_pushButton_3_SM_del_released")
        self.widget_3_button.hide()
        self.sM_manage_del.show()

    def on_pushButton_3_SM_view_released(self):
        """
        销售人员信息查看
        :return:
        """
        self.win_sM_view.show()
        self.pushButton_3_SM_view.hide()

    def on_lineEdit_mbr_bnum_editingFinished(self):
        print('on_linEdit_mbr_bnum_editingFinished')
        if DbMyClass.is_num(self.lineEdit_mbr_bnum.text()):
            pass
        else:
            self.lineEdit_mbr_bnum.setText('')

    def on_lineEdit_mbr_bno_editingFinished(self):
        print('on_linEdit_mbr_bno_editingFinished')
        exec = self.dbcur.select_parmeter_deal('Book',
                                        Bno = self.lineEdit_mbr_bno.text())
        self.dbcur.select_run_exec(exec)
        if len(self.dbcur.select_cursor_data_to_list()):
            pass
        else:
            self.lineEdit_mbr_bno.setText('')

    def on_lineEdit_msr_bnum_editingFinished(self):
        print('on_linEdit_msr_bnum_editingFinished')
        if DbMyClass.is_num(self.lineEdit_msr_bnum.text()):
            pass
        else:
            self.lineEdit_msr_bnum.setText('')

    def on_lineEdit_msr_bno_editingFinished(self):
        print('on_linEdit_msr_bno_editingFinished')

        exec = self.dbcur.select_parmeter_deal('Book',
                                        Bno=self.lineEdit_msr_bno.text())
        self.dbcur.select_run_exec(exec)
        if len(self.dbcur.select_cursor_data_to_list()):
            pass
        else:
            self.lineEdit_msr_bno.setText('')

    def on_pushButton_mbr_ensure_released(self):
        print('on_pushButton_mbr_ensure_released')
        if self.lineEdit_mbr_bno.text()!='' and self.lineEdit_mbr_bnum.text()!= '':
            date_time = str(QDateTime.toPyDateTime(QDateTime.currentDateTime()))[0:16]

            flag =  self.dbcur.manage_back_records(date_time,
                                           self.ano,
                                           self.lineEdit_mbr_bno.text(),
                                           self.lineEdit_mbr_bnum.text())
            if flag:
                self.dialog_text('退货记录录入成功')
                self.lineEdit_mbr_bnum.setText('')
                self.lineEdit_mbr_bno.setText('')
            else:
                self.dialog_text('退货记录录入失败')

    def on_pushButton_msr_ensure_released(self):
        print('on_pushButton_msr_ensure_released')
        if self.lineEdit_msr_bno.text() != '' and self.lineEdit_msr_bnum.text() != '':
            date_time = str(QDateTime.toPyDateTime(QDateTime.currentDateTime()))[0:16]

            flag = self.dbcur.manage_stock_records_insert(date_time,
                                                  self.ano,
                                                  self.lineEdit_msr_bno.text(),
                                                  self.lineEdit_msr_bnum.text())
            if flag:
                self.dialog_text('进货记录录入成功')
                self.lineEdit_msr_bno.setText('')
                self.lineEdit_msr_bnum.setText('')
            else:
                self.dialog_text('进货记录录入失败')

    def on_pushButton_4_br_released(self):
        print('pushButton_4_br')
        self.win_data_see.clear_table()
        self.dbcur.select_backrecords()
        self.win_data_see.setHorizontalHeader('单号','书号','会员号','售货员号','价格','数量','时间','日期')
        self.win_data_see.add_table_data(self.dbcur.cursor_data_to_list_all())

    def on_pushButton_4_mbr_released(self):
        print('pushButton_4_mbr')
        self.win_data_see.clear_table()
        self.dbcur.select_managebackrecords()
        self.win_data_see.setHorizontalHeader('管理员号','书号','时间日期','数量')
        self.win_data_see.add_table_data(self.dbcur.cursor_data_to_list_all())

    def on_pushButton_4_minfo_released(self):
        print('pushButton_4_minfo')
        self.win_data_see.clear_table()
        self.dbcur.select_member()
        self.win_data_see.setHorizontalHeader('会员编号','姓名','性别','电话号码','出生日期','积分')
        self.win_data_see.add_table_data(self.dbcur.cursor_data_to_list_all())

    def on_pushButton_4_msr_released(self):
        print('pushButton_4_msr')
        self.win_data_see.clear_table()
        self.dbcur.select_managestockrecords()
        self.win_data_see.setHorizontalHeader('管理员号','书号','时间日期','数量')
        self.win_data_see.add_table_data(self.dbcur.cursor_data_to_list_all())

    def on_pushButton_4_sr_released(self):
        print('pushButton_4_sr')
        self.win_data_see.clear_table()
        self.dbcur.select_salesrecords()
        self.win_data_see.setHorizontalHeader('单号','书号','会员号','售货员号','价格','数量','时间','日期')
        self.win_data_see.add_table_data(self.dbcur.cursor_data_to_list_all())

    def on_pushButton_quit_released(self):
        if self.dialog_yes_no('退出系统？'):
            self.close()

    def on_pushButton_back_released(self):
        try:
            self.extern_button.show()
        except AttributeError:
            print('NO EXTERN WIN')
        finally:
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    admini = UIAdmini(ano='4752123597')
    admini.show()
    sys.exit(app.exec_())
