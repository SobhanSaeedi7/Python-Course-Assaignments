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
    QPalette, QPixmap, QRadialGradient, QTransform, QFontDatabase)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QProgressBar,
    QPushButton, QSizePolicy, QSpinBox, QTabWidget,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        font_id = QFontDatabase.addApplicationFont("Font\Seven Segment.ttf")
        seven_segment = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(seven_segment, 9)
        MainWindow.setEnabled(True)
        MainWindow.resize(498, 372)
        MainWindow.setMouseTracking(False)
        MainWindow.setTabletTracking(False)
        MainWindow.setFocusPolicy(Qt.NoFocus)
        MainWindow.setContextMenuPolicy(Qt.DefaultContextMenu)
        MainWindow.setAcceptDrops(False)
        MainWindow.setToolTipDuration(-1)
        MainWindow.setLayoutDirection(Qt.RightToLeft)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: rgb(66, 66, 66);")
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMaximumSize(QSize(471, 321))
        font = QFont()
        font.setFamilies([u"Rockwell"])
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.tabWidget.setFont(font)
        self.tabWidget.setCursor(QCursor(Qt.ArrowCursor))
        self.tabWidget.setMouseTracking(False)
        self.tabWidget.setTabletTracking(False)
        self.tabWidget.setFocusPolicy(Qt.TabFocus)
        self.tabWidget.setAcceptDrops(False)
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(u"background-color: rgb(66, 66, 66);\n"
"color: rgb(255, 255, 255);")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.tabWidget.setElideMode(Qt.ElideMiddle)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.worldclock = QWidget()
        self.worldclock.setObjectName(u"worldclock")
        self.gmt = QLabel(self.worldclock)
        self.gmt.setObjectName(u"gmt")
        self.gmt.setGeometry(QRect(30, 40, 191, 61))
        font1 = QFont()
        font1.setFamilies([u"seven segment"])
        font1.setPointSize(24)
        font1.setBold(True)
        self.gmt.setFont(font1)
        self.gmt.setLayoutDirection(Qt.LeftToRight)
        self.gmt.setAutoFillBackground(False)
        self.gmt.setStyleSheet(u"color: rgb(154, 154, 154);\n"
"background-color:None;")
        self.gmt.setScaledContents(False)
        self.gmt.setAlignment(Qt.AlignCenter)
        self.gmt.setWordWrap(False)
        self.berlin = QLabel(self.worldclock)
        self.berlin.setObjectName(u"berlin")
        self.berlin.setGeometry(QRect(240, 170, 231, 61))
        self.berlin.setFont(font1)
        self.berlin.setLayoutDirection(Qt.LeftToRight)
        self.berlin.setAutoFillBackground(False)
        self.berlin.setStyleSheet(u"color: rgb(154, 154, 154);\n"
"background-color:None;")
        self.berlin.setScaledContents(False)
        self.berlin.setAlignment(Qt.AlignCenter)
        self.berlin.setWordWrap(False)
        self.tehran = QLabel(self.worldclock)
        self.tehran.setObjectName(u"tehran")
        self.tehran.setGeometry(QRect(260, 40, 191, 61))
        self.tehran.setFont(font1)
        self.tehran.setLayoutDirection(Qt.LeftToRight)
        self.tehran.setAutoFillBackground(False)
        self.tehran.setStyleSheet(u"color: rgb(154, 154, 154);\n"
"background-color:None;")
        self.tehran.setScaledContents(False)
        self.tehran.setAlignment(Qt.AlignCenter)
        self.tehran.setWordWrap(False)
        self.washington = QLabel(self.worldclock)
        self.washington.setObjectName(u"washington")
        self.washington.setGeometry(QRect(20, 170, 221, 61))
        self.washington.setFont(font1)
        self.washington.setLayoutDirection(Qt.LeftToRight)
        self.washington.setAutoFillBackground(False)
        self.washington.setStyleSheet(u"color: rgb(154, 154, 154);\n"
"background-color:None;")
        self.washington.setScaledContents(False)
        self.washington.setAlignment(Qt.AlignCenter)
        self.washington.setWordWrap(False)
        self.label_4 = QLabel(self.worldclock)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(310, 90, 91, 20))
        font2 = QFont()
        font2.setFamilies([u"Rockwell"])
        font2.setPointSize(16)
        font2.setBold(False)
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"background-color:None;\n"
"color: rgb(154, 154, 154);")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.worldclock)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 219, 181, 21))
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"background-color:None;\n"
"color: rgb(154, 154, 154);")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(self.worldclock)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(310, 220, 91, 20))
        font3 = QFont()
        font3.setFamilies([u"Rockwell"])
        font3.setPointSize(16)
        font3.setBold(True)
        self.label_6.setFont(font3)
        self.label_6.setStyleSheet(u"background-color:None;\n"
"color: rgb(154, 154, 154);")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_7 = QLabel(self.worldclock)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(330, 110, 49, 16))
        font4 = QFont()
        font4.setFamilies([u"Rockwell"])
        font4.setPointSize(12)
        font4.setBold(True)
        self.label_7.setFont(font4)
        self.label_7.setStyleSheet(u"background-color:None;\n"
"color: rgb(154, 154, 154);")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_8 = QLabel(self.worldclock)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(100, 240, 49, 21))
        self.label_8.setFont(font4)
        self.label_8.setStyleSheet(u"background-color:None;\n"
"color: rgb(154, 154, 154);")
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_9 = QLabel(self.worldclock)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(310, 240, 91, 20))
        self.label_9.setFont(font4)
        self.label_9.setStyleSheet(u"background-color:None;\n"
"color: rgb(154, 154, 154);")
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_10 = QLabel(self.worldclock)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(90, 90, 71, 41))
        self.label_10.setFont(font2)
        self.label_10.setStyleSheet(u"background-color:None;\n"
"color: rgb(154, 154, 154);")
        self.label_10.setAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.worldclock, "")
        self.alarm = QWidget()
        self.alarm.setObjectName(u"alarm")
        self.title_a = QLineEdit(self.alarm)
        self.title_a.setObjectName(u"title_a")
        self.title_a.setGeometry(QRect(210, 270, 151, 31))
        font5 = QFont()
        font5.setFamilies([u"Rockwell"])
        font5.setPointSize(11)
        font5.setBold(False)
        self.title_a.setFont(font5)
        self.title_a.setStyleSheet(u"border-color: rgb(162, 162, 162);\n"
"color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:7px;")
        self.title_a.setMaxLength(25)
        self.title_a.setFrame(True)
        self.title_a.setCursorPosition(0)
        self.title_a.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.title_a.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.title_a.setClearButtonEnabled(False)
        self.frame = QFrame(self.alarm)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 10, 471, 231))
        self.frame.setStyleSheet(u"border-color: rgb(162, 162, 162);\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 451, 21))
        font6 = QFont()
        font6.setPointSize(11)
        font6.setBold(True)
        self.label_3.setFont(font6)
        self.label_3.setStyleSheet(u"border-color: rgb(162, 162, 162);\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:4px;\n"
"border-bottom-color: rgb(66, 66, 66);")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.gridLayoutWidget_2 = QWidget(self.frame)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(20, 30, 431, 161))
        self.gl_a = QGridLayout(self.gridLayoutWidget_2)
        self.gl_a.setObjectName(u"gl_a")
        self.gl_a.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 200, 451, 24))
        self.pushButton.setAutoExclusive(False)
        self.add_a = QPushButton(self.alarm)
        self.add_a.setObjectName(u"add_a")
        self.add_a.setGeometry(QRect(370, 250, 91, 51))
        font7 = QFont()
        font7.setPointSize(32)
        self.add_a.setFont(font7)
        self.add_a.setStyleSheet(u"border-color: rgb(162, 162, 162);\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:7px;")
        self.label_11 = QLabel(self.alarm)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(50, 250, 101, 21))
        font8 = QFont()
        font8.setPointSize(14)
        font8.setBold(True)
        self.label_11.setFont(font8)
        self.label_11.setStyleSheet(u"background-color: None;\n"
"border-color: rgb(162, 162, 162);\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:4px;\n"
"color: white;\n"
"border-bottom-color: rgb(66, 66, 66);")
        self.label_11.setAlignment(Qt.AlignCenter)
        self.label_12 = QLabel(self.alarm)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(230, 250, 101, 21))
        self.label_12.setFont(font8)
        self.label_12.setStyleSheet(u"background-color: None;\n"
"border-color: rgb(162, 162, 162);\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:4px;\n"
"color: white;\n"
"border-bottom-color: rgb(66, 66, 66);")
        self.label_12.setAlignment(Qt.AlignCenter)
        self.min_a = QSpinBox(self.alarm)
        self.min_a.setObjectName(u"min_a")
        self.min_a.setGeometry(QRect(110, 270, 91, 31))
        self.min_a.setStyleSheet(u"border-color: rgb(162, 162, 162);\n"
"border-left-color: rgb(66, 66, 66);\n"
"border-style: outset;\n"
"border-width:2px;\n"
"")
        self.min_a.setAlignment(Qt.AlignCenter)
        self.min_a.setValue(30)
        self.hour_a = QSpinBox(self.alarm)
        self.hour_a.setObjectName(u"hour_a")
        self.hour_a.setGeometry(QRect(0, 270, 91, 31))
        self.hour_a.setStyleSheet(u"border-color: rgb(162, 162, 162);\n"
"border-right-color: rgb(66, 66, 66);\n"
"border-style: outset;\n"
"border-width:2px;\n"
"")
        self.hour_a.setAlignment(Qt.AlignCenter)
        self.hour_a.setValue(12)
        self.label_13 = QLabel(self.alarm)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(60, 270, 81, 31))
        self.label_13.setStyleSheet(u"border-color: rgb(162, 162, 162);\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-right-color: rgb(66, 66, 66);\n"
"border-left-color: rgb(66, 66, 66);")
        self.label_13.setAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.alarm, "")
        self.label_13.raise_()
        self.title_a.raise_()
        self.frame.raise_()
        self.add_a.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.min_a.raise_()
        self.hour_a.raise_()
        self.stopwatch = QWidget()
        self.stopwatch.setObjectName(u"stopwatch")
        self.stop_watch = QLabel(self.stopwatch)
        self.stop_watch.setObjectName(u"stop_watch")
        self.stop_watch.setGeometry(QRect(0, 10, 341, 61))
        font9 = QFont()
        font9.setFamilies([u"seven segment"])
        font9.setPointSize(32)
        font9.setBold(True)
        self.stop_watch.setFont(font9)
        self.stop_watch.setLayoutDirection(Qt.LeftToRight)
        self.stop_watch.setAutoFillBackground(False)
        self.stop_watch.setStyleSheet(u"color: rgb(154, 154, 154);\n"
"background-color:None;")
        self.stop_watch.setScaledContents(False)
        self.stop_watch.setAlignment(Qt.AlignCenter)
        self.stop_watch.setWordWrap(False)
        self.start_sw = QPushButton(self.stopwatch)
        self.start_sw.setObjectName(u"start_sw")
        self.start_sw.setGeometry(QRect(350, 10, 119, 31))
        font10 = QFont()
        font10.setPointSize(12)
        self.start_sw.setFont(font10)
        self.start_sw.setStyleSheet(u"border-color: rgb(162, 162, 162);\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;")
        self.flag_sw = QPushButton(self.stopwatch)
        self.flag_sw.setObjectName(u"flag_sw")
        self.flag_sw.setGeometry(QRect(350, 50, 119, 31))
        self.flag_sw.setFont(font10)
        self.flag_sw.setStyleSheet(u"border-color: rgb(162, 162, 162);\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;")
        self.reset_sw = QPushButton(self.stopwatch)
        self.reset_sw.setObjectName(u"reset_sw")
        self.reset_sw.setGeometry(QRect(350, 270, 119, 31))
        self.reset_sw.setFont(font10)
        self.reset_sw.setStyleSheet(u"border-color: rgb(162, 162, 162);\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;")
        self.stop_sw = QPushButton(self.stopwatch)
        self.stop_sw.setObjectName(u"stop_sw")
        self.stop_sw.setGeometry(QRect(350, 90, 119, 31))
        self.stop_sw.setFont(font10)
        self.stop_sw.setStyleSheet(u"border-color: rgb(162, 162, 162);\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;")
        self.gridLayoutWidget = QWidget(self.stopwatch)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(9, 100, 331, 201))
        self.gl_sw = QGridLayout(self.gridLayoutWidget)
        self.gl_sw.setObjectName(u"gl_sw")
        self.gl_sw.setContentsMargins(0, 0, 0, 0)
        self.tabWidget.addTab(self.stopwatch, "")
        self.timer = QWidget()
        self.timer.setObjectName(u"timer")
        self.start_t = QPushButton(self.timer)
        self.start_t.setObjectName(u"start_t")
        self.start_t.setGeometry(QRect(350, 10, 119, 31))
        self.start_t.setFont(font10)
        self.start_t.setStyleSheet(u"border-color: rgb(162, 162, 162);\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;")
        self.reset_t = QPushButton(self.timer)
        self.reset_t.setObjectName(u"reset_t")
        self.reset_t.setGeometry(QRect(350, 270, 119, 31))
        self.reset_t.setFont(font10)
        self.reset_t.setStyleSheet(u"border-color: rgb(162, 162, 162);\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;")
        self.stop_t = QPushButton(self.timer)
        self.stop_t.setObjectName(u"stop_t")
        self.stop_t.setGeometry(QRect(350, 50, 119, 31))
        self.stop_t.setFont(font10)
        self.stop_t.setStyleSheet(u"border-color: rgb(162, 162, 162);\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;")
        self.sec_t = QSpinBox(self.timer)
        self.sec_t.setObjectName(u"sec_t")
        self.sec_t.setGeometry(QRect(240, 200, 71, 41))
        self.sec_t.setStyleSheet(u"border-color: rgb(162, 162, 162);\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:1px;")
        self.sec_t.setAlignment(Qt.AlignCenter)
        self.sec_t.setValue(30)
        self.min_t = QSpinBox(self.timer)
        self.min_t.setObjectName(u"min_t")
        self.min_t.setGeometry(QRect(130, 200, 71, 41))
        font11 = QFont()
        font11.setPointSize(9)
        self.min_t.setFont(font11)
        self.min_t.setStyleSheet(u"border-color: rgb(162, 162, 162);\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:1px;")
        self.min_t.setAlignment(Qt.AlignCenter)
        self.min_t.setValue(1)
        self.hour_t = QSpinBox(self.timer)
        self.hour_t.setObjectName(u"hour_t")
        self.hour_t.setGeometry(QRect(20, 200, 71, 41))
        self.hour_t.setStyleSheet(u"border-color: rgb(162, 162, 162);\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:1px;")
        self.hour_t.setAlignment(Qt.AlignCenter)
        self.set = QPushButton(self.timer)
        self.set.setObjectName(u"set")
        self.set.setGeometry(QRect(20, 260, 291, 31))
        self.set.setStyleSheet(u"border-color: rgb(162, 162, 162);\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:5px;")
        self.label = QLabel(self.timer)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 200, 21, 41))
        font12 = QFont()
        font12.setPointSize(27)
        self.label.setFont(font12)
        self.label.setStyleSheet(u"background-color: None;\n"
"")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setOpenExternalLinks(False)
        self.label_2 = QLabel(self.timer)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(210, 200, 21, 41))
        self.label_2.setFont(font12)
        self.label_2.setStyleSheet(u"background-color: None;\n"
"")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setOpenExternalLinks(False)
        self.timer_2 = QLabel(self.timer)
        self.timer_2.setObjectName(u"timer_2")
        self.timer_2.setGeometry(QRect(60, 80, 201, 51))
        font13 = QFont()
        font13.setFamilies([u"seven segment"])
        font13.setPointSize(32)
        font13.setBold(True)
        font13.setItalic(False)
        self.timer_2.setFont(font13)
        self.timer_2.setStyleSheet(u"color: rgb(154, 154, 154);\n"
"background-color: None;")
        self.timer_2.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.timer)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QRect(20, 140, 291, 23))
        font14 = QFont()
        font14.setStrikeOut(False)
        font14.setKerning(True)
        self.progressBar.setFont(font14)
        self.progressBar.setMouseTracking(False)
        self.progressBar.setTabletTracking(False)
        self.progressBar.setFocusPolicy(Qt.NoFocus)
        self.progressBar.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.progressBar.setAcceptDrops(False)
        self.progressBar.setToolTipDuration(-1)
        self.progressBar.setLayoutDirection(Qt.RightToLeft)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setStyleSheet(u"")
        self.progressBar.setValue(100)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.BottomToTop)
        self.tabWidget.addTab(self.timer, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 498, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Clock", None))
        self.gmt.setText(QCoreApplication.translate("MainWindow", u"0 : 0 : 0", None))
        self.berlin.setText(QCoreApplication.translate("MainWindow", u"0 : 0 : 0", None))
        self.tehran.setText(QCoreApplication.translate("MainWindow", u"0 : 0 : 0", None))
        self.washington.setText(QCoreApplication.translate("MainWindow", u"0 : 0 : 0", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Tehran", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Washington", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Berlin", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"IRAN", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"U.S.A", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Germany", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"G.M.T", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.worldclock), QCoreApplication.translate("MainWindow", u"World Clock", None))
        self.title_a.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Title...", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Alarms", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Set Changes", None))
        self.add_a.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.alarm), QCoreApplication.translate("MainWindow", u"Alarm", None))
        self.stop_watch.setText(QCoreApplication.translate("MainWindow", u"0:0:0.0", None))
        self.start_sw.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.flag_sw.setText(QCoreApplication.translate("MainWindow", u"Flag", None))
        self.reset_sw.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.stop_sw.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.stopwatch), QCoreApplication.translate("MainWindow", u"Stop Watch", None))
        self.start_t.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.reset_t.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.stop_t.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.set.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.timer_2.setText(QCoreApplication.translate("MainWindow", u"0 : 1 : 30", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.timer), QCoreApplication.translate("MainWindow", u"Timer", None))
    # retranslateUi

