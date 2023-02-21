import sys
import random
from functools import partial
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.nums = []
        self.i = 0
        self.j = 0

        self.buttons = [[self.ui.btn1, self.ui.btn2, self.ui.btn3, self.ui.btn4],
                        [self.ui.btn5, self.ui.btn6, self.ui.btn7, self.ui.btn8],
                        [self.ui.btn9, self.ui.btn10, self.ui.btn11, self.ui.btn12],
                        [self.ui.btn13, self.ui.btn14, self.ui.btn15, self.ui.btn16]]

        for i in range(4):
            for j in range(4):
                r = random.randint(1,16)
                while r in self.nums:
                    r = random.randint(1, 16)
                self.nums.append(r)
                self.buttons[i][j].setText(str(r))
                self.buttons[i][j].clicked.connect(partial(self.play, i, j))
                if r == 16:
                    self.buttons[i][j].setVisible(False)
                    self.empty_i = i
                    self.empty_j = j

    def play(self, i , j):
        if abs(i-self.empty_i) + abs(j-self.empty_j) == 1:
            self.buttons[self.empty_i][self.empty_j].setText(self.buttons[i][j].text())        
            self.buttons[i][j].setText("16")
            self.buttons[self.empty_i][self.empty_j].setVisible(True)
            self.buttons[i][j].setVisible(False)
            self.empty_i = i
            self.empty_j = j
        if self.check_win() == True:
            msg_box = QMessageBox
            msg_box.setText("You Win!")
            msg_box.exec_()

    def check_win(self):
        index = 1 
        for i in range(4):
            for j in range(4):
                if int(self.buttons[i][j].text()) != index:
                    return False
                index += 1
        return True


app = QApplication(sys.argv)

main_window = MainWindow()
main_window.show()


app.exec()
