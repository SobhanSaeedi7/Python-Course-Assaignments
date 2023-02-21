from random import choice

kind = ['F', 'B']

uc = 0
p2c = 0
p3c = 0

scores = [0, 0, 0]

for i in range(5):
    print("Turn",i+1,"/ 5")
    while True:
        user_choice = input('Enter your choice;"F" for forehand or "B" for backhand : ')
        if user_choice == "F":
            print("Your choice : ✋")
            uc = 1
            break
        elif user_choice == "B":
            print("Your choice : 🤚")
            uc = 2
            break
        else: 
            print('Just enter "F" or "B"')

    player2_choice = choice(kind)
    if player2_choice == "F":
        print("Player 2 choice : ✋")
        p2c = 1
    elif player2_choice == "B":
        print("Player 2 choice : 🤚")
        p2c = 2

    player3_choice = choice(kind)
    if player3_choice == "F":
        print("Player 3 choice : ✋")
        p3c = 1
    elif player3_choice == "B":
        print("Player 3 choice : 🤚")
        p3c = 2

    if p2c == p3c and uc != p2c:
        scores[0] += 1
        print("You win this turn")
    elif uc == p3c and p2c != uc:
        scores[1] += 1
        print("Player 2 win this turn")
    elif uc == p2c and p3c != uc:
        scores[2] += 1
        print("Player 3 win this turn")
    else:
        print("This turn didn`t have winner!")

print('Your sccore:',scores[0])
print('Player 2 sccore:',scores[1])
print('Player 3 sccore:',scores[2])

if scores.index(max(scores)) == 0 :
    if scores[0] != scores[1] and scores[0] != scores[2]:
        print("You win✨")
elif scores.index(max(scores)) == 1:
    if scores[1] != scores[0] and scores[1] != scores[2]:
        print("Player 2 win✨")
elif scores.index(max(scores)) == 2:
    if scores[2] != scores[1] and scores[2] != scores[0]:
        print("Player 3 win✨")




