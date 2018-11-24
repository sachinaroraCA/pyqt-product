# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_collection/models_module.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class ModelWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(ModelWindow, self).__init__(parent)
        self.setWindowTitle("Financial Product Analysis Tool - Model")
        self.ui = Ui_MainWindow(self)


class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(615, 439)
        self.temp_window = MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txt_search = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_search.setGeometry(QtCore.QRect(50, 60, 329, 25))
        self.txt_search.setObjectName("txt_search")
        self.buttonBox = QtWidgets.QGroupBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(380, 40, 131, 151))
        self.buttonBox.setTitle("")
        self.buttonBox.setObjectName("buttonBox")
        self.btn_delete = QtWidgets.QPushButton(self.buttonBox)
        self.btn_delete.setGeometry(QtCore.QRect(20, 60, 91, 25))
        self.btn_delete.setObjectName("btn_delete")
        self.btn_addNew = QtWidgets.QPushButton(self.buttonBox)
        self.btn_addNew.setGeometry(QtCore.QRect(20, 30, 89, 25))
        self.btn_addNew.setObjectName("btn_addNew")
        self.btn_export = QtWidgets.QPushButton(self.buttonBox)
        self.btn_export.setGeometry(QtCore.QRect(20, 120, 91, 25))
        self.btn_export.setObjectName("btn_export")
        self.btn_modify = QtWidgets.QPushButton(self.buttonBox)
        self.btn_modify.setGeometry(QtCore.QRect(20, 90, 91, 25))
        self.btn_modify.setObjectName("btn_modify")
        self.scrollArea_products = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_products.setGeometry(QtCore.QRect(50, 90, 329, 101))
        self.scrollArea_products.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_products.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_products.setWidgetResizable(True)
        self.scrollArea_products.setObjectName("scrollArea_products")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 313, 99))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.scrollArea_products.setWidget(self.scrollAreaWidgetContents_3)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 20, 71, 17))
        self.label.setObjectName("label")
        self.groupBox_overview = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_overview.setGeometry(QtCore.QRect(50, 230, 481, 141))
        self.groupBox_overview.setObjectName("groupBox_overview")
        self.txt_overview = QtWidgets.QTextEdit(self.groupBox_overview)
        self.txt_overview.setGeometry(QtCore.QRect(10, 30, 461, 101))
        self.txt_overview.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.txt_overview.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txt_overview.setReadOnly(True)
        self.txt_overview.setObjectName("txt_overview")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 615, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.btn_addNew.clicked.connect(self.btn_addNew_clicked)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Financial Product Analysis Tool - Model"))
        self.txt_search.setPlaceholderText(_translate("MainWindow", " Search"))
        self.btn_delete.setText(_translate("MainWindow", "Delete"))
        self.btn_addNew.setText(_translate("MainWindow", "Add New"))
        self.btn_export.setText(_translate("MainWindow", "Export"))
        self.btn_modify.setText(_translate("MainWindow", "Modify"))
        self.label.setText(_translate("MainWindow", "Products:"))
        self.groupBox_overview.setTitle(_translate("MainWindow", "Overview"))

    def btn_addNew_clicked(self):
        from windows.models_addNew import ModelAddNewWindow
        self.model_addnew_win = ModelAddNewWindow(parent=self.temp_window)
        self.model_addnew_win.show()