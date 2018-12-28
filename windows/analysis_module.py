from PyQt5 import QtCore, QtWidgets


class AnalysisWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(AnalysisWindow, self).__init__(parent)
        self.setWindowTitle("Financial Product Analysis Tool - Analysis")
        self.ui = Ui_MainWindow(self)


class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedHeight(550)
        MainWindow.setFixedWidth(600)
        self.temp_window = MainWindow
        self.selected_timeseriesId = None
        self.layout = {}
        self.index_values_layout = {}
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_timeseries = QtWidgets.QLabel(self.centralwidget)
        self.lbl_timeseries.setGeometry(QtCore.QRect(30, 10, 101, 17))
        self.lbl_timeseries.setObjectName("lbl_timeseries")
        self.scrollArea_timeseries = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_timeseries.setGeometry(QtCore.QRect(30, 60, 329, 101))
        self.scrollArea_timeseries.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
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
        self.btn_return = QtWidgets.QPushButton(self.groupBox_timeseries)
        self.btn_return.setGeometry(QtCore.QRect(20, 110, 121, 25))
        self.btn_return.setObjectName("btn_return_2")
        self.txt_timeseries = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_timeseries.setGeometry(QtCore.QRect(30, 30, 329, 25))
        self.txt_timeseries.setObjectName("txt_timeseries")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 170, 531, 350))
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName("tabWidget")
        for index in range(1, 11):
            self.tab_index = QtWidgets.QWidget()
            self.tab_index.setObjectName("tab_index"+str(index))
            self.tabWidget.addTab(self.tab_index, "index"+str(index))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 615, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.timeseries_list_view()
        self.txt_timeseries.textChanged.connect(self.timeseriesfilterClicked)
        self.btn_analyse.clicked.connect(self.btn_analyse_clicked)
        self.btn_export.clicked.connect(self.btn_export_clicked)
        self.btn_return.clicked.connect(self.btn_return_clicked)
        self.btn_analyse.setDisabled(True)
        self.btn_export.setDisabled(True)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.show_graph(show=False)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Financial Product Analysis Tool - Analysis"))
        self.lbl_timeseries.setText(_translate("MainWindow", "Time Series :"))
        self.btn_analyse.setText(_translate("MainWindow", "Analyse"))
        self.btn_export.setText(_translate("MainWindow", "Export"))
        self.btn_return.setText(_translate("MainWindow", "Return"))
        self.txt_timeseries.setPlaceholderText(_translate("MainWindow", " Search"))

    def btn_analyse_clicked(self):
        from utils.database_utils import DatabaseConnect
        db = DatabaseConnect()
        self.show_graph(show=True)
        self.time_series_data = db.get_timeseries_details(timeseries_id= self.selected_timeseriesId,
                                                          window=self.temp_window)
        self.analysed_data = []
        for index in range(1, 11):
            self.create_graph(source_file=self.time_series_data["source_file"],
                              time_series_type=self.time_series_data["file_type"],
                              index=index)

    def btn_export_clicked(self):
        try:
            import pandas as pd
            if self.analysed_data:

                file_dailog = QtWidgets.QFileDialog()
                default_file_extension = '.csv'

                name = file_dailog.getSaveFileName(self.temp_window, 'Save File')[0]
                if name:
                    if default_file_extension not in name:
                        name += default_file_extension

                    df = pd.DataFrame(self.analysed_data)
                    df.to_csv(name, sep='\t', encoding='utf-8', index=False,
                              columns=['index', "sub_index", "standard_value", "analysed_value"])
                    QtWidgets.QMessageBox.about(self.temp_window, "info", "Exported data successfully !!!")
        except Exception as ex:
            QtWidgets.QMessageBox.about(self.temp_window, "Error", str(ex))

    def btn_return_clicked(self):
        self.temp_window.hide()

    def create_graph(self, source_file, time_series_type, index):
        from utils.algo_utils import analyse_module

        # Todo: algorithm is to be write for 2-9 index
        analysis_data = analyse_module(source_file=source_file,
                                       time_series_type=time_series_type,
                                       index=index
                                       )
        import pyqtgraph as pg
        import numpy as np
        standard_values = [float(value) for value in list(self.get_analysis_data(index, self.time_series_data["analyse_type"]).values())]
        x = np.arange(1, 13)
        y = np.array([list(analysis_data.values()),
                      standard_values,
                      ])
        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')
        plot_widget = pg.PlotWidget()

        colors = ['r', 'b' ]
        for i in range(2):
            curve = pg.PlotCurveItem(x, y[i], pen=colors[i])
            plot_widget.addItem(curve)

        tab_list = self.tabWidget.children()[0].children()
        for tab in tab_list:
            tab_name = tab.objectName()

            if tab_name == "tab_index"+str(index):

                if tab_name not in self.layout:
                    self.layout[tab_name] = QtWidgets.QHBoxLayout()

                if tab_name not in self.index_values_layout:
                    self.index_values_layout[tab_name] = QtWidgets.QVBoxLayout()

                if self.layout[tab_name]:
                    for i in reversed(range(self.layout[tab_name].count())):
                        if self.layout[tab_name].itemAt(i).widget() is not None:
                            self.layout[tab_name].itemAt(i).widget().setParent(None)

                self.deleteItemsOfLayout(self.layout[tab_name])

                for sub_index in range(12):
                    binding_layout = QtWidgets.QHBoxLayout()
                    lbl_index = QtWidgets.QLabel()
                    lbl_index.setText("index" + str(index) + "-" + str(sub_index + 1)+":")
                    lbl_index.setMinimumWidth(70)

                    binding_layout.addWidget(lbl_index)
                    txt_index = QtWidgets.QLineEdit()
                    txt_index.setMinimumWidth(90)
                    txt_index.setReadOnly(True)
                    value = analysis_data[sub_index + 1]
                    txt_index.setText(str(value))
                    binding_layout.addWidget(txt_index)
                    self.analysed_data.append({"index": index,
                                               "sub_index": sub_index+1,
                                               "analysed_value": analysis_data[sub_index+1],
                                               "standard_value": standard_values[sub_index]})

                    self.index_values_layout[tab_name].addLayout(binding_layout)
                self.layout[tab_name].addLayout(self.index_values_layout[tab_name])

                index_title = QtWidgets.QLabel()
                index_title.setStyleSheet("font: 16pt;color:#605252;")
                index_title.setText(str("        "+self.selected_timeseries + "-index" + str(index)).title())

                b_layout = QtWidgets.QVBoxLayout()
                b_layout.addWidget(index_title)
                b_layout.addWidget(plot_widget)

                from utils.graph_utils import create_graph_indicator
                create_graph_indicator(b_layout, self.selected_timeseries, True)

                self.layout[tab_name].addLayout(b_layout)
                tab.setLayout(self.layout[tab_name])

    def get_analysis_data(self, index, analyse_type):
        from utils.database_utils import DatabaseConnect
        db = DatabaseConnect()
        analysis_dict = db.get_index_analysis(index=index,
                                              analyse_type=analyse_type,
                                              window=self.temp_window)
        return analysis_dict

    def deleteItemsOfLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)
                else:
                    self.deleteItemsOfLayout(item.layout())

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                                Time-Series PART
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def timeseries_list_view(self):
        from utils.database_utils import DatabaseConnect
        db = DatabaseConnect()
        self.timeseries_list, self.timeseriesId_list = db.get_timeserieses(window=self.temp_window)
        self.timeseries_listWidget = QtWidgets.QListWidget()
        index = 0
        for item in self.timeseriesId_list:
            listitem = QtWidgets.QListWidgetItem()
            listitem.setText(self.timeseries_list[index])
            listitem.setData(1, item)
            index += 1
            self.timeseries_listWidget.addItem(listitem)
        self.timeseries_listWidget.currentItemChanged.connect(self.timeseries_list_item_event)
        self.scrollArea_timeseries.setWidget(self.timeseries_listWidget)

    def timeseries_list_item_event(self, item):
        try:
            if item:
                self.selected_timeseries = item.text()
                self.selected_timeseriesId = item.data(1)
                self.btn_analyse.setEnabled(True)
                self.btn_export.setEnabled(True)
                self.show_graph(show=False)
        except:
            pass

    def show_graph(self, show):
        if not show:
            self.tabWidget.children()[1].hide()
            self.tabWidget.children()[0].hide()
        else:
            self.tabWidget.children()[1].show()
            self.tabWidget.children()[0].show()

    def timeseriesfilterClicked(self):
        filter_text = str(self.txt_timeseries.text()).lower()
        self.timeseries_listWidget.clear()
        index = 0
        for item in self.timeseries_list:
            if item.lower().startswith(filter_text.lower()):
                listitem = QtWidgets.QListWidgetItem()
                listitem.setText(item)
                listitem.setData(1, self.timeseriesId_list[index])
                self.timeseries_listWidget.addItem(listitem)
            index += 1
        self.scrollArea_timeseries.setWidget(self.timeseries_listWidget)

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
