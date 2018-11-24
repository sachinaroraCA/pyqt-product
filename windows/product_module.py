from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import QListWidget, QCompleter, QMainWindow, QFileDialog


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
        self.txt_search.textChanged.connect(self.filterClicked)

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
        result = [x.row() for x in self.listWidget.selectedIndexes()]
        product_code = self.productcode_list[result[0]]
        product_name = self.products_list[result[0]]
        self.delete_product_byname(product_name)
        self.productcode_list.remove(product_code)
        self.products_list.remove(product_name)
        self.listWidget.clear()
        self.listWidget.addItems(self.products_list)
        # self.listWidget.itemClicked.connect(self.list_item_event)
        self.scrollArea.setWidget(self.listWidget)
        self.txt_overview.clear()

    def btn_modify_clicked(self):
        result = [x.row() for x in self.listWidget.selectedIndexes()]
        if result:
            # product_code = self.productcode_list[result[0]]
            product_detail_dict = self.get_product_details(product_name=self.selected_product)[1]
            print(product_detail_dict)
            from windows.add_product_main import AddNewProductWindow
            self.modify_win = AddNewProductWindow()
            if "Name" in product_detail_dict:
                self.modify_win.ui.txt_name.setText(product_detail_dict["Name"])
            if "Code" in product_detail_dict:
                self.modify_win.ui.txt_code.setText(product_detail_dict["Code"])
            if "Category_A" in product_detail_dict:
                self.modify_win.ui.combo_category_A.setCurrentText(product_detail_dict["Category_A"])
            if "Category_B" in product_detail_dict:
                self.modify_win.ui.combo_category_B.setCurrentText(product_detail_dict["Category_B"])
            if "info_1" in product_detail_dict:
                self.modify_win.ui.txt_info1.setText(product_detail_dict["info_1"])
            if "info_2" in product_detail_dict:
                self.modify_win.ui.txt_info_2.setText(product_detail_dict["info_2"])
            if "info_3" in product_detail_dict:
                self.modify_win.ui.txt_info_3.setText(product_detail_dict["info_3"])
            if "info_4" in product_detail_dict:
                self.modify_win.ui.txt_info_4.setText(product_detail_dict["info_4"])
            if "info_5" in product_detail_dict:
                self.modify_win.ui.txt_info_5.setText(product_detail_dict["info_5"])
            if "info_6" in product_detail_dict:
                self.modify_win.ui.txt_info_6.setText(product_detail_dict["info_6"])
            if "info_7" in product_detail_dict:
                self.modify_win.ui.txt_info_7.setPlainText(product_detail_dict["info_7"])
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
        self.listWidget.addItems(self.products_list)
        self.scrollArea.setWidget(self.listWidget)

    def filterClicked(self):
        filter_text = str(self.txt_search.text()).lower()
        filtered_list = []
        for item in self.products_list:
            if filter_text in item.lower():
                filtered_list.append(item)

        self.listWidget.clear()
        self.listWidget.addItems(filtered_list)
        # self.listWidget.itemClicked.connect(self.list_item_event)
        self.scrollArea.setWidget(self.listWidget)

    def delete_product_byname(self, name):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('sports.db')
        if not db.open():
            print("not created")
            return False

        query = QtSql.QSqlQuery()
        query.exec_("DELETE FROM Product WHERE Name='{name}'".format(name=name))

        if query.isValid():
            db.close()
            return True
        else:
            db.close()
            return False

    def get_products(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('sports.db')
        product_list = []
        productcode_list = []
        if not db.open():
            print("not created")
            return False

        query = QtSql.QSqlQuery()
        query.exec_("select Name,Code from Product")

        while query.next():
            print(query.value(0))
            product_list.append(query.value(0))
            productcode_list.append(query.value(1))
        db.close()
        self.productcode_list = productcode_list
        return product_list

    def get_product_details(self, product_name=None, product_code=None):

        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('sports.db')
        product_string = ""
        product_detail_dict = {}
        self.selected_product = product_name

        if not db.open():
            print("not created")
            return False

        query = QtSql.QSqlQuery()
        if product_name:
            query.exec_("select * from Product where Name = '{name}'".format(name=product_name))
        elif product_code:
            query.exec_("select * from Product where Code = '{code}'".format(code=product_code))

        if query.next():
            size = query.record().count()
            for index in range(0, size):
                # print(query.value(index))
                if query.value(index) != "" and query.value(index):
                    product_string += str(query.record().fieldName(index))+ ':  ' + str(query.value(index)) + "\n"
                    product_detail_dict.update({str(query.record().fieldName(index)): str(query.value(index))})
            print(product_string)
        self.product_detail_dict = product_detail_dict
        db.close()
        return product_string, product_detail_dict

    def list_item_event(self, item):
        print(repr(item.text()))
        item_detail = self.get_product_details(product_name=item.text())
        self.selected_product = item.text()
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

