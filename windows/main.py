import sys

from windows.login import Ui_LoginWindow
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_LoginWindow(MainWindow)
MainWindow.show()
sys.exit(app.exec_())