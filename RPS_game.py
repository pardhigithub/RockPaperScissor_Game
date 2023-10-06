import random as r
while True:
    user = input("enter your choice: ")
    action = ["rock","paper","scissors"]
    computer = r.choice(action)
    print(computer)
    if user == computer:
        print("both are winnwrs")
    elif user == "rock":
        if computer == "paper":
            print("computer is win")
        else:
            print("you win")
    elif user == "paper":
        if computer == "rock":
            print("you win")
        else:
            print("computer win")
    elif user == "scissors":
        if computer == "paper":
            print("you win")
        else:
            print("computer win")
    play_again = input("Do you want to continue yes / no: ")
    if play_again == "Y" or play_again == "y":
        continue
    else:
        break