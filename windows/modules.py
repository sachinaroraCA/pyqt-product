from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class ProductModulesWindow(QMainWindow):
    """
                Main class of the Main module
    """
    def __init__(self, parent=None):
        super(ProductModulesWindow, self).__init__(parent)
        self.setWindowTitle("Financial Product Analysis Tool - Modules")
        self.ui = Ui_ProductModulesWindow(self)


class Ui_ProductModulesWindow(object):
    """
                    UI class of the Product Window
    """
    def __init__(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedHeight(450)
        MainWindow.setFixedWidth(600)
        self.temp_window =MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBoxProducts = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxProducts.setGeometry(QtCore.QRect(80, 40, 451, 91))
        self.groupBoxProducts.setObjectName("groupBox")
        self.btn_products = QtWidgets.QPushButton(self.groupBoxProducts)
        self.btn_products.setGeometry(QtCore.QRect(40, 40, 121, 31))
        self.btn_products.setObjectName("btn_products")
        self.btn_evaluation = QtWidgets.QPushButton(self.groupBoxProducts)
        self.btn_evaluation.setGeometry(QtCore.QRect(270, 40, 121, 31))
        self.btn_evaluation.setObjectName("btn_evaluation")
        self.groupBoxEvaluation = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxEvaluation.setGeometry(QtCore.QRect(80, 160, 451, 91))
        self.groupBoxEvaluation.setObjectName("groupBoxEvaluation")
        self.btn_time_series = QtWidgets.QPushButton(self.groupBoxEvaluation)
        self.btn_time_series.setGeometry(QtCore.QRect(40, 40, 121, 31))
        self.btn_time_series.setObjectName("btn_time_series")
        self.btn_analysis = QtWidgets.QPushButton(self.groupBoxEvaluation)
        self.btn_analysis.setGeometry(QtCore.QRect(270, 40, 121, 31))
        self.btn_analysis.setObjectName("btn_analysis")
        self.groupBoxPredictions = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxPredictions.setGeometry(QtCore.QRect(80, 280, 451, 91))
        self.groupBoxPredictions.setObjectName("groupBoxPredictions")
        self.btn_model = QtWidgets.QPushButton(self.groupBoxPredictions)
        self.btn_model.setGeometry(QtCore.QRect(40, 40, 121, 31))
        self.btn_model.setObjectName("btn_model")
        self.btn_prediction = QtWidgets.QPushButton(self.groupBoxPredictions)
        self.btn_prediction.setGeometry(QtCore.QRect(270, 40, 121, 31))
        self.btn_prediction.setObjectName("btn_prediction")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 622, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.btn_products.clicked.connect(self.btn_products_clicked)
        self.btn_evaluation.clicked.connect(self.btn_evaluation_clicked)
        self.btn_time_series.clicked.connect(self.btn_time_series_clicked)
        self.btn_analysis.clicked.connect(self.btn_analysis_clicked)
        self.btn_model.clicked.connect(self.btn_models_clicked)
        self.btn_prediction.clicked.connect(self.btn_prediction_clicked)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        """
                Set the properties of the UI elements
        :param MainWindow:
        :return:
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Financial Product Analysis Tool - Modules"))
        self.groupBoxProducts.setTitle(_translate("MainWindow", "Products"))
        self.btn_products.setText(_translate("MainWindow", "Products"))
        self.btn_evaluation.setText(_translate("MainWindow", "Evaluation"))
        self.groupBoxEvaluation.setTitle(_translate("MainWindow", "Time Series"))
        self.btn_time_series.setText(_translate("MainWindow", "Time Series"))
        self.btn_analysis.setText(_translate("MainWindow", "Analysis"))
        self.groupBoxPredictions.setTitle(_translate("MainWindow", "Predictions"))
        self.btn_model.setText(_translate("MainWindow", "Models"))
        self.btn_prediction.setText(_translate("MainWindow", "Predictions"))

    def btn_products_clicked(self):
        """
                    Open the Product Window
        """
        from windows.product_module import ProductWindow
        self.product_window = ProductWindow(parent=self.temp_window)
        self.product_window.show()

    def btn_evaluation_clicked(self):
        """
                    Open the Evaluation Window
        """
        from  windows.evaluation_module import EvaluationWindow
        self.evaluation_window = EvaluationWindow(parent=self.temp_window)
        self.evaluation_window.show()

    def btn_time_series_clicked(self):
        """
                    Open the Time-series Window
        """
        from  windows.timeseries_module import TimeSeriesWindow
        self.timeseries_window = TimeSeriesWindow(parent=self.temp_window)
        self.timeseries_window.show()

    def btn_analysis_clicked(self):
        """
                    Open the Analysis Window
        """
        from  windows.analysis_module import AnalysisWindow
        self.analysis_window = AnalysisWindow(parent=self.temp_window)
        self.analysis_window.show()

    def btn_models_clicked(self):
        """
                    Open the Models Window
        """
        from windows.models_module import ModelWindow
        self.model_window = ModelWindow(parent=self.temp_window)
        self.model_window.show()

    def btn_prediction_clicked(self):
        """
                    Open the Prediction Window
        """
        from windows.prediction_module import PredictionWindow
        self.prediction_window = PredictionWindow(parent=self.temp_window)
        self.prediction_window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_ProductModulesWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

