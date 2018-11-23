import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QTabWidget, QMainWindow


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 Dynamic tabs'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 500
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        main_tab = self.create_tab_layout(object_name="main_tab")
        for tab_index in range(1,10):
            tab = self.create_tab(object_name="tab_"+str(tab_index))
            for ques_index in range(1,8):
                question_box = self.create_questionbox(tab, question="Question "+ str(ques_index), position=ques_index-1, object_name="quesBox{index}".format(index=ques_index))
                for option_index in range(0, 5):
                    self.create_option(question_box, text=str(option_index+1), index=option_index, object_name="option"+str(option_index+1))
            main_tab.addTab(tab, "Dimension "+ str(tab_index))
        self.setCentralWidget(tab)
        self.show()

    def create_tab_layout(self, object_name="tab"):
        tab = QTabWidget(self)
        tab.setGeometry(QtCore.QRect(20, 30, 581, 450))
        tab.setLayoutDirection(QtCore.Qt.LeftToRight)
        tab.setTabPosition(QtWidgets.QTabWidget.West)
        tab.setElideMode(QtCore.Qt.ElideNone)
        tab.setObjectName(object_name)
        return tab

    def create_tab(self, object_name="tab_dimension"):
        tab_dimension = QtWidgets.QWidget(self.centralWidget())
        tab_dimension.setObjectName(object_name)
        return tab_dimension

    def create_questionbox(self, tab_dimension, question, position=0, object_name="quesBox"):
        question_box = QtWidgets.QGroupBox(tab_dimension)
        question_box.setGeometry(QtCore.QRect(40, 10+(60*position), 450, 50))
        question_box.setObjectName(object_name)
        question_box.setTitle(question)
        return question_box

    def create_option(self, question_box, text, index=0, object_name="option"):
        option = QtWidgets.QRadioButton(question_box)
        option.setGeometry(QtCore.QRect(10+(90*index), 25, 81, 23))
        option.setObjectName(object_name)
        option.setText(text)
        return option


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
