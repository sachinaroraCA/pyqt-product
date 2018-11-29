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
        """""""""""""""""""""""""""""""""""""""
          USER INTERFACE OF TIME SERIES WINDOW 
        """""""""""""""""""""""""""""""""""""""
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

        self.timeseries_list_view()
        self.btn_addNew.clicked.connect(self.btn_addNew_clicked)
        self.btn_return.clicked.connect(self.btn_return_clicked)
        self.btn_export.clicked.connect(self.btn_export_clicked)
        self.btn_modify.clicked.connect(self.btn_modify_clicked)
        self.btn_delete.clicked.connect(self.btn_delete_clicked)
        self.btn_bind.clicked.connect(self.btn_bind_clicked)
        self.btn_unbind.clicked.connect(self.btn_unbind_clicked)

        self.products_list_view()

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

        file_dailog = QtWidgets.QFileDialog()
        default_file_extension = '.csv'

        name = file_dailog.getSaveFileName(self.temp_window, 'Save File')[0]
        if default_file_extension not in name:
            name += default_file_extension

        timeseries_info = self.get_timeseries_details()
        print(timeseries_info)
        keys = list(timeseries_info.keys())
        import csv
        with open(name, 'w+') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerow(timeseries_info)
            output_file.close()

    def btn_modify_clicked(self):
        result = [x.row() for x in self.timeseries_listWidget.selectedIndexes()]
        if result:
            timeseries_info = self.timeseries_info
            from windows.timeseries_addNew import TimeSeriesAddNewWindow
            self.modify_win = TimeSeriesAddNewWindow(parent=self.temp_window)
            self.modify_win.ui.selected_timeseriesId = self.timeseries_info["id"]
            self.modify_win.ui.selected_productId = self.timeseries_info["product_ID"]
            self.modify_win.ui.txt_memo.setPlainText(timeseries_info["description"])
            self.modify_win.ui.combo_filetype.setCurrentText(timeseries_info["file_type"])
            self.modify_win.ui.combo_analysetype.setCurrentText(timeseries_info["analyse_type"])
            self.modify_win.ui.txt_emptydata.setText(str(timeseries_info["empty_data"]))
            self.modify_win.ui.txt_seriesdata.setText(str(timeseries_info["series_data"]))
            # self.modify_win.ui.txt_endtime.setTime(timeseries_info["end_time"])
            # self.modify_win.ui.txt_starttime.setTime(timeseries_info["start_time"])
            self.modify_win.ui.txt_name.setText(timeseries_info["name"])
            self.modify_win.ui.modify = True
            self.modify_win.show()

    def btn_delete_clicked(self):
        self.delete_timeseries(self.selected_timeseriesId)
        # self.productId_list.remove(product_code)
        self.timeseries_list.remove(self.selected_timeseries)
        self.timeseriesId_list.remove(self.selected_timeseriesId)
        self.timeseries_list_view()

    def btn_bind_clicked(self):
        from windows.database_util import DatabaseConnect
        db = DatabaseConnect()
        updated = db.update_timeseries_productId(self.selected_timeseriesId, self.selected_productId)
        if updated:
            print("Successfully bind the product with time series !!!")

    def btn_unbind_clicked(self):
        from windows.database_util import DatabaseConnect
        db = DatabaseConnect()
        updated = db.update_timeseries_productId(self.selected_timeseriesId, "NULL")
        if updated:
            print("Successfully unbind the product from time series !!!")

    def timeseries_list_view(self):
        from windows.database_util import DatabaseConnect
        db = DatabaseConnect()
        self.timeseries_list, self.timeseriesId_list = db.get_timeserieses()
        self.timeseries_listWidget = QtWidgets.QListWidget()

        index =0
        for item in self.timeseriesId_list:
            listitem = QtWidgets.QListWidgetItem()
            listitem.setText(self.timeseries_list[index])
            listitem.setData(1, item)
            index += 1
            self.timeseries_listWidget.addItem(listitem)
        self.timeseries_listWidget.itemClicked.connect(self.timeseries_list_item_event)
        self.scrollArea_timeseries.setWidget(self.timeseries_listWidget)

    def timeseries_list_item_event(self, item):
        self.selected_timeseries = item.text()
        self.selected_timeseriesId = item.data(1)
        print(self.selected_timeseriesId)
        self.get_timeseries_details()

    def get_timeseries_details(self):
        from windows.database_util import DatabaseConnect
        db = DatabaseConnect()
        self.timeseries_info = db.get_timeseries_details(self.selected_timeseriesId)
        return self.timeseries_info

    def delete_timeseries(self, id):
        from windows.database_util import DatabaseConnect
        db = DatabaseConnect()
        deleted = db.delete_timeseries(id=id)
        if deleted:
            print("Successfully deleted the time series !!!")

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                      PRODUCT PART
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def get_products(self):
        from windows.database_util import DatabaseConnect
        db = DatabaseConnect()
        self.products_list, self.productId_list = db.get_products()

    def products_list_view(self):
        self.listWidget_product = QtWidgets.QListWidget()
        self.get_products()
        index = 0
        for item in self.productId_list:
            listitem = QtWidgets.QListWidgetItem()
            listitem.setText(self.products_list[index])
            listitem.setData(1, item)
            index += 1
            self.listWidget_product.addItem(listitem)
        self.listWidget_product.itemClicked.connect(self.list_item_event)
        self.scrollArea_products.setWidget(self.listWidget_product)

    def list_item_event(self, item):
        print(repr(item.text()))
        self.selected_product = item.text()
        self.selected_productId = item.data(1)
        print(self.selected_productId)
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
