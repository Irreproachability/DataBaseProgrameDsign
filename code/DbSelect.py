from DbBase import *


class DbSelect(DbDesignBase):

    def select_table(self, table_name):
        """
        查询某个表中的所有数据
        :param table_name: 表名
        :return: 游标 或 空
        """
        exec = "SELECT * FROM " + table_name
        try:
            self.cursor.execute(exec)
            print("SELECT " + table_name + " Successful")
            return self.cursor
        except pymssql.Error:
            print("SELECT " + table_name + " ERROR")
            return None

    def select_run_exec(self, exec):
        try:
            self.cursor.execute(exec)
            print(exec + " Successful")
            return self.cursor
        except pymssql.Error:
            print(exec + " ERROR")
            return None

    @staticmethod
    def select_parmeter_deal(table_name, ** kwargs):
        """
        查询参数处理

        :param table_name:表名
        :param kwargs: a = b and a1 = b1 and a2 = b2
        :return:
        """
        a = 'SELECT * FROM ' + table_name + " WHERE "
        b = ' 1 = 1 '
        for i in kwargs:
            b = b + ' AND ' +  str(i) + ' = ' + str(kwargs[i])

        return  a + b

    def select_show_data_console(self, cur = None):
        table_data = self.cursor_data_to_list(cur)
        print(table_data)

    def select_cursor_data_to_list(self, cur = None):
        table_data = self.cursor_data_to_list(cur)
        return table_data

    def select_book(self):
        self.select_table('Book')

    def select_member(self):
        self.select_table('Member')

    def select_salesman(self):
        self.select_table('SalesMan')

    def select_administrator(self, **kwargs):
        self.select_table('Administrator')

    def select_salesrecords(self):
        self.select_table('SalesRecords')

    def select_backrecords(self):
        self.select_table('BackRecords')

    def select_managestockrecords(self):
        self.select_table('ManageStockRecords')

    def select_managebackrecords(self):
        self.select_table('ManageBackRecords')



if __name__ == '__main__':
    db = DbSelect()
    db.select_salesrecords()
    db.select_show_data_console()
