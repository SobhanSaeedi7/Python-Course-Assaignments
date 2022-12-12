#Tic-Tac-Toe
import pyfiglet
from termcolor import colored
import random
import time
#Functions
def show():
    for row in game_board:
        for cell in row:
            print(cell, end=" ")
        print( )

def check_game_P(l):
        if l[1][1] == l[1][2] == l[1][3] == (colored("X", "red")) or l[2][1] == l[2][2] == l[2][3] == (colored("X", "red")) or l[3][1] == l[3][2] == l[3][3] == (colored("X", "red")) or l[1][1] == l[2][1] == l[3][1] == (colored("X", "red")) or l[1][2] == l[2][2] == l[3][2] == (colored("X", "red")) or l[1][3] == l[2][3] == l[3][3] == (colored("X", "red")) or l[1][1] == l[2][2] == l[3][3] == (colored("X", "red")) or l[1][3] == l[2][2] == l[3][1] == (colored("X", "red")):
            print("Player 1 win🎉💖")
            end = time.time()
            print("You played : ",(int(end - start )),"second")
            exit()
        elif l[1][1] == l[1][2] == l[1][3] == (colored("O", "blue")) or l[2][1] == l[2][2] == l[2][3] == (colored("O", "blue")) or l[3][1] == l[3][2] == l[3][3] == (colored("O", "blue")) or l[1][1] == l[2][1] == l[3][1] == (colored("O", "blue")) or l[1][2] == l[2][2] == l[3][2] == (colored("O", "blue")) or l[1][3] == l[2][3] == l[3][3] == (colored("O", "blue")) or l[1][1] == l[2][2] == l[3][3] == (colored("O", "blue")) or l[1][3] == l[2][2] == l[3][1] == (colored("O", "blue")):
            print("player 2 win🎉💙")
            end = time.time()
            print("You played : ",(int(end - start )),"second")
            exit()
        elif l[1][1]!= "_" and l[1][2]!= "_" and l[1][3]!= "_" and l[2][1]!= "_" and l[2][2]!= "_" and l[2][3]!= "_" and l[3][1]!= "_" and l[3][2]!= "_" and l[3][3] != "_":
            print("The game equalised🤝")
            end = time.time()
            print("You played : ",(int(end - start )),"second")
            exit()

def check_game_C(l):
        if l[1][1] == l[1][2] == l[1][3] == (colored("X", "red")) or l[2][1] == l[2][2] == l[2][3] == (colored("X", "red")) or l[3][1] == l[3][2] == l[3][3] == (colored("X", "red")) or l[1][1] == l[2][1] == l[3][1] == (colored("X", "red")) or l[1][2] == l[2][2] == l[3][2] == (colored("X", "red")) or l[1][3] == l[2][3] == l[3][3] == (colored("X", "red")) or l[1][1] == l[2][2] == l[3][3] == (colored("X", "red")) or l[1][3] == l[2][2] == l[3][1] == (colored("X", "red")):
            print("Player 1 win🎉💖")
            end = time.time()
            print("You played : ",(int(end - start )),"second")
            exit()
        elif l[1][1] == l[1][2] == l[1][3] == (colored("O", "blue")) or l[2][1] == l[2][2] == l[2][3] == (colored("O", "blue")) or l[3][1] == l[3][2] == l[3][3] == (colored("O", "blue")) or l[1][1] == l[2][1] == l[3][1] == (colored("O", "blue")) or l[1][2] == l[2][2] == l[3][2] == (colored("O", "blue")) or l[1][3] == l[2][3] == l[3][3] == (colored("O", "blue")) or l[1][1] == l[2][2] == l[3][3] == (colored("O", "blue")) or l[1][3] == l[2][2] == l[3][1] == (colored("O", "blue")):
            print("Camputer 2 win🎉👾")
            end = time.time()
            print("You played : ",(int(end - start )),"second")
            exit()
        elif l[1][1]!= "_" and l[1][2]!= "_" and l[1][3]!= "_" and l[2][1]!= "_" and l[2][2]!= "_" and l[2][3]!= "_" and l[3][1]!= "_" and l[3][2]!= "_" and l[3][3] != "_":
            print("The game equalised🤝")
            end = time.time()
            print("You played : ",(int(end - start )),"second")
            exit()

#Start
title = pyfiglet.Figlet(font = "isometric2")
print(colored(title.renderText("Tik"), "blue"))
print(colored(title.renderText("Tak"), "green"))
print(colored(title.renderText("Toe"), "red"))

while True:
    mode = input("How do you want to play? camputer with player mode(C) or player with player mode(P) ; ")
    start = time.time()
#Player with player mode
    if mode == "P":
        game_board = [["⇲","1","2","3"],
                ["1","_", "_", "_"],
                ["2","_", "_", "_"],
                ["3","_", "_", "_"]]

        show()
        while True:
            print("Player 1 : ")

            while True :
                row = int(input("Enter row of your choice : "))
                col = int (input("Enter column of your choice : "))
                if 1<=row<=3 and 1<=col<=3 :
                    if game_board[row][col] == "_":
                        game_board[row][col] = (colored("X", "red"))
                        break
                    else :
                     print("Select empty place!")
                else :
                    print ("Enter number 1 , 2 or 3")

            show()
            check_game_P(game_board)

            print("Player 2 : ")
            while True :
                row = int(input("Enter row of your choice : "))
                col = int (input("Enter column of your choice : "))
                if 1<=row<=3 and 1<=col<=3 :
                    if game_board[row][col] == "_":
                        game_board[row][col] = (colored("O", "blue"))
                        break
                    else :
                        print("Select empty place!")
                else :
                    print ("Enter number 1 , 2 or 3")
            show()
            check_game_P(game_board)
#Player with camputer mode
    elif mode == "C":
        game_board = [["⇲","1","2","3"],
                ["1","_", "_", "_"],
                ["2","_", "_", "_"],
                ["3","_", "_", "_"]]

        show()
        while True:
            print("Player 1 : ")

            while True :
                row = int(input("Enter row of your choice : "))
                col = int (input("Enter column of your choice : "))
                if 1<=row<=3 and 1<=col<=3 :
                    if game_board[row][col] == "_":
                        game_board[row][col] = (colored("X", "red"))
                        break
                    else :
                     print("Select empty place!")
                else :
                    print ("Enter number 1 , 2 or 3")

            show()
            check_game_C(game_board)

            print("Camputer is choosing... ")
            while True :
                raw = random.randint(1, 3)
                col = random.randint(1, 3)
                if game_board[col][row] == "_":
                    game_board[col][row] = (colored("O", "blue"))
                    break
                else:
                    continue
            show()
            check_game_C(game_board)
#Wrong input mode
    elif mode == "exit":
        exit()
    else:
        print("Please enter 'C' (camputer with player), 'P' (player with player) or 'exit' to exit")




