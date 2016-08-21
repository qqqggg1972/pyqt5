"""悬停提示信息"""
import sys
from PyQt5 import QtWidgets, QtCore, QtGui


class toolTip(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.setGeometry(385, 465, 250, 150)
        self.setWindowTitle("提示信息")

        self.setToolTip("<p>This is a <b>QWidgets</b> widget</p>")


app = QtWidgets.QApplication(sys.argv)
tooltip = toolTip()
tooltip.show()
sys.exit(app.exec_())
