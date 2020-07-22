USE BookStore

CREATE TRIGGER TG_SR_ADD
    ON SalesRecords
    AFTER INSERT
    AS
    UPDATE Book SET Bnum = Bnum - inserted.SRnum
    FROM Book, inserted
    WHERE Book.Bno = inserted.Bno

CREATE TRIGGER TG_BR_DEC
    ON BackRecords
    AFTER INSERT
    AS
    UPDATE Book SET Bnum=Bnum + inserted.BRnum
    FROM Book,inserted
    WHERE Book.Bno = inserted.Bno

CREATE TRIGGER TG_MSR_ADD
    ON ManageStockRecords
    AFTER INSERT
    AS
    UPDATE Book SET Bnum=Bnum + inserted.MSnum
    FROM Book,inserted
    WHERE Book.Bno = inserted.Bno

CREATE TRIGGER TG_MBR_DEC
    ON ManageBackRecords
    AFTER INSERT
    AS
    UPDATE Book SET Bnum=Bnum - inserted.MBnum
    FROM Book,inserted
    WHERE Book.Bno = inserted.Bno

CREATE TRIGGER TG_MemI_ADD
    ON SalesRecords
    AFTER INSERT
    AS
    UPDATE Member SET Mintegration=Mintegration + inserted.SRnum * inserted.SRprice
    FROM Member,inserted
    WHERE Member.Mno = inserted.Mno

CREATE TRIGGER TG_MemI_DEC
    ON BackRecords
    AFTER INSERT
    AS
    UPDATE Member SET Mintegration=Mintegration - inserted.BRnum * inserted.BRprice
    FROM Member,inserted
    WHERE Member.Mno = inserted.Mno










