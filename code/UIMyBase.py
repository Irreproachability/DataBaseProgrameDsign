from DbMyClass import *

class UIMy_base(object):
    def __init__(self):
        self.extern_win = None
        self.dbcur = DbMyClass()

    def connect_to_db(self, host='127.0.0.1:1433', user='123', password='123', database='BookStore'):
        self.dbcur = DbMyClass()

    def my_layout(self, parent=None, x=0, y=0, xx=1, yy=1, grid=''):
        if parent is not None:
            try:
                if grid == '':
                    parent.gridLayout.addWidget(self, x, y, xx, yy)
                elif grid == 'table':
                    parent.gridLayout_table.addWidget(self, x, y, xx, yy)
            except AttributeError:
                print("no gridayou")

    def my_set_exten_win(self, *win):
        """
        外部窗口接口
        :param win:外部窗口列表
        :return:
        """
        self.extern_win = win

    def my_win_deal(self, win=None, deal=None):
        try:
            if deal == self.WIN_DEAL_COSLE:
                self.extern_win[win].close()
            elif deal == self.WIN_DEAL_HIDE:
                self.extern_win[win].hide()
            elif deal == self.WIN_DEAL_SHOW:
                self.extern_win[win].show()
            print("WIN deal successful")
        except TypeError:
            print("This Win is NO exist")
        except AttributeError:
            print("win Errow")

    def my_win_close(self, win=None):
        self.my_win_deal(win, self.WIN_DEAL_COSLE)

    def my_win_hide(self, win=None):
        self.my_win_deal(win, self.WIN_DEAL_HIDE)

    def my_win_show(self, win=None):
        self.my_win_deal(win, self.WIN_DEAL_SHOW)

    def sys_quit(self):
        for i in range(len(self.extern_win)):
            self.my_win_deal(i, self.WIN_DEAL_COSLE)

    def get_file_name(self):
        import wx
        app = wx.App()
        # frame = wx.Frame(None, title="Gui Test Editor", pos=(1000, 200), size=(500, 400))
        dialog = wx.FileDialog(parent=None, message="file choose", wildcard="")

        dialog.ShowModal()
        file_path = dialog.GetPath()
        # print(file_path)
        app.MainLoop()
        return file_path

    def dialog_text(self, con="text", name="提示"):
        """
        只有确定的弹窗,可以做为一个显示提示信息的对话框
        :param con: 弹窗内容
        :param name: 弹窗名
        :return: 无返回值
        """
        import wx
        app = wx.App()
        dialog = wx.MessageDialog(None, con, name)
        dialog.ShowModal()
        app.MainLoop()

    def dialog_yes_no(self, con="ensure do something ?", name="确认"):
        """
        确认对话框，
        :param con: 对话框内容
        :param name: 对话框名
        :return: True 是， False 否
        """
        import wx
        app = wx.App()
        dialog = wx.MessageDialog(None, con, name, style=wx.YES_NO | wx.ICON_QUESTION)
        # dialog = wx.MessageDialog()
        id = dialog.ShowModal()
        app.MainLoop()
        if id == wx.ID_YES:
            return True
        elif id == wx.ID_NO:
            return False

    WIN_EXTERN_MAIN = 0
    WIN_EXTERN_ADMINI = 1
    WIN_EXTERN_SALEMAN = 2
    WIN_EXTERN_ROOT = 3
    WIN_EXTERN_SEARCH = 4
    WIN_EXTERN_LOGIN = 5
    WIN_EXTERN_TABLE = 6
    FLAG_LOGIN_FAIL = 0
    WIN_DEAL_COSLE = 1
    WIN_DEAL_HIDE = 2
    WIN_DEAL_SHOW = 3


if __name__ == '__main__':
    base = UIMy_base()
    base.dialog_text()
    print( base.dialog_yes_no())
