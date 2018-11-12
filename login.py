from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
                             QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
                             QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
                             QVBoxLayout, QMessageBox, QFileDialog, QTableView, QFrame, QMainWindow)
from PyQt5 import QtSql
import pandas as pd
import sys

db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
db.setDatabaseName('sports.db')

class Dialog(QDialog):
    NumGridRows = 3
    NumButtons = 4

    def __init__(self):
        super(Dialog, self).__init__()
        self.createFormGroupBox()
        self.loginForm()
        mainLayout = QVBoxLayout()
        # modulesLayout = QVBoxLayout()
        self.ProductFGBox.hide()
        self.TimeSeriesFGBox.hide()
        self.PredictionsFGBox.hide()
        mainLayout.addWidget(self.ProductFGBox)
        mainLayout.addWidget(self.TimeSeriesFGBox)
        mainLayout.addWidget(self.PredictionsFGBox)
        mainLayout.addWidget(self.formGroupBox2)
        # self.modulesLayout = modulesLayout
        self.btn_Submit.clicked.connect(self.submitButtonClicked)
        self.setLayout(mainLayout)
        self.setGeometry(200, 50, 500, 300)
        self.setWindowTitle("Financial Producut Analysis Tool - Login")

    def loginForm(self):
        self.formGroupBox2 = QGroupBox("")
        self.username = QLineEdit(self)
        self.QUserLabel = QLabel("USERNAME")


        self.password = QLineEdit(self)
        self.password.setEchoMode(QLineEdit.Password)
        self.QPasswordLabel = QLabel("PASSWORD")

        self.btn_Submit = QPushButton("LOGIN")
        self.btn_cancel = QPushButton("Exit")
        self.btn_Submit.resize(200, 64)
        self.btn_Submit.move(50, 50)

        layout = QFormLayout()
        layout.addRow(self.QUserLabel, self.username)
        layout.addRow(self.QPasswordLabel, self.password)
        layout.addRow(self.btn_cancel, self.btn_Submit)
        self.formGroupBox2.setLayout(layout)

    def createFormGroupBox(self):
        self.ProductFGBox = QGroupBox("Products")
        self.btn_products = QPushButton("Products")
        self.btn_evaluation = QPushButton("Evaluation")
        layout = QFormLayout()
        layout.addRow(self.btn_products, self.btn_evaluation)
        self.ProductFGBox.setLayout(layout)

        self.TimeSeriesFGBox = QGroupBox("Time Series")
        self.btn_time_series = QPushButton("Time Series")
        self.btn_ananlysis = QPushButton("Analysis")
        layout = QFormLayout()
        layout.addRow(self.btn_time_series, self.btn_ananlysis)
        self.TimeSeriesFGBox.setLayout(layout)

        self.PredictionsFGBox = QGroupBox("Predictions")
        self.btn_Models = QPushButton("Models")
        self.btn_Predictions = QPushButton("Predictions")
        layout = QFormLayout()
        layout.addRow(self.btn_Models, self.btn_Predictions)
        self.PredictionsFGBox.setLayout(layout)


    def submitButtonClicked(self):
        print(str(self.username.text())  + "    ///   " + str(self.password.text()))

        authenticate = self.auth_user(str(self.username.text()), str(self.password.text()))
        if authenticate:
            # window = QMainWindow()
            # widget = QWidget()
            # widget.setLayout(self.modulesLayout)
            # widget.show()
            # window.setLayout(self.modulesLayout)

            self.setWindowTitle("Financial Producut Analysis Tool - Modules")
            self.formGroupBox2.hide()
            self.ProductFGBox.show()
            self.TimeSeriesFGBox.show()
            self.PredictionsFGBox.show()
        else:
            QMessageBox.about(self, "Warning", "Invalid Username or Password !!!")


    # def cancelButtonClicked(self):


    def openFileNameDialog(self):
        f_dialog = QFileDialog()
        options = f_dialog.Options()
        options |= f_dialog.DontUseNativeDialog
        fileName, _ = f_dialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "*.csv;;All Files (*)", options=options)
        # file_path = f_dialog.Detail
        print("file_path : "+str(fileName))
        if ".csv" in fileName:
            return fileName
        else:
            buttonReply = QMessageBox.question(self, 'Warning', "Do you really want to upload other then CSV file",
                                               QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes:
                return False
            else:
                return False


    def uploadCSV(self):
        result = self.openFileNameDialog()
        if result:
            file = pd.read_csv(result)
            json_data = file.to_json()
            print(json_data)

    def auth_user(self, un, password):

        if not db.open():
            print("not created")
            return False

        query = QtSql.QSqlQuery()
        query.exec_("select username from user where username = '{username}' and password = '{password}'".format(
            username=un,
            password=password))
        if query.next():
            print("logged in")
            return True
        else:
            return False
        #     print(query.value(0))
        # result = query.value(0)
        # print(result)


# class dbConnect:
#     def __init__(self, db):
#         self.conn = sqlite3.connect(database=db)
#
#
#     def close_conn(self, conn):
#         conn.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Dialog()
sys.exit(dialog.exec_())


# def createDB():
#     db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
#     db.setDatabaseName('sports.db')
#
#     if not db.open():
#         print("not created")
#         return False
#
#     query = QtSql.QSqlQuery()
#
#     query.exec_("create table sportsmen(id int primary key, "
#                 "firstname varchar(20), lastname varchar(20))")
#
#     query.exec_("insert into sportsmen values(101, 'Roger', 'Federer')")
#     query.exec_("insert into sportsmen values(102, 'Christiano', 'Ronaldo')")
#     # query.exec_("insert into sportsmen values(103, 'Ussain', 'Bolt')")
#     # query.exec_("insert into sportsmen values(104, 'Sachin', 'Tendulkar')")
#     # query.exec_("insert into sportsmen values(105, 'Saina', 'Nehwal')")
#     return True



# auth_user('Aman', '7800')

# def executeQuery():
#     db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
#     db.setDatabaseName('sports.db')
#     if not db.open():
#         print("not created")
#         return False
#
#     query = QtSql.QSqlQuery()
#
#     query.exec_("create table sportsmen(id int primary key, "
#                 "firstname varchar(20), lastname varchar(20))")
#
#     query.exec_("insert into sportsmen values(101, 'Roger', 'Federer')")
#     query.exec_("insert into sportsmen values(102, 'Christiano', 'Ronaldo')")
#     # query.exec_("insert into sportsmen values(103, 'Ussain', 'Bolt')")
#     # query.exec_("insert into sportsmen values(104, 'Sachin', 'Tendulkar')")
#     # query.exec_("insert into sportsmen values(105, 'Saina', 'Nehwal')")
#     return True

# executeQuery()


# def initializeUserModel(model):
#     model.setTable('user')
#     model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
#     model.select()
#     # model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
#     # model.setHeaderData(1, QtCore.Qt.Horizontal, "First name")
#     # model.setHeaderData(2, Horizontal, "Last name")
#
#
#
# def initializeModel(model):
#     model.setTable('sportsmen')
#     model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
#     model.select()
#     # model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
#     # model.setHeaderData(1, QtCore.Qt.Horizontal, "First name")
#     # model.setHeaderData(2, Horizontal, "Last name")
#
#
# def createView(title, model):
#     view = QTableView()
#     view.setModel(model)
#     view.setWindowTitle(title)
#     return view
#
#
# def addrow():
#     print
#     model.rowCount()
#     ret = model.insertRows(model.rowCount(), 1)
#     print
#     ret
#
#
# def findrow(i):
#     delrow = i.row()


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
#     db.setDatabaseName('sports.db')
#     model = QtSql.QSqlTableModel()
#     delrow = -1
#     initializeModel(model)
#
#     view1 = createView("Table Model (View 1)", model)
#     view1.clicked.connect(findrow)
#
#     dlg = QDialog()
#     layout = QVBoxLayout()
#     layout.addWidget(view1)
#
#     button = QPushButton("Add a row")
#     button.clicked.connect(addrow)
#     layout.addWidget(button)
#
#     btn1 = QPushButton("del a row")
#     btn1.clicked.connect(lambda: model.removeRow(view1.currentIndex().row()))
#     layout.addWidget(btn1)
#
#     dlg.setLayout(layout)
#     dlg.setWindowTitle("Database Demo")
#     dlg.show()
#     sys.exit(app.exec_())

