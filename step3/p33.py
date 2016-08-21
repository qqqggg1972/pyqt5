# -*- coding: utf-8 -*-
"""网格布局跨行示例"""
import sys
from PyQt5 import QtWidgets


class GridLayout(QtWidgets.QMainWindow):
    def __init__(self):
        super(GridLayout, self).__init__()

        self.setWindowTitle("网格布局跨行演示程序")

        main_ground = QtWidgets.QWidget()
        self.setCentralWidget(main_ground)

        grid = QtWidgets.QGridLayout()
        grid.setSpacing(20)
        grid.addWidget(QtWidgets.QLabel("标题:"), 1, 0)
        grid.addWidget(QtWidgets.QLineEdit(), 1, 1)
        grid.addWidget(QtWidgets.QLabel("作者:"), 2, 0)
        grid.addWidget(QtWidgets.QLineEdit(), 2, 1)
        grid.addWidget(QtWidgets.QLabel("评论"), 3, 0)
        grid.addWidget(QtWidgets.QTextEdit(), 3, 1, 5, 1)

        main_ground.setLayout(grid)
        self.resize(350, 300)


app = QtWidgets.QApplication(sys.argv)
grid_layout = GridLayout()
grid_layout.show()
sys.exit(app.exec_())
