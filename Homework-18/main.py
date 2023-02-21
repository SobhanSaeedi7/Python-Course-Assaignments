import sys
import random
from functools import partial
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader

xscore = 0
oscore = 0
draw = 0
mode = "pvc"

def set_mode():
    global mode
    if main_window.pvcraidiobuttom.isChecked() == True:
        mode = "pvc"
    elif main_window.pvpraidiobuttom.isChecked() == True:
        mode = "pvp"

def new_game (state):
    global player
    for i in range(3):
        for j in range(3):
            buttons[i][j].setText("")
            buttons[i][j].setStyleSheet("border-style: outset; border-width:2px; border-radius:10px; border-color: white; color: rgb(255, 255, 255);")
    player = 1
    if state == True:
        xscore = 0
        oscore = 0 
        draw = 0
        main_window.Xscore.setText(str(xscore))
        main_window.Oscore.setText(str(oscore))

def check():
    global xscore
    global oscore
    global draw
    if (buttons[0][0].text()=="X" and buttons[0][1].text()=="X" and buttons[0][2].text()=="X")\
         or (buttons[1][0].text()=="X" and buttons[1][1].text()=="X" and buttons[1][2].text()=="X")\
             or (buttons[2][0].text()=="X" and buttons[2][1].text()=="X" and buttons[2][2].text()=="X")\
                 or (buttons[0][0].text()=="X" and buttons[1][0].text()=="X" and buttons[2][0].text()=="X")\
                     or (buttons[0][1].text()=="X" and buttons[1][1].text()=="X" and buttons[2][1].text()=="X")\
                         or (buttons[0][2].text()=="X" and buttons[1][2].text()=="X" and buttons[2][2].text()=="X")\
                             or (buttons[0][0].text()=="X" and buttons[1][1].text()=="X" and buttons[2][2].text()=="X")\
                                 or (buttons[0][2].text()=="X" and buttons[1][1].text()=="X" and buttons[2][0].text()=="X"):
        msg_box = QMessageBox(text="✨Player X win!✨")
        msg_box.exec()
        xscore += 1
        main_window.Xscore.setText(str(xscore))
        new_game(False)

    elif (buttons[0][0].text()=="O" and buttons[0][1].text()=="O" and buttons[0][2].text()=="O")\
        or (buttons[1][0].text()=="O" and buttons[1][1].text()=="O" and buttons[1][2].text()=="O")\
            or (buttons[2][0].text()=="O" and buttons[2][1].text()=="O" and buttons[2][2].text()=="O")\
                or (buttons[0][0].text()=="O" and buttons[1][0].text()=="O" and buttons[2][0].text()=="O")\
                    or (buttons[0][1].text()=="O" and buttons[1][1].text()=="O" and buttons[2][1].text()=="O")\
                        or (buttons[0][2].text()=="O" and buttons[1][2].text()=="O" and buttons[2][2].text()=="O")\
                            or (buttons[0][0].text()=="O" and buttons[1][1].text()=="O" and buttons[2][2].text()=="O")\
                                or (buttons[0][2].text()=="O" and buttons[1][1].text()=="O" and buttons[2][0].text()=="O"):
        msg_box = QMessageBox(text="✨Player O win!✨")
        msg_box.exec()
        oscore += 1
        main_window.Oscore.setText(str(oscore))
        new_game(False)
    
    elif buttons[0][0].text()!="" and buttons[0][1].text()!="" and buttons[0][2].text()!="" and buttons[1][0].text()!="" and buttons[1][1].text()!="" and buttons[1][2].text()!="" and buttons[2][0].text()!="" and buttons[2][1].text()!="" and buttons[2][2].text()!="":
        msg_box = QMessageBox(text="🤝Draw!🤝")
        msg_box.exec()
        draw += 1
        main_window.draw.setText(str(draw))
        new_game(False)  


def play(r, c):
    global player
    global buttons

    set_mode()

    if player == 1:
        if buttons[r][c].text() == "":
            buttons[r][c].setText("X")
            buttons[r][c].setStyleSheet("color: red; background-color: pink; border-style: outset; border-width:2px; border-radius:10px; border-color: red;")
            player = 2
            main_window.turn.setText("O")
            main_window.turn.setStyleSheet("color: blue; background-color: lightblue; border-style: outset; border-width:2px; border-radius:10px; border-color: blue;")
            if mode =="pvc":
                while True:
                    r=random.randint(0, 2)
                    c=random.randint(0, 2)
                    if buttons[r][c].text()=="":
                        buttons[r][c].setText("O")
                        buttons[r][c].setStyleSheet("color: blue; background-color: lightblue; border-style: outset; border-width:2px; border-radius:10px; border-color: blue;")
                        player=1
                        main_window.turn.setText("X")
                        main_window.turn.setStyleSheet("color: red; background-color: pink; border-style: outset; border-width:2px; border-radius:10px; border-color: red;")
                        break
    
    elif player == 2:
        if buttons[r][c].text() == "":
            buttons[r][c].setText("O")
            buttons[r][c].setStyleSheet("color: blue; background-color: lightblue; border-style: outset; border-width:2px; border-radius:10px; border-color: blue;")
            player = 1
            main_window.turn.setText("X")
            main_window.turn.setStyleSheet("color: red; background-color: pink; border-style: outset; border-width:2px; border-radius:10px; border-color: red;")
            
    
    check()

def about():
    msg_box = QMessageBox(windowTitle="How to Play", text="Player vs Player mode:\nIn this mode two player play together turn by turn and the first person how put three shape (X or O) in a line win the game\n\nPlayer vs CPU mode:\nIn this mode one player play with computer same as another mode")
    msg_box.exec()

#__________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#__________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#__________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

app = QApplication(sys.argv)

player = 1

loader = QUiLoader()
main_window = loader.load("main_window.ui")
main_window.show()

buttons = [[main_window.btn1, main_window.btn2, main_window.btn3],
        [main_window.btn4, main_window.btn5, main_window.btn6],
        [main_window.btn7, main_window.btn8, main_window.btn9]]

for i in range(3):
    for j in range(3):
        buttons[i][j].clicked.connect(partial(play, i, j))
main_window.ngbtn.clicked.connect(partial(new_game, True))
main_window.about.clicked.connect(about)
app.exec()