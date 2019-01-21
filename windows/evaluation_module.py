from PyQt5 import QtCore, QtWidgets, Qt
from PyQt5.QtWidgets import QMainWindow, QListWidget, QMessageBox, QListWidgetItem
from utils.database_utils import DatabaseConnect
from utils.graph_utils import BAR_COLORS, create_graph_indicator


class EvaluationWindow(QMainWindow):
    """
                Main class of the Evaluation module
    """
    def __init__(self, parent=None):
        super(EvaluationWindow, self).__init__(parent)
        self.setWindowTitle("Financial Product Analysis Tool - Evaluation")
        self.ui = Ui_MainWindow(self)
        self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, True)
        self.setWindowState(QtCore.Qt.WindowMaximized)


class Ui_MainWindow(object):
    """
            UI class of the Evaluation module
    """
    def __init__(self, MainWindow):
        self.temp_window = MainWindow
        MainWindow.setObjectName("MainWindow")

        from utils.window_utils import get_resolution_ratio
        self.width_ratio, self.height_ratio = get_resolution_ratio(600, 450)
        MainWindow.setMinimumHeight(self.height_ratio*450)
        MainWindow.setMinimumWidth(self.width_ratio*600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(self.width_ratio*50, self.height_ratio*20, self.width_ratio*71, self.height_ratio*17))
        self.label.setObjectName("label")

        self.txt_search = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_search.setPlaceholderText("  Search")
        self.txt_search.setGeometry(QtCore.QRect(self.width_ratio*50, self.height_ratio*60, self.width_ratio*329, self.height_ratio*25))
        self.txt_search.setObjectName("txt_search")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(self.width_ratio*380, self.height_ratio*45, self.width_ratio*131, self.height_ratio*150))
        self.groupBox.setObjectName("groupBox")

        self.btn_reset = QtWidgets.QPushButton(self.groupBox)
        self.btn_reset.setGeometry(QtCore.QRect(self.width_ratio*20, self.height_ratio*80, self.width_ratio*91, self.height_ratio*25))
        self.btn_reset.setObjectName("btn_reset")

        self.btn_evaluate = QtWidgets.QPushButton(self.groupBox)
        self.btn_evaluate.setGeometry(QtCore.QRect(self.width_ratio*20, self.height_ratio*40, self.width_ratio*89, self.height_ratio*25))
        self.btn_evaluate.setObjectName("btn_evaluate")

        self.btn_return = QtWidgets.QPushButton(self.groupBox)
        self.btn_return.setGeometry(QtCore.QRect(self.width_ratio*20, self.height_ratio*120, self.width_ratio*91, self.height_ratio*25))
        self.btn_return.setObjectName("btn_return")

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(self.width_ratio*50, self.height_ratio*90, self.width_ratio*329, self.height_ratio*105))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, self.width_ratio*309, self.height_ratio*105))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)

        import pyqtgraph as pg

        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')
        self.win = pg.PlotWidget()
        self.win.setXRange(0.5, 9.5)
        self.win.setYRange(0, 100)

        self.bg = pg.BarGraphItem(x=[], height=[], width=0.5, brushes=BAR_COLORS)
        self.win.addItem(self.bg)

        # set the layout
        self.graph_layout = QtWidgets.QVBoxLayout()
        self.graph_layout.setGeometry(QtCore.QRect(self.width_ratio*40, self.height_ratio*220, self.width_ratio*481, self.height_ratio*250))

        self.lbl_evaluation_status = QtWidgets.QLabel()
        self.lbl_evaluation_status.setGeometry(QtCore.QRect(self.width_ratio*10, self.height_ratio*30, self.width_ratio*500, self.height_ratio*17))
        self.lbl_evaluation_status.setObjectName("lbl_evaluation_status")

        self.graph_layout.addWidget(self.lbl_evaluation_status)

        self.groupBox_overview = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_overview.setGeometry(QtCore.QRect(self.width_ratio*40, self.height_ratio*220, self.width_ratio*481, self.height_ratio*180))
        self.groupBox_overview.setObjectName("groupBox_overview")
        self.groupBox_overview.setLayout(self.graph_layout)

        self.lbl_evaluation_none = QtWidgets.QLabel()
        self.lbl_evaluation_none.setGeometry(QtCore.QRect(0, 0, self.width_ratio * 500, self.height_ratio * 17))
        self.lbl_evaluation_none.setObjectName("lbl_evaluation_none")
        self.lbl_evaluation_none.setText("Not Evaluated")
        self.lbl_evaluation_none.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_evaluation_none.setStyleSheet("color:red;background-color:white;")

        self.none_layout = QtWidgets.QVBoxLayout()
        self.none_layout.setGeometry(QtCore.QRect(self.width_ratio*40, self.height_ratio*220, self.width_ratio*481, self.height_ratio*250))
        self.none_layout.addWidget(self.lbl_evaluation_none)

        self.graph_layout2 = QtWidgets.QVBoxLayout()
        self.graph_layout2.setGeometry(QtCore.QRect(self.width_ratio*40, self.height_ratio*378, self.width_ratio*481, self.height_ratio*55))

        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(self.width_ratio*40, self.height_ratio*378, self.width_ratio*481, self.height_ratio*55))
        self.groupBox_3.setLayout(self.graph_layout2)

        create_graph_indicator(self.graph_layout2)
        self.graph_layout.addLayout(self.graph_layout2)
        self.groupBox_3.hide()

        self.groupBox_overview_none = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_overview_none.setGeometry(QtCore.QRect(self.width_ratio*40, self.height_ratio*220, self.width_ratio*481, self.height_ratio*180))
        self.groupBox_overview_none.setObjectName("groupBox_overview_none")
        self.groupBox_overview_none.setLayout(self.none_layout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, self.width_ratio*615, self.height_ratio*22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusBar)

        self.load_products_list()
        self.selected_product = None

        self.listWidget.itemClicked.connect(self.list_item_event)
        self.btn_evaluate.clicked.connect(self.btn_evaluate_clicked)
        self.btn_reset.clicked.connect(self.btn_reset_clicked)
        self.btn_return.clicked.connect(self.btn_return_clicked)
        self.txt_search.textChanged.connect(self.search_product)

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
        self.groupBox_overview.setTitle(_translate("MainWindow", "Overview"))
        self.groupBox_overview_none.setTitle(_translate("MainWindow", "Overview"))
        self.groupBox_overview.setVisible(False)
        self.lbl_evaluation_status.setText(_translate("MainWindow", "\t\tNot evaluated"))

        MainWindow.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, True)

    def btn_evaluate_clicked(self):
        """
                Open the evaluation evaluate window and hide the current window.
        :return:
        """
        if self.selected_product:

            from windows.evaluation_evaluate import EvaluationEvaluateWindow
            self.evaluation_evaluate_win = EvaluationEvaluateWindow(parent=self.temp_window,
                                                                    selected_product_details=self.selected_product_details)
            self.evaluation_evaluate_win.ui.selected_product = self.selected_product
            self.evaluation_evaluate_win.ui.selected_productId = self.selected_productId
            product_title = str(self.selected_product).title()
            if len(product_title) > 70:
                product_title = product_title[:70] + "..."
            self.evaluation_evaluate_win.ui.lbl_prduct.setText("  "+product_title + " :")
            self.evaluation_evaluate_win.ui.lbl_prduct.setFixedHeight(self.height_ratio*20)
            if self.isEvaluated_product:
                self.evaluation_evaluate_win.ui.load_record()
            self.evaluation_evaluate_win.show()

    def list_item_event(self, item):
        """
                    call on click a product in the product list. It specifies the currently selected product.
        :param item:
        :return:
        """
        from utils.algo_utils import get_scores

        self.selected_product = item.text()
        self.selected_productId = item.data(3)
        self.isEvaluated_product = item.data(4)
        self.selected_product_details = [item for item in self.products_dict_list
                                         if 'id' in item and item['id'] == self.selected_productId][0]
        if self.isEvaluated_product:
            self.groupBox_overview.setVisible(True)
            self.groupBox_overview_none.setVisible(False)
            self.btn_reset.setEnabled(True)
            graph_scores = get_scores(product_id=self.selected_productId)
            x, y = list(graph_scores.keys()), list(graph_scores.values())
            self.create_graph(x=x, y=y)
            self.groupBox_3.show()
            self.lbl_evaluation_status.setText(self.selected_product + " Overview Diagram:")
        else:
            self.btn_reset.setDisabled(True)
            self.groupBox_3.hide()
            self.groupBox_overview.setVisible(False)
            self.groupBox_overview_none.setVisible(True)

    def search_product(self):
        """
                Filter the products from the product list as per the text entered in txt_search.
        :return:
        """
        filter_text = str(self.txt_search.text()).lower()
        self.listWidget.clear()
        index = 0
        for item in self.products_list:
            if str(filter_text.lower()) in str(item.lower()):
                listitem = QListWidgetItem()
                listitem.setText(item)
                listitem.setData(3, self.productId_list[index])
                listitem.setData(4, self.isEvaluated_list[index])
                self.listWidget.addItem(listitem)
            index += 1
        self.scrollArea.setWidget(self.listWidget)

    def btn_reset_clicked(self):
        """
                Reset the selected evaluation by calling the function reset_evaluation
        :return:
        """
        reset = self.reset_evaluation(self.selected_productId)
        if reset:
            self.load_products_list()
            self.groupBox_3.hide()
            self.groupBox_overview.setVisible(False)
            self.groupBox_overview_none.setVisible(True)

    def btn_return_clicked(self):
        """
                Save the current record and returns to the previous window
        :return:
        """
        self.temp_window.hide()

    def reset_evaluation(self, id):
        """
                Reset the evaluation by calling a function delete_evaluation from database_util file
        :param id:
        :return:
        """
        buttonReply = QtWidgets.QMessageBox.question(self.temp_window, "Message",
                                                     'Do you really want to reset this evaluation ?',
                                                     QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                     QtWidgets.QMessageBox.No)
        if buttonReply == QtWidgets.QMessageBox.Yes:
            from utils.database_utils import DatabaseConnect
            db = DatabaseConnect()
            deleted = db.delete_evaluation(product_id=id, window=self.temp_window)
            if deleted:
                self.temp_window.show()
                return True
        else:
            return False

    def load_products_list(self):
        """
                    Creates the items of list widget to display the list of products on the window
        :return:
        """
        db = DatabaseConnect()
        self.products_list, self.productId_list, self.isEvaluated_list, self.products_dict_list = db.get_products(evaluate=True,
                                                                                                                  window=self.temp_window)
        self.listWidget = QListWidget()
        self.btn_reset.setDisabled(True)

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
        """
                        Create a graph in the window
        :param x:
        :param y:
        :return:
        """
        final_x = []
        final_y = []
        temp_index = 0
        for index in range(1, 10):
            final_x.append(index)
            if index in x:
                final_y.append(y[temp_index])
                temp_index += 1
            else:
                final_y.append(0)

        import pyqtgraph as pg
        # create bar chart
        self.win.removeItem(self.bg)
        self.bg = pg.BarGraphItem(x=final_x, height=final_y, width=0.5, brushes=BAR_COLORS)
        self.win.addItem(self.bg)
        self.win.setXRange(0.5, 9.5)
        self.win.setYRange(0, 100)
        self.win.getPlotItem().getAxis('bottom').setTicks([list(zip(final_x, final_y))])
        self.graph_layout.addWidget(self.win)
        self.groupBox_overview.setLayout(self.graph_layout)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

