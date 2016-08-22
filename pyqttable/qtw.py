# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtGui, QtCore


class MyDialog(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)
        self.setGeometry(300, 300, 450, 210)

        self.MyTable = QtWidgets.QTableWidget(4, 3)
        self.MyTable.setHorizontalHeaderLabels(['姓名', '身高', '体重'])

        # 防止修改
        self.MyTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        # 整行选择
        self.MyTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        # 隐藏标题
        # self.MyTable.horizontalHeader().setVisible(False)

        # 对表头文件的字体,颜色进行设置
        for x in range(self.MyTable.columnCount()):
            headItem = self.MyTable.horizontalHeaderItem(x)  # 获得水平方向表头的Item对象
            # headItem.setTextColor(QtGui.QColor(200,111,100))

        # 单元格里加入控件
        # self.MyCombo=QtWidgets.QComboBox()
        # self.MyCombo.addItem("√")
        # self.MyCombo.addItem("×")
        # self.MyTable.setCellWidget(1,0,self.MyCombo)

        newItem = QtWidgets.QTableWidgetItem('松鼠松鼠松鼠松鼠松鼠')
        self.MyTable.setItem(0, 0, newItem)
        # newItem =
        self.MyTable.setItem(1, 0, QtWidgets.QTableWidgetItem('大松鼠松鼠松鼠松鼠松鼠'))

        self.MyTable.setItem(0, 1, QtWidgets.QTableWidgetItem('10cm'))
        self.MyTable.setItem(0, 2, QtWidgets.QTableWidgetItem('60g'))

        # 根据内容自适应列宽
        # self.MyTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.MyTable.setSortingEnabled(True)        # 排序
        # self.MyTable.setShowGrid(False)           # 显示 格子
        self.MyTable.setAlternatingRowColors(True)  # 隔行变色显示
        self.MyTable.setColumnWidth(0,150)


        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.MyTable)
        self.setLayout(layout)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    myWindow = MyDialog()
    myWindow.show()
    sys.exit(app.exec_())
