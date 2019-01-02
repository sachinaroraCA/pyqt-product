from PyQt5 import QtCore, QtWidgets

# static data to fill the M1 to M16 values
MODEL_DATA = {"1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7",
                   "8": "8", "9": "9", "10": "10", "11": "11", "12": "12", "13": "13",
                   "14": "14", "15": "15", "16": "16" }


class ModelAddNewWindow(QtWidgets.QMainWindow):
    """
                Main class of the Model:Add new module
    """
    def __init__(self, parent=None):
        super(ModelAddNewWindow, self).__init__(parent)
        self.setWindowTitle("Financial model Analysis Tool - Model")
        self.ui = Ui_MainWindow(self)
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.parent_window = parent


class Ui_MainWindow(object):
    """
                UI class of the Model:Add new module
    """
    def __init__(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedHeight(575)
        MainWindow.setFixedWidth(700)
        self.temp_window = MainWindow
        self.selected_timeseriesId = None
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(20, 10, 501, 17))
        self.label_title.setObjectName("label_title")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 67, 17))
        self.label_2.setObjectName("label_2")
        self.txt_name = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_name.setGeometry(QtCore.QRect(120, 40, 251, 25))
        self.txt_name.setObjectName("txt_name")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(390, 40, 51, 17))
        self.label_3.setObjectName("label_3")
        self.comboBox_type = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_type.setGeometry(QtCore.QRect(480, 40, 141, 25))
        self.comboBox_type.setObjectName("comboBox_type")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 70, 351, 131))
        self.groupBox.setObjectName("groupBox")
        self.txt_timeseries = QtWidgets.QLineEdit(self.groupBox)
        self.txt_timeseries.setGeometry(QtCore.QRect(0, 20, 351, 25))
        self.txt_timeseries.setObjectName("txt_timeseries")
        self.listWidget_timeseries = QtWidgets.QListWidget(self.groupBox)
        self.listWidget_timeseries.setGeometry(QtCore.QRect(-5, 50, 351, 81))
        self.listWidget_timeseries.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listWidget_timeseries.setObjectName("listWidget_timeseries")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(390, 70, 231, 131))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 30, 71, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 60, 71, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(10, 90, 71, 17))
        self.label_6.setObjectName("label_6")
        self.txt_param1 = QtWidgets.QLineEdit(self.groupBox_2)
        self.txt_param1.setGeometry(QtCore.QRect(90, 30, 113, 25))
        self.txt_param1.setObjectName("txt_param1")
        self.txt_param2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.txt_param2.setGeometry(QtCore.QRect(90, 60, 113, 25))
        self.txt_param2.setObjectName("txt_param2")
        self.txt_param3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.txt_param3.setGeometry(QtCore.QRect(90, 90, 113, 25))
        self.txt_param3.setObjectName("txt_param3")
        self.btn_evaluate_model = QtWidgets.QPushButton(self.centralwidget)
        self.btn_evaluate_model.setGeometry(QtCore.QRect(20, 210, 291, 25))
        self.btn_evaluate_model.setObjectName("btn_evaluate_model")
        self.btn_recommend_model = QtWidgets.QPushButton(self.centralwidget)
        self.btn_recommend_model.setGeometry(QtCore.QRect(330, 210, 291, 25))
        self.btn_recommend_model.setObjectName("btn_recommend_model")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 240, 601, 151))
        self.groupBox_3.setObjectName("groupBox_3")
        self.txt_me10 = QtWidgets.QLineEdit(self.groupBox_3)
        self.txt_me10.setGeometry(QtCore.QRect(360, 60, 71, 25))
        self.txt_me10.setReadOnly(True)
        self.txt_me10.setObjectName("txt_me10")
        self.txt_me11 = QtWidgets.QLineEdit(self.groupBox_3)
        self.txt_me11.setGeometry(QtCore.QRect(360, 90, 71, 25))
        self.txt_me11.setReadOnly(True)
        self.txt_me11.setObjectName("txt_me11")
        self.txt_me2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.txt_me2.setGeometry(QtCore.QRect(60, 60, 71, 25))
        self.txt_me2.setReadOnly(True)
        self.txt_me2.setObjectName("txt_me2")
        self.txt_me15 = QtWidgets.QLineEdit(self.groupBox_3)
        self.txt_me15.setGeometry(QtCore.QRect(510, 90, 71, 25))
        self.txt_me15.setReadOnly(True)
        self.txt_me15.setObjectName("txt_me15")
        self.txt_me14 = QtWidgets.QLineEdit(self.groupBox_3)
        self.txt_me14.setGeometry(QtCore.QRect(510, 60, 71, 25))
        self.txt_me14.setReadOnly(True)
        self.txt_me14.setObjectName("txt_me14")
        self.txt_me9 = QtWidgets.QLineEdit(self.groupBox_3)
        self.txt_me9.setGeometry(QtCore.QRect(360, 30, 71, 25))
        self.txt_me9.setReadOnly(True)
        self.txt_me9.setObjectName("txt_me9")
        self.txt_me16 = QtWidgets.QLineEdit(self.groupBox_3)
        self.txt_me16.setGeometry(QtCore.QRect(510, 120, 71, 25))
        self.txt_me16.setReadOnly(True)
        self.txt_me16.setObjectName("txt_me16")
        self.txt_me6 = QtWidgets.QLineEdit(self.groupBox_3)
        self.txt_me6.setGeometry(QtCore.QRect(210, 60, 71, 25))
        self.txt_me6.setReadOnly(True)
        self.txt_me6.setObjectName("txt_me6")
        self.txt_me1 = QtWidgets.QLineEdit(self.groupBox_3)
        self.txt_me1.setGeometry(QtCore.QRect(60, 30, 71, 25))
        self.txt_me1.setReadOnly(True)
        self.txt_me1.setObjectName("txt_me1")
        self.txt_me13 = QtWidgets.QLineEdit(self.groupBox_3)
        self.txt_me13.setGeometry(QtCore.QRect(510, 30, 71, 25))
        self.txt_me13.setReadOnly(True)
        self.txt_me13.setObjectName("txt_me13")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(20, 120, 41, 17))
        self.label_10.setObjectName("label_10")
        self.txt_me3 = QtWidgets.QLineEdit(self.groupBox_3)
        self.txt_me3.setGeometry(QtCore.QRect(60, 90, 71, 25))
        self.txt_me3.setReadOnly(True)
        self.txt_me3.setObjectName("txt_me3")
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        self.label_13.setGeometry(QtCore.QRect(170, 120, 41, 17))
        self.label_13.setObjectName("label_13")
        self.txt_me4 = QtWidgets.QLineEdit(self.groupBox_3)
        self.txt_me4.setGeometry(QtCore.QRect(60, 120, 71, 25))
        self.txt_me4.setReadOnly(True)
        self.txt_me4.setObjectName("txt_me4")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(20, 90, 41, 17))
        self.label_9.setObjectName("label_9")
        self.label_14 = QtWidgets.QLabel(self.groupBox_3)
        self.label_14.setGeometry(QtCore.QRect(170, 90, 41, 17))
        self.label_14.setObjectName("label_14")
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(170, 60, 41, 17))
        self.label_11.setObjectName("label_11")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(20, 30, 41, 17))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(20, 60, 41, 17))
        self.label_8.setObjectName("label_8")
        self.txt_me7 = QtWidgets.QLineEdit(self.groupBox_3)
        self.txt_me7.setGeometry(QtCore.QRect(210, 90, 71, 25))
        self.txt_me7.setReadOnly(True)
        self.txt_me7.setObjectName("txt_me7")
        self.txt_me5 = QtWidgets.QLineEdit(self.groupBox_3)
        self.txt_me5.setGeometry(QtCore.QRect(210, 30, 71, 25))
        self.txt_me5.setReadOnly(True)
        self.txt_me5.setObjectName("txt_me5")
        self.txt_me12 = QtWidgets.QLineEdit(self.groupBox_3)
        self.txt_me12.setGeometry(QtCore.QRect(360, 120, 71, 25))
        self.txt_me12.setReadOnly(True)
        self.txt_me12.setObjectName("txt_me12")
        self.txt_me8 = QtWidgets.QLineEdit(self.groupBox_3)
        self.txt_me8.setGeometry(QtCore.QRect(210, 120, 71, 25))
        self.txt_me8.setReadOnly(True)
        self.txt_me8.setObjectName("txt_me8")
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(170, 30, 41, 17))
        self.label_12.setObjectName("label_12")
        self.label_15 = QtWidgets.QLabel(self.groupBox_3)
        self.label_15.setGeometry(QtCore.QRect(310, 60, 41, 17))
        self.label_15.setObjectName("label_15")
        self.label_17 = QtWidgets.QLabel(self.groupBox_3)
        self.label_17.setGeometry(QtCore.QRect(310, 120, 41, 17))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.groupBox_3)
        self.label_18.setGeometry(QtCore.QRect(310, 90, 41, 17))
        self.label_18.setObjectName("label_18")
        self.label_16 = QtWidgets.QLabel(self.groupBox_3)
        self.label_16.setGeometry(QtCore.QRect(310, 30, 41, 17))
        self.label_16.setObjectName("label_16")
        self.label_20 = QtWidgets.QLabel(self.groupBox_3)
        self.label_20.setGeometry(QtCore.QRect(460, 30, 41, 17))
        self.label_20.setObjectName("label_20")
        self.label_22 = QtWidgets.QLabel(self.groupBox_3)
        self.label_22.setGeometry(QtCore.QRect(460, 90, 41, 17))
        self.label_22.setObjectName("label_22")
        self.label_21 = QtWidgets.QLabel(self.groupBox_3)
        self.label_21.setGeometry(QtCore.QRect(460, 120, 41, 17))
        self.label_21.setObjectName("label_21")
        self.label_19 = QtWidgets.QLabel(self.groupBox_3)
        self.label_19.setGeometry(QtCore.QRect(460, 60, 41, 17))
        self.label_19.setObjectName("label_19")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(20, 400, 67, 17))
        self.label_23.setObjectName("label_23")
        self.txt_memo = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_memo.setGeometry(QtCore.QRect(20, 420, 601, 61))
        self.txt_memo.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.txt_memo.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txt_memo.setObjectName("txt_memo")
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(20, 500, 151, 25))
        self.btn_back.setObjectName("btn_back")
        self.btn_add_another = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add_another.setGeometry(QtCore.QRect(250, 500, 151, 25))
        self.btn_add_another.setObjectName("btn_add_another")
        self.btn_save_and_return = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save_and_return.setGeometry(QtCore.QRect(470, 500, 151, 25))
        self.btn_save_and_return.setObjectName("btn_save_and_return")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 692, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.timeseries_list_view()
        self.set_events()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        """
                Set the properties of the UI elements
        :param MainWindow:
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title.setText(_translate("MainWindow", "Add a new Model : "))
        self.label_2.setText(_translate("MainWindow", "Name : "))
        self.label_3.setText(_translate("MainWindow", "Type : "))
        self.comboBox_type.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_type.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_type.setItemText(2, _translate("MainWindow", "3"))
        self.groupBox.setTitle(_translate("MainWindow", "Based Time Series : "))
        self.txt_timeseries.setPlaceholderText(_translate("MainWindow", "  Search"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Model Parameters"))
        self.label_4.setText(_translate("MainWindow", "PARAM. 1 : "))
        self.label_5.setText(_translate("MainWindow", "PARAM. 2 : "))
        self.label_6.setText(_translate("MainWindow", "PARAM. 3 : "))
        self.btn_evaluate_model.setText(_translate("MainWindow", "Evaluate Model"))
        self.btn_recommend_model.setText(_translate("MainWindow", "Recommend Model"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Model Evaluation"))
        self.label_10.setText(_translate("MainWindow", "ME4:"))
        self.label_13.setText(_translate("MainWindow", "ME8:"))
        self.label_9.setText(_translate("MainWindow", "ME3:"))
        self.label_14.setText(_translate("MainWindow", "ME7:"))
        self.label_11.setText(_translate("MainWindow", "ME6:"))
        self.label_7.setText(_translate("MainWindow", "ME1:"))
        self.label_8.setText(_translate("MainWindow", "ME2:"))
        self.label_12.setText(_translate("MainWindow", "ME5:"))
        self.label_15.setText(_translate("MainWindow", "ME10:"))
        self.label_17.setText(_translate("MainWindow", "ME12:"))
        self.label_18.setText(_translate("MainWindow", "ME11:"))
        self.label_16.setText(_translate("MainWindow", "ME9:"))
        self.label_20.setText(_translate("MainWindow", "ME13:"))
        self.label_22.setText(_translate("MainWindow", "ME15:"))
        self.label_21.setText(_translate("MainWindow", "ME16:"))
        self.label_19.setText(_translate("MainWindow", "ME14:"))
        self.label_23.setText(_translate("MainWindow", "Memo : "))
        self.btn_back.setText(_translate("MainWindow", "Back"))
        self.btn_add_another.setText(_translate("MainWindow", "Add Another"))
        self.btn_save_and_return.setText(_translate("MainWindow", "Save and Return"))

    def set_events(self):
        """
                    set all the actions on all the elements of the Window UI
        :return:
        """
        self.btn_back.clicked.connect(self.btn_back_clicked)
        self.btn_add_another.clicked.connect(self.btn_add_another_clicked)
        self.btn_evaluate_model.clicked.connect(self.btn_evaluate_model_clicked)
        self.btn_recommend_model.clicked.connect(self.btn_recommend_model_clicked)
        self.btn_save_and_return.clicked.connect(self.btn_saveAndReturn_clicked)
        self.txt_timeseries.textChanged.connect(self.timeseriesfilterClicked)

    def btn_saveAndReturn_clicked(self):
        """
                    Save the Model record and close current window
        """
        saved = self.save_model()
        if saved:
            self.temp_window.hide()

    def btn_saveAndReturnUpdate_clicked(self):
        """
                    Updates the product record by calling a function update_product
        """
        saved = self.save_model(update=True)
        if saved:
            self.temp_window.hide()

    def btn_add_another_clicked(self):
        """
            Creates a product in a database and refreshes the window to add a new product.
        """
        saved = self.save_model()
        if saved:
            self.clear_window()

    def clear_window(self):
        """
                    clear all the field value values in the current window.
        """
        self.txt_memo.setPlainText("")
        self.txt_timeseries.setText("")
        self.comboBox_type.setCurrentIndex(0)
        self.txt_name.setText("")
        self.txt_param1.setText("")
        self.txt_param2.setText("")
        self.txt_param3.setText("")
        self.txt_me1.setText("")
        self.txt_me2.setText("")
        self.txt_me3.setText("")
        self.txt_me4.setText("")
        self.txt_me5.setText("")
        self.txt_me6.setText("")
        self.txt_me7.setText("")
        self.txt_me8.setText("")
        self.txt_me9.setText("")
        self.txt_me10.setText("")
        self.txt_me11.setText("")
        self.txt_me12.setText("")
        self.txt_me13.setText("")
        self.txt_me14.setText("")
        self.txt_me15.setText("")
        self.txt_me16.setText("")

    def btn_evaluate_model_clicked(self):
        """
                Evaluate model and set the values in text edit 1 to 16
        """
        # TODO: Write an algorithm to evaluate models
        if self.selected_timeseries:
            self.param_one = self.txt_param1.text()
            self.param_two = self.txt_param2.text()
            self.param_three = self.txt_param3.text()
            self.txt_me1.setText(MODEL_DATA["1"])
            self.txt_me2.setText(MODEL_DATA["2"])
            self.txt_me3.setText(MODEL_DATA["3"])
            self.txt_me4.setText(MODEL_DATA["4"])
            self.txt_me5.setText(MODEL_DATA["5"])
            self.txt_me6.setText(MODEL_DATA["6"])
            self.txt_me7.setText(MODEL_DATA["7"])
            self.txt_me8.setText(MODEL_DATA["8"])
            self.txt_me9.setText(MODEL_DATA["9"])
            self.txt_me10.setText(MODEL_DATA["10"])
            self.txt_me11.setText(MODEL_DATA["11"])
            self.txt_me12.setText(MODEL_DATA["12"])
            self.txt_me13.setText(MODEL_DATA["13"])
            self.txt_me14.setText(MODEL_DATA["14"])
            self.txt_me15.setText(MODEL_DATA["15"])
            self.txt_me16.setText(MODEL_DATA["16"])
        else:
            QtWidgets.QMessageBox.about(self.temp_window, "message",
                                        "Select a time-series !!!")

    def btn_recommend_model_clicked(self):
        """
        Todo: Write an algorithm to recommend model
        :return:
        """
        pass

    def btn_back_clicked(self):
        """
                Hide current window and show Model window
        :return:
        """
        self.temp_window.parent_window.show()
        self.temp_window.hide()

    def save_model(self, update=False):
        """
                        Save the model in the database ( Create or update a Model)
        :param update:
        """
        from utils.database_utils import DatabaseConnect
        db = DatabaseConnect()
        try:
            name = str(self.txt_name.text())
            type = str(self.comboBox_type.currentText())
            me1 = float(str(self.txt_me1.text()))
            me2 = float(str(self.txt_me2.text()))
            me3 = float(str(self.txt_me3.text()))
            me4 = float(str(self.txt_me4.text()))
            me5 = float(str(self.txt_me5.text()))
            me6 = float(str(self.txt_me6.text()))
            me7 = float(str(self.txt_me7.text()))
            me8 = float(str(self.txt_me8.text()))
            me9 = float(str(self.txt_me9.text()))
            me10 = float(str(self.txt_me10.text()))
            me11 = float(str(self.txt_me11.text()))
            me12 = float(str(self.txt_me12.text()))
            me13 = float(str(self.txt_me13.text()))
            me14 = float(str(self.txt_me14.text()))
            me15 = float(str(self.txt_me15.text()))
            me16 = float(str(self.txt_me16.text()))
            param1 = str(self.txt_param1.text())
            param2 = str(self.txt_param2.text())
            param3 = str(self.txt_param3.text())
            description = str(self.txt_memo.toPlainText())
            time_series_ID = self.selected_timeseriesId

            if (name and type and me1 and me2 and me3 and me4 and me5 and me6 and me7 and me8 and me9 and me10 and me11 and
                me12 and me13 and me14 and me15 and me16 and param1 and param2 and param3):

                if not update:
                    saved = db.save_model_record(
                        name=name, type=type, me1=me1, me2=me2, me3=me3, me4=me4, me5=me5, me6=me6, me7=me7, me8=me8,
                        me9=me9, me10=me10, me11=me11, me12=me12, me13=me13, me14=me14, me15=me15, me16=me16,
                        param1=param1, param2=param2, param3=param3, description=description,
                        time_series_ID=time_series_ID, window=self.temp_window
                    )
                else:
                    saved = db.update_model_record(
                        name=name, type=type, me1=me1, me2=me2, me3=me3, me4=me4, me5=me5, me6=me6, me7=me7, me8=me8,
                        me9=me9, me10=me10, me11=me11, me12=me12, me13=me13, me14=me14, me15=me15, me16=me16,
                        param1=param1, param2=param2, param3=param3, description=description,
                        time_series_ID=time_series_ID, model_id=self.selected_modelId, window=self.temp_window
                    )
                if saved:
                    QtWidgets.QMessageBox.about(self.temp_window, "info!", "Successfully saved the model !!!")
                    self.temp_window.parent_window.ui.models_list_view()
                return saved

            else:
                QtWidgets.QMessageBox.about(self.temp_window, "Error!!!", "Fill the mendetory fields on window !!!")
                return False
        except Exception as ex:
            QtWidgets.QMessageBox.about(self.temp_window, "Error!!!", str(ex))

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
                set the currently selected time-series
        :param item:
        """
        self.selected_timeseries = item.text()
        self.selected_timeseriesId = item.data(1)

    def select_timeseries_byId(self, timeseries_id):
        """
                Set the time-series properties by using time-series id
        :param timeseries_id:
        :return:
        """
        if timeseries_id:
            index = self.timeseriesId_list.index(timeseries_id)
            self.selected_timeseriesId = timeseries_id
            self.selected_timeseries = self.timeseries_list[index]
            self.listWidget_timeseries.setCurrentRow(index)

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

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
