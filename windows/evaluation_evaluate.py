# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_collection/evaluation_evaluate.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QFileDialog


class TabBar(QtWidgets.QTabBar):
    def tabSizeHint(self, index):
        s = QtWidgets.QTabBar.tabSizeHint(self, index)
        s.transpose()
        return s

    def paintEvent(self, event):
        painter = QtWidgets.QStylePainter(self)
        opt = QtWidgets.QStyleOptionTab()

        for i in range(self.count()):
            self.initStyleOption(opt, i)
            painter.drawControl(QtWidgets.QStyle.CE_TabBarTabShape, opt)
            painter.save()

            s = opt.rect.size()
            s.transpose()
            r = QtCore.QRect(QtCore.QPoint(), s)
            r.moveCenter(opt.rect.center())
            opt.rect = r

            c = self.tabRect(i).center()
            painter.translate(c)
            painter.rotate(90)
            painter.translate(-c)
            painter.drawControl(QtWidgets.QStyle.CE_TabBarTabLabel, opt);
            painter.restore()


class TabWidget(QtWidgets.QTabWidget):
    def __init__(self, *args, **kwargs):
        QtWidgets.QTabWidget.__init__(self, *args, **kwargs)
        self.setTabBar(TabBar(self))
        self.setTabPosition(QtWidgets.QTabWidget.West)


class EvaluationEvaluateWindow(QMainWindow):
    def __init__(self, parent=None):
        super(EvaluationEvaluateWindow, self).__init__(parent)
        self.ui = Ui_MainWindow(self)
        self.ui.temp_window.setWindowTitle("Financial Product Analysis Tool - Evaluation:Evaluate")


class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 525)
        self.temp_window = MainWindow
        self.selected_productId = None
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
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
                        self.create_option(question_box, text=str(option_index+1), index=option_index,
                                           object_name="option" + str(option_index+1))
            self.tab.addTab(tab, "Dimension " + str(tab_index))

        self.tab_overview = QtWidgets.QWidget()
        self.tab_overview.setObjectName("tab_overview")
        self.graphicsView = QtWidgets.QGraphicsView(self.tab_overview)
        self.graphicsView.setGeometry(QtCore.QRect(40, 30, 400, 251))
        self.graphicsView.setMidLineWidth(10)
        self.graphicsView.setObjectName("graphicsView")
        self.btn_attachment1 = QtWidgets.QPushButton(self.tab_overview)
        self.btn_attachment1.setGeometry(QtCore.QRect(70, 340, 121, 51))
        self.btn_attachment1.setObjectName("btn_attachment1")
        self.btn_attachment2 = QtWidgets.QPushButton(self.tab_overview)
        self.btn_attachment2.setGeometry(QtCore.QRect(300, 340, 121, 51))
        self.btn_attachment2.setObjectName("btn_attachment2")
        self.tab.addTab(self.tab_overview, "")

        self.btn_save = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save.setGeometry(QtCore.QRect(370, 480, 100, 25))
        self.btn_save.setObjectName("btn_save")
        self.btn_return = QtWidgets.QPushButton(self.centralwidget)
        self.btn_return.setGeometry(QtCore.QRect(490, 480, 100, 25))
        self.btn_return.setObjectName("btn_return")
        self.btn_reset = QtWidgets.QPushButton(self.centralwidget)
        self.btn_reset.setGeometry(QtCore.QRect(250, 480, 100, 25))
        self.btn_reset.setObjectName("btn_reset")
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(130, 480, 100, 25))
        self.btn_back.setObjectName("btn_back")
        self.lbl_prduct = QtWidgets.QLabel(self.centralwidget)
        self.lbl_prduct.setGeometry(QtCore.QRect(10, 10, 91, 17))
        self.lbl_prduct.setObjectName("lbl_prduct")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.set_window_actions()
        self.retranslateUi(MainWindow)
        self.tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        # MainWindow.setWindowTitle(_translate("MainWindow", "Financial Product Analysis Tool - Evaluation:Evaluate"))
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
        self.btn_attachment1.clicked.connect(self.btn_attachment1_clicked)
        self.btn_attachment2.clicked.connect(self.btn_attachment2_clicked)
        self.btn_back.clicked.connect(self.btn_back_clicked)
        self.btn_reset.clicked.connect(self.btn_reset_clicked)
        self.btn_return.clicked.connect(self.btn_return_clicked)
        self.btn_save.clicked.connect(self.btn_save_clicked)

    def btn_attachment1_clicked(self):
        from PyQt5.QtCore import QSize
        from PyQt5.QtGui import QIcon
        file_dailog = QFileDialog(self.temp_window)
        file_path = file_dailog.getOpenFileName(self.temp_window, filter="Images (*.png *.jpg)")[0]
        icon = QIcon(file_path)
        self.btn_attachment1.setAutoFillBackground(True)
        self.btn_attachment1.setIconSize(QSize(self.btn_attachment1.width(), self.btn_attachment1.height()))
        self.btn_attachment1.setText("")
        self.btn_attachment1.setIcon(icon)
        self.btn_attachment1.show()

    def btn_attachment2_clicked(self):
        from PyQt5.QtCore import QSize
        from PyQt5.QtGui import QIcon
        file_dailog = QFileDialog(self.temp_window)
        file_path = file_dailog.getOpenFileName(self.temp_window, filter="Images (*.png *.jpg)")[0]
        icon = QIcon(file_path)
        self.btn_attachment2.setAutoFillBackground(True)
        self.btn_attachment2.setIconSize(QSize(self.btn_attachment2.width(), self.btn_attachment2.height()))
        self.btn_attachment2.setText("")
        self.btn_attachment2.setIcon(icon)
        self.btn_attachment2.show()

    def btn_back_clicked(self):
        self.temp_window.hide()

    def btn_reset_clicked(self):
        selected_tab = self.tab.currentWidget()
        print("selected tab:", selected_tab.objectName())
        for group_box in selected_tab.children():
            group_box.children()[0].setExclusive(False)
            print("group_box:", group_box.title())
            for option in group_box.children()[1:]:
                if option.isChecked():
                    print("Options", option.text())
                    option.setChecked(False)
            group_box.children()[0].setExclusive(True)

    def get_questions(self):
        from windows.database_util import DatabaseConnect
        db = DatabaseConnect()
        questions = db.get_all_questions()
        return questions

    def create_tab_layout(self, object_name="tab"):
        tab = TabWidget(self.centralwidget)
        tab.setGeometry(QtCore.QRect(20, 30, 581, 450))
        tab.setLayoutDirection(QtCore.Qt.LeftToRight)
        tab.setTabPosition(QtWidgets.QTabWidget.West)
        tab.setElideMode(QtCore.Qt.ElideNone)
        tab.setObjectName(object_name)
        return tab

    def create_tab(self, object_name="tab_dimension"):
        tab_dimension = QtWidgets.QWidget(self.temp_window.centralWidget())
        tab_dimension.setObjectName(object_name)
        return tab_dimension

    def create_questionbox(self, tab_dimension, question, position=0, object_name="quesBox"):
        question_box = QtWidgets.QGroupBox(tab_dimension)
        question_box.setGeometry(QtCore.QRect(40, 10 + (60 * position), 450, 50))
        question_box.setObjectName(object_name)
        question_box.setTitle(question)
        buttonbox = QtWidgets.QButtonGroup(question_box)
        return question_box

    def create_option(self, question_box, text, index=0, object_name="option"):
        option = QtWidgets.QRadioButton(question_box)
        option.setGeometry(QtCore.QRect(10 + (90 * index), 25, 81, 23))
        option.setObjectName(object_name)
        option.setText(text)
        question_box.children()[0].addButton(option)
        return option

    def btn_return_clicked(self):
        # print(self.tab.children()[0].children()[1].children()[0].children()[0].text())
        self.btn_save_clicked()
        self.temp_window.hide()
        pass

    def btn_save_clicked(self):
        tabs = self.tab.children()[0].children()
        for tab in tabs:
            if tab and tab.objectName() == "tab_overview":
                attachment1 = ""
                attachment2 = ""
                for tab_child in tab.children():
                    if tab_child.objectName() == "btn_attachment1":
                        attachment1 += ""
                    elif tab_child.objectName() == "btn_attachment2":
                        attachment2 += ""
                self.create_evaluation(attachment1, attachment2)

            elif tab and "tab_" in tab.objectName():
                tab_name = str(tab.objectName())
                dimension = int((tab_name).replace("tab_", ""))
                for quesbox in tab.children():
                    question = quesbox.title()
                    for option in quesbox.children()[1:]:
                        if option.isChecked():
                            answer = int(option.text())
                            print("question::", question, "\nAnswer", answer, "\n Dimension", dimension)
                            self.save_answers(question, answer, dimension)

    def save_answers(self, question, answer, dimension):
        from windows.database_util import DatabaseConnect
        conn = DatabaseConnect()
        answer_id = conn.save_answers(answer=answer, question=question, dimension=dimension)
        is_executed = conn.map_evaluation_answer(self.evaluation_id, answer_id)
        if is_executed:
            print("Executed Successfully !!!!")

    def create_evaluation(self, attachment_one, attachment_two):
        from windows.database_util import DatabaseConnect
        conn = DatabaseConnect()
        self.evaluation_id = conn.create_evaluation(self.selected_productId, attachment_one, attachment_two)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

