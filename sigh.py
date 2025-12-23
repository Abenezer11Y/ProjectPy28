import random

def play():
    userAction = input("Enter a choice: \na.Rock\nb.paper\nc.scissors\n").upper()
    computer = random.randint(1,3)

    if userAction == "A":
        if computer == 1:
            print("Draw. The opponent chose paper too.")
        elif computer == 2:
            print("You Lose. \nThe opponent chose paper.")
        else:
            print("You Win! \nThe opponent chose scissors")

    elif userAction == "B":
        if computer == 1:
            print("You Win! \nThe opponent chose rock")
        elif computer == 2:
            print("Draw. The opponent chose paper too.")
        else:
            print("You Lose. \nThe opponent chose scissors.")
    elif userAction == "C": 
        if computer == 1:
            print("You Lose. \nThe opponent chose rock.")
        elif computer == 2:
            print("You Win! \nThe opponent chose paper")
        else:
            print("Draw. The opponent chose paper too.")
    ask = input("\nWanna play again? (y/n) ").upper()
    if ask == "Y":
        play()
    elif ask == "N":
        print("Thank you for playing!")

play()