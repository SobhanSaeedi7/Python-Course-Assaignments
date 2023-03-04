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
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QFrame, QGridLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(364, 572)
        MainWindow.setStyleSheet(u"background-color: rgb(3, 79, 100);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 9pt \"Papyrus\";\n"
"background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 0, 0, 69), stop:0.147727 rgba(255, 0, 219, 145), stop:0.295455 rgba(171, 0, 255, 69), stop:0.426136 rgba(160, 0, 255, 208), stop:0.477581 rgba(71, 160, 255, 130), stop:0.517045 rgba(0, 189, 255, 255), stop:0.642045 rgba(71, 255, 137, 130), stop:0.715909 rgba(204, 255, 0, 130), stop:0.857955 rgba(255, 87, 0, 69), stop:1 rgba(255, 0, 0, 69));\n"
"color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-width:4px;\n"
"border-radius:10px;\n"
"border-color: white;")

        self.verticalLayout.addWidget(self.label_4)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamilies([u"Papyrus"])
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"font: 9pt \"Papyrus\";\n"
"background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 0, 0, 69), stop:0.147727 rgba(255, 0, 219, 145), stop:0.295455 rgba(171, 0, 255, 69), stop:0.426136 rgba(160, 0, 255, 208), stop:0.477581 rgba(71, 160, 255, 130), stop:0.517045 rgba(0, 189, 255, 255), stop:0.642045 rgba(71, 255, 137, 130), stop:0.715909 rgba(204, 255, 0, 130), stop:0.857955 rgba(255, 87, 0, 69), stop:1 rgba(255, 0, 0, 69));\n"
"color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-width:4px;\n"
"border-radius:10px;\n"
"border-color: white;")

        self.verticalLayout.addWidget(self.label_2)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout.addWidget(self.label_7)

        self.gl_tasks = QGridLayout()
        self.gl_tasks.setObjectName(u"gl_tasks")

        self.verticalLayout.addLayout(self.gl_tasks)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout.addWidget(self.label_8)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setEnabled(True)
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(False)
        self.line.setFont(font1)
        self.line.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 0, 0, 69), stop:0.147727 rgba(255, 0, 219, 145), stop:0.295455 rgba(171, 0, 255, 69), stop:0.426136 rgba(160, 0, 255, 208), stop:0.477581 rgba(71, 160, 255, 130), stop:0.517045 rgba(0, 189, 255, 255), stop:0.642045 rgba(71, 255, 137, 130), stop:0.715909 rgba(204, 255, 0, 130), stop:0.857955 rgba(255, 87, 0, 69), stop:1 rgba(255, 0, 0, 69)); color: rgb(255, 255, 255); border-style: outset; border-width:3px; border-radius:10px; border-color: white;")

        self.gridLayout_2.addWidget(self.label_3, 4, 0, 1, 1)

        self.normal = QRadioButton(self.centralwidget)
        self.normal.setObjectName(u"normal")
        self.normal.setFont(font2)
        self.normal.setStyleSheet(u"border-right-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 0, 0, 69), stop:0.147727 rgba(255, 0, 219, 145), stop:0.295455 rgba(171, 0, 255, 69), stop:0.426136 rgba(160, 0, 255, 208), stop:0.477581 rgba(71, 160, 255, 130), stop:0.517045 rgba(0, 189, 255, 255), stop:0.642045 rgba(71, 255, 137, 130), stop:0.715909 rgba(204, 255, 0, 130), stop:0.857955 rgba(255, 87, 0, 69), stop:1 rgba(255, 0, 0, 69));\n"
"border-left-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 0, 0, 69), stop:0.147727 rgba(255, 0, 219, 145), stop:0.295455 rgba(171, 0, 255, 69), stop:0.426136 rgba(160, 0, 255, 208), stop:0.477581 rgba(71, 160, 255, 130), stop:0.517045 rgba(0, 189, 255, 255), stop:0.642045 rgba(71, 255, 137, 130), stop:0.715909 rgba(204, 255, 0, 130), stop:0.857955 rgba(255, 87, 0, 69), stop:1 rgba(255, 0, 0, 69));\n"
"background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 0, 0, 69), stop:0.147727 rgba(255, 0, 219, 145), stop:0.295455 rgba(171, 0, 255, 69), stop:0.426136 rgb"
                        "a(160, 0, 255, 208), stop:0.477581 rgba(71, 160, 255, 130), stop:0.517045 rgba(0, 189, 255, 255), stop:0.642045 rgba(71, 255, 137, 130), stop:0.715909 rgba(204, 255, 0, 130), stop:0.857955 rgba(255, 87, 0, 69), stop:1 rgba(255, 0, 0, 69));\n"
"color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: white;\n"
"border-bottom-color: rgb(255, 255, 255);\n"
"border-top-color: rgb(255, 255, 255);\n"
"")
        self.normal.setChecked(True)

        self.gridLayout_2.addWidget(self.normal, 5, 1, 1, 1)

        self.tb_new_task_datetime = QDateTimeEdit(self.centralwidget)
        self.tb_new_task_datetime.setObjectName(u"tb_new_task_datetime")
        self.tb_new_task_datetime.setFont(font2)
        self.tb_new_task_datetime.setStyleSheet(u"background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 0, 0, 69), stop:0.147727 rgba(255, 0, 219, 145), stop:0.295455 rgba(171, 0, 255, 69), stop:0.426136 rgba(160, 0, 255, 208), stop:0.477581 rgba(71, 160, 255, 130), stop:0.517045 rgba(0, 189, 255, 255), stop:0.642045 rgba(71, 255, 137, 130), stop:0.715909 rgba(204, 255, 0, 130), stop:0.857955 rgba(255, 87, 0, 69), stop:1 rgba(255, 0, 0, 69));\n"
"color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width:3px;\n"
"border-radius:10px;\n"
"border-color: white;")

        self.gridLayout_2.addWidget(self.tb_new_task_datetime, 4, 1, 1, 2)

        self.tb_new_task_title = QLineEdit(self.centralwidget)
        self.tb_new_task_title.setObjectName(u"tb_new_task_title")
        font3 = QFont()
        font3.setPointSize(14)
        self.tb_new_task_title.setFont(font3)
        self.tb_new_task_title.setStyleSheet(u"background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 0, 0, 69), stop:0.147727 rgba(255, 0, 219, 145), stop:0.295455 rgba(171, 0, 255, 69), stop:0.426136 rgba(160, 0, 255, 208), stop:0.477581 rgba(71, 160, 255, 130), stop:0.517045 rgba(0, 189, 255, 255), stop:0.642045 rgba(71, 255, 137, 130), stop:0.715909 rgba(204, 255, 0, 130), stop:0.857955 rgba(255, 87, 0, 69), stop:1 rgba(255, 0, 0, 69));\n"
"border-style: outset;\n"
"border-width:3px;\n"
"border-radius:10px;\n"
"border-color: white;\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.tb_new_task_title, 0, 0, 1, 2)

        self.tb_new_task_description = QTextEdit(self.centralwidget)
        self.tb_new_task_description.setObjectName(u"tb_new_task_description")
        font4 = QFont()
        font4.setPointSize(14)
        font4.setBold(True)
        self.tb_new_task_description.setFont(font4)
        self.tb_new_task_description.setStyleSheet(u"background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 0, 0, 69), stop:0.147727 rgba(255, 0, 219, 145), stop:0.295455 rgba(171, 0, 255, 69), stop:0.426136 rgba(160, 0, 255, 208), stop:0.477581 rgba(71, 160, 255, 130), stop:0.517045 rgba(0, 189, 255, 255), stop:0.642045 rgba(71, 255, 137, 130), stop:0.715909 rgba(204, 255, 0, 130), stop:0.857955 rgba(255, 87, 0, 69), stop:1 rgba(255, 0, 0, 69));\n"
"border-style: outset;\n"
"border-width:4px;\n"
"border-radius:10px;\n"
"border-color: white;\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.tb_new_task_description, 1, 0, 1, 3)

        self.btn_new_task = QPushButton(self.centralwidget)
        self.btn_new_task.setObjectName(u"btn_new_task")
        font5 = QFont()
        font5.setPointSize(16)
        font5.setBold(True)
        self.btn_new_task.setFont(font5)
        self.btn_new_task.setStyleSheet(u"background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 0, 0, 69), stop:0.147727 rgba(255, 0, 219, 145), stop:0.295455 rgba(171, 0, 255, 69), stop:0.426136 rgba(160, 0, 255, 208), stop:0.477581 rgba(71, 160, 255, 130), stop:0.517045 rgba(0, 189, 255, 255), stop:0.642045 rgba(71, 255, 137, 130), stop:0.715909 rgba(204, 255, 0, 130), stop:0.857955 rgba(255, 87, 0, 69), stop:1 rgba(255, 0, 0, 69));\n"
"border-style: outset;\n"
"border-width:3px;\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"border-color: white;")

        self.gridLayout_2.addWidget(self.btn_new_task, 0, 2, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font2)
        self.label.setStyleSheet(u"background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 0, 0, 69), stop:0.147727 rgba(255, 0, 219, 145), stop:0.295455 rgba(171, 0, 255, 69), stop:0.426136 rgba(160, 0, 255, 208), stop:0.477581 rgba(71, 160, 255, 130), stop:0.517045 rgba(0, 189, 255, 255), stop:0.642045 rgba(71, 255, 137, 130), stop:0.715909 rgba(204, 255, 0, 130), stop:0.857955 rgba(255, 87, 0, 69), stop:1 rgba(255, 0, 0, 69));\n"
"border-right-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 0, 0, 69), stop:0.147727 rgba(255, 0, 219, 145), stop:0.295455 rgba(171, 0, 255, 69), stop:0.426136 rgba(160, 0, 255, 208), stop:0.477581 rgba(71, 160, 255, 130), stop:0.517045 rgba(0, 189, 255, 255), stop:0.642045 rgba(71, 255, 137, 130), stop:0.715909 rgba(204, 255, 0, 130), stop:0.857955 rgba(255, 87, 0, 69), stop:1 rgba(255, 0, 0, 69));\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label, 5, 0, 1, 1)

        self.high = QRadioButton(self.centralwidget)
        self.high.setObjectName(u"high")
        self.high.setFont(font2)
        self.high.setStyleSheet(u"background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 0, 0, 69), stop:0.147727 rgba(255, 0, 219, 145), stop:0.295455 rgba(171, 0, 255, 69), stop:0.426136 rgba(160, 0, 255, 208), stop:0.477581 rgba(71, 160, 255, 130), stop:0.517045 rgba(0, 189, 255, 255), stop:0.642045 rgba(71, 255, 137, 130), stop:0.715909 rgba(204, 255, 0, 130), stop:0.857955 rgba(255, 87, 0, 69), stop:1 rgba(255, 0, 0, 69));\n"
"color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: white;\n"
"border-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.high, 5, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 364, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MyToDoList", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:700; color:#f8f8f8;\">\u2a58 MyToDoList \u2a57</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:700; color:#ffffff;\">\u203b Do it &amp; Enjoy it \u203b</span></p></body></html>", None))
        self.label_6.setText("")
        self.label_7.setText("")
        self.label_8.setText("")
        self.label_5.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Date & Time", None))
        self.normal.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.tb_new_task_title.setInputMask("")
        self.tb_new_task_title.setText("")
        self.tb_new_task_title.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter task title...", None))
        self.tb_new_task_description.setDocumentTitle("")
        self.tb_new_task_description.setMarkdown("")
        self.tb_new_task_description.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter description ...", None))
        self.btn_new_task.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-weight:700; color:#ffffff;\">Priority :</span></p></body></html>", None))
        self.high.setText(QCoreApplication.translate("MainWindow", u"High", None))
    # retranslateUi

