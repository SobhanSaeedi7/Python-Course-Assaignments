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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(535, 310)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.164773 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.scissors = QPushButton(self.centralwidget)
        self.scissors.setObjectName(u"scissors")
        self.scissors.setGeometry(QRect(440, 0, 91, 81))
        font = QFont()
        font.setPointSize(32)
        self.scissors.setFont(font)
        self.scissors.setStyleSheet(u"background-color:white;\n"
"border-style: outset;\n"
"border-width:3px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"color: black;")
        self.paper = QPushButton(self.centralwidget)
        self.paper.setObjectName(u"paper")
        self.paper.setGeometry(QRect(440, 100, 91, 81))
        self.paper.setFont(font)
        self.paper.setStyleSheet(u"background-color:white;\n"
"border-style: outset;\n"
"border-width:3px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"color: black;")
        self.rock = QPushButton(self.centralwidget)
        self.rock.setObjectName(u"rock")
        self.rock.setGeometry(QRect(440, 200, 91, 81))
        self.rock.setFont(font)
        self.rock.setStyleSheet(u"background-color:white;\n"
"border-style: outset;\n"
"border-width:3px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"color: black;")
        self.newgame = QPushButton(self.centralwidget)
        self.newgame.setObjectName(u"newgame")
        self.newgame.setGeometry(QRect(10, 150, 91, 131))
        font1 = QFont()
        font1.setPointSize(12)
        self.newgame.setFont(font1)
        self.newgame.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:15px;\n"
"border-color: white;\n"
"color: rgb(255, 255, 255);\n"
"color: rgb(244, 192, 58);")
        self.round = QPushButton(self.centralwidget)
        self.round.setObjectName(u"round")
        self.round.setGeometry(QRect(10, 0, 91, 131))
        self.round.setFont(font1)
        self.round.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:15px;\n"
"border-color: white;\n"
"color: rgb(255, 255, 255);\n"
"color: rgb(244, 192, 58);")
        self.player = QPushButton(self.centralwidget)
        self.player.setObjectName(u"player")
        self.player.setGeometry(QRect(320, 90, 101, 101))
        self.player.setStyleSheet(u"border-color: rgb(0, 85, 0);\n"
"border-width: 3px;\n"
"border-style : dashed;\n"
"background-color: None;")
        self.computer = QPushButton(self.centralwidget)
        self.computer.setObjectName(u"computer")
        self.computer.setGeometry(QRect(120, 90, 101, 101))
        self.computer.setStyleSheet(u"border-color: white;\n"
"border-width: 3px;\n"
"border-style : dashed;\n"
"background-color: None;")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(120, 49, 101, 31))
        self.label_2.setStyleSheet(u"background-color: None;")
        self.copmputer_score = QLabel(self.centralwidget)
        self.copmputer_score.setObjectName(u"copmputer_score")
        self.copmputer_score.setGeometry(QRect(120, 200, 101, 31))
        self.copmputer_score.setStyleSheet(u"background-color: None;")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(320, 59, 101, 21))
        self.label_4.setStyleSheet(u"background-color: None;")
        self.player_score = QLabel(self.centralwidget)
        self.player_score.setObjectName(u"player_score")
        self.player_score.setGeometry(QRect(320, 200, 101, 31))
        self.player_score.setStyleSheet(u"background-color: None;")
        self.result = QLabel(self.centralwidget)
        self.result.setObjectName(u"result")
        self.result.setGeometry(QRect(240, 0, 61, 281))
        self.result.setFont(font)
        self.result.setStyleSheet(u"border-style: outset;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.164773 rgba(255, 255, 255, 255), stop:1 rgba(0, 0, 0, 255));\n"
"border-width:4px;\n"
"border-radius:15px;\n"
"border-top-color:rgb(255, 255, 255);\n"
"border-right-color: rgb(255, 255, 255);\n"
"border-bottom-color: rgb(0, 0, 0);\n"
"border-left-color:  rgb(0, 0, 0);\n"
"color: rgb(244, 192, 58);\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 535, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"RockPaperScissors", None))
        self.scissors.setText(QCoreApplication.translate("MainWindow", u"\ud83e\udd1e", None))
        self.paper.setText(QCoreApplication.translate("MainWindow", u"\ud83d\udd90", None))
        self.rock.setText(QCoreApplication.translate("MainWindow", u"\u270a", None))
        self.newgame.setText(QCoreApplication.translate("MainWindow", u"New Game", None))
        self.round.setText(QCoreApplication.translate("MainWindow", u"Round : 1", None))
        self.player.setText("")
        self.computer.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">Computer</span></p></body></html>", None))
        self.copmputer_score.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">Score : 0</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">You</span></p></body></html>", None))
        self.player_score.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Score : 0</span></p></body></html>", None))
        self.result.setText("")
    # retranslateUi

