import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)





if __name__ == "__main__":
    app = QApplication()

    main_window = MainWindow()
    main_window.show()

    app.exec()