from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from utils.tab_utils import TabWidget
from utils.path_utils import copy_file
from utils.graph_utils import BAR_COLORS, create_graph_indicator


class EvaluationEvaluateWindow(QMainWindow):
    """
                Main class of the Evaluation - evaluate module
    """
    def __init__(self, parent=None, selected_product_details=None):
        super(EvaluationEvaluateWindow, self).__init__(parent)
        self.ui = Ui_MainWindow(self, selected_product_details)
        self.parent_win = parent
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.ui.temp_window.setWindowTitle("Financial Product Analysis Tool - Evaluation:Evaluate")


class Ui_MainWindow(object):
    """
                UI of the Evaluation - evaluate module
    """
    def __init__(self, MainWindow, selected_product_details):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedHeight(580)
        MainWindow.setFixedWidth(640)
        self.temp_window = MainWindow
        self.selected_product_details = selected_product_details
        self.selected_productId = None
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.attachment1_path = None
        self.attachment2_path = None

        """************************************************************************""""""
                                DYNAMICALLY CREATED TABS
        """""""***********************************************************************"""
        self.questions = self.get_questions()
        tabs =list(set([question['dimension'] for question in self.questions]))
        self.tab = self.create_tab_layout(object_name="main_tab")
        for tab_index in tabs:
            question_index = 0
            tab = self.create_tab(object_name="tab_"+str(tab_index))
            for question_data in self.questions:
                if question_data["dimension"] == tab_index:

                    question_box = self.create_questionbox(tab, question=question_data["question"],
                                                           position=question_index,
                                                           object_name="quesBox{index}".format(index=question_index+1))
                    question_index += 1

                    for option_index in range(0, 5):
                        print(self.selected_product_details, tab_index, question_index)
                        if self.selected_product_details["categorya"] == '1' and tab_index == 6 and question_index == 7:
                            disable = True
                        elif self.selected_product_details["categorya"] == '2' and tab_index == 6 and question_index == 6:
                            disable = True
                        else:
                            disable = False

                        self.create_option(question_box, text=str(option_index+1), index=option_index,
                                           object_name="option" + str(option_index+1), disable=disable)

            self.tab.addTab(tab, "Dimension " + str(tab_index))

        self.tab_overview = QtWidgets.QWidget()
        self.tab_overview.setObjectName("tab_overview")
        self.tab.currentChanged.connect(self.tab_overview_selected)
        """
                                                 GRAPH UI
        """

        import pyqtgraph as pg

        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')
        self.win = pg.PlotWidget()

        self.bg = pg.BarGraphItem(x=[], height=[], width=0.5, brushes=BAR_COLORS)
        self.win.setXRange(0.5, 9.5)
        self.win.addItem(self.bg)

        # set the layout
        self.graph_layout = QtWidgets.QVBoxLayout()
        self.graph_layout.setGeometry(QtCore.QRect(30, 30, 450, 251))
        self.graph_layout.addWidget(self.win)

        self.graph_layout2 = QtWidgets.QVBoxLayout()
        self.graph_layout2.setGeometry(QtCore.QRect(30, 260, 450, 100))
        # self.graph_layout.addLayout(self.graph_layout2)

        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_overview)
        self.groupBox_3.setGeometry(QtCore.QRect(30, 260, 450, 55))
        self.groupBox_3.setLayout(self.graph_layout2)
        self.groupBox_3.setStyleSheet("background-color:white;")

        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_overview)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 30, 450, 251))
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_2.setLayout(self.graph_layout)
        """                            *********         """

        self.lbl_graph = QtWidgets.QLabel(self.groupBox_2)
        self.lbl_graph.setGeometry(QtCore.QRect(10, 30, 500, 17))
        self.lbl_graph.setObjectName("lbl_graph")
        self.lbl_graph.setText("Not Evaluated Yet")

        create_graph_indicator(self.graph_layout2)
        self.graph_layout.addLayout(self.graph_layout2)

        self.btn_attachment1 = QtWidgets.QPushButton(self.tab_overview)
        self.btn_attachment1.setGeometry(QtCore.QRect(70, 370, 121, 51))
        self.btn_attachment1.setObjectName("btn_attachment1")
        self.btn_attachment2 = QtWidgets.QPushButton(self.tab_overview)
        self.btn_attachment2.setGeometry(QtCore.QRect(300, 370, 121, 51))
        self.btn_attachment2.setObjectName("btn_attachment2")
        self.tab.addTab(self.tab_overview, "")

        """"__________________________________________****************_____________________________________________"""

        self.btn_save = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save.setGeometry(QtCore.QRect(370, 540, 100, 25))
        self.btn_save.setObjectName("btn_save")
        self.btn_return = QtWidgets.QPushButton(self.centralwidget)
        self.btn_return.setGeometry(QtCore.QRect(490, 540, 100, 25))
        self.btn_return.setObjectName("btn_return")
        self.btn_reset = QtWidgets.QPushButton(self.centralwidget)
        self.btn_reset.setGeometry(QtCore.QRect(250, 540, 100, 25))
        self.btn_reset.setObjectName("btn_reset")
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(130, 540, 100, 25))
        self.btn_back.setObjectName("btn_back")
        self.lbl_prduct = QtWidgets.QLabel(self.centralwidget)
        self.lbl_prduct.setGeometry(QtCore.QRect(15, 5, 550, 17))
        self.lbl_prduct.setObjectName("lbl_prduct")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.set_window_actions()
        self.retranslateUi()
        self.tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self):
        """
               Set the properties of the UI elements
        :return:
        """
        _translate = QtCore.QCoreApplication.translate
        self.btn_save.setText(_translate("MainWindow", "Save"))
        self.btn_return.setText(_translate("MainWindow", "Return"))
        self.btn_attachment1.setText(_translate("MainWindow", "Attachment 1"))
        self.btn_attachment2.setText(_translate("MainWindow", "Attachment 2"))
        self.tab.setTabText(self.tab.indexOf(self.tab_overview), _translate("MainWindow", "Overview"))
        self.btn_reset.setText(_translate("MainWindow", "Reset"))
        self.btn_back.setText(_translate("MainWindow", "Back"))
        self.lbl_prduct.setText(_translate("MainWindow", "lbl_product :"))
        self.tab.show()

    def set_window_actions(self):
        """
                        SET ALL EVENTS AND ACTIONS ON COMPONENTS OF THE WINDOW
        :return:
        """
        self.btn_attachment1.clicked.connect(self.btn_attachment1_clicked)
        self.btn_attachment2.clicked.connect(self.btn_attachment2_clicked)
        self.btn_back.clicked.connect(self.btn_back_clicked)
        self.btn_reset.clicked.connect(self.btn_reset_clicked)
        self.btn_return.clicked.connect(self.btn_return_clicked)
        self.btn_save.clicked.connect(self.btn_save_clicked)

    def btn_attachment1_clicked(self):
        """
                                            UPLOAD ATTACHMENT 1
        :return:
        """
        from PyQt5.QtCore import QSize
        from PyQt5.QtGui import QIcon
        file_dailog = QFileDialog(self.temp_window)
        file_path = file_dailog.getOpenFileName(self.temp_window)[0]
        if file_path:
            icon = QIcon(file_path)
            self.attachment1_path = copy_file(file_path, dest="attachment")
            self.btn_attachment1.setAutoFillBackground(True)
            self.btn_attachment1.setIconSize(QSize(self.btn_attachment1.width(), self.btn_attachment1.height()))

            self.btn_attachment1.setIcon(icon)
            self.btn_attachment1.setText(file_path.split("/")[-1])
            self.btn_attachment1.show()

    def btn_attachment2_clicked(self):
        """
                                            UPLOAD ATTACHMENT 2
        :return:
        """
        from PyQt5.QtCore import QSize
        from PyQt5.QtGui import QIcon
        file_dailog = QFileDialog(self.temp_window)
        file_path = file_dailog.getOpenFileName(self.temp_window, filter="Images (*.png *.jpg)")[0]
        if file_path:
            icon = QIcon(file_path)
            self.attachment2_path = copy_file(file_path, dest="attachment")
            self.btn_attachment2.setAutoFillBackground(True)
            self.btn_attachment2.setIconSize(QSize(self.btn_attachment2.width(), self.btn_attachment2.height()))
            self.btn_attachment1.setIcon(icon)
            self.btn_attachment1.setText(file_path.split("/")[-1])
            self.btn_attachment2.show()

    def btn_back_clicked(self):
        """
                                        HIDE CURRENT WINDOW AND SHOW PARENT WINDOW
        :return:
        """
        self.temp_window.parent_win.show()
        self.temp_window.hide()

    def btn_reset_clicked(self):
        selected_tab = self.tab.currentWidget()
        print("selected tab:", selected_tab.objectName())
        if selected_tab.objectName() != "tab_overview":
            for group_box in selected_tab.children():
                group_box.children()[0].setExclusive(False)
                print("group_box:", group_box.title())
                for option in group_box.children()[1:]:
                    if option.isChecked():
                        print("Options", option.text())
                        option.setChecked(False)
                group_box.children()[0].setExclusive(True)

    def get_questions(self):
        """
                                        GET ALL THE QUESTIONS FROM DATABASE
        :return: questions
        """
        from utils.database_utils import DatabaseConnect
        db = DatabaseConnect()
        questions = db.get_all_questions(window=self.temp_window)
        return questions

    def create_tab_layout(self, object_name="tab"):
        """
                                Create the layout of the tab
        :param object_name:
        :return: tab
        """
        tab = TabWidget(self.centralwidget)
        tab.setGeometry(QtCore.QRect(25, 30, 700, 500))
        tab.setLayoutDirection(QtCore.Qt.LeftToRight)
        tab.setTabPosition(QtWidgets.QTabWidget.West)
        tab.setElideMode(QtCore.Qt.ElideNone)
        tab.setObjectName(object_name)
        return tab

    def create_tab(self, object_name="tab_dimension"):
        """
                        Create a tab for the dimension
        :param object_name:
        :return:
        """
        tab_dimension = QtWidgets.QWidget(self.temp_window.centralWidget())
        tab_dimension.setObjectName(object_name)
        return tab_dimension

    def create_questionbox(self, tab_dimension, question, position, object_name):
        """
                        Create a question the dimension
        :param tab_dimension:
        :param question:
        :param position:
        :param object_name:
        :return:
        """
        question_box = QtWidgets.QGroupBox(tab_dimension)
        question_box.setGeometry(QtCore.QRect(40, 10 + (60 * position), 450, 50))
        question_box.setObjectName(object_name)
        question_box.setTitle(question)
        QtWidgets.QButtonGroup(question_box)
        return question_box

    def create_option(self, question_box, text, index, object_name, disable=False):
        """
                                Create 5 options 1-5 to select a answer
        :param question_box:
        :param text:
        :param index:
        :param object_name:
        :param disable:
        :return: option
        """
        option = QtWidgets.QRadioButton(question_box)
        option.setGeometry(QtCore.QRect(10 + (90 * index), 25, 81, 23))
        option.setObjectName(object_name)
        option.setText(text)
        question_box.children()[0].addButton(option)
        option.setDisabled(disable)
        return option

    def btn_return_clicked(self):
        """
                    Save evaluation and return to the Evaluation window
        """
        buttonReply = QtWidgets.QMessageBox.question(self.temp_window, "Message",
                                                     'Do you want to save the Evaluation of product"{}" ?'.format(self.selected_product),
                                                     QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                     QtWidgets.QMessageBox.No)
        if buttonReply == QtWidgets.QMessageBox.Yes:
            self.btn_save_clicked()
        self.temp_window.hide()

    def btn_save_clicked(self):
        """
                    Save the Evaluation in the fpat_evaluation table
        :return:
        """
        tabs = self.tab.children()[0].children()
        answer_list = []
        self.create_evaluation(self.attachment1_path, self.attachment2_path)
        for tab in tabs:
            if tab and "tab_" in tab.objectName() and tab.objectName() != "tab_overview":
                tab_name = str(tab.objectName())
                dimension = int((tab_name).replace("tab_", ""))
                for quesbox in tab.children():
                    question = quesbox.title()
                    for option in quesbox.children()[1:]:
                        if option.isChecked():
                            answer = int(option.text())
                            answer_list.append(answer)
                            print("question::", question, "\nAnswer", answer, "\nDimension", dimension)
                            self.save_answers(question, answer, dimension)

        self.temp_window.parent_win.ui.load_products_list()
        self.btn_reset.setDisabled(True)
        self.btn_save.setDisabled(True)
        self.btn_return.setDisabled(True)
        QtWidgets.QMessageBox.about(self.temp_window, "Message", 'Evaluation saved successfully !!!')

    def save_answers(self, question, answer, dimension):
        """
                            Save the answers of the evaluation in the database
        :param question:
        :param answer:
        :param dimension:
        :return:
        """
        from utils.database_utils import DatabaseConnect
        conn = DatabaseConnect()
        saved = conn.save_answers(answer=answer, question=question, dimension=dimension,
                                  evaluation_id=self.evaluation_id, window=self.temp_window)
        if saved:
            print("Answer saved Successfully !!!!")

    def create_evaluation(self, attachment_one, attachment_two):
        """
                            Save gthe evaluation with attachment paths in the database
        :param attachment_one:
        :param attachment_two:
        :return:
        """
        from utils.database_utils import DatabaseConnect
        conn = DatabaseConnect()
        self.evaluation_id = conn.create_evaluation(self.selected_productId, attachment_one, attachment_two,
                                                    window=self.temp_window)

    def create_graph(self, x, y):
        """
                    Create a graph in the UI of the window
        :param x:
        :param y:
        :return:
        """
        print("x", x, "y", y)
        import pyqtgraph as pg
        # create bar chart
        self.win.removeItem(self.bg)
        self.bg = pg.BarGraphItem(x=x, height=y, width=0.5, brushes=BAR_COLORS)
        self.win.addItem(self.bg)
        self.win.setXRange(0.5, 9.5)
        self.win.setYRange(0, 100)
        self.graph_layout.addWidget(self.win)
        self.groupBox_2.setLayout(self.graph_layout)

    def tab_overview_selected(self):
        """
                    Evaluate the questions and create a graph to display on UI aof the overview tab
        """
        selected_tab = self.tab.currentWidget()
        if selected_tab.objectName() == "tab_overview":
            tabs = self.tab.children()[0].children()
            answers ={}
            dimension_scores ={}
            for tab in tabs:
                if tab and tab.objectName() == "tab_overview":
                    pass

                elif tab and "tab_" in tab.objectName():
                    tab_name = str(tab.objectName())
                    dimension = int((tab_name).replace("tab_", ""))
                    answer_list = []
                    for quesbox in tab.children():
                        question = quesbox.title()
                        for option in quesbox.children()[1:]:
                            if option.isChecked():
                                answer = int(option.text())
                                answer_list.append(answer)
                    answers.update({dimension: answer_list})

            from utils.algo_utils import get_dimension_score
            for dimension, answers in answers.items():
                d_score = get_dimension_score(answers)
                dimension_scores.update({dimension: d_score})

            x= [item for item in range(1,10)]
            y= [dimension_scores[item] for item in x]
            self.create_graph(x=x, y=y)
            self.lbl_graph.setText("")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

