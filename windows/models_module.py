from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *


class ModelWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(ModelWindow, self).__init__(parent)
        self.setWindowTitle("Financial model Analysis Tool - Model")
        self.ui = Ui_MainWindow(self)


class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(615, 439)
        self.temp_window = MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txt_search = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_search.setGeometry(QtCore.QRect(50, 60, 329, 25))
        self.txt_search.setObjectName("txt_search")
        self.buttonBox = QtWidgets.QGroupBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(380, 40, 131, 151))
        self.buttonBox.setTitle("")
        self.buttonBox.setObjectName("buttonBox")
        self.btn_delete = QtWidgets.QPushButton(self.buttonBox)
        self.btn_delete.setGeometry(QtCore.QRect(20, 60, 91, 25))
        self.btn_delete.setObjectName("btn_delete")
        self.btn_addNew = QtWidgets.QPushButton(self.buttonBox)
        self.btn_addNew.setGeometry(QtCore.QRect(20, 30, 89, 25))
        self.btn_addNew.setObjectName("btn_addNew")
        self.btn_export = QtWidgets.QPushButton(self.buttonBox)
        self.btn_export.setGeometry(QtCore.QRect(20, 120, 91, 25))
        self.btn_export.setObjectName("btn_export")
        self.btn_modify = QtWidgets.QPushButton(self.buttonBox)
        self.btn_modify.setGeometry(QtCore.QRect(20, 90, 91, 25))
        self.btn_modify.setObjectName("btn_modify")
        self.scrollArea_models = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_models.setGeometry(QtCore.QRect(50, 90, 329, 101))
        self.scrollArea_models.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_models.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_models.setWidgetResizable(True)
        self.scrollArea_models.setObjectName("scrollArea_models")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 313, 99))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.scrollArea_models.setWidget(self.scrollAreaWidgetContents_3)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 20, 71, 17))
        self.label.setObjectName("label")
        self.groupBox_overview = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_overview.setGeometry(QtCore.QRect(50, 230, 481, 141))
        self.groupBox_overview.setObjectName("groupBox_overview")
        self.txt_overview = QtWidgets.QTextEdit(self.groupBox_overview)
        self.txt_overview.setGeometry(QtCore.QRect(10, 30, 461, 101))
        self.txt_overview.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.txt_overview.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txt_overview.setReadOnly(True)
        self.txt_overview.setObjectName("txt_overview")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 615, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.models_list_view()
        self.btn_addNew.clicked.connect(self.btn_addNew_clicked)
        self.btn_delete.clicked.connect(self.btn_delete_clicked)
        self.btn_modify.clicked.connect(self.btn_modify_clicked)
        self.btn_export.clicked.connect(self.btn_export_clicked)
        self.txt_search.textChanged.connect(self.search_models)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
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
        from windows.models_addNew import ModelAddNewWindow
        self.model_addnew_win = ModelAddNewWindow(parent=self.temp_window)
        self.model_addnew_win.show()

    def btn_delete_clicked(self):
        self.delete_model_byId(self.selected_modelId)
        # self.modelId_list.remove(model_code)
        self.models_list.remove(self.selected_model)
        self.modelId_list.remove(self.selected_modelId)
        self.models_list_view()
        self.txt_overview.clear()

    def btn_modify_clicked(self):
        result = [x.row() for x in self.listWidget.selectedIndexes()]
        if result:
            model_detail_dict = self.model_detail_dict
            from windows.models_addNew import ModelAddNewWindow
            self.modify_win = ModelAddNewWindow(parent=self.temp_window)
            self.modify_win.ui.model_id = self.model_detail_dict["id"]
            if "name" in model_detail_dict:
                self.modify_win.ui.txt_name.setText(model_detail_dict["name"])
            if "code" in model_detail_dict:
                self.modify_win.ui.txt_code.setText(model_detail_dict["code"])
            if "categorya" in model_detail_dict:
                self.modify_win.ui.combo_category_A.setCurrentText(model_detail_dict["categorya"])
            if "categoryb" in model_detail_dict:
                self.modify_win.ui.combo_category_B.setCurrentText(model_detail_dict["categoryb"])
            if "info1" in model_detail_dict:
                self.modify_win.ui.txt_info1.setText(model_detail_dict["info1"])
            if "info2" in model_detail_dict:
                self.modify_win.ui.txt_info_2.setText(model_detail_dict["info2"])
            if "info3" in model_detail_dict:
                self.modify_win.ui.txt_info_3.setText(model_detail_dict["info3"])
            if "info4" in model_detail_dict:
                self.modify_win.ui.txt_info_4.setText(model_detail_dict["info4"])
            if "info5" in model_detail_dict:
                self.modify_win.ui.txt_info_5.setText(model_detail_dict["info5"])
            if "info6" in model_detail_dict:
                self.modify_win.ui.txt_info_6.setText(model_detail_dict["info6"])
            if "info7" in model_detail_dict:
                self.modify_win.ui.txt_info_7.setPlainText(model_detail_dict["info7"])
            self.modify_win.setWindowTitle("Financial Financial model Analysis Tool - model:Update")
            self.modify_win.ui.btn_addAnother.hide()
            self.modify_win.ui.btn_saveAndReturn.clicked.disconnect(self.modify_win.ui.btn_saveAndReturn_clicked)
            self.modify_win.ui.btn_saveAndReturn.clicked.connect(self.modify_win.ui.btn_saveAndReturnUpdate_clicked)

            self.modify_win.show()

    def btn_export_clicked(self):
        file_dailog = QtWidgets.QFileDialog()
        default_file_extension = '.csv'

        name = file_dailog.getSaveFileName(self.temp_window, 'Save File')[0]
        if default_file_extension not in name:
            name += default_file_extension

        model_info = self.model_detail_dict
        print(model_info)
        keys = list(model_info.keys())
        import csv
        with open(name, 'w+') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerow(model_info)

        output_file.close()

    def search_models(self):
        filter_text = self.txt_search.text().lower()
        # filtered_list = []
        # for item in self.models_list:
        #     if filter_text in item.lower():
        #         filtered_list.append(item)

        self.filtered_list = self.listWidget.findItems(filter_text, QtCore.Qt.MatchStartsWith)
        new_list_widget = QtWidgets.QListWidget(self.scrollArea)

        index = 0
        for item in self.filtered_list:
            self.listWidget.removeItemWidget(item)
            # listitem = QListWidgetItem()
            # listitem.setText(item.text())
            # listitem.setData(1, item.data(1))
            # index += 1
            # new_list_widget.addItem(listitem)
        # # listWidget.itemClicked.connect(self.list_item_event)
        self.scrollArea_models.setWidget(self.listWidget)

    def delete_model_byId(self, id):
        from windows.database_util import DatabaseConnect
        db = DatabaseConnect()
        result = db.delete_model(id)
        return result

    def get_models(self):
        from windows.database_util import DatabaseConnect
        db = DatabaseConnect()
        self.models_list, self.modelId_list = db.get_models()
        return self.models_list

    def get_model_details(self, id):
        from windows.database_util import DatabaseConnect
        db = DatabaseConnect()
        model_string, self.model_detail_dict = db.get_model_details(id)
        return model_string, self.model_detail_dict

    def models_list_view(self):
        self.listWidget = QListWidget()
        self.get_models()
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
        print(repr(item.text()))
        self.selected_model = item.text()
        self.selected_modelId = item.data(1)
        print(self.selected_modelId)
        item_detail = self.get_model_details(id=self.selected_modelId)
        self.txt_overview.setPlainText(item_detail[0])


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    # ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
