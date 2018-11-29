# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_collection/analysis_module.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class AnalysisWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(AnalysisWindow, self).__init__(parent)
        self.setWindowTitle("Financial Product Analysis Tool - Analysis")
        self.ui = Ui_MainWindow(self)


class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(615, 439)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_timeseries = QtWidgets.QLabel(self.centralwidget)
        self.lbl_timeseries.setGeometry(QtCore.QRect(30, 10, 101, 17))
        self.lbl_timeseries.setObjectName("lbl_timeseries")
        self.scrollArea_timeseries = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_timeseries.setGeometry(QtCore.QRect(30, 60, 329, 101))
        self.scrollArea_timeseries.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_timeseries.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_timeseries.setWidgetResizable(True)
        self.scrollArea_timeseries.setObjectName("scrollArea_timeseries")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 313, 99))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.scrollArea_timeseries.setWidget(self.scrollAreaWidgetContents_3)
        self.groupBox_timeseries = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_timeseries.setGeometry(QtCore.QRect(400, 10, 161, 151))
        self.groupBox_timeseries.setTitle("")
        self.groupBox_timeseries.setObjectName("groupBox_timeseries")
        self.btn_analyse = QtWidgets.QPushButton(self.groupBox_timeseries)
        self.btn_analyse.setGeometry(QtCore.QRect(20, 30, 121, 25))
        self.btn_analyse.setObjectName("btn_analyse")
        self.btn_export = QtWidgets.QPushButton(self.groupBox_timeseries)
        self.btn_export.setGeometry(QtCore.QRect(20, 70, 121, 25))
        self.btn_export.setObjectName("btn_export")
        self.btn_return_2 = QtWidgets.QPushButton(self.groupBox_timeseries)
        self.btn_return_2.setGeometry(QtCore.QRect(20, 110, 121, 25))
        self.btn_return_2.setObjectName("btn_return_2")
        self.txt_timeseries = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_timeseries.setGeometry(QtCore.QRect(30, 30, 329, 25))
        self.txt_timeseries.setObjectName("txt_timeseries")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 170, 531, 221))
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_index1 = QtWidgets.QWidget()
        self.tab_index1.setObjectName("tab_index1")
        self.tabWidget.addTab(self.tab_index1, "")
        self.tab_index2 = QtWidgets.QWidget()
        self.tab_index2.setObjectName("tab_index2")
        self.tabWidget.addTab(self.tab_index2, "")
        self.tab_index3 = QtWidgets.QWidget()
        self.tab_index3.setObjectName("tab_index3")
        self.tabWidget.addTab(self.tab_index3, "")
        self.tab_index4 = QtWidgets.QWidget()
        self.tab_index4.setObjectName("tab_index4")
        self.tabWidget.addTab(self.tab_index4, "")
        self.tab_index5 = QtWidgets.QWidget()
        self.tab_index5.setObjectName("tab_index5")
        self.tabWidget.addTab(self.tab_index5, "")
        self.tab_index6 = QtWidgets.QWidget()
        self.tab_index6.setObjectName("tab_index6")
        self.tabWidget.addTab(self.tab_index6, "")
        self.tab_index7 = QtWidgets.QWidget()
        self.tab_index7.setObjectName("tab_index7")
        self.tabWidget.addTab(self.tab_index7, "")
        self.tab_index8 = QtWidgets.QWidget()
        self.tab_index8.setObjectName("tab_index8")
        self.tabWidget.addTab(self.tab_index8, "")
        self.tab_index9 = QtWidgets.QWidget()
        self.tab_index9.setObjectName("tab_index9")
        self.tabWidget.addTab(self.tab_index9, "")
        self.tab_index10 = QtWidgets.QWidget()
        self.tab_index10.setObjectName("tab_index10")
        self.tabWidget.addTab(self.tab_index10, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 615, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.timeseries_list_view()

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Financial Product Analysis Tool - Analysis"))
        self.lbl_timeseries.setText(_translate("MainWindow", "Time Series :"))
        self.btn_analyse.setText(_translate("MainWindow", "Analyse"))
        self.btn_export.setText(_translate("MainWindow", "Export"))
        self.btn_return_2.setText(_translate("MainWindow", "Return"))
        self.txt_timeseries.setPlaceholderText(_translate("MainWindow", " Search"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_index1), _translate("MainWindow", "index1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_index2), _translate("MainWindow", "index2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_index3), _translate("MainWindow", "index3"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_index4), _translate("MainWindow", "index4"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_index5), _translate("MainWindow", "index5"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_index6), _translate("MainWindow", "index6"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_index7), _translate("MainWindow", "index7"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_index8), _translate("MainWindow", "index8"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_index9), _translate("MainWindow", "index9"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_index10), _translate("MainWindow", "index10"))

    def timeseries_list_view(self):
        from windows.database_util import DatabaseConnect
        db = DatabaseConnect()
        self.timeseries_list, self.timeseriesId_list = db.get_timeserieses()
        self.timeseries_listWidget = QtWidgets.QListWidget()

        index = 0
        for item in self.timeseriesId_list:
            listitem = QtWidgets.QListWidgetItem()
            listitem.setText(self.timeseries_list[index])
            listitem.setData(1, item)
            index += 1
            self.timeseries_listWidget.addItem(listitem)
        self.timeseries_listWidget.itemClicked.connect(self.timeseries_list_item_event)
        self.scrollArea_timeseries.setWidget(self.timeseries_listWidget)

    def timeseries_list_item_event(self, item):
        self.selected_timeseries = item.text()
        self.selected_timeseriesId = item.data(1)
        print(self.selected_timeseries, self.selected_timeseriesId)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
