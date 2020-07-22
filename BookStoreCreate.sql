USE BookStore


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
    SRdate DATE NOT NULL,
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
    BRdate DATE NOT NULL,
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
    MSdatetime SMALLDATETIME NOT NULL,
    Ano CHAR(10) NOT NULL, 
    Bno CHAR(10) NOT NULL, 
    MSnum INT,
    PRIMARY KEY( MSdatetime,Ano, Bno),
    CONSTRAINT FK_MS_Ano FOREIGN KEY(Ano) REFERENCES Administrator(Ano),
    CONSTRAINT FK_MS_Bno FOREIGN KEY(Bno) REFERENCES Book(Bno),
)
CREATE TABLE ManageBackRecords(
    MBdatetime SMALLDATETIME NOT NULL,
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
CREATE INDEX IX_Book_Bauthor ON Book(Bauthor)
CREATE INDEX IX_Book_Btype ON Book(Btype)
CREATE INDEX IX_Book_Bpublish ON Book(Bpublish)

/*
DROP INDEX IX_Book_Bno ON Book
DROP INDEX IX_Book_Bname ON Book
DROP INDEX IX_Book_Bauthor ON Book
DROP INDEX IX_Book_Btype ON Book
DROP INDEX IX_Book_Bpublish ON Book
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













