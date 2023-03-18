import sys
from random import randint
from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.num = randint(1, 100)
        self.turn = 0

        self.ui.check_game.clicked.connect(self.check)
        self.ui.new_game.clicked.connect(self.new_game)


    def check(self):
        self.turn += 1
        self.ui.turn.setText(f"Turn : {self.turn}")
        guess = int(self.ui.guess_number.text())

        if guess > self.num:
            self.ui.order.setText("Go : Down ⬇")
            if self.turn >= 20:
                self.new_game()
                msg_box = QMessageBox()
                msg_box.setWindowTitle("Oops🥴")
                msg_box.setText("You Couldn`t Guess Number In 20 Turn😕")
                msg_box.exec()
            


        elif guess < self.num:
            self.ui.order.setText("Go : Up ⬆")
            if self.turn >= 20:
                self.new_game()
                msg_box = QMessageBox()
                msg_box = QMessageBox()
                msg_box.setWindowTitle("Oops🥴")
                msg_box.setText("You Couldn`t Guess Number In 20 Turn😕")
                msg_box.exec()



        else:
            self.new_game()
            msg_box = QMessageBox()
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Well Done👌")
            msg_box.setText("You Guessed Number True✨")
            msg_box.exec()


    def new_game(self):
        self.num = randint(0, 100)
        self.turn = 0      
        self.ui.guess_number.setValue(0)
        self.ui.order.setText("Go : ")
        self.ui.turn.setText("Turn : 0")



if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    app.exec()
