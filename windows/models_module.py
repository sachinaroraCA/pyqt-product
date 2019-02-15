from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *


class ModelWindow(QtWidgets.QMainWindow):
    """
                Main class of the Model module
    """
    def __init__(self, parent=None):
        super(ModelWindow, self).__init__(parent)
        self.setWindowTitle("Financial model Analysis Tool - Model")
        self.ui = Ui_MainWindow(self)
        self.parent_window = parent
        self.setWindowState(QtCore.Qt.WindowMaximized)


class Ui_MainWindow(object):
    """
            UI class of the Model module
    """
    def __init__(self, MainWindow):
        MainWindow.setObjectName("MainWindow")

        from utils.window_utils import get_resolution_ratio
        self.width_ratio, self.height_ratio = get_resolution_ratio(600, 450)
        MainWindow.setMinimumHeight(self.height_ratio*450)
        MainWindow.setMinimumWidth(self.width_ratio*600)
        self.temp_window = MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(self.width_ratio*50, self.height_ratio*20, self.width_ratio*71, self.height_ratio*17))
        self.label.setObjectName("label")

        self.txt_search = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_search.setGeometry(QtCore.QRect(self.width_ratio*50, self.height_ratio*60, self.width_ratio*329, self.height_ratio*25))
        self.txt_search.setObjectName("txt_search")

        self.buttonBox = QtWidgets.QGroupBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(self.width_ratio*380, self.height_ratio*46, self.width_ratio*131, self.height_ratio*146))
        self.buttonBox.setTitle("")
        self.buttonBox.setObjectName("buttonBox")

        self.btn_addNew = QtWidgets.QPushButton(self.buttonBox)
        self.btn_addNew.setGeometry(QtCore.QRect(self.width_ratio*20, self.height_ratio*25, self.width_ratio*90, self.height_ratio*25))
        self.btn_addNew.setObjectName("btn_addNew")
        self.btn_delete = QtWidgets.QPushButton(self.buttonBox)
        self.btn_delete.setGeometry(QtCore.QRect(self.width_ratio*20, self.height_ratio*55, self.width_ratio*90, self.height_ratio*25))
        self.btn_delete.setObjectName("btn_delete")
        self.btn_modify = QtWidgets.QPushButton(self.buttonBox)
        self.btn_modify.setGeometry(QtCore.QRect(self.width_ratio*20, self.height_ratio*85, self.width_ratio*90, self.height_ratio*25))
        self.btn_modify.setObjectName("btn_modify")
        self.btn_export = QtWidgets.QPushButton(self.buttonBox)
        self.btn_export.setGeometry(QtCore.QRect(self.width_ratio*20, self.height_ratio*115, self.width_ratio*90, self.height_ratio*25))
        self.btn_export.setObjectName("btn_export")

        self.scrollArea_models = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_models.setGeometry(QtCore.QRect(self.width_ratio*50, self.height_ratio*90, self.width_ratio*329, self.height_ratio*101))
        self.scrollArea_models.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_models.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_models.setWidgetResizable(True)
        self.scrollArea_models.setObjectName("scrollArea_models")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, self.width_ratio*309, self.height_ratio*99))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.scrollArea_models.setWidget(self.scrollAreaWidgetContents_3)

        self.groupBox_overview = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_overview.setGeometry(QtCore.QRect(self.width_ratio*50, self.height_ratio*230, self.width_ratio*461, self.height_ratio*181))
        self.groupBox_overview.setObjectName("groupBox_overview")
        self.txt_overview = QtWidgets.QTextEdit(self.groupBox_overview)
        self.txt_overview.setGeometry(QtCore.QRect(0, self.height_ratio*15, self.width_ratio*461, self.height_ratio*165))
        self.txt_overview.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.txt_overview.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.txt_overview.setReadOnly(True)
        self.txt_overview.setObjectName("txt_overview")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, self.width_ratio*615, self.height_ratio*22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusBar)

        self.selected_modelId = None

        self.models_list_view()
        self.btn_addNew.clicked.connect(self.btn_addNew_clicked)
        self.btn_delete.clicked.connect(self.btn_delete_clicked)
        self.btn_modify.clicked.connect(self.btn_modify_clicked)
        self.btn_export.clicked.connect(self.btn_export_clicked)
        self.txt_search.textChanged.connect(self.search_models)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        """
                Set the properties of the UI elements
        :param MainWindow:
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Financial model Analysis Tool - Model"))
        self.txt_search.setPlaceholderText(_translate("MainWindow", " Search"))
        self.btn_delete.setText(_translate("MainWindow", "Delete"))
        self.btn_addNew.setText(_translate("MainWindow", "Add New"))
        self.btn_export.setText(_translate("MainWindow", "Export"))
        self.btn_modify.setText(_translate("MainWindow", "Modify"))
        self.label.setText(_translate("MainWindow", "models:"))
        self.groupBox_overview.setTitle(_translate("MainWindow", "Overview"))

    def btn_addNew_clicked(self):
        """
                        Open the "Model:Add new" window
        """
        from windows.models_addNew import ModelAddNewWindow
        self.temp_window.ui = self
        self.model_addnew_win = ModelAddNewWindow(parent=self.temp_window)
        self.model_addnew_win.show()
        self.temp_window.hide()

    def btn_delete_clicked(self):
        """
                    Call a function delete_model_byId to delete the selected Model
        """
        if self.selected_modelId:
            buttonReply = QtWidgets.QMessageBox.question(self.temp_window, "Message",
                                                         'Delete the model "{}" ?'.format(self.selected_model),
                                                         QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                         QtWidgets.QMessageBox.No)
            if buttonReply == QtWidgets.QMessageBox.Yes:
                deleted = self.delete_model_byId(self.selected_modelId)
                if deleted[0]:
                    self.models_list.remove(self.selected_model)
                    self.modelId_list.remove(self.selected_modelId)
                    self.models_list_view()
                    self.txt_overview.clear()
                else:
                    QMessageBox.about(self.temp_window, "Warning", "Database Error !!!")

    def btn_modify_clicked(self):
        """
                    Open the "Model:Add new" window with pre-filled values of selected Model to update
        """
        if self.selected_modelId:
            result = [x.row() for x in self.listWidget.selectedIndexes()]
            if result:
                model_detail_dict = self.model_detail_dict
                from windows.models_addNew import ModelAddNewWindow
                self.modify_win = ModelAddNewWindow(parent=self.temp_window)
                self.modify_win.ui.model_id = self.model_detail_dict["id"]
                if "name" in model_detail_dict:
                    self.modify_win.ui.txt_name.setText(model_detail_dict["name"])
                if "type" in model_detail_dict:
                    self.modify_win.ui.comboBox_type.setCurrentText(model_detail_dict["type"])
                if "param1" in model_detail_dict:
                    self.modify_win.ui.txt_param1.setText(model_detail_dict["param1"])
                if "param2" in model_detail_dict:
                    self.modify_win.ui.txt_param2.setText(model_detail_dict["param2"])
                if "param3" in model_detail_dict:
                    self.modify_win.ui.txt_param3.setText(model_detail_dict["param3"])
                if "description" in model_detail_dict:
                    self.modify_win.ui.txt_memo.setPlainText(model_detail_dict["description"])
                if "me1" in model_detail_dict:
                    self.modify_win.ui.txt_me1.setText(str(model_detail_dict["me1"]))
                if "me2" in model_detail_dict:
                    self.modify_win.ui.txt_me2.setText(str(model_detail_dict["me2"]))
                if "me3" in model_detail_dict:
                    self.modify_win.ui.txt_me3.setText(str(model_detail_dict["me3"]))
                if "me4" in model_detail_dict:
                    self.modify_win.ui.txt_me4.setText(str(model_detail_dict["me4"]))
                if "me5" in model_detail_dict:
                    self.modify_win.ui.txt_me5.setText(str(model_detail_dict["me5"]))
                if "me6" in model_detail_dict:
                    self.modify_win.ui.txt_me6.setText(str(model_detail_dict["me6"]))
                if "me7" in model_detail_dict:
                    self.modify_win.ui.txt_me7.setText(str(model_detail_dict["me7"]))
                if "me8" in model_detail_dict:
                    self.modify_win.ui.txt_me8.setText(str(model_detail_dict["me8"]))
                if "me9" in model_detail_dict:
                    self.modify_win.ui.txt_me9.setText(str(model_detail_dict["me9"]))
                if "me10" in model_detail_dict:
                    self.modify_win.ui.txt_me10.setText(str(model_detail_dict["me10"]))
                if "me11" in model_detail_dict:
                    self.modify_win.ui.txt_me11.setText(str(model_detail_dict["me11"]))
                if "me12" in model_detail_dict:
                    self.modify_win.ui.txt_me12.setText(str(model_detail_dict["me12"]))
                if "me13" in model_detail_dict:
                    self.modify_win.ui.txt_me13.setText(str(model_detail_dict["me13"]))
                if "me14" in model_detail_dict:
                    self.modify_win.ui.txt_me14.setText(str(model_detail_dict["me14"]))
                if "me15" in model_detail_dict:
                    self.modify_win.ui.txt_me15.setText(str(model_detail_dict["me15"]))
                if "me16" in model_detail_dict:
                    self.modify_win.ui.txt_me16.setText(str(model_detail_dict["me16"]))
                if "time_series_ID" in model_detail_dict:
                    time_series_ID = model_detail_dict["time_series_ID"]
                    self.modify_win.ui.select_timeseries_byId(time_series_ID)
                self.modify_win.setWindowTitle("Financial Financial model Analysis Tool - model:Update")
                self.modify_win.ui.selected_modelId = self.selected_modelId
                self.modify_win.ui.btn_add_another.hide()
                self.modify_win.ui.btn_save_and_return.clicked.disconnect(self.modify_win.ui.btn_saveAndReturn_clicked)
                self.modify_win.ui.btn_save_and_return.clicked.connect(self.modify_win.ui.btn_saveAndReturnUpdate_clicked)

                self.modify_win.show()
                self.temp_window.hide()

    def btn_export_clicked(self):
        """
                    Export the product field values into a csv file
        """
        model_data = self.model_detail_dict
        model_data.pop('time_series_ID')
        model_data.update({'Time-series': self.selected_model})
        from utils.window_utils import export_file
        export_file(window=self.temp_window, export_data=self.model_detail_dict)

    def search_models(self):
        """
                        Filter the Model list on the basis on basis searched keyword
        """
        filter_text = self.txt_search.text().lower()
        self.listWidget.clear()
        index = 0
        for item in self.models_list:
            if str(filter_text.lower()) in str(item.lower()):
                listitem = QListWidgetItem()
                listitem.setText(item)
                listitem.setData(1, self.modelId_list[index])
                self.listWidget.addItem(listitem)
            index += 1
        self.listWidget.itemClicked.connect(self.list_item_event)
        self.scrollArea_models.setWidget(self.listWidget)

    def delete_model_byId(self, id):
        """
                        Delete the models from the database on the basis of id
        :param id:
        :return: status i.e, Model deleted or not
        """
        from utils.database_utils import DatabaseConnect
        db = DatabaseConnect()
        result = db.delete_model(id, window=self.temp_window)
        return result

    def get_models(self):
        """
                        Get the list of all models in the database
        :return: models_list
        """
        from utils.database_utils import DatabaseConnect
        db = DatabaseConnect()
        self.models_list, self.modelId_list = db.get_models(window=self.temp_window)
        return self.models_list

    def get_model_details(self, id):
        """
                        Get the details of the Model from the database on the basis of provided id
        :param id:
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
        self.listWidget = QListWidget()
        self.get_models()
        self.txt_overview.clear()
        self.txt_search.clear()
        index =0
        for item in self.modelId_list:
            listitem = QListWidgetItem()
            listitem.setText(self.models_list[index])
            listitem.setData(1, item)
            index += 1
            self.listWidget.addItem(listitem)
        self.listWidget.itemClicked.connect(self.list_item_event)
        self.scrollArea_models.setWidget(self.listWidget)

    def list_item_event(self, item):
        """
                Selected a model from the product list. So display model details in Overview
        :param item:
        """
        self.selected_model = item.text()
        self.selected_modelId = item.data(1)
        item_detail = self.get_model_details(id=self.selected_modelId)
        self.txt_overview.setPlainText(item_detail[0])


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
