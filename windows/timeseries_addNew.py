# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_collection/timeseries_addNew.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

FILE_TYPE = ['1', '2']  # Constant list containing available type of FILES to select in timeseries module
ANALYSE_TYPE = ['A', 'B', 'C']   # Constant list containing available type of ANALYSIS to select in timeseries module


class TimeSeriesAddNewWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(TimeSeriesAddNewWindow, self).__init__(parent)
        self.setWindowTitle("Financial Product Analysis Tool - Time Series:Add new")
        self.ui = Ui_MainWindow(self)


class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        """
        # Constructor containing the UI of the "Time Series:Add new" window
        :param MainWindow: Parent class of the current class
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(644, 460)
        self.temp_window = MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_header = QtWidgets.QLabel(self.centralwidget)
        self.lbl_header.setGeometry(QtCore.QRect(10, 20, 181, 17))
        self.lbl_header.setObjectName("lbl_header")
        self.lbl_name = QtWidgets.QLabel(self.centralwidget)
        self.lbl_name.setGeometry(QtCore.QRect(20, 50, 67, 17))
        self.lbl_name.setObjectName("lbl_name")
        self.txt_name = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_name.setGeometry(QtCore.QRect(120, 50, 291, 25))
        self.txt_name.setObjectName("txt_name")
        self.btn_load_file = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load_file.setGeometry(QtCore.QRect(420, 50, 171, 25))
        self.btn_load_file.setObjectName("btn_load_file")
        self.lbl_name_2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_name_2.setGeometry(QtCore.QRect(20, 80, 67, 17))
        self.lbl_name_2.setObjectName("lbl_name_2")
        self.combo_filetype = QtWidgets.QComboBox(self.centralwidget)
        self.combo_filetype.setGeometry(QtCore.QRect(120, 80, 151, 25))
        self.combo_filetype.setObjectName("combo_filetype")
        self.combo_filetype.addItems(FILE_TYPE)
        self.lbl_name_3 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_name_3.setGeometry(QtCore.QRect(300, 80, 111, 17))
        self.lbl_name_3.setObjectName("lbl_name_3")
        self.combo_analysetype = QtWidgets.QComboBox(self.centralwidget)
        self.combo_analysetype.setGeometry(QtCore.QRect(420, 80, 171, 25))
        self.combo_analysetype.setObjectName("combo_analysetype")
        self.combo_analysetype.addItems(ANALYSE_TYPE)
        self.groupBox_verification = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_verification.setGeometry(QtCore.QRect(20, 120, 571, 91))
        self.groupBox_verification.setObjectName("groupBox_verification")
        self.lbl_name_4 = QtWidgets.QLabel(self.groupBox_verification)
        self.lbl_name_4.setGeometry(QtCore.QRect(10, 30, 81, 17))
        self.lbl_name_4.setObjectName("lbl_name_4")
        self.lbl_name_5 = QtWidgets.QLabel(self.groupBox_verification)
        self.lbl_name_5.setGeometry(QtCore.QRect(10, 60, 81, 17))
        self.lbl_name_5.setObjectName("lbl_name_5")
        self.txt_starttime = QtWidgets.QTimeEdit(self.groupBox_verification)
        self.txt_starttime.setGeometry(QtCore.QRect(100, 30, 171, 26))
        self.txt_starttime.setReadOnly(True)
        self.txt_starttime.setObjectName("txt_starttime")
        self.txt_endtime = QtWidgets.QTimeEdit(self.groupBox_verification)
        self.txt_endtime.setGeometry(QtCore.QRect(390, 30, 171, 26))
        self.txt_endtime.setReadOnly(True)
        self.txt_endtime.setObjectName("txt_endtime")
        self.lbl_name_6 = QtWidgets.QLabel(self.groupBox_verification)
        self.lbl_name_6.setGeometry(QtCore.QRect(300, 30, 71, 17))
        self.lbl_name_6.setObjectName("lbl_name_6")
        self.txt_seriesdata = QtWidgets.QLineEdit(self.groupBox_verification)
        self.txt_seriesdata.setGeometry(QtCore.QRect(100, 60, 171, 25))
        self.txt_seriesdata.setReadOnly(True)
        self.txt_seriesdata.setObjectName("txt_seriesdata")
        self.lbl_name_7 = QtWidgets.QLabel(self.groupBox_verification)
        self.lbl_name_7.setGeometry(QtCore.QRect(300, 60, 81, 17))
        self.lbl_name_7.setObjectName("lbl_name_7")
        self.txt_emptydata = QtWidgets.QLineEdit(self.groupBox_verification)
        self.txt_emptydata.setGeometry(QtCore.QRect(390, 60, 171, 25))
        self.txt_emptydata.setText("")
        self.txt_emptydata.setReadOnly(True)
        self.txt_emptydata.setObjectName("txt_emptydata")
        self.lbl_name_8 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_name_8.setGeometry(QtCore.QRect(20, 230, 67, 17))
        self.lbl_name_8.setObjectName("lbl_name_8")
        self.txt_memo = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_memo.setGeometry(QtCore.QRect(20, 250, 571, 101))
        self.txt_memo.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txt_memo.setObjectName("txt_memo")
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(20, 370, 141, 25))
        self.btn_back.setObjectName("btn_back")
        self.btn_addanother = QtWidgets.QPushButton(self.centralwidget)
        self.btn_addanother.setGeometry(QtCore.QRect(230, 370, 141, 25))
        self.btn_addanother.setObjectName("btn_addanother")
        self.btn_saveAndReturn = QtWidgets.QPushButton(self.centralwidget)
        self.btn_saveAndReturn.setGeometry(QtCore.QRect(430, 370, 161, 25))
        self.btn_saveAndReturn.setObjectName("btn_saveAndReturn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 644, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.modify =False
        self.btn_load_file.clicked.connect(self.btn_load_file_clicked)
        self.btn_back.clicked.connect(self.btn_back_clicked)
        self.btn_addanother.clicked.connect(self.btn_addanother_clicked)
        self.btn_saveAndReturn.clicked.connect(self.btn_saveAndReturn_clicked)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Financial Product Analysis Tool - Time Series:Add new"))
        self.lbl_header.setText(_translate("MainWindow", "Add a new Time Series : "))
        self.lbl_name.setText(_translate("MainWindow", "Name :"))
        self.btn_load_file.setText(_translate("MainWindow", "Load Source File"))
        self.lbl_name_2.setText(_translate("MainWindow", "File Type :"))
        self.lbl_name_3.setText(_translate("MainWindow", "Analyse Type : "))
        self.groupBox_verification.setTitle(_translate("MainWindow", "Verification : "))
        self.lbl_name_4.setText(_translate("MainWindow", "Start time :"))
        self.lbl_name_5.setText(_translate("MainWindow", "Series data : "))
        self.lbl_name_6.setText(_translate("MainWindow", "End time :"))
        self.lbl_name_7.setText(_translate("MainWindow", "Empty data : "))
        self.lbl_name_8.setText(_translate("MainWindow", "Memo :"))
        self.btn_back.setText(_translate("MainWindow", "Back"))
        self.btn_addanother.setText(_translate("MainWindow", "Add another"))
        self.btn_saveAndReturn.setText(_translate("MainWindow", "Save and Return"))

    def btn_load_file_clicked(self):
        file_dailog = QtWidgets.QFileDialog(self.temp_window)
        file_path = file_dailog.getOpenFileName(self.temp_window, filter="Docs (*.csv *.xls)")[0]
        print(file_path)

    def btn_back_clicked(self):
        self.temp_window.hide()

    def btn_addanother_clicked(self):
        self.save_timeseries()
        self.clear_window()

    def btn_saveAndReturn_clicked(self):
        self.save_timeseries()
        self.btn_back_clicked()

    def save_timeseries(self):
        from windows.database_util import DatabaseConnect
        db = DatabaseConnect()
        analyse_type = self.combo_analysetype.currentText()
        name = self.txt_name.text()
        start_time = 34  # self.txt_starttime.text()
        end_time = 67  # self.txt_endtime.text()
        series_data = 23456789  # int(self.txt_seriesdata.text())
        empty_data = 3456789  # int(self.txt_emptydata.text())
        file_type = self.combo_filetype.currentText()
        memo = self.txt_memo.toPlainText()

        if self.modify:
            id = db.update_timeseries(product_id=self.selected_productId, timeseries_id=self.selected_timeseriesId,
                                      analyse_type=analyse_type, description=memo, empty_data=empty_data,
                                      end_time=end_time, file_type=file_type, name=name, series_data=series_data,
                                      start_time=start_time)
        else:
            id = db.save_timeseries(analyse_type=analyse_type, description=memo, empty_data=empty_data, end_time=end_time,
                                    file_type=file_type, name=name, series_data=series_data, start_time=start_time,)
        if id:
            QtWidgets.QMessageBox.about(self.temp_window, "Info", "Record Saved Successfully !!!")

    def clear_window(self):
        self.txt_memo.clear()
        self.combo_filetype.setCurrentText(FILE_TYPE[0])
        self.combo_analysetype.setCurrentText(ANALYSE_TYPE[0])
        self.txt_emptydata.clear()
        self.txt_seriesdata.clear()
        # self.txt_endtime.setTime()
        # self.txt_starttime.clear()
        self.txt_name.clear()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

