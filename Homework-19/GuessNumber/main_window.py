# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpinBox, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(436, 282)
        MainWindow.setStyleSheet(u"background-color:qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255))")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:15px;\n"
"border-color: white;\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 4)

        self.check_game = QPushButton(self.centralwidget)
        self.check_game.setObjectName(u"check_game")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.check_game.sizePolicy().hasHeightForWidth())
        self.check_game.setSizePolicy(sizePolicy1)
        self.check_game.setStyleSheet(u"background-color:white;\n"
"border-style: outset;\n"
"border-width:3px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"color: black;")

        self.gridLayout.addWidget(self.check_game, 3, 1, 1, 2)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        sizePolicy1.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(9)
        self.line.setFont(font1)
        self.line.setStyleSheet(u"background-color: None;\n"
"color: rgb(0, 0, 0);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 1, 0, 1, 4)

        self.order = QLabel(self.centralwidget)
        self.order.setObjectName(u"order")
        sizePolicy.setHeightForWidth(self.order.sizePolicy().hasHeightForWidth())
        self.order.setSizePolicy(sizePolicy)
        self.order.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:15px;\n"
"border-color: white;\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.order, 3, 0, 1, 1)

        self.guess_number = QSpinBox(self.centralwidget)
        self.guess_number.setObjectName(u"guess_number")
        self.guess_number.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.guess_number.sizePolicy().hasHeightForWidth())
        self.guess_number.setSizePolicy(sizePolicy1)
        self.guess_number.setFont(font)
        self.guess_number.setStyleSheet(u"background-color:white;\n"
"border-style: outset;\n"
"border-width:3px;\n"
"border-radius:5px;\n"
"border-color: black;\n"
"color: black;")

        self.gridLayout.addWidget(self.guess_number, 2, 0, 1, 4)

        self.turn = QLabel(self.centralwidget)
        self.turn.setObjectName(u"turn")
        sizePolicy.setHeightForWidth(self.turn.sizePolicy().hasHeightForWidth())
        self.turn.setSizePolicy(sizePolicy)
        self.turn.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:15px;\n"
"border-color: white;\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.turn, 3, 3, 1, 1)

        self.new_game = QPushButton(self.centralwidget)
        self.new_game.setObjectName(u"new_game")
        sizePolicy1.setHeightForWidth(self.new_game.sizePolicy().hasHeightForWidth())
        self.new_game.setSizePolicy(sizePolicy1)
        self.new_game.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:15px;\n"
"border-color: white;\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.new_game, 4, 0, 1, 4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 436, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"GuessNumber", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Guess Number</span></p></body></html>", None))
        self.check_game.setText(QCoreApplication.translate("MainWindow", u"Check", None))
        self.order.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Go : </p></body></html>", None))
        self.turn.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Turn : 0</p></body></html>", None))
        self.new_game.setText(QCoreApplication.translate("MainWindow", u"New_Game", None))
    # retranslateUi

