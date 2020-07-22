# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTuiTable_empty.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Frame_table_empty(object):
    def setupUi(self, Frame_table_empty):
        Frame_table_empty.setObjectName("Frame_table_empty")
        Frame_table_empty.setEnabled(True)
        Frame_table_empty.resize(695, 511)
        font = QtGui.QFont()
        font.setPointSize(12)
        Frame_table_empty.setFont(font)
        Frame_table_empty.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gridLayout_2 = QtWidgets.QGridLayout(Frame_table_empty)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lable_table_name = QtWidgets.QLabel(Frame_table_empty)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.lable_table_name.setFont(font)
        self.lable_table_name.setAlignment(QtCore.Qt.AlignCenter)
        self.lable_table_name.setObjectName("lable_table_name")
        self.horizontalLayout.addWidget(self.lable_table_name)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_hide = QtWidgets.QPushButton(Frame_table_empty)
        self.pushButton_hide.setObjectName("pushButton_hide")
        self.horizontalLayout.addWidget(self.pushButton_hide)
        self.spinBox = QtWidgets.QSpinBox(Frame_table_empty)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(100)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.label_page = QtWidgets.QLabel(Frame_table_empty)
        self.label_page.setObjectName("label_page")
        self.horizontalLayout.addWidget(self.label_page)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(Frame_table_empty)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setDragDropOverwriteMode(True)
        self.tableWidget.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(50)
        self.tableWidget.setColumnCount(15)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Frame_table_empty)
        QtCore.QMetaObject.connectSlotsByName(Frame_table_empty)

    def retranslateUi(self, Frame_table_empty):
        _translate = QtCore.QCoreApplication.translate
        Frame_table_empty.setWindowTitle(_translate("Frame_table_empty", "数据表"))
        self.lable_table_name.setText(_translate("Frame_table_empty", "TextName"))
        self.pushButton_hide.setText(_translate("Frame_table_empty", "退出"))
        self.label_page.setText(_translate("Frame_table_empty", "共1页"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)

