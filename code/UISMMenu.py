import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFrame
from UIMyBase import UIMy_base
from UISMMenu_prame import Ui_Frame_sales_man

from UISMInfo import UISMInfo
from UISearch import UISearch
from UIBuy import UIBuy
from UIBecomeMember import UIBecomeMember
from UIBackBook import UIBackBook
from UISeeMemberInfo import UISeeMemberInfo

class UISMMenu(QFrame, UIMy_base, Ui_Frame_sales_man):
    def __init__(self, parent=None, x=0, y=0, xx=1, yy=1, sMno = '', pushButton=None):
        super(UISMMenu, self).__init__()
        self.setupUi(self)
        self.my_layout(parent, x, y, xx, yy)
        self.sMno = sMno
        self.extern_button = pushButton
        self.init()
        # self.widget_sm_menu.hide()

        self.win_sm_info = UISMInfo(sMno=sMno, pushButton=self.widget_sm_menu)
        self.gridLayout.addWidget(self.win_sm_info, 1, 0, 1, 4)
        self.win_sm_info.hide()

        self.win_book_seach = UISearch(pushButton=self.widget_sm_menu)
        self.gridLayout.addWidget(self.win_book_seach, 1, 0, 1, 4)
        self.win_book_seach.hide()

        self.win_buy_book = UIBuy(sMno=sMno, pushButton=self.widget_sm_menu)
        self.gridLayout.addWidget(self.win_buy_book, 1, 0, 1, 4)
        self.win_buy_book.hide()

        self.win_become_member = UIBecomeMember(pushButton=self.widget_sm_menu)
        self.gridLayout.addWidget(self.win_become_member, 1, 0, 1, 4)
        self.win_become_member.hide()

        self.win_back_book = UIBackBook(self, 1, 0, 1, 4, pushButton=self.widget_sm_menu)
        self.win_back_book.hide()

        self.win_see_m_info = UISeeMemberInfo(self, 1, 0, 1, 4, pushButton=self.widget_sm_menu)
        self.win_see_m_info.hide()

    def init(self):
        pass

    def on_pushButton_menu_become_member_released(self):
        print('on_pushButton_menu_become_member_released')
        self.win_become_member.show()
        self.widget_sm_menu.hide()

    def on_pushButton_menu_book_back_released(self):
        print('on_pushButton_menu_book_back_released')
        self.win_back_book.show()
        self.widget_sm_menu.hide()

    def on_pushButton_menu_buy_released(self):
        print('on_pushButton_menu_buy_released')
        self.win_buy_book.show()
        self.widget_sm_menu.hide()

    def on_pushButton_menu_see_member_released(self):
        print('on_pushButton_menu_see_member_released')
        self.win_see_m_info.show()
        self.widget_sm_menu.hide()

    def on_pushButton_menu_search_released(self):
        print('on_pushButton_menu_search_released')
        self.win_book_seach.show()
        self.widget_sm_menu.hide()

    def on_pushButton_menu_sm_info_released(self):
        print('on_pushButton_menu_sm_info_released')
        self.win_sm_info.show()

        self.widget_sm_menu.hide()

    def on_pushButton_back_released(self):
        print('on_pushButton_back_released')
        try:
            self.extern_button.show()
        except AttributeError:
            print('NO BUTTON')
        finally:
            self.close()

    def on_pushButton_quit_released(self):
        if self.dialog_yes_no('退出系统？'):
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    buy = UISMMenu(sMno='4584445321')
    buy.show()
    sys.exit(app.exec_())