from DbBase import *


class DbDelete(DbDesignBase):

    @staticmethod
    def delete_parmeter_deal(table_name, ** kwargs):
        a = 'DELETE FROM ' + table_name + " WHERE "
        b = ' 1 = 1'
        print(kwargs)
        for i in kwargs:
            b = b + ' AND ' + str(i) + ' = ' + str(kwargs[i])

        return a + b

    def delete_run_exec(self,exec):
        try:
            self.cursor.execute(exec)
            self.conn.commit()
        except pymssql.Error:
            print(exec," DELETE ERROR")
            return False
        else:
            print(exec, " DELETE successful")
            return True

    def delete_book(self, bno):
        exec = self.delete_parmeter_deal('Book', Bno = bno)
        return self.delete_run_exec(exec)

    def delete_salesMan(self, SMno):
        exec = self.delete_parmeter_deal('SalesMan', SMno = SMno)
        return self.delete_run_exec(exec)

if __name__ == '__main__':
    db = DbDelete()
    db.delete_book('1012')