# -*- coding: utf-8 -*-
"""网格布局示例"""
import sys
from PyQt5 import QtWidgets


class GridLayout(QtWidgets.QMainWindow):
    def __init__(self):
        super(GridLayout, self).__init__()

        self.setWindowTitle("网格布局演示程序")
        button_names = ['Cls', 'Bck', '', 'Close',
                        '7', '8', '9', '/',
                        '4', '5', '6', '*',
                        '1', '2', '3', '-',
                        '0', '.', '=', '+']
        main_ground = QtWidgets.QWidget()
        self.setCentralWidget(main_ground)
        grid = QtWidgets.QGridLayout()

        for [n, (x, y)] in enumerate([(i, j) for i in range(5) for j in range(4)]):
            if (x, y) == (0, 2):
                grid.addWidget(QtWidgets.QLabel(button_names[n]), x, y)
            else:
                grid.addWidget(QtWidgets.QPushButton(button_names[n]), x, y)

        main_ground.setLayout(grid)


app = QtWidgets.QApplication(sys.argv)
grid_layout = GridLayout()
grid_layout.show()
sys.exit(app.exec_())
