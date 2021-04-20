#!/usr/bin/env
# -*- coding: utf-8 -*-

import sys
from PySide2 import QtCore, QtWidgets, QtGui
from GTAGVui import Ui_MainWindow as GTAGVui

class GTAGV(QtWidgets.QMainWindow, GTAGVui):

    def __init__(self, parent=None):
        super(GTAGV, self).__init__(parent)
        self.setupUi(self)
        self.Change_Font()
        self.Connecter()


    def Connecter(self):
        self.Btn_selectall.clicked.connect(self.Selectall)
        self.Btn_unselectall.clicked.connect(self.Unselectall)
        self.Btn_ok.clicked.connect(self.calcu)
        self.Btn_Set.clicked.connect(self.Change_TBtn)

    def Change_Font(self):
        FindLE = []
        FindLE.append(self.findChildren(QtWidgets.QPushButton))
        FindLE.append(self.findChildren(QtWidgets.QLabel))
        FindLE.append(self.findChildren(QtWidgets.QLineEdit))
        self.font = QtGui.QFont("Times New Roman", 12)
        for i in FindLE:
            for j in i:
                j.setFont(self.font)


    def Change_TBtn(self):
        for i in range(self.TRight.count()):
            self.TRight.itemAt(i).widget().deleteLater()
        for i in range(self.T_Left.count()):
            self.T_Left.itemAt(i).widget().deleteLater()
        number = 0
        self.varList = []
        a = int(self.Led_Col.text())
        b = int(self.Led_Row.text())
        for i in range(a*b):
            self.varList.append('Btn' + str(number))
        for j in range(a):
            if j == 0:
                self.lay = self.T_Left
            else:
                self.lay = self.TRight
            for i in range(b):
                self.varList[number] = QtWidgets.QToolButton(self.centralwidget)
                self.varList[number].setText(str(j+1)+ "-" +str(i+1))
                self.varList[number].setCheckable(True)
                self.varList[number].setFont(QtGui.QFont("Times New Roman", 24))
                self.lay.addWidget(self.varList[number])
                number += 1


    def Selectall(self):
            FindLE = []
            FindLE.append(self.findChildren(QtWidgets.QToolButton))
            for i in FindLE:
                for j in i:
                    j.setChecked(True)

    def Unselectall(self):
        FindLE = []
        FindLE.append(self.findChildren(QtWidgets.QToolButton))
        for i in FindLE:
            for j in i:
                j.setChecked(False)

    def calcu(self):
        FindLE = []
        data = []
        FindLE.append(self.findChildren(QtWidgets.QToolButton))
        for i in FindLE:
            for j in i:
                if j.isChecked():
                    data.append(j.text().replace(" ",""))
        self.data = data
        print(data)
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Login_1 = GTAGV()
    Login_1.show()
    app.exec_()
    print(1)
    # sys.exit(app.exec_())
