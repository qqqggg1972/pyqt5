# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets, QtCore, QtGui


class OpenFileDialog(QtWidgets.QMainWindow):
    def __init__(self):
        super(OpenFileDialog, self).__init__()

        self.setWindowTitle("文件对话框演示程序")
        self.setGeometry(300, 300, 400, 300)

        self.text_edit = QtWidgets.QTextEdit()
        self.setCentralWidget(self.text_edit)
        self.statusBar()
        self.setFocus()

        self.file_item = QtWidgets.QAction(QtGui.QIcon(r"..\ye.gif"), "打开", self)
        self.file_item.setShortcut("ctrl+o")
        self.file_item.setStatusTip("打开新文件")
        self.file_item.triggered.connect(self.show_dialog)

        self.file = self.menuBar().addMenu("文件")
        self.file.addAction(self.file_item)

    def show_dialog(self):
        file_name = QtWidgets.QFileDialog.getOpenFileName(self, '打开文件', r'd:\ls.txt')
        try:
            file = open(file_name[0], 'r')
            data = file.read()
        except UnicodeDecodeError:
            data = "不是合法的txt文件"
        except FileNotFoundError:
            data = ""
        self.text_edit.setText(data)


if __name__=="_main__":
    app = QtWidgets.QApplication(sys.argv)
    file_d = OpenFileDialog()
    file_d.show()
    sys.exit(app.exec_())
