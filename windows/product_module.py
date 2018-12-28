from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QListWidget, QMainWindow, QFileDialog
from PyQt5.QtWidgets import QListWidgetItem


class ProductWindow(QMainWindow):
    """
                Main class of the Product module
    """
    def __init__(self, parent=None):
        super(ProductWindow, self).__init__(parent)
        self.setWindowTitle("Financial Product Analysis Tool - Product")
        self.parent_win = parent
        self.ui = Ui_MainWindow(self)


class Ui_MainWindow(object):
    """
                    UI class of the Product Window
    """
    def __init__(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedHeight(450)
        MainWindow.setFixedWidth(600)
        self.temp_window = MainWindow
        self.products_list = self.get_products()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 20, 71, 17))
        self.label.setObjectName("label")
        
        self.txt_search = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_search.setPlaceholderText("    Search")
        self.txt_search.setGeometry(QtCore.QRect(50, 60, 329, 25))
        self.txt_search.setObjectName("txt_search")
        # self.txt_search.setStyleSheet("""background: #ffffff;
        #                                 background-image: "/home/cloudanalogy/PycharmProjects/test_pyqt/windows/search.svg"; /* actual size, e.g. 16x16 */
        #                                 background-repeat: no-repeat;
        #                                 background-position: left;
        #                                 color: #252424;
        #                                 font-family: SegoeUI;
        #                                 font-size: 14px;
        #                                 padding: 2 2 2 20; /* left padding (last number) must be more than the icon's width */
        #                                     """)
        
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(380, 40, 131, 155))
        self.groupBox.setObjectName("groupBox")
        
        self.btn_addNew = QtWidgets.QPushButton(self.groupBox)
        self.btn_addNew.setGeometry(QtCore.QRect(20, 30, 89, 25))
        self.btn_addNew.setObjectName("btn_addNew")
        
        self.btn_delete = QtWidgets.QPushButton(self.groupBox)
        self.btn_delete.setGeometry(QtCore.QRect(20, 60, 91, 25))
        self.btn_delete.setObjectName("btn_delete")
        
        self.btn_modify = QtWidgets.QPushButton(self.groupBox)
        self.btn_modify.setGeometry(QtCore.QRect(20, 90, 89, 25))
        self.btn_modify.setObjectName("btn_modify")

        self.btn_export = QtWidgets.QPushButton(self.groupBox)
        self.btn_export.setGeometry(QtCore.QRect(20, 120, 91, 25))
        self.btn_export.setObjectName("btn_export")
        
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(50, 90, 329, 105))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 313, 99))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        
        self.groupBox_overview = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_overview.setGeometry(QtCore.QRect(50, 230, 481, 141))
        self.groupBox_overview.setObjectName("groupBox_overview")
        self.groupBox_overview.setTitle("Overview")
        
        self.txt_overview = QtWidgets.QTextEdit(self.groupBox_overview)
        self.txt_overview.setGeometry(QtCore.QRect(0, 20, 481, 121))
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

        self.load_products_list()
        self.btn_addNew.clicked.connect(self.btn_addNew_clicked)
        self.btn_delete.clicked.connect(self.btn_delete_clicked)
        self.btn_modify.clicked.connect(self.btn_modify_clicked)
        self.btn_export.clicked.connect(self.btn_export_clicked)
        self.btn_delete.setDisabled(True)
        self.btn_modify.setDisabled(True)
        self.btn_export.setDisabled(True)
        self.txt_search.textChanged.connect(self.search_products)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        """
                Set the properties of the UI elements
        :param MainWindow:
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Financial Product Analysis Tool - Product"))
        self.btn_delete.setText(_translate("MainWindow", "Delete"))
        self.btn_addNew.setText(_translate("MainWindow", "Add New"))
        self.btn_export.setText(_translate("MainWindow", "Export"))
        self.btn_modify.setText(_translate("MainWindow", "Modify"))
        self.label.setText(_translate("MainWindow", "Products:"))
        self.groupBox_overview.setTitle(_translate("MainWindow", "Overview"))

    def btn_delete_clicked(self):
        """
                    Call a function delete_product_byId to delete the selected product
        """
        buttonReply = QtWidgets.QMessageBox.question(self.temp_window, "Message",
                                                     'Delete the product "{}" ?'.format(self.selected_product),
                                                     QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                     QtWidgets.QMessageBox.No)
        if buttonReply == QtWidgets.QMessageBox.Yes:
            deleted = self.delete_product_byId(self.selected_productId)
            if deleted:
                self.products_list.remove(self.selected_product)
                self.productId_list.remove(self.selected_productId)
                self.load_products_list()
                self.txt_overview.clear()

    def btn_modify_clicked(self):
        """
                    Open the "Product:Add new" window with pre-filled values of selected product to update
        """
        result = [x.row() for x in self.listWidget.selectedIndexes()]
        if result:
            product_detail_dict = self.product_detail_dict
            from windows.product_addNew import AddNewProductWindow
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
            self.temp_window.hide()

    def btn_export_clicked(self):
        """
                    Export the product field values into a csv file
        """
        try:
            file_dailog = QFileDialog()
            default_file_extension = '.csv'

            name = file_dailog.getSaveFileName(self.temp_window, 'Save File')[0]
            if name:
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
                QtWidgets.QMessageBox.about(self.temp_window, "info", "Exported data successfully !!!")
        except Exception as ex:
            QtWidgets.QMessageBox.about(self.temp_window, "Error", str(ex))

    def search_products(self):
        """
                        Filter the product list on the basis on basis searched keyword
        """
        filter_text = str(self.txt_search.text()).lower()
        self.listWidget.clear()
        index = 0
        for item in self.products_list:
            if item.lower().startswith(filter_text.lower()):
                listitem = QListWidgetItem()
                listitem.setText(item)
                listitem.setData(1, self.productId_list[index])
                self.listWidget.addItem(listitem)
            index += 1
        self.scrollArea.setWidget(self.listWidget)

    def delete_product_byId(self, id):
        """
                        Delete the products from the database on the basis of id
        :param id:
        :return: status i.e, Product deleted or not
        """
        from utils.database_utils import DatabaseConnect
        db = DatabaseConnect()
        status = db.delete_product(id)
        if not status:
            QtWidgets.QMessageBox.about(self.temp_window, "Warning", "Database Error !!!")
        return status

    def get_products(self):
        """
                        Get the list of all products in the database
        :return: products_list
        """
        from utils.database_utils import DatabaseConnect
        db = DatabaseConnect()
        self.products_list, self.productId_list = db.get_products(window=self.temp_window)
        return self.products_list

    def get_product_details(self, id):
        """
                        Get the details of the Product from the database on the basis of provided id
        :param id:
        :return: string, dictionary
        """
        from utils.database_utils import DatabaseConnect
        db = DatabaseConnect()
        product_string, self.product_detail_dict = db.get_product_details(id, window=self.temp_window)
        return product_string, self.product_detail_dict

    def load_products_list(self):
        """
                        add the products into the list widget of the window
        """
        self.listWidget = QListWidget()
        index =0
        for item in self.productId_list:
            listitem = QListWidgetItem()
            listitem.setText(self.products_list[index])
            listitem.setData(1, item)
            index += 1
            self.listWidget.addItem(listitem)
        self.listWidget.itemActivated.connect(self.list_item_event)
        self.listWidget.itemClicked.connect(self.list_item_event)
        self.scrollArea.setWidget(self.listWidget)

    def list_item_event(self, item):
        """
                Selected a product from the product list. So display product details in Overview
        :param item:
        """
        self.selected_product = item.text()
        self.selected_productId = item.data(1)
        self.btn_delete.setEnabled(True)
        self.btn_modify.setEnabled(True)
        self.btn_export.setEnabled(True)
        item_detail = self.get_product_details(id=self.selected_productId)
        self.txt_overview.setPlainText(item_detail[0])

    def btn_addNew_clicked(self):
        """
                        Open the "Product:Add new" window
        """
        from windows.product_addNew import AddNewProductWindow
        self.add_new_win = AddNewProductWindow(parent=self.temp_window)
        self.add_new_win.show()
        self.temp_window.hide()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

