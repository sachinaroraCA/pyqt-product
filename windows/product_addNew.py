from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox

CATEGORY_A_CHOICES = ['1', '2']  # Constant list for Category A
CATEGORY_B_CHOICES = ['A', 'B', 'C']  # Constant list for Category B


class AddNewProductWindow(QMainWindow):
    """
                Main class of the Product:Add new module
    """
    def __init__(self, parent=None):
        super(AddNewProductWindow, self).__init__(parent)
        self.setWindowTitle("Financial Product Analysis Tool - Product:Add new")
        self.parent_win = parent
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.ui = Ui_MainWindow(self)


class Ui_MainWindow(object):
    """
                UI class of the Product:Add new module
    """
    def __init__(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedHeight(450)
        MainWindow.setFixedWidth(600)
        self.temp_window = MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(50, 40, 141, 17))
        self.title.setObjectName("title")

        self.lbl_name = QtWidgets.QLabel(self.centralwidget)
        self.lbl_name.setGeometry(QtCore.QRect(50, 80, 81, 17))
        self.lbl_name.setObjectName("name")
        self.txt_name = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_name.setGeometry(QtCore.QRect(150, 80, 113, 25))
        self.txt_name.setObjectName("txt_name")
        self.txt_name.setMaxLength(250)

        self.lbl_code = QtWidgets.QLabel(self.centralwidget)
        self.lbl_code.setGeometry(QtCore.QRect(310, 80, 81, 17))
        self.lbl_code.setObjectName("lbl_code")
        self.txt_code = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_code.setGeometry(QtCore.QRect(410, 80, 113, 25))
        self.txt_code.setObjectName("txt_code")
        self.txt_code.setMaxLength(250)

        self.lbl_category_a = QtWidgets.QLabel(self.centralwidget)
        self.lbl_category_a.setGeometry(QtCore.QRect(50, 110, 81, 17))
        self.lbl_category_a.setObjectName("lbl_category_a")
        self.combo_category_A = QtWidgets.QComboBox(self.centralwidget)
        self.combo_category_A.setGeometry(QtCore.QRect(150, 110, 111, 25))
        self.combo_category_A.setObjectName("combo_category_A")
        self.combo_category_A.addItems(CATEGORY_A_CHOICES)

        self.lbl_category_b = QtWidgets.QLabel(self.centralwidget)
        self.lbl_category_b.setGeometry(QtCore.QRect(310, 110, 81, 17))
        self.lbl_category_b.setObjectName("lbl_category_b")
        self.combo_category_B = QtWidgets.QComboBox(self.centralwidget)
        self.combo_category_B.setGeometry(QtCore.QRect(410, 110, 111, 25))
        self.combo_category_B.setObjectName("combo_category_B")
        self.combo_category_B.addItems(CATEGORY_B_CHOICES)
        
        self.lbl_info_1 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_info_1.setGeometry(QtCore.QRect(50, 140, 81, 17))
        self.lbl_info_1.setObjectName("lbl_info_1")
        self.txt_info1 = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_info1.setGeometry(QtCore.QRect(150, 140, 113, 25))
        self.txt_info1.setObjectName("txt_info1")
        self.txt_info1.setMaxLength(250)

        self.lbl_info_2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_info_2.setGeometry(QtCore.QRect(310, 140, 81, 17))
        self.lbl_info_2.setObjectName("lbl_info_2")
        self.txt_info_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_info_2.setGeometry(QtCore.QRect(410, 140, 113, 25))
        self.txt_info_2.setText("")
        self.txt_info_2.setObjectName("txt_info_2")
        self.txt_info_2.setMaxLength(250)

        self.lbl_info_3 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_info_3.setGeometry(QtCore.QRect(50, 170, 81, 17))
        self.lbl_info_3.setObjectName("lbl_info_3")
        self.txt_info_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_info_3.setGeometry(QtCore.QRect(150, 170, 113, 25))
        self.txt_info_3.setObjectName("txt_info_3")
        self.txt_info_3.setMaxLength(250)

        self.lbl_info_4 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_info_4.setGeometry(QtCore.QRect(310, 170, 81, 17))
        self.lbl_info_4.setObjectName("lbl_info_4")
        self.txt_info_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_info_4.setGeometry(QtCore.QRect(410, 170, 113, 25))
        self.txt_info_4.setObjectName("txt_info_4")
        self.txt_info_4.setMaxLength(250)

        self.lbl_info_5 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_info_5.setGeometry(QtCore.QRect(50, 200, 81, 17))
        self.lbl_info_5.setObjectName("lbl_info_5")
        self.txt_info_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_info_5.setGeometry(QtCore.QRect(150, 200, 113, 25))
        self.txt_info_5.setObjectName("txt_info_5")
        self.txt_info_5.setMaxLength(250)

        self.lbl_info_6 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_info_6.setGeometry(QtCore.QRect(310, 200, 81, 17))
        self.lbl_info_6.setObjectName("lbl_info_6")
        self.txt_info_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_info_6.setGeometry(QtCore.QRect(410, 200, 113, 25))
        self.txt_info_6.setObjectName("txt_info_6")
        self.txt_info_6.setMaxLength(250)

        self.lbl_info_7 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_info_7.setGeometry(QtCore.QRect(50, 230, 81, 17))
        self.lbl_info_7.setObjectName("lbl_info_7")
        self.txt_info_7 = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_info_7.setGeometry(QtCore.QRect(50, 250, 471, 70))
        self.txt_info_7.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.txt_info_7.setObjectName("txt_info_7")

        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(50, 350, 89, 25))
        self.btn_back.setObjectName("btn_back")
        
        self.btn_addAnother = QtWidgets.QPushButton(self.centralwidget)
        self.btn_addAnother.setGeometry(QtCore.QRect(210, 350, 111, 25))
        self.btn_addAnother.setObjectName("btn_addAnother")
        
        self.btn_saveAndReturn = QtWidgets.QPushButton(self.centralwidget)
        self.btn_saveAndReturn.setGeometry(QtCore.QRect(370, 350, 141, 25))
        self.btn_saveAndReturn.setObjectName("btn_saveAndReturn")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 583, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.btn_back.clicked.connect(self.btn_back_clicked)
        self.btn_saveAndReturn.clicked.connect(self.btn_saveAndReturn_clicked)
        self.btn_addAnother.clicked.connect(self.btn_addAnother_clicked)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        """
                Set the properties of the UI elements
        :param MainWindow:
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Financial Product Analysis Tool - Product:Add new"))
        self.title.setText(_translate("MainWindow", "Add a new product:"))
        self.lbl_name.setText(_translate("MainWindow", "Name:"))
        self.lbl_code.setText(_translate("MainWindow", "Code:"))
        self.lbl_category_a.setText(_translate("MainWindow", "Category A:"))
        self.lbl_category_b.setText(_translate("MainWindow", "Category B:"))
        self.lbl_info_1.setText(_translate("MainWindow", "Info 1:"))
        self.lbl_info_2.setText(_translate("MainWindow", "Info 2:"))
        self.lbl_info_3.setText(_translate("MainWindow", "Info 3:"))
        self.lbl_info_4.setText(_translate("MainWindow", "Info 4:"))
        self.lbl_info_5.setText(_translate("MainWindow", "Info 5:"))
        self.lbl_info_6.setText(_translate("MainWindow", "info 6:"))
        self.lbl_info_7.setText(_translate("MainWindow", "Info 7:"))
        self.btn_back.setText(_translate("MainWindow", "Back"))
        self.btn_addAnother.setText(_translate("MainWindow", "Add Another"))
        self.btn_saveAndReturn.setText(_translate("MainWindow", "Save and Return"))

    def btn_back_clicked(self):
        """
                    Close current window and show the Product window
        :return:
        """
        self.temp_window.parent_win.show()
        self.temp_window.hide()

    def btn_saveAndReturn_clicked(self):
        """
                    Save the Product record and close current window
        :return:
        """
        saved = self.save_product()
        if saved:
            self.temp_window.parent_win.parent_win.show()
            self.temp_window.hide()

    def btn_addAnother_clicked(self):
        """
            Creates a product in a database and refreshes the window to add a new product.
        """

        saved = self.save_product()
        if saved:
            self.clear_window()
        else:
            self.new_win = AddNewProductWindow(parent=self.temp_window.parent_win)
            self.temp_window.show()

    def btn_saveAndReturnUpdate_clicked(self):
        """
                    Updates the product record by calling a function update_product
        """
        updated = self.update_product()
        if updated:
            self.temp_window.parent_win.parent_win.show()
            self.temp_window.hide()

    def update_product(self):
        """
                    Updates the product record in the database.
        :return:
        """
        from utils.database_utils import DatabaseConnect
        conn = DatabaseConnect()
        name = self.txt_name.text()
        code = self.txt_code.text()
        categorya = self.combo_category_A.currentText()
        categoryb = self.combo_category_B.currentText()
        info1 = self.txt_info1.text()
        info2 = self.txt_info_2.text()
        info3 = self.txt_info_3.text()
        info4 = self.txt_info_4.text()
        info5 = self.txt_info_5.text()
        info6 = self.txt_info_6.text()
        info7 = self.txt_info_7.toPlainText()
        id = self.product_id
        if name and code:
            updated = conn.update_product_record(id=id, name=name, code=code, categorya=categorya, categoryb=categoryb, info1=info1,
                                       info2=info2, info3=info3, info4=info4, info5=info5, info6=info6, info7=info7)
            if updated:
                self.temp_window.parent_win.ui.get_products()
                self.temp_window.parent_win.ui.load_products_list()
                self.temp_window.parent_win.ui.txt_overview.clear()
                QMessageBox.about(self.temp_window, "info", "Product is updated Successfully !!!")
                return True
            else:
                QMessageBox.about(self.temp_window, "Warning", "Database Error !!!")
                return False
        else:
            QMessageBox.about(self.temp_window, "warning", "name and code field is mendetory !!!")
            return False

    def save_product(self):
        """
                    Creates a product in a database
        :return:
        """
        from utils.database_utils import DatabaseConnect
        conn = DatabaseConnect()

        name = self.txt_name.text()
        code = self.txt_code.text()
        category_a = self.combo_category_A.currentText()
        category_b = self.combo_category_B.currentText()
        info_1 = self.txt_info1.text()
        info_2 = self.txt_info_2.text()
        info_3 = self.txt_info_3.text()
        info_4 = self.txt_info_4.text()
        info_5 = self.txt_info_5.text()
        info_6 = self.txt_info_6.text()
        info_7 = self.txt_info_7.toPlainText()
        if name and code:
            saved = conn.save_product_record(name, code, category_a, category_b, info_1, info_2, info_3, info_4, info_5, info_6, info_7)
            if saved:
                self.temp_window.parent_win.ui.get_products()
                self.temp_window.parent_win.ui.load_products_list()
                QMessageBox.about(self.temp_window, "info", "Product is added Successfully !!!")
                return True
            else:
                QMessageBox.about(self.temp_window, "Warning", "Database Error !!!")
                return False
        else:
            if not name:
                self.txt_name.setFocusPolicy(QtCore.Qt.StrongFocus)
                self.txt_name.setFocus()
            elif not code:
                self.txt_code.setFocus()

    def clear_window(self):
        """
                    clear all the field value values in the current window.
        """
        self.txt_name.setText("")
        self.txt_code.setText("")
        self.combo_category_A.setCurrentText("1")
        self.combo_category_B.setCurrentText("A")
        self.txt_info1.setText("")
        self.txt_info_2.setText("")
        self.txt_info_3.setText("")
        self.txt_info_4.setText("")
        self.txt_info_5.setText("")
        self.txt_info_6.setText("")
        self.txt_info_7.setText("")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
    ui = Ui_MainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
