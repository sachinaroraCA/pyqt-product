from PyQt5 import QtCore, QtGui, QtWidgets

# Dummy data for prediction pe1 tp pe16
PREDICTION_DATA = {"PE1": "PE1", "PE2": "PE2", "PE3": "PE3", "PE4": "PE4", "PE5": "PE5", "PE6": "PE6", "PE7": "PE7",
                   "PE8": "PE8", "PE9": "PE9", "PE10": "PE10", "PE11": "PE11", "PE12": "PE12", "PE13": "PE13",
                   "PE14": "PE14", "PE15": "PE15", "PE16": "PE16"}


class PredictionWindow(QtWidgets.QMainWindow):
    """
                Main class of the Prediction module
    """
    def __init__(self, parent=None):
        super(PredictionWindow, self).__init__(parent)
        self.setWindowTitle("Financial Product Analysis Tool - Prediction")
        self.ui = Ui_MainWindow(self)


class Ui_MainWindow(object):
    """
                UI class of the Prediction module
    """
    def __init__(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedHeight(565)
        MainWindow.setFixedWidth(700)
        self.temp_window = MainWindow
        self.selected_timeseries = None
        self.selected_model = None
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 50, 311, 141))
        self.groupBox.setObjectName("groupBox")
        self.txt_timeseries = QtWidgets.QLineEdit(self.groupBox)
        self.txt_timeseries.setGeometry(QtCore.QRect(0, 20, 311, 25))
        self.txt_timeseries.setObjectName("txt_timeseries")
        self.listWidget_timeseries = QtWidgets.QListWidget(self.groupBox)
        self.listWidget_timeseries.setGeometry(QtCore.QRect(-5, 50, 311, 91))
        self.listWidget_timeseries.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listWidget_timeseries.setObjectName("listWidget_timeseries")

        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(350, 50, 311, 141))
        self.groupBox_4.setObjectName("groupBox_4")
        self.txt_model = QtWidgets.QLineEdit(self.groupBox_4)
        self.txt_model.setGeometry(QtCore.QRect(0, 20, 311, 25))
        self.txt_model.setObjectName("txt_model")
        self.listWidget_model = QtWidgets.QListWidget(self.groupBox_4)
        self.listWidget_model.setGeometry(QtCore.QRect(-5, 50, 311, 91))
        self.listWidget_model.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listWidget_model.setObjectName("listWidget_model")

        self.groupBox_prediction_parameter = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_prediction_parameter.setGeometry(QtCore.QRect(30, 210, 601, 61))
        self.groupBox_prediction_parameter.setObjectName("groupBox_prediction_parameter")
        self.label_4 = QtWidgets.QLabel(self.groupBox_prediction_parameter)
        self.label_4.setGeometry(QtCore.QRect(10, 30, 81, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_prediction_parameter)
        self.label_5.setGeometry(QtCore.QRect(200, 30, 81, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_prediction_parameter)
        self.label_6.setGeometry(QtCore.QRect(400, 30, 81, 17))
        self.label_6.setObjectName("label_6")
        self.txt_param1 = QtWidgets.QLineEdit(self.groupBox_prediction_parameter)
        self.txt_param1.setGeometry(QtCore.QRect(90, 30, 101, 25))
        self.txt_param1.setReadOnly(True)
        self.txt_param1.setObjectName("txt_param1")
        self.txt_param2 = QtWidgets.QLineEdit(self.groupBox_prediction_parameter)
        self.txt_param2.setGeometry(QtCore.QRect(280, 30, 101, 25))
        self.txt_param2.setReadOnly(True)
        self.txt_param2.setObjectName("txt_param2")
        self.txt_param3 = QtWidgets.QLineEdit(self.groupBox_prediction_parameter)
        self.txt_param3.setGeometry(QtCore.QRect(482, 30, 111, 25))
        self.txt_param3.setReadOnly(True)
        self.txt_param3.setObjectName("txt_param3")

        self.btn_evaluate_prediction = QtWidgets.QPushButton(self.centralwidget)
        self.btn_evaluate_prediction.setGeometry(QtCore.QRect(30, 300, 291, 25))
        self.btn_evaluate_prediction.setObjectName("btn_evaluate_prediction")
        self.btn_export_prediction = QtWidgets.QPushButton(self.centralwidget)
        self.btn_export_prediction.setGeometry(QtCore.QRect(340, 300, 291, 25))
        self.btn_export_prediction.setObjectName("btn_export_prediction")
        self.btn_return = QtWidgets.QPushButton(self.centralwidget)
        self.btn_return.setGeometry(QtCore.QRect(480, 490, 151, 25))
        self.btn_return.setObjectName("btn_return")

        self.groupBox_model_evaluation = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_model_evaluation.setGeometry(QtCore.QRect(30, 330, 601, 151))
        self.groupBox_model_evaluation.setObjectName("groupBox_model_evaluation")

        self.txt_pe1 = QtWidgets.QLineEdit(self.groupBox_model_evaluation)
        self.txt_pe1.setGeometry(QtCore.QRect(60, 30, 71, 25))
        self.txt_pe1.setReadOnly(True)
        self.txt_pe1.setObjectName("txt_pe1")

        self.txt_pe2 = QtWidgets.QLineEdit(self.groupBox_model_evaluation)
        self.txt_pe2.setGeometry(QtCore.QRect(60, 60, 71, 25))
        self.txt_pe2.setReadOnly(True)
        self.txt_pe2.setObjectName("txt_pe2")

        self.txt_pe3 = QtWidgets.QLineEdit(self.groupBox_model_evaluation)
        self.txt_pe3.setGeometry(QtCore.QRect(60, 90, 71, 25))
        self.txt_pe3.setReadOnly(True)
        self.txt_pe3.setObjectName("txt_pe3")

        self.txt_pe4 = QtWidgets.QLineEdit(self.groupBox_model_evaluation)
        self.txt_pe4.setGeometry(QtCore.QRect(60, 120, 71, 25))
        self.txt_pe4.setReadOnly(True)
        self.txt_pe4.setObjectName("txt_pe4")

        self.txt_pe5 = QtWidgets.QLineEdit(self.groupBox_model_evaluation)
        self.txt_pe5.setGeometry(QtCore.QRect(210, 30, 71, 25))
        self.txt_pe5.setReadOnly(True)
        self.txt_pe5.setObjectName("txt_pe5")

        self.txt_pe6 = QtWidgets.QLineEdit(self.groupBox_model_evaluation)
        self.txt_pe6.setGeometry(QtCore.QRect(210, 60, 71, 25))
        self.txt_pe6.setReadOnly(True)
        self.txt_pe6.setObjectName("txt_pe6")

        self.txt_pe7 = QtWidgets.QLineEdit(self.groupBox_model_evaluation)
        self.txt_pe7.setGeometry(QtCore.QRect(210, 90, 71, 25))
        self.txt_pe7.setReadOnly(True)
        self.txt_pe7.setObjectName("txt_pe7")

        self.txt_pe8 = QtWidgets.QLineEdit(self.groupBox_model_evaluation)
        self.txt_pe8.setGeometry(QtCore.QRect(210, 120, 71, 25))
        self.txt_pe8.setReadOnly(True)
        self.txt_pe8.setObjectName("txt_pe8")

        self.txt_pe9 = QtWidgets.QLineEdit(self.groupBox_model_evaluation)
        self.txt_pe9.setGeometry(QtCore.QRect(360, 30, 71, 25))
        self.txt_pe9.setReadOnly(True)
        self.txt_pe9.setObjectName("txt_pe9")

        self.txt_pe10 = QtWidgets.QLineEdit(self.groupBox_model_evaluation)
        self.txt_pe10.setGeometry(QtCore.QRect(360, 60, 71, 25))
        self.txt_pe10.setReadOnly(True)
        self.txt_pe10.setObjectName("txt_pe10")

        self.txt_pe11 = QtWidgets.QLineEdit(self.groupBox_model_evaluation)
        self.txt_pe11.setGeometry(QtCore.QRect(360, 90, 71, 25))
        self.txt_pe11.setReadOnly(True)
        self.txt_pe11.setObjectName("txt_pe11")

        self.txt_pe12 = QtWidgets.QLineEdit(self.groupBox_model_evaluation)
        self.txt_pe12.setGeometry(QtCore.QRect(360, 120, 71, 25))
        self.txt_pe12.setReadOnly(True)
        self.txt_pe12.setObjectName("txt_pe12")

        self.txt_pe13 = QtWidgets.QLineEdit(self.groupBox_model_evaluation)
        self.txt_pe13.setGeometry(QtCore.QRect(510, 30, 71, 25))
        self.txt_pe13.setReadOnly(True)
        self.txt_pe13.setObjectName("txt_pe13")

        self.txt_pe14 = QtWidgets.QLineEdit(self.groupBox_model_evaluation)
        self.txt_pe14.setGeometry(QtCore.QRect(510, 60, 71, 25))
        self.txt_pe14.setReadOnly(True)
        self.txt_pe14.setObjectName("txt_pe14")

        self.txt_pe15 = QtWidgets.QLineEdit(self.groupBox_model_evaluation)
        self.txt_pe15.setGeometry(QtCore.QRect(510, 90, 71, 25))
        self.txt_pe15.setReadOnly(True)
        self.txt_pe15.setObjectName("txt_pe15")

        self.txt_pe16 = QtWidgets.QLineEdit(self.groupBox_model_evaluation)
        self.txt_pe16.setGeometry(QtCore.QRect(510, 120, 71, 25))
        self.txt_pe16.setReadOnly(True)
        self.txt_pe16.setObjectName("txt_pe16")

        self.label_10 = QtWidgets.QLabel(self.groupBox_model_evaluation)
        self.label_10.setGeometry(QtCore.QRect(20, 120, 41, 17))
        self.label_10.setObjectName("label_10")

        self.label_13 = QtWidgets.QLabel(self.groupBox_model_evaluation)
        self.label_13.setGeometry(QtCore.QRect(170, 120, 41, 17))
        self.label_13.setObjectName("label_13")

        self.label_9 = QtWidgets.QLabel(self.groupBox_model_evaluation)
        self.label_9.setGeometry(QtCore.QRect(20, 90, 41, 17))
        self.label_9.setObjectName("label_9")
        self.label_14 = QtWidgets.QLabel(self.groupBox_model_evaluation)
        self.label_14.setGeometry(QtCore.QRect(170, 90, 41, 17))
        self.label_14.setObjectName("label_14")
        self.label_11 = QtWidgets.QLabel(self.groupBox_model_evaluation)
        self.label_11.setGeometry(QtCore.QRect(170, 60, 41, 17))
        self.label_11.setObjectName("label_11")
        self.label_7 = QtWidgets.QLabel(self.groupBox_model_evaluation)
        self.label_7.setGeometry(QtCore.QRect(20, 30, 41, 17))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_model_evaluation)
        self.label_8.setGeometry(QtCore.QRect(20, 60, 41, 17))
        self.label_8.setObjectName("label_8")



        self.label_12 = QtWidgets.QLabel(self.groupBox_model_evaluation)
        self.label_12.setGeometry(QtCore.QRect(170, 30, 41, 17))
        self.label_12.setObjectName("label_12")
        self.label_15 = QtWidgets.QLabel(self.groupBox_model_evaluation)
        self.label_15.setGeometry(QtCore.QRect(310, 60, 41, 17))
        self.label_15.setObjectName("label_15")
        self.label_17 = QtWidgets.QLabel(self.groupBox_model_evaluation)
        self.label_17.setGeometry(QtCore.QRect(310, 120, 41, 17))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.groupBox_model_evaluation)
        self.label_18.setGeometry(QtCore.QRect(310, 90, 41, 17))
        self.label_18.setObjectName("label_18")
        self.label_16 = QtWidgets.QLabel(self.groupBox_model_evaluation)
        self.label_16.setGeometry(QtCore.QRect(310, 30, 41, 17))
        self.label_16.setObjectName("label_16")
        self.label_20 = QtWidgets.QLabel(self.groupBox_model_evaluation)
        self.label_20.setGeometry(QtCore.QRect(460, 30, 41, 17))
        self.label_20.setObjectName("label_20")
        self.label_22 = QtWidgets.QLabel(self.groupBox_model_evaluation)
        self.label_22.setGeometry(QtCore.QRect(460, 90, 41, 17))
        self.label_22.setObjectName("label_22")
        self.label_21 = QtWidgets.QLabel(self.groupBox_model_evaluation)
        self.label_21.setGeometry(QtCore.QRect(460, 120, 41, 17))
        self.label_21.setObjectName("label_21")
        self.label_19 = QtWidgets.QLabel(self.groupBox_model_evaluation)
        self.label_19.setGeometry(QtCore.QRect(460, 60, 41, 17))
        self.label_19.setObjectName("label_19")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 692, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.timeseries_list_view()
        self.models_list_view()

        self.txt_timeseries.textChanged.connect(self.timeseriesfilterClicked)
        self.txt_model.textChanged.connect(self.search_models)
        self.btn_return.clicked.connect(self.btn_return_clicked)
        self.btn_evaluate_prediction.clicked.connect(self.btn_evaluate_prediction_clicked)
        self.btn_export_prediction.clicked.connect(self.btn_export_prediction_clicked)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        """
                Set the properties of the UI elements
        :param MainWindow:
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Time Series to be predicted : "))
        self.txt_timeseries.setPlaceholderText(_translate("MainWindow", "  Search"))
        self.groupBox_prediction_parameter.setTitle(_translate("MainWindow", "Prediction Parameters :"))
        self.label_4.setText(_translate("MainWindow", "PARAM. 1 : "))
        self.label_5.setText(_translate("MainWindow", "PARAM. 2 : "))
        self.label_6.setText(_translate("MainWindow", "PARAM. 3 : "))
        self.btn_evaluate_prediction.setText(_translate("MainWindow", "Evaluate Prediction"))
        self.btn_export_prediction.setText(_translate("MainWindow", "Export Prediction Data"))
        self.btn_return.setText(_translate("MainWindow", "Return"))
        self.groupBox_model_evaluation.setTitle(_translate("MainWindow", "Model Evaluation"))
        self.label_10.setText(_translate("MainWindow", "PE4:"))
        self.label_13.setText(_translate("MainWindow", "PE8:"))
        self.label_9.setText(_translate("MainWindow", "PE3:"))
        self.label_14.setText(_translate("MainWindow", "PE7:"))
        self.label_11.setText(_translate("MainWindow", "PE6:"))
        self.label_7.setText(_translate("MainWindow", "PE1:"))
        self.label_8.setText(_translate("MainWindow", "PE2:"))
        self.label_12.setText(_translate("MainWindow", "PE5:"))
        self.label_15.setText(_translate("MainWindow", "PE10:"))
        self.label_17.setText(_translate("MainWindow", "PE12:"))
        self.label_18.setText(_translate("MainWindow", "PE11:"))
        self.label_16.setText(_translate("MainWindow", "PE9:"))
        self.label_20.setText(_translate("MainWindow", "PE13:"))
        self.label_22.setText(_translate("MainWindow", "PE15:"))
        self.label_21.setText(_translate("MainWindow", "PE16:"))
        self.label_19.setText(_translate("MainWindow", "PE14:"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Basing on Model : "))
        self.txt_model.setPlaceholderText(_translate("MainWindow", "  Search"))

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                                Events PART
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def btn_export_prediction_clicked(self):
        """
                    Export the Prediction data as a CSV file
        """
        try:
            prediction_data = ({"Time Series": self.selected_timeseries,
                                "Model": self.selected_model,
                                "Param 1": self.param_one.text(),
                                "Param 2": self.param_two.text(),
                                "Param 3": self.param_three.text()})
            prediction_data.update(PREDICTION_DATA)

            file_dailog = QtWidgets.QFileDialog()
            default_file_extension = '.csv'

            name = file_dailog.getSaveFileName(self.temp_window, 'Save File')[0]
            if name:
                if default_file_extension not in name:
                    name += default_file_extension

                keys = list(prediction_data.keys())
                import csv
                with open(name, 'w+') as output_file:
                    dict_writer = csv.DictWriter(output_file, keys)
                    dict_writer.writeheader()
                    dict_writer.writerow(prediction_data)

                output_file.close()
                QtWidgets.QMessageBox.about(self.temp_window, "info", "Exported data successfully !!!")
        except Exception as ex:
            QtWidgets.QMessageBox.about(self.temp_window, "Error", str(ex))

    def btn_evaluate_prediction_clicked(self):
        """
                Set the dummy data into inlineEdit pe1 to pe16
                Todo: Write an algorithm for Prediction
        """
        if self.selected_model and self.selected_timeseries:
            self.param_one = self.txt_param1
            self.param_two = self.txt_param2
            self.param_three = self.txt_param3
            self.txt_pe1.setText(PREDICTION_DATA["PE1"])
            self.txt_pe2.setText(PREDICTION_DATA["PE2"])
            self.txt_pe3.setText(PREDICTION_DATA["PE3"])
            self.txt_pe4.setText(PREDICTION_DATA["PE4"])
            self.txt_pe5.setText(PREDICTION_DATA["PE5"])
            self.txt_pe6.setText(PREDICTION_DATA["PE6"])
            self.txt_pe7.setText(PREDICTION_DATA["PE7"])
            self.txt_pe8.setText(PREDICTION_DATA["PE8"])
            self.txt_pe9.setText(PREDICTION_DATA["PE9"])
            self.txt_pe10.setText(PREDICTION_DATA["PE10"])
            self.txt_pe11.setText(PREDICTION_DATA["PE11"])
            self.txt_pe12.setText(PREDICTION_DATA["PE12"])
            self.txt_pe13.setText(PREDICTION_DATA["PE13"])
            self.txt_pe14.setText(PREDICTION_DATA["PE14"])
            self.txt_pe15.setText(PREDICTION_DATA["PE15"])
            self.txt_pe16.setText(PREDICTION_DATA["PE16"])
        else:
            QtWidgets.QMessageBox.about(self.temp_window, "message",
                                        "Select a model and a time-series !!!")

    def btn_return_clicked(self):
        """
                    Close current window
        """
        buttonReply = QtWidgets.QMessageBox.question(self.temp_window, "message",
                                       "Do you want to export prediction data?",
                                                         QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                         QtWidgets.QMessageBox.No)
        if buttonReply == QtWidgets.QMessageBox.Yes:
            self.btn_evaluate_prediction_clicked()
        self.temp_window.hide()

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                                Time-Series PART
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def timeseries_list_view(self):
        """
                 creates the items of list widget to display the list of Time-series on the window
        """
        from utils.database_utils import DatabaseConnect
        db = DatabaseConnect()
        self.timeseries_list, self.timeseriesId_list = db.get_timeserieses(window=self.temp_window)
        self.listWidget_timeseries.clear()
        index = 0
        for item in self.timeseriesId_list:
            listitem = QtWidgets.QListWidgetItem()
            listitem.setText(self.timeseries_list[index])
            listitem.setData(1, item)
            index += 1
            self.listWidget_timeseries.addItem(listitem)
        self.listWidget_timeseries.itemClicked.connect(self.timeseries_list_item_event)

    def timeseries_list_item_event(self, item):
        """
                set the currently selected time-series for the window with its availability to bind or unbind
        :param item:
        """
        self.selected_timeseries = item.text()
        self.selected_timeseriesId = item.data(1)

    def timeseriesfilterClicked(self):
        """
                Filter the time-series from the time-series list as per the text entered in txt_timeseries
        """
        filter_text = str(self.txt_timeseries.text()).lower()
        self.listWidget_timeseries.clear()
        index = 0
        for item in self.timeseries_list:
            if item.lower().startswith(filter_text.lower()):
                listitem = QtWidgets.QListWidgetItem()
                listitem.setText(item)
                listitem.setData(1, self.timeseriesId_list[index])
                self.listWidget_timeseries.addItem(listitem)
            index += 1
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                                Models PART
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def get_model_details(self, id):
        """
                get details of the model from the database.
        :return: string, dictionary
        """
        from utils.database_utils import DatabaseConnect
        db = DatabaseConnect()
        model_string, self.model_detail_dict = db.get_model_details(id, window=self.temp_window)
        return model_string, self.model_detail_dict

    def models_list_view(self):
        """
                        Add the models into the list widget of the window
        """
        from utils.database_utils import DatabaseConnect
        db = DatabaseConnect()
        self.models_list, self.modelId_list = db.get_models(window=self.temp_window)
        self.listWidget_model.clear()
        index =0
        for item in self.modelId_list:
            listitem = QtWidgets.QListWidgetItem()
            listitem.setText(self.models_list[index])
            listitem.setData(1, item)
            index += 1
            self.listWidget_model.addItem(listitem)
        self.listWidget_model.itemClicked.connect(self.model_list_item_event)

    def model_list_item_event(self, item):
        """
                Selected a model from the model list and get 3 params from Model
        :param item:
        """
        print(repr(item.text()))
        self.selected_model = item.text()
        self.selected_modelId = item.data(1)
        print(self.selected_modelId)
        model_data = self.get_model_details(id=self.selected_modelId)[1]
        self.txt_param1.setText(str(model_data["param1"]))
        self.txt_param2.setText(str(model_data['param2']))
        self.txt_param3.setText(str(model_data['param3']))

    def search_models(self):
        """
                        Filter the Model list on the basis on basis searched keyword
        """
        filter_text = self.txt_model.text().lower()
        self.listWidget_model.clear()
        index = 0
        for item in self.models_list:
            if item.lower().startswith(filter_text.lower()):
                listitem = QtWidgets.QListWidgetItem()
                listitem.setText(item)
                listitem.setData(1, self.modelId_list[index])
                self.listWidget_model.addItem(listitem)
            index += 1
        self.listWidget_model.itemClicked.connect(self.model_list_item_event)

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
