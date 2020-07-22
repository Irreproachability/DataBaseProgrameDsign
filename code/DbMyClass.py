from DbSelect import DbSelect
from DbInsert import DbInsert
from DbUpdata import DbUpdata
from DbDetele import DbDelete
import re


class DbMyClass(DbDelete, DbUpdata, DbInsert, DbSelect):

    def __init__(self):
        super(DbMyClass, self).__init__()


if __name__ == '__main__':
    db = DbMyClass()
    db.delete_book('4123')
    db.select_book()
    while True:
        pass

