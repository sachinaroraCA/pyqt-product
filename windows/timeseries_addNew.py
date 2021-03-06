from PyQt5 import QtCore, QtWidgets

FILE_TYPE = ['1', '2']  # Constant list containing available type of FILES to select in timeseries module
ANALYSE_TYPE = ['A', 'B', 'C']   # Constant list containing available type of ANALYSIS to select in timeseries module


class TimeSeriesAddNewWindow(QtWidgets.QMainWindow):
    """
                Main class of the Time-series:Add new module
    """
    def __init__(self, parent=None):
        super(TimeSeriesAddNewWindow, self).__init__(parent)
        self.parent_win = parent
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.ui = Ui_MainWindow(self)
        self.setWindowState(QtCore.Qt.WindowMaximized)


class Ui_MainWindow(object):
    """
            UI class of the Time-series:Add new module
    """
    def __init__(self, MainWindow):
        """
        # init function containing the UI of the "Time Series:Add new" window
        :param MainWindow: Parent class of the current class
        """
        MainWindow.setObjectName("MainWindow")
        from utils.window_utils import get_resolution_ratio
        self.width_ratio, self.height_ratio = get_resolution_ratio(644, 460)
        MainWindow.setMinimumHeight(self.height_ratio*460)
        MainWindow.setMinimumWidth(self.width_ratio*644)
        self.temp_window = MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_header = QtWidgets.QLabel(self.centralwidget)
        self.lbl_header.setGeometry(QtCore.QRect(self.width_ratio*10, self.height_ratio*20, self.width_ratio*181, self.height_ratio*17))
        self.lbl_header.setObjectName("lbl_header")
        self.lbl_name = QtWidgets.QLabel(self.centralwidget)
        self.lbl_name.setGeometry(QtCore.QRect(self.width_ratio*20, self.height_ratio*50, self.width_ratio*67, self.height_ratio*17))
        self.lbl_name.setObjectName("lbl_name")
        self.txt_name = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_name.setGeometry(QtCore.QRect(self.width_ratio*120, self.height_ratio*50, self.width_ratio*291, self.height_ratio*25))
        self.txt_name.setObjectName("txt_name")
        self.btn_load_file = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load_file.setGeometry(QtCore.QRect(self.width_ratio*420, self.height_ratio*50, self.width_ratio*171, self.height_ratio*25))
        self.btn_load_file.setObjectName("btn_load_file")
        self.lbl_name_2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_name_2.setGeometry(QtCore.QRect(self.width_ratio*20, self.height_ratio*80, self.width_ratio*67, self.height_ratio*17))
        self.lbl_name_2.setObjectName("lbl_name_2")
        self.combo_filetype = QtWidgets.QComboBox(self.centralwidget)
        self.combo_filetype.setGeometry(QtCore.QRect(self.width_ratio*120, self.height_ratio*80, self.width_ratio*151, self.height_ratio*25))
        self.combo_filetype.setObjectName("combo_filetype")
        self.combo_filetype.addItems(FILE_TYPE)
        self.lbl_name_3 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_name_3.setGeometry(QtCore.QRect(self.width_ratio*300, self.height_ratio*80, self.width_ratio*111, self.height_ratio*17))
        self.lbl_name_3.setObjectName("lbl_name_3")
        self.combo_analysetype = QtWidgets.QComboBox(self.centralwidget)
        self.combo_analysetype.setGeometry(QtCore.QRect(self.width_ratio*420, self.height_ratio*80, self.width_ratio*171, self.height_ratio*25))
        self.combo_analysetype.setObjectName("combo_analysetype")
        self.combo_analysetype.addItems(ANALYSE_TYPE)
        self.groupBox_verification = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_verification.setGeometry(QtCore.QRect(self.width_ratio*20, self.height_ratio*120, self.width_ratio*571, self.height_ratio*91))
        self.groupBox_verification.setObjectName("groupBox_verification")
        self.lbl_name_4 = QtWidgets.QLabel(self.groupBox_verification)
        self.lbl_name_4.setGeometry(QtCore.QRect(self.width_ratio*10, self.height_ratio*30, self.width_ratio*81, self.height_ratio*17))
        self.lbl_name_4.setObjectName("lbl_name_4")
        self.lbl_name_5 = QtWidgets.QLabel(self.groupBox_verification)
        self.lbl_name_5.setGeometry(QtCore.QRect(self.width_ratio*10, self.height_ratio*60, self.width_ratio*81, self.height_ratio*17))
        self.lbl_name_5.setObjectName("lbl_name_5")
        self.txt_starttime = QtWidgets.QLineEdit(self.groupBox_verification)
        self.txt_starttime.setGeometry(QtCore.QRect(self.width_ratio*100, self.height_ratio*30, self.width_ratio*171, self.height_ratio*26))
        self.txt_starttime.setReadOnly(True)
        self.txt_starttime.setObjectName("txt_starttime")
        self.txt_endtime = QtWidgets.QLineEdit(self.groupBox_verification)
        self.txt_endtime.setGeometry(QtCore.QRect(self.width_ratio*390, self.height_ratio*30, self.width_ratio*171, self.height_ratio*26))
        self.txt_endtime.setReadOnly(True)
        self.txt_endtime.setObjectName("txt_endtime")
        self.lbl_name_6 = QtWidgets.QLabel(self.groupBox_verification)
        self.lbl_name_6.setGeometry(QtCore.QRect(self.width_ratio*300, self.height_ratio*30, self.width_ratio*71, self.height_ratio*17))
        self.lbl_name_6.setObjectName("lbl_name_6")
        self.txt_seriesdata = QtWidgets.QLineEdit(self.groupBox_verification)
        self.txt_seriesdata.setGeometry(QtCore.QRect(self.width_ratio*100, self.height_ratio*60, self.width_ratio*171, self.height_ratio*25))
        self.txt_seriesdata.setReadOnly(True)
        self.txt_seriesdata.setObjectName("txt_seriesdata")
        self.lbl_name_7 = QtWidgets.QLabel(self.groupBox_verification)
        self.lbl_name_7.setGeometry(QtCore.QRect(self.width_ratio*300, self.height_ratio*60, self.width_ratio*81, self.height_ratio*17))
        self.lbl_name_7.setObjectName("lbl_name_7")
        self.txt_emptydata = QtWidgets.QLineEdit(self.groupBox_verification)
        self.txt_emptydata.setGeometry(QtCore.QRect(self.width_ratio*390, self.height_ratio*60, self.width_ratio*171, self.height_ratio*25))
        self.txt_emptydata.setText("")
        self.txt_emptydata.setReadOnly(True)
        self.txt_emptydata.setObjectName("txt_emptydata")
        self.lbl_name_8 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_name_8.setGeometry(QtCore.QRect(self.width_ratio*20, self.height_ratio*230, self.width_ratio*67, self.height_ratio*17))
        self.lbl_name_8.setObjectName("lbl_name_8")
        self.txt_memo = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_memo.setGeometry(QtCore.QRect(self.width_ratio*20, self.height_ratio*250, self.width_ratio*571, self.height_ratio*101))
        self.txt_memo.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txt_memo.setObjectName("txt_memo")
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(self.width_ratio*20, self.height_ratio*370, self.width_ratio*141, self.height_ratio*25))
        self.btn_back.setObjectName("btn_back")
        self.btn_addanother = QtWidgets.QPushButton(self.centralwidget)
        self.btn_addanother.setGeometry(QtCore.QRect(self.width_ratio*230, self.height_ratio*370, self.width_ratio*141, self.height_ratio*25))
        self.btn_addanother.setObjectName("btn_addanother")
        self.btn_saveAndReturn = QtWidgets.QPushButton(self.centralwidget)
        self.btn_saveAndReturn.setGeometry(QtCore.QRect(self.width_ratio*430, self.height_ratio*370, self.width_ratio*161, self.height_ratio*25))
        self.btn_saveAndReturn.setObjectName("btn_saveAndReturn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, self.width_ratio*644, self.height_ratio*22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusBar)
        self.modify = False
        self.btn_load_file.clicked.connect(self.btn_load_file_clicked)
        self.btn_back.clicked.connect(self.btn_back_clicked)
        self.btn_addanother.clicked.connect(self.btn_addanother_clicked)
        self.btn_saveAndReturn.clicked.connect(self.btn_saveAndReturn_clicked)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        """
                            Set the properties of the UI elements
        :param MainWindow:
        """
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
        """
                                    LOAD SOURCE FILE AND CALCULATE RELATED FIELDS
        """
        try:
            file_dailog = QtWidgets.QFileDialog(self.temp_window)
            file_path = file_dailog.getOpenFileName(self.temp_window, filter="Docs (*.csv *.xls)")[0]
            from utils.path_utils import copy_file
            import pandas as pd

            df = pd.read_excel(file_path, header=None, usecols=[0, 1])
            empty_data = 0
            for time, data in df.get_values():
                if pd.isnull(data):
                    empty_data += 1
            self.txt_emptydata.setText(str(empty_data))
            self.txt_seriesdata.setText(str(df.__len__() - empty_data))
            self.txt_starttime.setText(str(df[0].min()))
            self.txt_endtime.setText(str(df[0].max()))
            self.source_file = copy_file(source = file_path, dest="source_file")
        except Exception as ex:
            QtWidgets.QMessageBox.about(self.temp_window, "Error", "Select a proper source file")

    def btn_back_clicked(self):
        """
                        Close the current window and show Time-series window
        """
        self.temp_window.parent_win.show()
        self.temp_window.hide()

    def btn_addanother_clicked(self):
        """
                    Save the time series and clear all values from the fields of the window
        """
        saved = self.save_timeseries()
        if saved:
            self.clear_window()

    def btn_saveAndReturn_clicked(self):
        """
                    Save the time-series, close the current window and show Time-series window
        """
        saved = self.save_timeseries()
        if saved:
            self.temp_window.parent_win.parent_win.show()
            self.temp_window.hide()

    def save_timeseries(self):
        """
                      Save the time-series in the database ( Create or update the time-series record)
        :return: Status i.e, time-series is saved or not
        """
        from utils.database_utils import DatabaseConnect
        from utils.time_utils import unix_time_millis  # Function to convert the time from datetime to milliseconds
        db = DatabaseConnect()
        analyse_type = self.combo_analysetype.currentText()
        name = self.txt_name.text().strip()
        try:
            start_time = unix_time_millis(self.txt_starttime.text())
            end_time = unix_time_millis(self.txt_endtime.text())
        except ValueError:
            start_time = None
            end_time = None
        series_data = self.txt_seriesdata.text()
        empty_data = self.txt_emptydata.text()
        file_type = self.combo_filetype.currentText()
        memo = self.txt_memo.toPlainText()

        if name and start_time and end_time and end_time and series_data and empty_data:
            if self.modify:
                id = db.update_timeseries(product_id=self.selected_productId, timeseries_id=self.selected_timeseriesId,
                                          analyse_type=analyse_type, description=memo, empty_data=empty_data,
                                          end_time=end_time, file_type=file_type, name=name, series_data=series_data,
                                          start_time=start_time, source_file=self.source_file, window=self.temp_window)
            else:
                id = db.save_timeseries(analyse_type=analyse_type, description=memo, empty_data=empty_data, end_time=end_time,
                                        file_type=file_type, name=name, series_data=series_data, start_time=start_time,
                                        source_file=self.source_file, window=self.temp_window)
            if id:
                self.temp_window.parent_win.ui.timeseries_list_view()
                QtWidgets.QMessageBox.about(self.temp_window, "Info", "Record Saved Successfully !!!")
                return True
        else:
            if not name:
                self.txt_name.setText("")
                self.txt_name.setFocus()
            elif not start_time or not end_time or not series_data or not empty_data:
                QtWidgets.QMessageBox.about(self.temp_window, "Info", "Upload a proper source file!!!")
            return False

    def clear_window(self):
        """
                                CLEAR ALL THE FIELDS VALUES FROM TIME_SERIES WINDOW
        """
        self.txt_memo.clear()
        self.combo_filetype.setCurrentText(FILE_TYPE[0])
        self.combo_analysetype.setCurrentText(ANALYSE_TYPE[0])
        self.txt_emptydata.clear()
        self.txt_seriesdata.clear()
        self.txt_endtime.clear()
        self.txt_starttime.clear()
        self.txt_name.clear()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

