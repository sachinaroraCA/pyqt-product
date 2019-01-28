from PyQt5 import QtCore, QtWidgets


class AnalysisWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(AnalysisWindow, self).__init__(parent)
        self.setWindowTitle("Financial Product Analysis Tool - Analysis")
        self.ui = Ui_MainWindow(self)
        self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, True)
        self.setWindowState(QtCore.Qt.WindowMaximized)

class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        from utils.window_utils import get_resolution_ratio
        self.width_ratio, self.height_ratio = get_resolution_ratio(600, 550)
        MainWindow.setMinimumHeight(self.height_ratio*550)
        MainWindow.setMinimumWidth(self.width_ratio*600)
        self.temp_window = MainWindow
        self.selected_timeseriesId = None
        self.layout = {}
        self.index_values_layout = {}
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_timeseries = QtWidgets.QLabel(self.centralwidget)
        self.lbl_timeseries.setGeometry(QtCore.QRect(self.width_ratio*30, self.height_ratio*10, self.width_ratio*101, self.height_ratio*17))
        self.lbl_timeseries.setObjectName("lbl_timeseries")
        self.scrollArea_timeseries = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_timeseries.setGeometry(QtCore.QRect(self.width_ratio*30, self.height_ratio*60, self.width_ratio*329, self.height_ratio*101))
        self.scrollArea_timeseries.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_timeseries.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_timeseries.setWidgetResizable(True)
        self.scrollArea_timeseries.setObjectName("scrollArea_timeseries")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, self.width_ratio*313, self.height_ratio*99))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.scrollArea_timeseries.setWidget(self.scrollAreaWidgetContents_3)
        self.groupBox_timeseries = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_timeseries.setGeometry(QtCore.QRect(self.width_ratio*400, self.height_ratio*10, self.width_ratio*161, self.height_ratio*151))
        self.groupBox_timeseries.setTitle("")
        self.groupBox_timeseries.setObjectName("groupBox_timeseries")

        self.btn_analyse = QtWidgets.QPushButton(self.groupBox_timeseries)
        self.btn_analyse.setGeometry(QtCore.QRect(self.width_ratio*20, self.height_ratio*30, self.width_ratio*121, self.height_ratio*25))
        self.btn_analyse.setObjectName("btn_analyse")
        self.btn_export = QtWidgets.QPushButton(self.groupBox_timeseries)
        self.btn_export.setGeometry(QtCore.QRect(self.width_ratio*20, self.height_ratio*70, self.width_ratio*121, self.height_ratio*25))
        self.btn_export.setObjectName("btn_export")
        self.btn_return = QtWidgets.QPushButton(self.groupBox_timeseries)
        self.btn_return.setGeometry(QtCore.QRect(self.width_ratio*20, self.height_ratio*110, self.width_ratio*121, self.height_ratio*25))
        self.btn_return.setObjectName("btn_return_2")
        self.txt_timeseries = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_timeseries.setGeometry(QtCore.QRect(self.width_ratio*30, self.height_ratio*30, self.width_ratio*329, self.height_ratio*25))
        self.txt_timeseries.setObjectName("txt_timeseries")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(self.width_ratio*30, self.height_ratio*170, self.width_ratio*531, self.height_ratio*350))
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName("tabWidget")

        for index in range(1, 11):

            self.tab_index = QtWidgets.QWidget()
            self.tab_index.setObjectName("tab_index"+str(index))
            self.tabWidget.addTab(self.tab_index, "index"+str(index))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, self.width_ratio*615, self.height_ratio*22))
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
        self.statusbar.showMessage("Analysing " + self.selected_timeseries + "...")
        from utils.database_utils import DatabaseConnect
        db = DatabaseConnect()
        self.time_series_data = db.get_timeseries_details(timeseries_id= self.selected_timeseriesId, window=self.temp_window)
        self.analysed_data = []
        if "source_file" in self.time_series_data.keys() and self.time_series_data["source_file"]:
            import os
            if os.path.exists(self.time_series_data["source_file"]):
                for index in range(1, 11):
                    self.create_graph(source_file=self.time_series_data["source_file"],
                                      time_series_type=self.time_series_data["file_type"],
                                      index=index)
                    self.show_graph(show=True)
                    self.statusbar.showMessage("", 1)
            else:
                QtWidgets.QMessageBox.about(self.temp_window, "Info", "Invalid source file !!!")

        else:
            QtWidgets.QMessageBox.about(self.temp_window, "Info", "No source file found !!!" )

    def btn_export_clicked(self):
        try:

            import pandas as pd
            if self.analysed_data:
                from utils.window_utils import export_file
                self.statusbar.showMessage("Exporting " + self.selected_timeseries + "...")
                export_file(window=self.temp_window, export_data=self.analysed_data)
                self.statusbar.showMessage("", 1)
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
                    lbl_index.setMinimumWidth(80)

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
            if str(filter_text.lower()) in str(item.lower()):
                listitem = QtWidgets.QListWidgetItem()
                listitem.setText(item)
                listitem.setData(1, self.timeseriesId_list[index])
                self.timeseries_listWidget.addItem(listitem)
            index += 1
        self.scrollArea_timeseries.setWidget(self.timeseries_listWidget)

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
