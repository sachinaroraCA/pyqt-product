import sys

from windows.login import Ui_LoginWindow
from PyQt5 import QtWidgets

import os

# Directory paths
UTIL_DIRECTORY = os.getcwd()
PROJECT_DIRECTORY = os.path.abspath(os.pardir)

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_LoginWindow(MainWindow)
MainWindow.show()
sys.exit(app.exec_())