from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QLineEdit


class Ui_LoginWindow(object):
    """

    """
    def __init__(self, MainWindow):
        """
                        UI class of the Login window
        """
        MainWindow.setObjectName("MainWindow")
        # MainWindow.resize(614, 417)
        MainWindow.setFixedHeight(450)
        MainWindow.setFixedWidth(600)
        # self.screen_resolution = screen_resolution
        self.temp_window = MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.lbl_username = QtWidgets.QLabel(self.centralwidget)
        self.lbl_username.setGeometry(QtCore.QRect(130, 90, 81, 17))
        self.lbl_username.setObjectName("lbl_username")
        self.combo_username = QtWidgets.QComboBox(self.centralwidget)
        self.combo_username.setGeometry(QtCore.QRect(320, 90, 121, 25))
        self.combo_username.setObjectName("combo_username")
        self.combo_username.addItems(self.get_users())

        self.lbl_secret_code = QtWidgets.QLabel(self.centralwidget)
        self.lbl_secret_code.setGeometry(QtCore.QRect(130, 140, 91, 17))
        self.lbl_secret_code.setObjectName("lbl_secret_code")
        self.txt_secret_code = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_secret_code.setGeometry(QtCore.QRect(320, 140, 121, 25))
        self.txt_secret_code.setObjectName("txt_secret_code")
        self.txt_secret_code.setEchoMode(QLineEdit.Password)

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

        self.btn_login.clicked.connect(self.loginButtonClicked)
        self.btn_exit.clicked.connect(self.temp_window.close)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        """
                Set the properties of the UI elements
        :param MainWindow:
        :return:
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Financial Product Analysis Tool -Login"))
        self.lbl_username.setText(_translate("MainWindow", "Username:"))
        self.lbl_secret_code.setText(_translate("MainWindow", "Secret code:"))
        self.btn_exit.setText(_translate("MainWindow", "Exit"))
        self.btn_login.setText(_translate("MainWindow", "Login"))

    def loginButtonClicked(self):
        """
            Call a function auth_user to authenticate the user and redirect to the “modules” window if the user is authenticated.
        :return:
        """
        authenticated = self.auth_user(str(self.combo_username.currentText()).strip(), str(self.txt_secret_code.text()))
        if authenticated:
            from windows.modules import ProductModulesWindow
            self.modules_window = ProductModulesWindow(parent=self.temp_window)
            self.modules_window.show()
            self.temp_window.hide()
        else:
            QtWidgets.QMessageBox.about(self.temp_window, "Warning", "Invalid Secret code !!!")

    def auth_user(self, un, password):
        """
            Matches the username and password in the database and returns the response as the user is authorised or not
        :param un:
        :param password:
        :return:
        """
        from utils.database_utils import DatabaseConnect
        db = DatabaseConnect()
        return db.auth_user(un, password)

    def get_users(self):
        """
            This function returns the list of all users in the database
        :return:
        """
        from utils.database_utils import DatabaseConnect
        db = DatabaseConnect()
        user_list = db.get_users()
        if type(user_list) == bool:
            QtWidgets.QMessageBox.about(self.temp_window, "Warning", "Database Error !!!")
            return []
        return user_list
