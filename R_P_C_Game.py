from random import *


def gamewin(computer, you):
    if computer == you:
        return None
    if computer == 'r':
        if you == 'c':
            return False
        else:
            you == 'p'
            return True
    elif computer == 'p':
        if you == 'r':
            return False
        else:
            you == 'c'
            return True
    elif computer == 'c':
        if you == 'p':
            return False
        else:
            you == 'r'
            return True

i = 0
j = 0
a = 1

while (a):
    randno = randint(1, 3)
    if randno == 1:
        computer = 'r'
    elif randno == 2:
        computer = 'p'
    elif randno == 3:
        computer = 'c'
    you = input("You turn : Rock(r) Paper(p) Scissor(c)\n")
    print(f"computer choose {computer}")
    print(f"you choose {you}")

    a = gamewin(computer, you)
    if a == None:
        print("Game is tie")
    elif a:
        print("Your are win")
        j += 1
    else:
        print("Your are lose")
        i += 1
    print("You win ",j,"Computer win ",i,"\n\n\n")
    a = int(input("Do you again play type '1' otherwise '0'"))