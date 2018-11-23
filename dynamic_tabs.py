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
        for tab_index in range(1, 10):
            tab = self.create_tab(object_name="tab_"+str(tab_index))
            for ques_index in range(1, 8):
                question_box = self.create_questionbox(tab, question="T" + str(tab_index) + "Question " + str(ques_index),
                                                       position=ques_index-1,
                                                       object_name="quesBox{index}".format(index=ques_index))
                for option_index in range(0, 5):
                    self.create_option(question_box, text=str(option_index+1), index=option_index,
                                       object_name="option" + str(option_index+1))
            main_tab.addTab(tab, "Dimension " + str(tab_index))
        self.setCentralWidget(main_tab)
        self.btn_save = QtWidgets.QPushButton(self)
        self.btn_save.setGeometry(QtCore.QRect(360, 450, 101, 25))
        self.btn_save.setObjectName("btn_save")
        self.btn_save.setText("Save")
        self.btn_return = QtWidgets.QPushButton(self)
        self.btn_return.setGeometry(QtCore.QRect(480, 450, 101, 25))
        self.btn_return.setObjectName("btn_return")
        self.btn_return.setText("Return")
        self.btn_reset = QtWidgets.QPushButton(self)
        self.btn_reset.setGeometry(QtCore.QRect(240, 450, 101, 25))
        self.btn_reset.setObjectName("btn_reset")
        self.btn_reset.setText("Reset")
        self.btn_back = QtWidgets.QPushButton(self)
        self.btn_back.setGeometry(QtCore.QRect(120, 450, 101, 25))
        self.btn_back.setObjectName("btn_back")
        self.btn_back.setText("Back")
        self.btn_reset.clicked.connect(self.btn_reset_clicked)
        # test_tab = self.centralWidget().children()[0].children()[0].children()
        # for group in test_tab:
        #     for option in group.children():
        #         print(option.setChecked(False))
        self.show()

    def btn_reset_clicked(self):
        main_tab = self.centralWidget().children()[0]
        selected_tab = main_tab.currentWidget()
        for group_box in selected_tab.children():
            group_box.children()[0].setExclusive(False)
            for option in group_box.children()[1:]:
                if option.isChecked():
                    option.setChecked(False)
            group_box.children()[0].setExclusive(True)

    def create_tab_layout(self, object_name="tab"):
        tab = TabWidget(self)
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
        button_box = QtWidgets.QButtonGroup(question_box)
        return question_box

    def create_option(self, question_box, text, index=0, object_name="option"):
        option = QtWidgets.QRadioButton(question_box)
        option.setGeometry(QtCore.QRect(10+(90*index), 25, 81, 23))
        option.setObjectName(object_name)
        option.setText(text)
        question_box.children()[0].addButton(option)
        return option


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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
