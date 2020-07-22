from DbBase import *
import re


class DbInsert(DbDesignBase):

    @staticmethod
    def insert_parameter_deal(where, *args):
        """

        :param self:
        :param where: str 插入的表名
        :param args: 插入参数列表
        :return: str 嵌入语句，可直接使用
        """
        # print("参数处理", where, args)
        exc = "INSERT INTO " + where + " VALUES " + str(args)
        print("参数处理", exc)
        return str(exc)



    def insert(self, where, exec):
        """

        :param where:str 插入数据的表
        :param exec:str SQL嵌入语句
        :return: bool, 插入成功？

        """
        try:
            self.cursor.execute(exec)
            self.conn.commit()
        except pymssql.Error:
            print(exec, " INSERT ERROR")
            return False
        else:
            print(exec, " INSERT successful")
            print('cursor close')
            return True

    def book_insert(self, Bno, Bname, Bauthor, Bprice, Btype, Bpublish, Bnum):
        exec = self.insert_parameter_deal('Book', Bno, Bname, Bauthor, Bprice, Btype, Bpublish, Bnum)
        if self.insert( 'Book', exec) is True:
            return True
        else:
            return False


    @staticmethod
    def insert_data_check_book(Bno, Bname, Bauthor, Bprice, Btype, Bpublish, Bnum):
        flag = 0
        if re.match(r'^\d{4,11}$',Bno):
            flag |= 1 << 0
            # print('Bno')
        if re.match(r'\S', Bname):
            flag |= 1 << 1
            # print('Bname')
        if re.match(r'\S', Bauthor):
            flag |= 1 << 2
            # print('Bauthor')
        if re.match(r'^[1-9][0-9]*$|^[1-9][0-9]*\.[0-9]+$|^0\.[0-9]+$',Bprice):
            flag |= 1 << 3
            # print('Bprice')

        type = r'^经典名著$|^专业图书类$|^古典文学$|^外国文学$|^现当代文学$|^历史地理类$|^哲学类$|^社会科学类$|^玄幻文学$|^儿童文学$'
        if re.match(type, Btype):
            flag |= 1 << 4
            # print('Btype')

        if re.match(r'\S+出版社$', Bpublish):
            flag |= 1 << 5
            # print('Bpublish')
        if re.match(r'0$|[1-9]\d*$', Bnum):
            flag |= 1 << 6
            # print('Bnum')
        if flag == 0x7F :
            flag = 0xff
        print(flag)
        return flag

    @staticmethod
    def insert_data_check_salesMan(SMno, SMname, SMsex, SMpassword):
        flag = 0
        if re.match(r'^[a-zA-Z0-9_]{4,15}$', SMno):
            flag |= 1 << 0
        if re.match(r'^\S{5,20}$',SMname):
            flag |= 1 << 1
        if re.match(r'^[a-zA-Z0-9_]{4,15}$', SMpassword):
            flag |= 1 << 2
        if re.match(r'^男|女$', SMsex):
            flag |= 1 << 3

        flag |= 7 << 4

        if flag == 0x7f:
            flag = 0xff

        print(flag)
        return flag

    def member_insert(self, Mno, Mname=None,Msex=None, Mtel=None, Mbir=None, Mintegration=None):
        exc = self.insert_parameter_deal('Member',Mno, Mname, Msex, Mtel, Mbir, Mintegration)
        self.insert( 'Member', exc)

    def administrator_insert(self, Ano, Aname, Asex, Apassword):

        exc = self.insert_parameter_deal( 'Administrator',Ano, Aname, Asex, Apassword)
        self.insert( 'Administrator', exc)

    def salesman_insert(self, SMno, SMname, SMsex, SMpassword):
        exc = self.insert_parameter_deal(  'SalesMan',SMno, SMname, SMsex, SMpassword)
        self.insert( 'SalesMan', exc)

    def sales_records_insert(self, SRno, Bno, Mno, SMno, SRprice, SRnum, SRtime, SRdate):
        exc = self.insert_parameter_deal( 'SalesRecords', SRdate, SRno, Bno, Mno, SMno, SRprice, SRnum, SRtime)
        self.insert( 'SalesRecords', exc)

    def back_records_insert(self, BRno, Bno, Mno, SMno, BRprice, BRnum, BRtime, BRdate):
        exc = self.insert_parameter_deal( 'BackRecords', BRdate, BRno, Bno, Mno, SMno, BRprice, BRnum, BRtime)
        if self.insert( 'BackRecords', exc):
            return True
        else:
            return False

    def manage_stock_records_insert(self,MSdatetime, Ano, Bno,  MSnum):
        exc = self.insert_parameter_deal( 'ManageStockRecords',MSdatetime, Ano, Bno,  MSnum)
        if self.insert( 'ManageStockRecords', exc):
            return True
        else:
            return False
    def manage_back_records(self,MBdatetime, Ano, Bno,  MBnum):
        exc = self.insert_parameter_deal( 'ManageBackRecords', MBdatetime, Ano, Bno,MBnum)
        if self.insert('ManageBackRecords', exc):
            return True
        else:
            return False

    BOOK_INSERT_OK = 0xFF
    INSERT_OK = 0xFF
if __name__ == '__main__':
    print(type('dfsajk'))
    DbInsert.insert_data_check_salesMan('1223434',
                                    '2asfd',
                                    '3fsadf',
                                    '男',
                                        )
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
