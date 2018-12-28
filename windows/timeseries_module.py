from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class TimeSeriesWindow(QMainWindow):
    """
                Main class of the Time-series module
    """
    def __init__(self, parent=None):
        super(TimeSeriesWindow, self).__init__(parent)
        self.setWindowTitle("Financial Product Analysis Tool - Time Series")
        self.ui = Ui_MainWindow(self)
        self.parent_win = parent


class Ui_MainWindow(object):
    """
            USER INTERFACE CLASS OF TIME SERIES WINDOW
    """
    def __init__(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedHeight(439)
        MainWindow.setFixedWidth(615)
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
        self.scrollArea_timeseries.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
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
        self.scrollArea_products.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
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

        self.btn_delete.setDisabled(True)
        self.btn_bind.setDisabled(True)
        self.btn_unbind.setDisabled(True)
        self.btn_modify.setDisabled(True)
        self.btn_export.setDisabled(True)
        self.btn_unbind.setDisabled(True)

        self.txt_products.textChanged.connect(self.productfilterClicked)
        self.txt_timeseries.textChanged.connect(self.timeseriesfilterClicked)

        self.load_products_list()
        self.selected_timeseries = None
        self.selected_product = None

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        """
                Set the properties of the UI elements
        :param MainWindow:
        """
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
        """
                        Open the "Time-series:Add new" window
        """
        from windows.timeseries_addNew import TimeSeriesAddNewWindow
        self.timeseries_addnew_win = TimeSeriesAddNewWindow(self.temp_window)
        self.timeseries_addnew_win.show()
        self.temp_window.hide()

    def btn_return_clicked(self):
        """
                        Close the current window
        :return:
        """
        self.temp_window.hide()

    def btn_export_clicked(self):
        """
                    Export the time-series data as a CSV file
        """
        try:
            file_dailog = QtWidgets.QFileDialog()
            default_file_extension = '.csv'

            name = file_dailog.getSaveFileName(self.temp_window, 'Save File')[0]
            if name:
                if default_file_extension not in name:
                    name += default_file_extension

                timeseries_info = self.get_timeseries_details()
                keys = list(timeseries_info.keys())
                import csv
                with open(name, 'w+') as output_file:
                    dict_writer = csv.DictWriter(output_file, keys)
                    dict_writer.writeheader()
                    dict_writer.writerow(timeseries_info)
                    output_file.close()
                QtWidgets.QMessageBox.about(self.temp_window, "info", "Exported data successfully !!!")
        except Exception as ex:
            QtWidgets.QMessageBox.about(self.temp_window, "Error", str(ex))

    def btn_modify_clicked(self):
        """
                    Open the "Time-series:Add new" window with pre-filled values of selected product to update
        """
        import datetime
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
            end_time = datetime.datetime.fromtimestamp(timeseries_info["end_time"]/1000).strftime('%Y-%m-%d %H:%M:%S.%f')
            start_time = datetime.datetime.fromtimestamp(timeseries_info["start_time"]/1000).strftime('%Y-%m-%d %H:%M:%S.%f')
            self.modify_win.ui.txt_endtime.setText(str(end_time)[:-10])
            self.modify_win.ui.txt_starttime.setText(str(start_time)[:-10])
            self.modify_win.ui.txt_name.setText(timeseries_info["name"])
            self.modify_win.ui.source_file = timeseries_info["source_file"]
            self.modify_win.ui.modify = True
            self.modify_win.show()
            self.temp_window.hide()

    def btn_delete_clicked(self):
        """
                    Call a function delete_timeseries to delete the selected time-series
        """
        buttonReply = QtWidgets.QMessageBox.question(self.temp_window, "Message",
                                                     'Delete the Time series "{}" ?'.format(self.selected_timeseries),
                                                     QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                     QtWidgets.QMessageBox.No)
        if buttonReply == QtWidgets.QMessageBox.Yes:
            deleted = self.delete_timeseries(self.selected_timeseriesId)
            if deleted:
                self.timeseries_list.remove(self.selected_timeseries)
                self.timeseriesId_list.remove(self.selected_timeseriesId)
                self.timeseries_list_view()

    def btn_bind_clicked(self):
        """
                    Update the id of the selected product in the selected time series
        :return:
        """
        from utils.database_utils import DatabaseConnect
        db = DatabaseConnect()
        updated = db.update_timeseries_productId(self.selected_timeseriesId, self.selected_productId,
                                                 window=self.temp_window)
        if updated:
            self.btn_bind.setDisabled(True)
            self.btn_unbind.setDisabled(True)
            QtWidgets.QMessageBox.about(self.temp_window, "info",
                                        "Successfully bind the product with time series !!!")
            self.timeseries_list_view()
            self.load_products_list()

    def btn_unbind_clicked(self):
        """
                    Remove the id of the product from the selected time-series
        :return:
        """
        from utils.database_utils import DatabaseConnect
        db = DatabaseConnect()
        updated = db.update_timeseries_productId(self.selected_timeseriesId, "NULL", window=self.temp_window)
        if updated:
            self.btn_bind.setDisabled(True)
            self.btn_unbind.setDisabled(True)
            QtWidgets.QMessageBox.about(self.temp_window, "info",
                                        "Successfully unbind the product from time series !!!")
            self.timeseries_list_view()
            self.load_products_list()

    def timeseries_list_view(self):
        """
                 creates the items of list widget to display the list of Time-series on the window
        """
        from utils.database_utils import DatabaseConnect
        db = DatabaseConnect()
        self.timeseries_list, self.timeseriesId_list = db.get_timeserieses(window=self.temp_window)
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
        """
                set the currently selected time-series for the window with its availability to bind or unbind
        :param item:
        """
        self.selected_timeseries = item.text()
        self.selected_timeseriesId = item.data(1)
        self.btn_export.setEnabled(True)
        self.btn_delete.setEnabled(True)
        self.btn_modify.setEnabled(True)
        self.get_timeseries_details()
        if self.selected_timeseries and self.selected_product:
            if self.timeseries_info["product_ID"] == self.selected_productId:
                self.btn_unbind.setEnabled(True)
                self.btn_bind.setDisabled(True)
            elif not self.timeseries_info["product_ID"] or self.timeseries_info["product_ID"] == "":
                self.btn_bind.setEnabled(True)
                self.btn_unbind.setDisabled(True)
            else:
                self.btn_bind.setDisabled(True)
                self.btn_unbind.setDisabled(True)

    def get_timeseries_details(self):
        """
                Get details of the Time series from the database.
        :return: timeseries_info
        """
        from utils.database_utils import DatabaseConnect
        db = DatabaseConnect()
        self.timeseries_info = db.get_timeseries_details(self.selected_timeseriesId, window=self.temp_window)
        return self.timeseries_info

    def delete_timeseries(self, id):
        """
                Calls a function delete_timeseries from database_util.py class to delete the Time series.
        :param id:
        :return:
        """
        from utils.database_utils import DatabaseConnect
        db = DatabaseConnect()
        deleted = db.delete_timeseries(id=id, window=self.temp_window)
        return deleted

    def timeseriesfilterClicked(self):
        """
                Filter the time-series from the time-series list as per the text entered in txt_timeseries
        """
        filter_text = str(self.txt_timeseries.text()).lower()
        self.timeseries_listWidget.clear()
        index = 0
        for item in self.timeseries_list:
            if item.lower().startswith(filter_text.lower()):
                listitem = QtWidgets.QListWidgetItem()
                listitem.setText(item)
                listitem.setData(1, self.timeseriesId_list[index])
                self.timeseries_listWidget.addItem(listitem)
            index += 1
        self.scrollArea_timeseries.setWidget(self.timeseries_listWidget)

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                      PRODUCT PART
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def get_products(self):
        """
                        Get the list of all products in the database
        :return: products_list
        """
        from utils.database_utils import DatabaseConnect
        db = DatabaseConnect()
        self.products_list, self.productId_list = db.get_products(window=self.temp_window)

    def load_products_list(self):
        """
                        add the products into the list widget of the window
        """
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
        """
                Selected a product from the product list. So display product details in Overview
        :param item:
        :return:
        """
        self.selected_product = item.text()
        self.selected_productId = item.data(1)
        if self.selected_timeseries and self.selected_product:
            if self.timeseries_info["product_ID"] == self.selected_productId:
                self.btn_unbind.setEnabled(True)
                self.btn_bind.setDisabled(True)
            elif not self.timeseries_info["product_ID"] or self.timeseries_info["product_ID"] == "":
                self.btn_bind.setEnabled(True)
                self.btn_unbind.setDisabled(True)
            else:
                self.btn_bind.setDisabled(True)
                self.btn_unbind.setDisabled(True)

    def productfilterClicked(self):
        """
                        Filter the product list on the basis on basis searched keyword
        """
        filter_text = str(self.txt_products.text()).lower()
        self.listWidget_product.clear()
        index = 0
        for item in self.products_list:
            if item.lower().startswith(filter_text.lower()):
                listitem = QtWidgets.QListWidgetItem()
                listitem.setText(item)
                listitem.setData(1, self.productId_list[index])
                self.listWidget_product.addItem(listitem)
            index += 1
        self.scrollArea_products.setWidget(self.listWidget_product)
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
