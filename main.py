import sys
from windows.login import Ui_LoginWindow
from PyQt5 import QtWidgets
from utils.window_utils import SCREEN_RESOLUTION

app = QtWidgets.QApplication(sys.argv)
resolution = app.desktop().screenGeometry()
SCREEN_RESOLUTION.update({"width": resolution.width(), "height": resolution.height()})
MainWindow = QtWidgets.QMainWindow()
ui = Ui_LoginWindow(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
