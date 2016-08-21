# -*- coding: utf-8 -*-
"""主窗口,菜单栏"""
import sys
from PyQt5 import QtWidgets, QtGui


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.resize(250, 150)
        self.setWindowTitle("状态栏程序示例")
        self.statusBar().showMessage("就绪")

        exit_menu = QtWidgets.QAction(QtGui.QIcon(r"../ye.gif"),"退出",self)
        exit_menu = QtWidgets.QAction( "退出", self)
        exit_menu.setShortcut("ctrl+Q")

        exit_menu.setStatusTip("退出程序")
        exit_menu.triggered.connect(QtWidgets.qApp.quit)
        self.statusBar()

        menubar = self.menuBar()
        file = menubar.addMenu("文件")
        file.addAction(exit_menu)

        menubar.addMenu("Code").addAction(exit_menu)






app = QtWidgets.QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
sys.exit(app.exec_())
