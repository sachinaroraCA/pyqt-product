from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.QtWidgets import QMessageBox, QLineEdit


class Ui_LoginWindow(object):
    def __init__(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(614, 417)
        self.temp_window = MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_username = QtWidgets.QLabel(self.centralwidget)
        self.lbl_username.setGeometry(QtCore.QRect(130, 90, 81, 17))
        self.lbl_username.setObjectName("lbl_username")
        self.lbl_secret_code = QtWidgets.QLabel(self.centralwidget)
        self.lbl_secret_code.setGeometry(QtCore.QRect(130, 140, 91, 17))
        self.lbl_secret_code.setObjectName("lbl_secret_code")
        self.txt_secret_code = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_secret_code.setGeometry(QtCore.QRect(320, 140, 121, 25))
        self.txt_secret_code.setObjectName("txt_secret_code")
        self.txt_secret_code.setEchoMode(QLineEdit.Password)
        self.combo_username = QtWidgets.QComboBox(self.centralwidget)
        self.combo_username.setGeometry(QtCore.QRect(320, 90, 121, 25))
        self.combo_username.setObjectName("combo_username")
        self.combo_username.addItems(self.get_users())
        self.btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_exit.setGeometry(QtCore.QRect(130, 240, 91, 25))
        self.btn_exit.setObjectName("btn_exit")
        self.btn_login = QtWidgets.QPushButton(self.centralwidget)
        self.btn_login.setGeometry(QtCore.QRect(310, 240, 101, 25))
        self.btn_login.setObjectName("btn_login")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 614, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        from windows.modules import ProductModulesWindow
        self.modules_window = ProductModulesWindow()
        self.btn_login.clicked.connect(self.loginButtonClicked)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Financial Product Analysis Tool -Login"))
        self.lbl_username.setText(_translate("MainWindow", "Username:"))
        self.lbl_secret_code.setText(_translate("MainWindow", "Secret code:"))
        self.btn_exit.setText(_translate("MainWindow", "Exit"))
        self.btn_login.setText(_translate("MainWindow", "Login"))

    def loginButtonClicked(self):
        print(str(self.combo_username.currentText()) + "    ///   " + str(self.txt_secret_code.text()))

        authenticate = self.auth_user(str(self.combo_username.currentText()).strip(), str(self.txt_secret_code.text()))
        if authenticate:
            print("authenticated")
            self.modules_window.show()
            self.temp_window.hide()

        else:
            QMessageBox.about(QMessageBox(), "Warning", "Invalid Username or Password !!!")
            print("Invalid username")

    def auth_user(self, un, password):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('sports.db')
        if not db.open():
            print("not created")
            return False

        query = QtSql.QSqlQuery()
        query.exec_("select username from user where username = '{username}' and password = '{password}'".format(
            username=un,
            password=password))

        if query.next():
            print("logged in")
            db.close()
            # QMessageBox.about(QMessageBox(), "Greetings", "Successfully logged in")
            return True
        else:
            QMessageBox.about(QMessageBox(), "Warning", "Invalid Username or Password !!!")
            db.close()
            return False

    def get_users(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('sports.db')
        user_list = []

        if not db.open():
            print("not created")
            return False

        query = QtSql.QSqlQuery()
        query.exec_("select username from user")
        print(query.result())
        while query.next():
            print(query.value(0))
            user_list.append(query.value(0))
        db.close()
        return user_list



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

