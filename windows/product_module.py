from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import QListWidget, QCompleter, QMainWindow, QFileDialog
from PyQt5.QtWidgets import QListWidgetItem


class ProductWindow(QMainWindow):
    def __init__(self, parent=None):
        super(ProductWindow, self).__init__(parent)
        self.setWindowTitle("Financial Product Analysis Tool - Product")
        self.ui = Ui_MainWindow(self)


class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(615, 439)
        self.temp_window = MainWindow
        self.products_list = self.get_products()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txt_search = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_search.setPlaceholderText("  Search")
        self.txt_search.setGeometry(QtCore.QRect(50, 60, 329, 25))
        self.txt_search.setObjectName("txt_search")
        # self.txt_search.setCompleter(self.completer)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(380, 40, 131, 151))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.btn_delete = QtWidgets.QPushButton(self.groupBox)
        self.btn_delete.setGeometry(QtCore.QRect(20, 60, 91, 25))
        self.btn_delete.setObjectName("btn_delete")
        self.btn_addNew = QtWidgets.QPushButton(self.groupBox)
        self.btn_addNew.setGeometry(QtCore.QRect(20, 30, 89, 25))
        self.btn_addNew.setObjectName("btn_addNew")
        self.btn_export = QtWidgets.QPushButton(self.groupBox)
        self.btn_export.setGeometry(QtCore.QRect(20, 120, 91, 25))
        self.btn_export.setObjectName("btn_export")
        self.btn_modify = QtWidgets.QPushButton(self.groupBox)
        self.btn_modify.setGeometry(QtCore.QRect(20, 90, 89, 25))
        self.btn_modify.setObjectName("btn_modify")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(50, 90, 329, 101))
        # self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 313, 99))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 20, 71, 17))
        self.label.setObjectName("label")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(50, 230, 481, 141))
        self.groupBox_2.setObjectName("groupBox_2")
        self.txt_overview = QtWidgets.QTextEdit(self.groupBox_2)
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

        self.products_list_view()
        self.listWidget.itemClicked.connect(self.list_item_event)
        self.btn_addNew.clicked.connect(self.open_addNew)
        self.btn_delete.clicked.connect(self.btn_delete_clicked)
        self.btn_modify.clicked.connect(self.btn_modify_clicked)
        self.btn_export.clicked.connect(self.btn_export_clicked)
        self.txt_search.textChanged.connect(self.search_products)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Financial Product Analysis Tool - Product"))
        self.btn_delete.setText(_translate("MainWindow", "Delete"))
        self.btn_addNew.setText(_translate("MainWindow", "Add New"))
        self.btn_export.setText(_translate("MainWindow", "Export"))
        self.btn_modify.setText(_translate("MainWindow", "Modify"))
        self.label.setText(_translate("MainWindow", "Products:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Overview"))

    def btn_delete_clicked(self):
        self.delete_product_byId(self.selected_productId)
        # self.productId_list.remove(product_code)
        self.products_list.remove(self.selected_product)
        self.listWidget.clear()
        self.listWidget.addItems(self.products_list)
        # self.listWidget.itemClicked.connect(self.list_item_event)
        self.scrollArea.setWidget(self.listWidget)
        self.txt_overview.clear()

    def btn_modify_clicked(self):
        result = [x.row() for x in self.listWidget.selectedIndexes()]
        if result:
            product_detail_dict = self.product_detail_dict
            from windows.add_product_main import AddNewProductWindow
            self.modify_win = AddNewProductWindow(parent=self.temp_window)
            self.modify_win.ui.product_id = self.product_detail_dict["id"]
            if "name" in product_detail_dict:
                self.modify_win.ui.txt_name.setText(product_detail_dict["name"])
            if "code" in product_detail_dict:
                self.modify_win.ui.txt_code.setText(product_detail_dict["code"])
            if "categorya" in product_detail_dict:
                self.modify_win.ui.combo_category_A.setCurrentText(product_detail_dict["categorya"])
            if "categoryb" in product_detail_dict:
                self.modify_win.ui.combo_category_B.setCurrentText(product_detail_dict["categoryb"])
            if "info1" in product_detail_dict:
                self.modify_win.ui.txt_info1.setText(product_detail_dict["info1"])
            if "info2" in product_detail_dict:
                self.modify_win.ui.txt_info_2.setText(product_detail_dict["info2"])
            if "info3" in product_detail_dict:
                self.modify_win.ui.txt_info_3.setText(product_detail_dict["info3"])
            if "info4" in product_detail_dict:
                self.modify_win.ui.txt_info_4.setText(product_detail_dict["info4"])
            if "info5" in product_detail_dict:
                self.modify_win.ui.txt_info_5.setText(product_detail_dict["info5"])
            if "info6" in product_detail_dict:
                self.modify_win.ui.txt_info_6.setText(product_detail_dict["info6"])
            if "info7" in product_detail_dict:
                self.modify_win.ui.txt_info_7.setPlainText(product_detail_dict["info7"])
            self.modify_win.setWindowTitle("Financial Financial Product Analysis Tool - Product:Update")
            self.modify_win.ui.btn_addAnother.hide()
            self.modify_win.ui.btn_saveAndReturn.clicked.disconnect(self.modify_win.ui.btn_saveAndReturn_clicked)
            self.modify_win.ui.btn_saveAndReturn.clicked.connect(self.modify_win.ui.btn_saveAndReturnUpdate_clicked)

            self.modify_win.show()

    def btn_export_clicked(self):
        file_dailog = QFileDialog()
        default_file_extension = '.csv'

        name = file_dailog.getSaveFileName(self.temp_window, 'Save File')[0]
        if default_file_extension not in name:
            name += default_file_extension

        product_info = self.product_detail_dict
        print(product_info)
        keys = list(product_info.keys())
        import csv
        with open(name, 'w+') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerow(product_info)

        output_file.close()

    def products_list_view(self):
        self.listWidget = QListWidget()
        index =0
        for item in self.productId_list:
            listitem = QListWidgetItem()
            listitem.setText(self.products_list[index])
            listitem.setData(1, item)
            index += 1
            self.listWidget.addItem(listitem)
        self.scrollArea.setWidget(self.listWidget)

    def search_products(self):
        filter_text = self.txt_search.text().lower()
        # filtered_list = []
        # for item in self.products_list:
        #     if filter_text in item.lower():
        #         filtered_list.append(item)

        self.filtered_list = self.listWidget.findItems(filter_text, QtCore.Qt.MatchStartsWith)
        new_list_widget = QListWidget(self.scrollArea)

        index = 0
        for item in self.filtered_list:
            self.listWidget.removeItemWidget(item)
            # listitem = QListWidgetItem()
            # listitem.setText(item.text())
            # listitem.setData(1, item.data(1))
            # index += 1
            # new_list_widget.addItem(listitem)
        # # listWidget.itemClicked.connect(self.list_item_event)
        self.scrollArea.setWidget(self.listWidget)

    def delete_product_byId(self, id):
        from windows.database_util import DatabaseConnect
        db = DatabaseConnect()
        result = db.delete_product(id)
        return result

    def get_products(self):
        from windows.database_util import DatabaseConnect
        db = DatabaseConnect()
        self.products_list, self.productId_list = db.get_products()
        return self.products_list

    def get_product_details(self, id):
        from windows.database_util import DatabaseConnect
        db = DatabaseConnect()
        product_string, self.product_detail_dict = db.get_product_details(id)
        return product_string, self.product_detail_dict

    def list_item_event(self, item):
        print(repr(item.text()))
        self.selected_product = item.text()
        self.selected_productId = item.data(1)
        print(self.selected_productId)
        item_detail = self.get_product_details(id=self.selected_productId)
        self.txt_overview.setPlainText(item_detail[0])
        # self.txt_search.setText("")

    # def itemActivated_event(self, item):
    #     print(item)
    #     item_detail = self.get_product_details(item)
    #     self.txt_overview.setPlainText(item_detail[0])

    def open_addNew(self):
        from windows.add_product_main import AddNewProductWindow
        self.add_new = AddNewProductWindow()
        self.add_new.show()


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow(MainWindow)
#     # ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

