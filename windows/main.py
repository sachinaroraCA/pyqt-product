import sys

from windows.login import Ui_LoginWindow
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_LoginWindow(MainWindow)
MainWindow.show()
sys.exit(app.exec_())

# # pyqtgraph examples : bar chart
# # pythonprogramminglanguage.com
# import pyqtgraph as pg
# from pyqtgraph.Qt import QtCore, QtGui
# import numpy as np
#
# win = pg.plot()
# win.setWindowTitle('pyqtgraph BarGraphItem')
#
# # create list of floats
# y1 = np.linspace(10, 50, num=10)
#
# # create horizontal list
# x = np.arange(5)
#
# # create bar chart
# bg1 = pg.BarGraphItem(x=x, height=y1, width=0.5, brush='g')
# win.addItem(bg1)
#
# ## Start Qt event loop unless running in interactive mode or using
# if __name__ == '__main__':
#     import sys
#     if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
#         QtGui.QApplication.instance().exec_()

# from PyQt5 import QtCore, QtGui, QtWidgets
#
#
# class TabBar(QtWidgets.QTabBar):
#     def tabSizeHint(self, index):
#         s = QtWidgets.QTabBar.tabSizeHint(self, index)
#         s.transpose()
#         return s
#
#     def paintEvent(self, event):
#         painter = QtWidgets.QStylePainter(self)
#         opt = QtWidgets.QStyleOptionTab()
#
#         for i in range(self.count()):
#             self.initStyleOption(opt, i)
#             painter.drawControl(QtWidgets.QStyle.CE_TabBarTabShape, opt)
#             painter.save()
#
#             s = opt.rect.size()
#             s.transpose()
#             r = QtCore.QRect(QtCore.QPoint(), s)
#             r.moveCenter(opt.rect.center())
#             opt.rect = r
#
#             c = self.tabRect(i).center()
#             painter.translate(c)
#             painter.rotate(90)
#             painter.translate(-c)
#             painter.drawControl(QtWidgets.QStyle.CE_TabBarTabLabel, opt)
#             painter.restore()
#
#
# class TabWidget(QtWidgets.QTabWidget):
#     def __init__(self, *args, **kwargs):
#         QtWidgets.QTabWidget.__init__(self, *args, **kwargs)
#         self.setTabBar(TabBar(self))
#         self.setTabPosition(QtWidgets.QTabWidget.West)
#
#
# class ProxyStyle(QtWidgets.QProxyStyle):
#     def drawControl(self, element, opt, painter, widget):
#         if element == QtWidgets.QStyle.CE_TabBarTabLabel:
#             ic = self.pixelMetric(QtWidgets.QStyle.PM_TabBarIconSize)
#             r = QtCore.QRect(opt.rect)
#             w =  0 if opt.icon.isNull() else opt.rect.width() + self.pixelMetric(QtWidgets.QStyle.PM_TabBarIconSize)
#             r.setHeight(opt.fontMetrics.width(opt.text) + w)
#             r.moveBottom(opt.rect.bottom())
#             opt.rect = r
#         QtWidgets.QProxyStyle.drawControl(self, element, opt, painter, widget)
#
#
# if __name__ == '__main__':
#     import sys
#
#     app = QtWidgets.QApplication(sys.argv)
#     QtWidgets.QApplication.setStyle(ProxyStyle())
#     w = TabWidget()
#     w.addTab(QtWidgets.QWidget(), QtGui.QIcon("zoom.png"), "ABC")
#     w.addTab(QtWidgets.QWidget(), QtGui.QIcon("zoom-in.png"), "ABCDEFGH")
#     w.addTab(QtWidgets.QWidget(), QtGui.QIcon("zoom-out.png"), "XYZ")
#
#     w.resize(640, 480)
#     w.show()

    # sys.exit(app.exec_())