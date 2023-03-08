import sys
import random
from functools import partial
from sudoku import Sudoku #https://github.com/jeffsieu/py-sudoku
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from main_window import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.grid_layout.setSpacing(0)
        self.ui.new_game.triggered.connect(self.new_game)
        self.ui.open_file.triggered.connect(self.open_file)
        self.line_edits = [[None for i in range(9)] for j in range(9)]

        self.new_game()


    def new_game(self):
        for i in reversed(range(self.ui.grid_layout.count())): 
            self.ui.grid_layout.itemAt(i).widget().setParent(None)
        for i in range(9):
            for j in range(9):
                new_cell = QLineEdit()
                new_cell.setAlignment(Qt.AlignCenter)
                new_cell.heightForWidth(10)
                new_cell.setStyleSheet("border-style: outset; border-width:0.5px; color: black; border-color: black; background-color: rgb(214, 197, 81);")
                self.ui.grid_layout.addWidget(new_cell, i, j)
                new_cell.textChanged.connect(partial(self.validation, i, j))
                self.line_edits[i][j] = new_cell
        puzzle = Sudoku(3, seed= random.randint(1, 1000)).difficulty(0.5) 
        for i in range(9):
            for j in range(9):
                if puzzle.board[i][j] != None:
                    self.line_edits[i][j].setText(str(puzzle.board[i][j]))
                    self.line_edits[i][j].setReadOnly(True)
                else:
                    self.line_edits[i][j].setText("")


    def validation(self, i, j, text):
        if text not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            self.line_edits[i][j].setText("")
        
        if self.check() == False:
            self.line_edits[i][j].setStyleSheet("border-style: outset; border-width:0.5px; color: red; border-color: black; background-color: rgb(214, 197, 81);")
        else:
            self.line_edits[i][j].setStyleSheet("border-style: outset; border-width:0.5px; color: black; border-color: black; background-color: rgb(214, 197, 81);")
            for k in range(9):
                for l in range(9):
                    if self.line_edits[k][l] == "":
                        break
            else:
                msg_box = QMessageBox()
                msg_box.setWindowTitle("Well Done!")
                msg_box.setText("You did this Sudoku puzzle!👌✨\nPress OK to start new one")
        

    def open_file(self):
        file_path = QFileDialog.getOpenFileName(self, "Open File..")[0]
        f = open(file_path, r)
        big_text = f.read()
        rows = big_text.split("\n")
        puzzle_board = [[None for i in range(9)] for j in range(9)]
        for i in range(len(rows)):
            cells = rows[i].split(" ")
            for j in range(len(cells)):
                puzzle_board[i][j] = int(cells[j])

        for i in range(9):
            for j in range(9):
                self.line_edits[i][j].setReadOnly(False)
                if puzzle_board[i][j] != 0:
                    self.line_edits[i][j].setText(str(puzzle_board[i][j]))
                    self.line_edits[i][j].setReadOnly(True)
                else:
                    self.line_edits[i][j].setText("")


    def check(self):
        #Check Rows
        for i in range(9):
            nums = []
            for j in range(9):
                num = self.line_edits[i][j].text()
                if num != "":
                    if num in nums:
                        return False
                    else:
                        nums.append(num)

        #Check Column
        for i in range(9):
            nums = []
            for j in range(9):
                num = self.line_edits[j][i].text()
                if num != "":
                    if num in nums:
                        return False
                    else:
                        nums.append(num)

        #Check Boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                nums = []
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        num = self.line_edits[k][l].text()
                        if num != "":
                            if num in nums:
                                return False
                            else:
                                nums.append(num)


        #Check Finished
        # for i in range(9):
        #     for j in range(9):
        #         if self.line_edits[j][i].text() == "":
        #             break
        # else:
        #     return True


        



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()