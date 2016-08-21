# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets, QtGui


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.resize(350, 250)
        self.setWindowTitle("我的程序")
        text_edit = QtWidgets.QTextEdit()
        self.setCentralWidget(text_edit)

        #exit_action = QtWidgets.QAction(QtGui.QIcon(r'..\ye.gif'), '退出', self)
        exit_action.setStatusTip("退出程序")
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(QtWidgets.qApp.quit)

        self.statusBar()

        self.menu_bar = self.menuBar()
        file = self.menu_bar.addMenu("文件")
        file.addAction(exit_action)

        self.addToolBar("退出").addAction(exit_action)


app = QtWidgets.QApplication(sys.argv)
main_Window = MainWindow()
main_Window.show()
sys.exit(app.exec_())
