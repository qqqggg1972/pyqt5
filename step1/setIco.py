'''图标'''
import sys
from PyQt5 import QtWidgets, QtGui


class Icon(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("图标")
        self.setWindowIcon(QtGui.QIcon('ye.gif'))
        self.setWindowIcon('aa')

app = QtWidgets.QApplication(sys.argv)
icon = Icon()
icon.show()
sys.exit(app.exec_())

