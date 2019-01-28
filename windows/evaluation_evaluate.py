from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from utils.tab_utils import TabWidget
from utils.path_utils import copy_file
from utils.graph_utils import BAR_COLORS, create_graph_indicator
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon


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
        self.setWindowState(QtCore.Qt.WindowMaximized)

    def eventFilter(self, object, event):
        if event.type() == QtCore.QEvent.HoverEnter:
            if object.objectName() == "btn_attachment1":
                self.ui.btn_attachment1_enter()
                return True
            if object.objectName() == "btn_attachment2":
                self.ui.btn_attachment2_enter()
                return True

        if event.type() == QtCore.QEvent.HoverLeave:
            if object.objectName() == "btn_attachment1":
                self.ui.btn_attachment1_leave()
                return True
            if object.objectName() == "btn_attachment2":
                self.ui.btn_attachment2_leave()
                return True
        return False


class Ui_MainWindow(object):
    """
                UI of the Evaluation - evaluate module
    """
    def __init__(self, MainWindow, selected_product_details):
        MainWindow.setObjectName("MainWindow")
        from utils.window_utils import get_resolution_ratio
        self.width_ratio, self.height_ratio = get_resolution_ratio(640, 580)
        MainWindow.setMinimumHeight(self.height_ratio*580)
        MainWindow.setMinimumWidth(self.width_ratio*640)
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
        self.graph_win = pg.PlotWidget()

        self.bg = pg.BarGraphItem(x=[], height=[], width=0.5, brushes=BAR_COLORS)
        self.graph_win.setXRange(0.5, 9.5)
        self.graph_win.addItem(self.bg)

        # set the layout
        self.graph_layout = QtWidgets.QVBoxLayout()
        self.graph_layout.setGeometry(QtCore.QRect(self.width_ratio*30, self.height_ratio*30, self.width_ratio*450, self.height_ratio*251))
        self.graph_layout.addWidget(self.graph_win)

        self.graph_layout2 = QtWidgets.QVBoxLayout()
        self.graph_layout2.setGeometry(QtCore.QRect(self.width_ratio*30, self.height_ratio*260, self.width_ratio*450, self.height_ratio*100))
        # self.graph_layout.addLayout(self.graph_layout2)

        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_overview)
        self.groupBox_3.setGeometry(QtCore.QRect(self.width_ratio*30, self.height_ratio*260, self.width_ratio*450, self.height_ratio*55))
        self.groupBox_3.setLayout(self.graph_layout2)
        self.groupBox_3.setStyleSheet("background-color:white;")

        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_overview)
        self.groupBox_2.setGeometry(QtCore.QRect(self.width_ratio*30, self.height_ratio*30, self.width_ratio*450, self.height_ratio*251))
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_2.setLayout(self.graph_layout)
        """                            *********         """

        self.lbl_graph = QtWidgets.QLabel(self.groupBox_2)
        self.lbl_graph.setGeometry(QtCore.QRect(self.width_ratio*10, self.height_ratio*30, self.width_ratio*500, self.height_ratio*17))
        self.lbl_graph.setObjectName("lbl_graph")
        self.lbl_graph.setText("Not Evaluated Yet")

        create_graph_indicator(self.graph_layout2)
        self.graph_layout.addLayout(self.graph_layout2)

        self.btn_attachment1 = QtWidgets.QPushButton(self.tab_overview)
        self.btn_attachment1.setGeometry(QtCore.QRect(self.width_ratio*70, self.height_ratio*370, self.width_ratio*121, self.height_ratio*51))
        self.btn_attachment1.setObjectName("btn_attachment1")
        self.btn_attachment1.installEventFilter(self.temp_window)
        self.btn_attachment2 = QtWidgets.QPushButton(self.tab_overview)
        self.btn_attachment2.setObjectName("btn_attachment2")
        self.btn_attachment2.setGeometry(QtCore.QRect(self.width_ratio*300, self.height_ratio*370, self.width_ratio*121, self.height_ratio*51))
        self.btn_attachment2.installEventFilter(self.temp_window)
        self.tab.addTab(self.tab_overview, "")

        """"__________________________________________****************_____________________________________________"""

        self.btn_save = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save.setGeometry(QtCore.QRect(self.width_ratio*370, self.height_ratio*540, self.width_ratio*100, self.height_ratio*25))
        self.btn_save.setObjectName("btn_save")
        self.btn_return = QtWidgets.QPushButton(self.centralwidget)
        self.btn_return.setGeometry(QtCore.QRect(self.width_ratio*490, self.height_ratio*540, self.width_ratio*100, self.height_ratio*25))
        self.btn_return.setObjectName("btn_return")
        self.btn_reset = QtWidgets.QPushButton(self.centralwidget)
        self.btn_reset.setGeometry(QtCore.QRect(self.width_ratio*250, self.height_ratio*540, self.width_ratio*100, self.height_ratio*25))
        self.btn_reset.setObjectName("btn_reset")
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(self.width_ratio*130, self.height_ratio*540, self.width_ratio*100, self.height_ratio*25))
        self.btn_back.setObjectName("btn_back")
        self.lbl_prduct = QtWidgets.QLabel(self.centralwidget)
        self.lbl_prduct.setGeometry(QtCore.QRect(self.width_ratio*15, self.height_ratio*5, self.width_ratio*550, self.height_ratio*17))
        self.lbl_prduct.setObjectName("lbl_prduct")

        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusBar)

        MainWindow.setCentralWidget(self.centralwidget)
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
        file_dailog = QFileDialog(self.temp_window)
        self.attachment1_path = file_dailog.getOpenFileName(self.temp_window)[0]
        file_path = self.attachment1_path
        if file_path:
            self.attachment1_path = str(copy_file(file_path, dest="attachment")).replace("\\", '/')
            self.btn_attachment1.setAutoFillBackground(True)
            self.btn_attachment1.setText(file_path.split("/")[-1])
            self.btn_attachment1.show()

    def btn_attachment2_clicked(self):
        """
                                            UPLOAD ATTACHMENT 2
        :return:
        """
        file_dailog = QFileDialog(self.temp_window)
        self.attachment2_path = str(file_dailog.getOpenFileName(self.temp_window)[0]).replace("\\", '/')
        file_path = self.attachment2_path
        if file_path:
            self.attachment2_path = str(copy_file(file_path, dest="attachment")).replace("\\", '/')
            self.btn_attachment2.setAutoFillBackground(True)
            self.btn_attachment2.setText(file_path.split("/")[-1])
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
        if selected_tab.objectName() != "tab_overview":
            for group_box in selected_tab.children():
                group_box.children()[0].setExclusive(False)
                for option in group_box.children()[1:]:
                    if option.isChecked():
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
        tab.setGeometry(QtCore.QRect(self.width_ratio*25, self.height_ratio*30, self.width_ratio*700, self.height_ratio*500))
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
        question_box.setGeometry(QtCore.QRect(self.width_ratio*40, self.height_ratio*(10 + (60 * position)), self.width_ratio*450, self.height_ratio*50))
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
        option.setGeometry(QtCore.QRect(self.width_ratio*(10 + (90 * index)), self.height_ratio*25, self.width_ratio*81, self.height_ratio*23))
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
        self.statusBar.showMessage("Saving evaluation...", 2000)
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
                            self.save_answers(question, answer, dimension)

        self.temp_window.parent_win.ui.load_products_list()
        self.btn_reset.setDisabled(True)
        self.btn_save.setDisabled(True)
        self.btn_return.setDisabled(True)
        self.statusBar.showMessage("", 2000)
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
        conn.save_answers(answer=answer, question=question, dimension=dimension,
                          evaluation_id=self.evaluation_id, window=self.temp_window)

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
        import pyqtgraph as pg
        # create bar chart
        self.graph_win.removeItem(self.bg)
        self.bg = pg.BarGraphItem(x=x, height=y, width=0.5, brushes=BAR_COLORS)
        self.graph_win.addItem(self.bg)
        self.graph_win.setXRange(0.5, 9.5)
        self.graph_win.setYRange(0, 100)
        self.graph_win.getPlotItem().getAxis('bottom').setTicks([list(zip(range(1, len(y)+1), y))])
        self.graph_layout.addWidget(self.graph_win)
        self.groupBox_2.setLayout(self.graph_layout)

    def tab_overview_selected(self):
        """
                    Evaluate the questions and create a graph to display on UI aof the overview tab
        """
        selected_tab = self.tab.currentWidget()
        if selected_tab.objectName() == "tab_overview":
            tabs = self.tab.children()[0].children()
            answers ={}

            for tab in tabs:
                if tab and tab.objectName() != "tab_overview" and "tab_" in tab.objectName():
                    tab_name = str(tab.objectName())
                    dimension = int((tab_name).replace("tab_", ""))
                    answer_list = []
                    for quesbox in tab.children():
                        for option in quesbox.children()[1:]:
                            if option.isChecked():
                                answer = int(option.text())
                                answer_list.append(answer)
                    answers.update({dimension: answer_list})

            from utils.algo_utils import get_dimension_score
            dimension_scores = {}
            for item in answers.items():
                d_score = get_dimension_score(item[1])
                dimension_scores.update({item[0]: d_score})

            x = [item for item in range(1, 10)]
            y = [dimension_scores[item] for item in x]
            self.create_graph(x=x, y=y)
            self.lbl_graph.setText("")

    def load_record(self):
        tabs = self.tab.children()[0].children()
        from utils.database_utils import DatabaseConnect
        db = DatabaseConnect()
        answer_list = db.get_answers_by_evaluation(self.selected_productId)

        attachments = db.get_attachments(window=self.temp_window, product_id=self.selected_productId)
        if attachments:
            if attachments["attachment_one"] and attachments["attachment_one"] != 'None' and attachments["attachment_one"] != "":
                self.attachment1_path = attachments["attachment_one"]
                file_path = self.attachment1_path
                self.btn_attachment1.setText(file_path.split("/")[-1][:10]+"..")
            self.btn_attachment1.setAutoFillBackground(True)
            self.btn_attachment1.clicked.disconnect(self.btn_attachment1_clicked)
            self.btn_attachment1.clicked.connect(self.show_attachment1)
            self.btn_attachment1.show()
            self.btn_attachment1.installEventFilter(self.temp_window)

            if attachments["attachment_two"] and attachments["attachment_two"] != 'None' and attachments["attachment_two"] != "":
                self.attachment2_path = attachments["attachment_two"]
                file_path = self.attachment2_path
                self.btn_attachment2.setAutoFillBackground(True)
                self.btn_attachment2.setText(file_path.split("/")[-1][:10]+"..")
            self.btn_attachment2.show()
            self.btn_attachment2.clicked.disconnect(self.btn_attachment2_clicked)
            self.btn_attachment2.clicked.connect(self.show_attachment2)
            self.btn_attachment2.installEventFilter(self.temp_window)

        for tab in tabs:
            if tab and "tab_" in tab.objectName() and tab.objectName() != "tab_overview":
                tab_name = str(tab.objectName())
                dimension = int((tab_name).replace("tab_", ""))

                for quesbox in tab.children():

                    for d in answer_list:
                        if d["question"] == quesbox.title() and d["dimension"] == dimension:
                            final_answer = str(d["answer"])

                            for option in quesbox.children()[1:]:
                                if str(option.text()) == str(final_answer):
                                    option.setChecked(True)
                    quesbox.setDisabled(True)

        self.btn_reset.setDisabled(True)
        self.btn_save.setDisabled(True)
        self.btn_return.setDisabled(True)

    def show_attachment1(self):
        if self.attachment1_path and self.attachment1_path != 'None':
            from utils.window_utils import ImageWindow
            ImageWindow(win=self.temp_window, image_path=self.attachment1_path)

    def show_attachment2(self):
        if self.attachment2_path and self.attachment2_path != 'None':
            from utils.window_utils import ImageWindow
            ImageWindow(win=self.temp_window, image_path=self.attachment2_path)

    def btn_attachment1_leave(self):

        if self.attachment1_path:
            file_path = self.attachment1_path
            self.btn_attachment1.setText(file_path.split("/")[-1][:10] + "..")
            self.btn_attachment1.setIcon(QIcon(""))
            self.btn_attachment1.show()

    def btn_attachment1_enter(self):
        if self.attachment1_path:
            import os

            file_path = self.attachment1_path
            file_path = os.path.abspath(file_path)
            icon = QIcon(file_path)
            self.btn_attachment1.setText("")
            self.btn_attachment1.setAutoFillBackground(True)
            self.btn_attachment1.setIconSize(QSize(self.btn_attachment1.width(), self.btn_attachment1.height()))
            self.btn_attachment1.setIcon(icon)
            self.btn_attachment1.show()

    def btn_attachment2_leave(self):
        if self.attachment2_path:
            file_path = self.attachment2_path
            self.btn_attachment2.setText(file_path.split("/")[-1][:10] + "..")
            self.btn_attachment2.setIcon(QIcon(""))
            self.btn_attachment2.show()

    def btn_attachment2_enter(self):
        if self.attachment2_path:
            file_path = self.attachment2_path
            icon = QIcon(file_path)
            self.btn_attachment2.setText("")
            self.btn_attachment2.setAutoFillBackground(True)
            self.btn_attachment2.setIconSize(QSize(self.btn_attachment2.width(), self.btn_attachment2.height()))
            self.btn_attachment2.setIcon(icon)
            self.btn_attachment2.show()
