# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GTAGVui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(268, 652)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.Led_Col = QLineEdit(self.centralwidget)
        self.Led_Col.setObjectName(u"Led_Col")

        self.horizontalLayout.addWidget(self.Led_Col)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.Led_Row = QLineEdit(self.centralwidget)
        self.Led_Row.setObjectName(u"Led_Row")

        self.horizontalLayout.addWidget(self.Led_Row)

        self.Btn_Set = QPushButton(self.centralwidget)
        self.Btn_Set.setObjectName(u"Btn_Set")

        self.horizontalLayout.addWidget(self.Btn_Set)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Btn_selectall = QPushButton(self.centralwidget)
        self.Btn_selectall.setObjectName(u"Btn_selectall")

        self.horizontalLayout_3.addWidget(self.Btn_selectall)

        self.Btn_unselectall = QPushButton(self.centralwidget)
        self.Btn_unselectall.setObjectName(u"Btn_unselectall")

        self.horizontalLayout_3.addWidget(self.Btn_unselectall)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.T_TOP = QHBoxLayout()
        self.T_TOP.setObjectName(u"T_TOP")
        self.T_Left = QVBoxLayout()
        self.T_Left.setObjectName(u"T_Left")

        self.T_TOP.addLayout(self.T_Left)

        self.TRight = QVBoxLayout()
        self.TRight.setObjectName(u"TRight")

        self.T_TOP.addLayout(self.TRight)


        self.verticalLayout_3.addLayout(self.T_TOP)

        self.Btn_ok = QPushButton(self.centralwidget)
        self.Btn_ok.setObjectName(u"Btn_ok")

        self.verticalLayout_3.addWidget(self.Btn_ok)

        self.verticalLayout_3.setStretch(3, 10)

        self.verticalLayout.addLayout(self.verticalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Col:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Row:", None))
        self.Btn_Set.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.Btn_selectall.setText(QCoreApplication.translate("MainWindow", u"Select All", None))
        self.Btn_unselectall.setText(QCoreApplication.translate("MainWindow", u"Unselect All", None))
        self.Btn_ok.setText(QCoreApplication.translate("MainWindow", u"OK", None))
    # retranslateUi

