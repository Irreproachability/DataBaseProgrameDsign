from DbBase import *
import re

class DbUpdata(DbDesignBase):

    def __init__(self):
        super(DbUpdata,self).__init__()

    def update_run_exec(self, exec):
        try:
            self.cursor.execute(exec)
            self.conn.commit()
        except pymssql.Error:
            print(exec," UPDATE ERROR")
            return False
        else:
            print(exec, " UPDATE successful")
            return True

    @staticmethod
    def updata_parmeter_deal(table_name='', set={}, where={}):

        update = "UPDATE " + table_name + ' SET '
        a = ''
        for i, j in set.items():
            a = a + ', ' + (str(i)) + ' = ' + DbDesignBase.str_add_quotation(str(j))
        a = a + '  WHERE '
        b = ''
        for i, j in where.items():
            b = b + ', ' + (str(i)) + ' = ' + DbDesignBase.str_add_quotation(str(j))

        a = re.sub(r"^, ", ' ', a)
        b = re.sub(r"^, ", ' ', b)
        return update + a + b


if __name__ == '__main__':
    str = DbUpdata.updata_parmeter_deal('Book') #,{'BNo':'fas'}, {'con"':'dfsal'})
    print(str)

