from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QListWidget, QMessageBox, QListWidgetItem
from windows.database_util import DatabaseConnect


class EvaluationWindow(QMainWindow):
    def __init__(self, parent=None):
        super(EvaluationWindow, self).__init__(parent)
        self.setWindowTitle("Financial Product Analysis Tool - Evaluation")
        self.ui = Ui_MainWindow(self)


class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        self.temp_window = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(615, 445)
        MainWindow.setMouseTracking(False)
        MainWindow.setTabletTracking(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.txt_search = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_search.setPlaceholderText("  Search")
        self.txt_search.setGeometry(QtCore.QRect(50, 60, 329, 25))
        self.txt_search.setObjectName("txt_search")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(380, 40, 131, 151))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.btn_reset = QtWidgets.QPushButton(self.groupBox)
        self.btn_reset.setGeometry(QtCore.QRect(20, 80, 91, 25))
        self.btn_reset.setObjectName("btn_reset")
        self.btn_evaluate = QtWidgets.QPushButton(self.groupBox)
        self.btn_evaluate.setGeometry(QtCore.QRect(20, 40, 89, 25))
        self.btn_evaluate.setObjectName("btn_evaluate")
        self.btn_return = QtWidgets.QPushButton(self.groupBox)
        self.btn_return.setGeometry(QtCore.QRect(20, 120, 91, 25))
        self.btn_return.setObjectName("btn_return")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(50, 90, 329, 101))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 313, 99))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 20, 71, 17))
        self.label.setObjectName("label")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 220, 481, 181))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 181, 17))
        self.label_2.setObjectName("label_2")
        self.graphicsView = QtWidgets.QGraphicsView(self.groupBox_2)
        self.graphicsView.setGeometry(QtCore.QRect(30, 80, 411, 71))
        self.graphicsView.setObjectName("graphicsView")
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

        self.btn_evaluate.clicked.connect(self.btn_evaluate_clicked)
        self.btn_reset.clicked.connect(self.btn_reset_clicked)
        self.btn_return.clicked.connect(self.btn_return_clicked)
        self.txt_search.textChanged.connect(self.filterClicked)
        self.selected_product = None

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Financial Product Analysis Tool - Evaluation"))
        self.txt_search.setPlaceholderText(_translate("MainWindow", "  Search"))
        self.btn_reset.setText(_translate("MainWindow", "Reset"))
        self.btn_evaluate.setText(_translate("MainWindow", "Evaluate"))
        self.btn_return.setText(_translate("MainWindow", "Return"))
        self.label.setText(_translate("MainWindow", "Products:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Overview"))
        self.label_2.setText(_translate("MainWindow", "Not evaluated/Diagram:"))

    def btn_evaluate_clicked(self):
        if self.selected_product:
            from windows.evaluation_evaluate import EvaluationEvaluateWindow
            self.evaluation_evaluate_win = EvaluationEvaluateWindow(parent=self.temp_window)
            self.evaluation_evaluate_win.ui.selected_product = self.selected_product
            self.evaluation_evaluate_win.ui.selected_productId = self.selected_productId
            self.evaluation_evaluate_win.ui.lbl_prduct.setText("  "+self.selected_product + " :")
            self.evaluation_evaluate_win.ui.lbl_prduct.setFixedHeight(20)
            self.evaluation_evaluate_win.show()

    def list_item_event(self, item):
        self.selected_product = item.text()
        self.selected_productId = item.data(1)

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

    def btn_reset_clicked(self):
        self.reset_record(self.selected_productId)

    def btn_return_clicked(self):
        self.temp_window.hide()

    def reset_record(self, id):
        from windows.database_util import DatabaseConnect
        db = DatabaseConnect()
        db.delete_evaluation(product_id=id)

    def products_list_view(self):
        db = DatabaseConnect()
        self.products_list, self.productId_list = db.get_products()
        self.listWidget = QListWidget()
        index =0
        for item in self.productId_list:
            listitem = QListWidgetItem()
            listitem.setData(1, item)
            listitem.setText(self.products_list[index])
            index += 1
            self.listWidget.addItem(listitem)
        self.scrollArea.setWidget(self.listWidget)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

