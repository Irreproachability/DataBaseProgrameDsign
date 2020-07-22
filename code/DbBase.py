import pymssql
import re

class DbDesignBase():

    def __init__(self):
        self.conn = None
        self.cursor = None
        self.login()

    def login(self, host='127.0.0.1:1433', user='123', password='123', database='BookStore'):
        try:
            self.conn = pymssql.connect(host=host, user=user, password=password, database=database)
            self.cursor = self.conn.cursor()
            print("longin successful")
            return True
        except pymssql.Error:
            print("longin ERROR")
            return False

    def run_exec(self, exec):
        print(exec)
        try:
            self.cursor.execute(exec)
            print(" exec successful")
            return True
        except pymssql.Error:
            print(" exec ERROR")
            print(exec)
            return False


    @staticmethod
    def str_add_quotation(string):
        string = str(string)
        string = "'" + string + "'"
        return string

    @staticmethod
    def is_money(string):
        if re.match(r'^[1-9][0-9]*$|^[1-9][0-9]*\.[0-9]+$|^0\.[0-9]+$', str(string)):
            return True
        else:
            return False

    @staticmethod
    def is_no(string):
        if re.match(r'^\d{4,11}$', str(string)):
            return True
        else:
            return False

    @staticmethod
    def is_sale_num(string):
        if re.match(r'^[1-9]\d{0,2}$', str(string)):
            return True
        else:
            return False

    @staticmethod
    def is_tel(string):
        if  re.match(r'^1\d{10}$|^\d{7,8}$', str(string)):
            return True
        else:
            return False

    @staticmethod
    def is_name(string):
        if re.match(r'^[\u4e00-\u9fa5]{2,4}$', str(string)):
            return True
        else:
            return False

    @staticmethod
    def is_num(string):
        if re.match((r'^[1-9]\d*$'), str(string)):
            return True
        else:
            return False

    def close(self):
        try:
            if self.conn is not None:
                self.conn.commit()
                self.cursor.close()
                self.conn.close()
                self.cursor = None
                self.conn = None
            print("close successful")
        except AttributeError:
            print("AttributeError")

    def sql_init(self):
        # Create table
        x = """
    
    DROP TABLE ManageBackRecords
    DROP TABLE ManageStockRecords
    
    DROP TABLE SalesRecords
    DROP TABLE BackRecords
    
    DROP TABLE Administrator
    DROP TABLE SalesMan
    DROP TABLE Member
    DROP TABLE Book
    
    
    CREATE TABLE Book(
        Bno CHAR(10) NOT NULL PRIMARY KEY,
        Bname NVARCHAR(20) NOT NULL,
        Bauthor VARCHAR(20) NOT NULL,
        Bprice MONEY NOT NULL,
        Btype VARCHAR(10),
        Bpublish VARCHAR(20),
        Bnum INT,
    )
    CREATE TABLE Member(
        Mno CHAR(15) NOT NULL PRIMARY KEY,
        Mname VARCHAR(20),
        Msex CHAR(2) CHECK (Msex IN('男','女')),
        Mtel VARCHAR(11),
        Mbir DATE,
        Mintegration INT,
    )
    CREATE TABLE SalesMan(
        SMno CHAR(10) NOT NULL PRIMARY KEY,
        SMname VARCHAR(20) NOT NULL,
        SMsex CHAR(2) CHECK (SMsex IN('男','女')),
        SMpassword VARCHAR(13),
    )
    CREATE TABLE Administrator(
        Ano CHAR(10) NOT NULL PRIMARY KEY,
        Aname VARCHAR(20) NOT NULL, 
        Asex CHAR(2) CHECK (Asex IN('男','女')) ,
        Apassword VARCHAR(13),
    )
       CREATE TABLE SalesRecords(
        SRdate DATE,
        SRno CHAR(10) NOT NULL, 
        Bno CHAR(10)  NOT NULL  , 
        Mno CHAR(15)  NOT NULL  ,
        SMno CHAR(10) NOT NULL  ,
        SRprice MONEY,
        SRnum INT,
        SRtime TIME,
        
        PRIMARY KEY(SRdate, SRno, Bno, Mno, SMno),
        CONSTRAINT FK_SR_Bno FOREIGN KEY(Bno) REFERENCES Book(Bno),
        CONSTRAINT FK_SR_Mno FOREIGN KEY(Mno) REFERENCES Member(Mno),
        CONSTRAINT FK_SR_SMno FOREIGN KEY(SMno) REFERENCES SalesMan(SMno),
        
    )
    CREATE TABLE BackRecords(
        BRdate DATE,
        BRno CHAR(10) NOT NULL  , 
        Bno CHAR(10)  NOT NULL  , 
        Mno CHAR(15)  NOT NULL  ,
        SMno CHAR(10) NOT NULL  ,
        BRprice MONEY,
        BRnum INT,
        BRtime TIME,
        
        PRIMARY KEY(SRdate, BRno, Bno, Mno, SMno),
        CONSTRAINT FK_BR_Bno FOREIGN KEY(Bno) REFERENCES Book(Bno),
        CONSTRAINT FK_BR_Mno FOREIGN KEY(Mno) REFERENCES Member(Mno),
        CONSTRAINT FK_BR_SMno FOREIGN KEY(SMno) REFERENCES SalesMan(SMno),
        
    )
    CREATE TABLE ManageStockRecords(
        MSdatetime SMALLDATETIME, 
        Ano CHAR(10) NOT NULL, 
        Bno CHAR(10) NOT NULL, 
        MSnum INT,
        PRIMARY KEY( MSdatetime,Ano, Bno),
        CONSTRAINT FK_MS_Ano FOREIGN KEY(Ano) REFERENCES Administrator(Ano),
        CONSTRAINT FK_MS_Bno FOREIGN KEY(Bno) REFERENCES Book(Bno),
    )
    CREATE TABLE ManageBackRecords(
        MBdatetime SMALLDATETIME,
        Ano CHAR(10) NOT NULL, 
        Bno CHAR(10) NOT NULL, 
        MBnum INT,
        PRIMARY KEY(Mbdatetime, Ano,  Bno),
        CONSTRAINT FK_MB_Ano FOREIGN KEY(Ano) REFERENCES Administrator(Ano),
        CONSTRAINT FK_MB_Bno FOREIGN KEY(Bno) REFERENCES Book(Bno),
    )
    
    
    
    
    -- book
    CREATE INDEX IX_Book_Bno ON Book(Bno)
    CREATE INDEX IX_Book_Bname ON Book(Bname)
    
    /*
    DROP INDEX IX_Book_Bno ON Book
    DROP INDEX IX_Book_Bname ON Book
     */
    
    -- member
    CREATE INDEX IX_Member_Mno ON Member(Mno)
    CREATE INDEX IX_Member_Mname ON Member(Mname)
    CREATE INDEX IX_Member_Mtel ON Member(Mtel)
    
    /* 
    DROP INDEX IX_Member_Mno ON Member
    DROP INDEX IX_Member_Mname ON Member
    DROP INDEX IX_Member_Mtel ON Member
     */
    -- MSR MBR
    
    CREATE INDEX IX_MSR_DateTime ON ManageStockRecords(MSdatetime)
    CREATE INDEX IX_MBR_DateTime ON ManageBackRecords(MBdatetime)
    /* 
    DROP INDEX IX_MSR_DateTime ON ManageStockRecords
    DROP INDEX IX_MBR_DateTime ON ManageBackRecords
     */
    -- BR SR
    CREATE INDEX IX_SR_Date ON SalesRecords(SRdate)
    CREATE INDEX IX_BR_Date ON BackRecords(BRdate)
    /* 
    DROP INDEX IX_SR_Date ON SalesRecords
    DROP INDEX IX_BR_Date ON BackRecords
    
     */
    """
        self.run_exec(x)
        # Cretae Trige
        x = ["""
            CREATE TRIGGER TG_SR_ADD
                ON SalesRecords
                AFTER INSERT
                AS
                UPDATE Book SET Bnum = Bnum - inserted.SRnum
                FROM Book, inserted
                WHERE Book.Bno = inserted.Bno
            """, """
            CREATE TRIGGER TG_BR_DEC
                ON BackRecords
                AFTER INSERT
                AS
                UPDATE Book SET Bnum=Bnum + inserted.BRnum
                FROM Book,inserted
                WHERE Book.Bno = inserted.Bno
            """, """
            CREATE TRIGGER TG_MSR_ADD
                ON ManageStockRecords
                AFTER INSERT
                AS
                UPDATE Book SET Bnum=Bnum + inserted.MSnum
                FROM Book,inserted
                WHERE Book.Bno = inserted.Bno
            """, """
            CREATE TRIGGER TG_MBR_DEC
                ON ManageBackRecords
                AFTER INSERT
                AS
                UPDATE Book SET Bnum=Bnum - inserted.MBnum
                FROM Book,inserted
                WHERE Book.Bno = inserted.Bno
            """, """
            CREATE TRIGGER TG_MemI_ADD
                ON SalesRecords
                AFTER INSERT
                AS
                UPDATE Member SET Mintegration=Mintegration + inserted.SRnum * inserted.SRprice
                FROM Member,inserted
                WHERE Member.Mno = inserted.Mno
            """, """
            CREATE TRIGGER TG_MemI_DEC
                ON BackRecords
                AFTER INSERT
                AS
                UPDATE Member SET Mintegration=Mintegration - inserted.BRnum * inserted.BRprice
                FROM Member,inserted
                WHERE Member.Mno = inserted.Mno
            """]
        for i in x:
            self.run_exec(i)

        # Data Inert
        x = """
    DELETE FROM ManageBackRecords
    DELETE FROM ManageStockRecords
    
    DELETE FROM SalesRecords
    DELETE FROM BackRecords
    
    DELETE FROM Administrator
    DELETE FROM SalesMan
    DELETE FROM Member
    DELETE FROM Book
    
    INSERT INTO Member VALUES ('C20140405000004', NULL, NULL, NULL, NULL, NULL)
    INSERT INTO Member VALUES ('C20140405000005', NULL, NULL, NULL, NULL, NULL)
    INSERT INTO Member VALUES ('V20130201000001', '赵非中','男', '13298438769', '1992-03-04', 0)
    INSERT INTO Member VALUES ('V20130201000002', '赵超鹏','男', '18798063427', '1992-04-04', 0)
    INSERT INTO Member VALUES ('V20130201000003', '张泰'  ,'女', '15687639423', '1990-05-07', 0)
    INSERT INTO Member VALUES ('V20140405000001', '秦灰奇','女', '15598076534', '1983-02-22', 0)
    INSERT INTO Member VALUES ('V20140405000002', '程舱'  ,'女', '15834019830', '2000-12-03', 0)
    INSERT INTO Member VALUES ('V20140405000003', '孙其中','男', '17730406349', '1998-04-25', 0)
    INSERT INTO Member VALUES ('V20140405000007', '徐物照','女', '13823647859', '2012-03-21', 0)
    
    INSERT INTO Book VALUES ('9991', '草房子', '曹文轩', '¥24.30',  '儿童文学', '人民文学出版社', 0)
    INSERT INTO Book VALUES ('1012', '朝花夕拾', '鲁迅', '¥35.90',  '经典名著', '台海出版社', 0)
    INSERT INTO Book VALUES ('1823', '红楼梦', '曹雪芹', '¥18.75',  '古典文学', '安徽教育出版社', 0)
    INSERT INTO Book VALUES ('4288', '老人与海', '欧内斯特米勒尔海明威', '¥19.60',  '外国文学', '作家出版社', 0)
    INSERT INTO Book VALUES ('5273', '倾城之恋', '张爱玲', '¥47.50',  '现当代文学', '北京十月文艺出版社', 0)
    INSERT INTO Book VALUES ('6737', '中国国家地理美丽的地球系列-高山', '斯特凡诺.阿尔迪托', '¥61.90',  '历史地理类', '中信出版社', 0)
    INSERT INTO Book VALUES ('7188', '道德经', '老子', '¥19.80',  '哲学类', '中国华侨出版社', 0)
    INSERT INTO Book VALUES ('8182', '情感社会学', '戴尔斯潘塞', '¥30.00',  '社会科学类', '江苏教育出版社', 0)
    INSERT INTO Book VALUES ('9128', '斗破苍穹', '天蚕土豆', '¥372.30',  '玄幻文学', '青岛出版社', 0)
    INSERT INTO Book VALUES ('1018', '中国海洋与湿地鸟类', '郑光美', '¥528.00',  '专业图书类', '湖南科技出版社', 0)
    
    INSERT INTO Administrator VALUES ('4752123597', '顾一德', '男', 'Ed1212slt')
    
    INSERT INTO SalesMan VALUES ('4584445321', '李华', '男', 'li2304shu')
    INSERT INTO SalesMan VALUES ('4665757765', '张芳', '女', '673ils336tty')
    
    
       /*  ('BR') */                              
    INSERT INTO BackRecords VALUES ('2016/5/23', '000001', '1012', 'V20130201000001', '4584445321', '40'    , '2', '12:10:00')
    INSERT INTO BackRecords VALUES ('2017/1/2' , '000002', '1823', 'V20130201000002', '4665757765', '20.99' , '3', '12:20:00')
    INSERT INTO BackRecords VALUES ('2017/2/2' , '000003', '4288', 'V20130201000003', '4665757765', '20.89' , '1', '13:00:00')
    INSERT INTO BackRecords VALUES ('2018/3/1' , '000004', '6737', 'V20140405000001', '4665757765', '65.22' , '3', '14:22:00')
    INSERT INTO BackRecords VALUES ('2019/2/1' , '000005', '1012', 'V20140405000002', '4584445321', '39'    , '1', '17:17:00')
    INSERT INTO BackRecords VALUES ('2013/5/1' , '000006', '9128', 'V20140405000003', '4584445321', '380.99', '3', '4:20:00' )
    INSERT INTO BackRecords VALUES ('2014/7/21', '000007', '1018', 'C20140405000004', '4584445321', '535'   , '2', '7:55:00' )
    INSERT INTO BackRecords VALUES ('2015/2/3' , '000008', '4288', 'C20140405000005', '4665757765', '21.1'  , '2', '8:30:00' )
    INSERT INTO BackRecords VALUES ('2018/6/4' , '000009', '7188', 'V20140405000007', '4665757765', '23.4'  , '6', '9:29:00' )
    INSERT INTO BackRecords VALUES ('2016/3/12', '000010', '6737', 'V20140405000007', '4665757765', '65.34' , '3', '0:11:00' )
     
    /*  ('SR') */
    INSERT INTO SalesRecords VALUES ('2016/1/2' , '000001', '9991', 'V20130201000001', '4584445321', '34.3'  , '2', '9:20:00' )
    INSERT INTO SalesRecords VALUES ('2016/1/4' , '000002', '1012', 'V20130201000002', '4665757765', '40.9'  , '3', '2:10:00' )
    INSERT INTO SalesRecords VALUES ('2017/3/1' , '000003', '1823', 'V20130201000003', '4584445321', '20.75' , '1', '12:22:00')
    INSERT INTO SalesRecords VALUES ('2017/4/3' , '000004', '9991', 'V20140405000001', '4584445321', '30.3'  , '2', '7:10:00' )
    INSERT INTO SalesRecords VALUES ('2018/3/12', '000005', '4288', 'V20140405000002', '4584445321', '30'    , '1', '20:10:00')
    INSERT INTO SalesRecords VALUES ('2018/2/1' , '000006', '4288', 'V20140405000003', '4665757765', '21.2'  , '2', '1:10:00' )
    INSERT INTO SalesRecords VALUES ('2017/2/4' , '000007', '8182', 'C20140405000004', '4665757765', '40'    , '3', '11:00:00')
    INSERT INTO SalesRecords VALUES ('2010/1/20', '000008', '9128', 'C20140405000005', '4665757765', '399.1' , '4', '17:10:00')
    INSERT INTO SalesRecords VALUES ('2018/3/11', '000009', '9128', 'V20140405000007', '4584445321', '398.23', '2', '14:12:00')
    INSERT INTO SalesRecords VALUES ('2019/1/1' , '000010', '8182', 'V20140405000007', '4584445321', '33.4'  , '2', '15:44:00')
    INSERT INTO SalesRecords VALUES ('2019/1/1' , '000011', '8182', 'V20140405000007', '4584445321', '33.4'  , '2', '15:44:00')
    INSERT INTO SalesRecords VALUES ('2019/1/1' , '000012', '8182', 'V20140405000007', '4584445321', '33.4'  , '2', '15:44:00')
    INSERT INTO SalesRecords VALUES ('2019/1/1' , '000013', '8182', 'V20140405000007', '4584445321', '33.4'  , '2', '15:44:00')
    
  
    
    /* ('MSR') 统一入库500本*/
    INSERT INTO ManageStockRecords VALUES ('2000/3/3 8:30','4752123597','9991','500')
    INSERT INTO ManageStockRecords VALUES ('2000/3/3 8:30','4752123597','1012','500')
    INSERT INTO ManageStockRecords VALUES ('2000/3/3 8:30','4752123597','1823','500')
    INSERT INTO ManageStockRecords VALUES ('2000/3/3 8:30','4752123597','4288','500')
    INSERT INTO ManageStockRecords VALUES ('2000/3/3 8:30','4752123597','5273','500')
    INSERT INTO ManageStockRecords VALUES ('2000/3/3 8:30','4752123597','6737','500')
    INSERT INTO ManageStockRecords VALUES ('2000/3/3 8:30','4752123597','7188','500')
    INSERT INTO ManageStockRecords VALUES ('2000/3/3 8:30','4752123597','8182','500')
    INSERT INTO ManageStockRecords VALUES ('2000/3/3 8:30','4752123597','9128','500')
    INSERT INTO ManageStockRecords VALUES ('2000/3/3 8:30','4752123597','1018','500')
    
    
    /* ('MSR') */
    INSERT INTO ManageStockRecords VALUES ('2013/3/3 8:30', '4752123597', '9991', '100')
    INSERT INTO ManageStockRecords VALUES ('2013/3/3 8:34', '4752123597', '1012', '100')
    INSERT INTO ManageStockRecords VALUES ('2014/4/5 7:50', '4752123597', '1823', '200')
    INSERT INTO ManageStockRecords VALUES ('2014/4/5 8:43', '4752123597', '4288', '20')
    INSERT INTO ManageStockRecords VALUES ('2014/5/5 8:20', '4752123597', '4288', '50')
    INSERT INTO ManageStockRecords VALUES ('2014/6/6 7:58', '4752123597', '4288', '70')
    INSERT INTO ManageStockRecords VALUES ('2015/3/3 8:27', '4752123597', '1823', '100')
    INSERT INTO ManageStockRecords VALUES ('2015/9/3 7:32', '4752123597', '1012', '50')
    INSERT INTO ManageStockRecords VALUES ('2015/10/2 8:38','4752123597', '1012', '40')
    
    
    /* ('MBR') */
    INSERT INTO ManageBackRecords VALUES ('2013/3/3 8:30', '4752123597', '6737', '10')
    INSERT INTO ManageBackRecords VALUES ('2013/3/3 8:34', '4752123597', '1012', '100')
    INSERT INTO ManageBackRecords VALUES ('2014/4/5 7:50', '4752123597', '1823', '20')
    INSERT INTO ManageBackRecords VALUES ('2014/4/5 8:43', '4752123597', '7188', '20')
    INSERT INTO ManageBackRecords VALUES ('2014/5/5 8:20', '4752123597', '7188', '50')
    INSERT INTO ManageBackRecords VALUES ('2014/6/6 7:58', '4752123597', '7188', '70')
    INSERT INTO ManageBackRecords VALUES ('2015/3/3 8:27', '4752123597', '1823', '100')
    INSERT INTO ManageBackRecords VALUES ('2015/9/3 7:32', '4752123597', '1018', '50')
    INSERT INTO ManageBackRecords VALUES ('2015/10/2 8:38','4752123597', '1018', '40')
    """
        self.run_exec(x)

    def cursor_data_to_list(self, cur = None):
        """
        游标数据变为list
        :param cur: 游标
        :return:数据表
        """
        if isinstance(cur, pymssql.Cursor):
            self.cursor = cur
        else:
            pass

        table_data = []
        try :
            row = self.cursor.fetchone()
            while row:
                # print(row)
                table_data.append((row))
                if len(table_data) == 50:
                    break
                row = self.cursor.fetchone()
            return table_data

        except pymssql.OperationalError:
            return table_data

    def cursor_data_to_list_all(self, cur = None):
        """
        游标数据变为list
        :param cur: 游标
        :return:数据表
        """
        if isinstance(cur, pymssql.Cursor):
            self.cursor = cur
        else:
            pass
        table = []
        x = self.cursor_data_to_list()
        while len(x):
            # print(x, len(x))
            table.append(x)
            x = self.cursor_data_to_list()

        return table


    def __del__(self):
        self.close()


if __name__ == '__main__':
    dbbase = DbDesignBase()
    print(dbbase.is_name('的的口区'))