# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTuiFrame_back_book.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Frame_back_book(object):
    def setupUi(self, Frame_back_book):
        Frame_back_book.setObjectName("Frame_back_book")
        Frame_back_book.resize(400, 250)
        font = QtGui.QFont()
        font.setPointSize(14)
        Frame_back_book.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(Frame_back_book)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 27, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 2)
        self.pushButton_back = QtWidgets.QPushButton(Frame_back_book)
        self.pushButton_back.setObjectName("pushButton_back")
        self.gridLayout.addWidget(self.pushButton_back, 0, 3, 1, 1)
        self.label_hint = QtWidgets.QLabel(Frame_back_book)
        self.label_hint.setText("")
        self.label_hint.setAlignment(QtCore.Qt.AlignCenter)
        self.label_hint.setObjectName("label_hint")
        self.gridLayout.addWidget(self.label_hint, 1, 1, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(Frame_back_book)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(Frame_back_book)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(Frame_back_book)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(Frame_back_book)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_brbno = QtWidgets.QLineEdit(Frame_back_book)
        self.lineEdit_brbno.setObjectName("lineEdit_brbno")
        self.verticalLayout.addWidget(self.lineEdit_brbno)
        self.lineEdit_brmno = QtWidgets.QLineEdit(Frame_back_book)
        self.lineEdit_brmno.setObjectName("lineEdit_brmno")
        self.verticalLayout.addWidget(self.lineEdit_brmno)
        self.lineEdit_brprice = QtWidgets.QLineEdit(Frame_back_book)
        self.lineEdit_brprice.setObjectName("lineEdit_brprice")
        self.verticalLayout.addWidget(self.lineEdit_brprice)
        self.lineEdit_brnum = QtWidgets.QLineEdit(Frame_back_book)
        self.lineEdit_brnum.setObjectName("lineEdit_brnum")
        self.verticalLayout.addWidget(self.lineEdit_brnum)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 1, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(72, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 3, 1, 1)
        self.pushButton_ensure = QtWidgets.QPushButton(Frame_back_book)
        self.pushButton_ensure.setObjectName("pushButton_ensure")
        self.gridLayout.addWidget(self.pushButton_ensure, 3, 1, 1, 1)
        self.pushButton_clear = QtWidgets.QPushButton(Frame_back_book)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.gridLayout.addWidget(self.pushButton_clear, 3, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 4, 1, 1, 2)

        self.retranslateUi(Frame_back_book)
        QtCore.QMetaObject.connectSlotsByName(Frame_back_book)

    def retranslateUi(self, Frame_back_book):
        _translate = QtCore.QCoreApplication.translate
        Frame_back_book.setWindowTitle(_translate("Frame_back_book", "退货"))
        self.pushButton_back.setText(_translate("Frame_back_book", "返回"))
        self.label.setText(_translate("Frame_back_book", "书号"))
        self.label_2.setText(_translate("Frame_back_book", "顾客号"))
        self.label_4.setText(_translate("Frame_back_book", "购买价格"))
        self.label_3.setText(_translate("Frame_back_book", "退货数量"))
        self.pushButton_ensure.setText(_translate("Frame_back_book", "确认"))
        self.pushButton_clear.setText(_translate("Frame_back_book", "清空"))

