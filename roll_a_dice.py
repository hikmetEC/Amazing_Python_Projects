import random 

def roll_a_dice():
    return random.randint(1,6)

def func():
    flag = input("Would you like to roll a dice?(Y=yes, N=no):\n ")
    if flag == "Y":
        print(roll_a_dice())
        func()
    else:
        flag2 = input("Would you like exit?(Y=yes, N=no):\n")
        if flag2 == "Y":
            exit()
        else:
            func()
func()
