# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_collection/time_series_module.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class TimeSeriesWindow(QMainWindow):
    def __init__(self, parent=None):
        super(TimeSeriesWindow, self).__init__(parent)
        self.setWindowTitle("Financial Product Analysis Tool - Time Series")
        self.ui = Ui_MainWindow(self)


class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(615, 439)
        self.temp_window = MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txt_timeseries = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_timeseries.setGeometry(QtCore.QRect(50, 60, 329, 25))
        self.txt_timeseries.setObjectName("txt_timeseries")
        self.groupBox_timeseries = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_timeseries.setGeometry(QtCore.QRect(380, 40, 131, 151))
        self.groupBox_timeseries.setTitle("")
        self.groupBox_timeseries.setObjectName("groupBox_timeseries")
        self.btn_delete = QtWidgets.QPushButton(self.groupBox_timeseries)
        self.btn_delete.setGeometry(QtCore.QRect(20, 60, 91, 25))
        self.btn_delete.setObjectName("btn_delete")
        self.btn_addNew = QtWidgets.QPushButton(self.groupBox_timeseries)
        self.btn_addNew.setGeometry(QtCore.QRect(20, 30, 89, 25))
        self.btn_addNew.setObjectName("btn_addNew")
        self.btn_export = QtWidgets.QPushButton(self.groupBox_timeseries)
        self.btn_export.setGeometry(QtCore.QRect(20, 120, 91, 25))
        self.btn_export.setObjectName("btn_export")
        self.btn_modify = QtWidgets.QPushButton(self.groupBox_timeseries)
        self.btn_modify.setGeometry(QtCore.QRect(20, 90, 89, 25))
        self.btn_modify.setObjectName("btn_modify")
        self.scrollArea_timeseries = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_timeseries.setGeometry(QtCore.QRect(50, 90, 329, 101))
        self.scrollArea_timeseries.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_timeseries.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_timeseries.setWidgetResizable(True)
        self.scrollArea_timeseries.setObjectName("scrollArea_timeseries")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 313, 99))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.scrollArea_timeseries.setWidget(self.scrollAreaWidgetContents_3)
        self.lbl_timeseries = QtWidgets.QLabel(self.centralwidget)
        self.lbl_timeseries.setGeometry(QtCore.QRect(50, 20, 101, 17))
        self.lbl_timeseries.setObjectName("lbl_timeseries")
        self.scrollArea_products = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_products.setGeometry(QtCore.QRect(50, 280, 329, 101))
        self.scrollArea_products.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_products.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_products.setWidgetResizable(True)
        self.scrollArea_products.setObjectName("scrollArea_products")
        self.scrollAreaWidgetContents_7 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_7.setGeometry(QtCore.QRect(0, 0, 313, 99))
        self.scrollAreaWidgetContents_7.setObjectName("scrollAreaWidgetContents_7")
        self.scrollArea_products.setWidget(self.scrollAreaWidgetContents_7)
        self.txt_products = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_products.setGeometry(QtCore.QRect(50, 250, 329, 25))
        self.txt_products.setObjectName("txt_products")
        self.lbl_product = QtWidgets.QLabel(self.centralwidget)
        self.lbl_product.setGeometry(QtCore.QRect(50, 220, 101, 17))
        self.lbl_product.setObjectName("lbl_product")
        self.groupBox_products = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_products.setGeometry(QtCore.QRect(380, 230, 131, 151))
        self.groupBox_products.setTitle("")
        self.groupBox_products.setObjectName("groupBox_products")
        self.btn_unbind = QtWidgets.QPushButton(self.groupBox_products)
        self.btn_unbind.setGeometry(QtCore.QRect(20, 80, 91, 25))
        self.btn_unbind.setObjectName("btn_unbind")
        self.btn_bind = QtWidgets.QPushButton(self.groupBox_products)
        self.btn_bind.setGeometry(QtCore.QRect(20, 50, 89, 25))
        self.btn_bind.setObjectName("btn_bind")
        self.btn_return = QtWidgets.QPushButton(self.groupBox_products)
        self.btn_return.setGeometry(QtCore.QRect(20, 110, 89, 25))
        self.btn_return.setObjectName("btn_return")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 615, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.btn_addNew.clicked.connect(self.btn_addNew_clicked)
        self.btn_return.clicked.connect(self.btn_return_clicked)
        self.btn_export.clicked.connect(self.btn_export_clicked)
        self.btn_modify.clicked.connect(self.btn_modify_clicked)
        self.btn_delete.clicked.connect(self.btn_delete_clicked)
        self.btn_bind.clicked.connect(self.btn_bind_clicked)
        self.btn_unbind.clicked.connect(self.btn_unbind_clicked)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Financial Product Analysis Tool - Time Series"))
        self.txt_timeseries.setPlaceholderText(_translate("MainWindow", " Search"))
        self.btn_delete.setText(_translate("MainWindow", "Delete"))
        self.btn_addNew.setText(_translate("MainWindow", "Add New"))
        self.btn_export.setText(_translate("MainWindow", "Export"))
        self.btn_modify.setText(_translate("MainWindow", "Modify"))
        self.lbl_timeseries.setText(_translate("MainWindow", "Time Series :"))
        self.txt_products.setPlaceholderText(_translate("MainWindow", " Search"))
        self.lbl_product.setText(_translate("MainWindow", "Products :"))
        self.btn_unbind.setText(_translate("MainWindow", "Unbind"))
        self.btn_bind.setText(_translate("MainWindow", "Bind"))
        self.btn_return.setText(_translate("MainWindow", "Return"))

    def btn_addNew_clicked(self):
        from windows.timeseries_addNew import TimeSeriesAddNewWindow
        self.timeseries_addnew_win = TimeSeriesAddNewWindow(self.temp_window)
        self.timeseries_addnew_win.show()

    def btn_return_clicked(self):
        self.temp_window.hide()

    def btn_export_clicked(self):
        pass

    def btn_modify_clicked(self):
        pass

    def btn_delete_clicked(self):
        pass

    def btn_bind_clicked(self):
        pass

    def btn_unbind_clicked(self):
        pass

