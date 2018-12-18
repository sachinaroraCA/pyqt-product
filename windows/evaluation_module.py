from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QListWidget, QMessageBox, QListWidgetItem
from utils.database_utils import DatabaseConnect


class EvaluationWindow(QMainWindow):
    def __init__(self, parent=None):
        super(EvaluationWindow, self).__init__(parent)
        self.setWindowTitle("Financial Product Analysis Tool - Evaluation")
        self.ui = Ui_MainWindow(self)


class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        self.temp_window = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedHeight(450)
        MainWindow.setFixedWidth(600)
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
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
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

        import pyqtgraph as pg

        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')
        self.win = pg.PlotWidget()

        self.bg = pg.BarGraphItem(x=[], height=[], width=0.5, brush='r')
        self.win.addItem(self.bg)

        # set the layout
        self.graph_layout = QtWidgets.QHBoxLayout()
        self.graph_layout.setGeometry(QtCore.QRect(40, 220, 481, 181))
        self.graph_layout.addWidget(self.win)

        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 220, 481, 181))
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_2.setLayout(self.graph_layout)

        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 500, 17))
        self.label_2.setObjectName("label_2")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 615, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.load_products_list()
        self.selected_product = None

        self.listWidget.itemClicked.connect(self.list_item_event)
        # self.listWidget.itemActivated()
        self.btn_evaluate.clicked.connect(self.btn_evaluate_clicked)
        self.btn_reset.clicked.connect(self.btn_reset_clicked)
        self.btn_return.clicked.connect(self.btn_return_clicked)
        self.txt_search.textChanged.connect(self.search_product)

        self.btn_evaluate.setDisabled(True)
        self.btn_reset.setDisabled(True)

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
        self.label_2.setText(_translate("MainWindow", "\t\tNot evaluated"))

    def btn_evaluate_clicked(self):
        if self.selected_product:

            from windows.evaluation_evaluate import EvaluationEvaluateWindow
            self.evaluation_evaluate_win = EvaluationEvaluateWindow(parent=self.temp_window,
                                                                    selected_product_details=self.selected_product_details)
            self.evaluation_evaluate_win.ui.selected_product = self.selected_product
            self.evaluation_evaluate_win.ui.selected_productId = self.selected_productId
            self.evaluation_evaluate_win.ui.lbl_prduct.setText("  "+self.selected_product + " :")
            self.evaluation_evaluate_win.ui.lbl_prduct.setFixedHeight(20)
            self.evaluation_evaluate_win.show()

    def list_item_event(self, item):
        from utils.algo_utils import get_scores

        self.selected_product = item.text()
        self.selected_productId = item.data(3)
        self.isEvaluated_product = item.data(4)
        self.selected_product_details = [item for item in self.products_dict_list
                                         if 'id' in item and item['id'] == self.selected_productId][0]
        if self.isEvaluated_product:
            self.btn_evaluate.setDisabled(True)
            self.btn_reset.setEnabled(True)
            graph_scores = get_scores(product_id=self.selected_productId)
            x, y = list(graph_scores.keys()), list(graph_scores.values())
            self.create_graph(x=x, y=y)
            self.label_2.setText("")
        else:
            self.btn_evaluate.setEnabled(True)
            self.btn_reset.setDisabled(True)
            self.create_graph(x=[], y=[])
            self.label_2.setText("\t\tNot evaluated")

    def search_product(self):
        filter_text = str(self.txt_search.text()).lower()
        self.listWidget.clear()
        index = 0
        for item in self.products_list:
            if item.lower().startswith(filter_text.lower()):
                listitem = QListWidgetItem()
                listitem.setText(item)
                listitem.setData(3, self.productId_list[index])
                listitem.setData(4, self.isEvaluated_list[index])
                self.listWidget.addItem(listitem)
            index += 1
        self.scrollArea.setWidget(self.listWidget)

    def btn_reset_clicked(self):
        self.reset_record(self.selected_productId)
        self.create_graph(x=[], y=[])
        self.label_2.setText("\t\tNot evaluated")
        self.load_products_list()

    def btn_return_clicked(self):
        self.temp_window.hide()

    def reset_record(self, id):
        buttonReply = QtWidgets.QMessageBox.question(self.temp_window, "Message",
                                                     'Do you really want to reset this evaluatioon ?',
                                                     QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                     QtWidgets.QMessageBox.No)
        if buttonReply == QtWidgets.QMessageBox.Yes:
            from utils.database_utils import DatabaseConnect
            db = DatabaseConnect()
            deleted = db.delete_evaluation(product_id=id)
            if deleted:
                self.temp_window.show()

    def load_products_list(self):
        db = DatabaseConnect()
        self.products_list, self.productId_list, self.isEvaluated_list, self.products_dict_list = db.get_products(evaluate=True)
        self.listWidget = QListWidget()

        self.btn_reset.setDisabled(True)
        self.btn_evaluate.setDisabled(True)

        index =0
        for item in self.productId_list:
            listitem = QListWidgetItem()
            listitem.setText(self.products_list[index])
            listitem.setData(3, item)
            listitem.setData(4, self.isEvaluated_list[index])
            index += 1
            self.listWidget.addItem(listitem)
        self.listWidget.itemActivated.connect(self.list_item_event)
        self.listWidget.itemClicked.connect(self.list_item_event)
        self.scrollArea.setWidget(self.listWidget)

    def create_graph(self, x, y):
        print("x", x, "y", y)
        import pyqtgraph as pg
        # create bar chart
        self.win.removeItem(self.bg)
        self.bg = pg.BarGraphItem(x=x, height=y, width=0.5, brush='r')
        self.win.addItem(self.bg)
        self.graph_layout.addWidget(self.win)
        self.groupBox_2.setLayout(self.graph_layout)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

