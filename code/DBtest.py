# coding=utf-8
import pymssql
import time
''' 
    
    host='127.0.0.1',
    user='1234',
    password='123',
    database = 's1',
    
    host='172.18.64.138:1433',
    user='s1033170230',
    password='1033170230',
    database='s1033170230',
     '''
start = time.clock()
conn = pymssql.connect(
    host='127.0.0.1',
    user='123',
    password='123',
    database='s1',

    )

x='''
drop table CP
drop table Paper
drop table Customer

CREATE TABLE Paper(
    pno CHAR(6) Not NULL PRIMARY KEY,
    pns CHAR(10) Not NULL,
    ppr smallmoney,
    );


CREATE TABLE Customer(
    cno CHAR(8) Not NULL PRIMARY KEY,
    cna CHAR(8) Not NULL,
    adr CHAR(20) Not NULL,
    );

CREATE TABLE CP(
    cno CHAR(8),
    pno CHAR(6),
    num smallint default 1,
    PRIMARY KEY(cno, pno),
    constraint FK_CP_cno foreign key(cno) references Customer(cno),
    constraint FK_CP_pno foreign key(pno) references Paper(pno),
    );

        
INSERT INTO Paper VALUES('000001', '人民日报', 12.5)
INSERT INTO Paper VALUES('000002', '解放日报', 14.5)
INSERT INTO Paper VALUES('000003', '光明日报', 10.5)
INSERT INTO Paper VALUES('000004', '青年报', 11.5)
INSERT INTO Paper VALUES('000005', '扬子晚报', 18.5)

INSERT INTO Customer VALUES('10000001', '李涛', '无锡市解放东路132号')
INSERT INTO Customer VALUES('10000002', '钱金浩', '无锡市人民西路234号')
INSERT INTO Customer VALUES('10000003', '邓杰', '无锡市惠河路270号')
INSERT INTO Customer VALUES('10000004', '朱海文', '无锡市中山东路432号')
INSERT INTO Customer VALUES('10000005', '欧阳阳文', '无锡市中山东路532号')

INSERT INTO CP VALUES('10000001', '000001', 2)
INSERT INTO CP VALUES('10000001', '000002', 4)
INSERT INTO CP VALUES('10000001', '000005', 6)
INSERT INTO CP VALUES('10000002', '000001', 2)
INSERT INTO CP VALUES('10000002', '000003', 2)
INSERT INTO CP VALUES('10000002', '000005', 2)
INSERT INTO CP VALUES('10000003', '000003', 2)
INSERT INTO CP VALUES('10000003', '000004', 4)
INSERT INTO CP VALUES('10000004', '000001', 1)
INSERT INTO CP VALUES('10000004', '000003', 3)
INSERT INTO CP VALUES('10000004', '000005', 2)
INSERT INTO CP VALUES('10000005', '000003', 4)
INSERT INTO CP VALUES('10000005', '000002', 1)
INSERT INTO CP VALUES('10000005', '000004', 3)
INSERT INTO CP VALUES('10000005', '000005', 5)
INSERT INTO CP VALUES('10000005', '000001', 4)
'''


cursor = conn.cursor()

try:
    cursor.execute(x)
except (pymssql.OperationalError):
    print("pymssql.OperationalError")
else:
    print("Operatina OK")


# 插入一条数据
# cur.execute("insert into student values('2','Tom','3 year 2 class','9')")


# 修改查询条件的数据
# cur.execute("update student set class='3 year 1 class' where name = 'Tom'")

# 删除查询条件的数据
# cur.execute("delete from student where age='9'")
cursor.execute("select * from Paper")
row = cursor.fetchone()

while row:
    print(row)
    row = cursor.fetchone()
conn.cursor()
conn.commit()
cursor.close()
conn.commit()
conn.close()
