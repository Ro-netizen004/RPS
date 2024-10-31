#Rock Paper Scissors Game
import random
Running=True
while Running:
    Options=["rock","paper","scissors"]
    Player_2=random.choice(Options)
    while True:
        Player_1=input("Choose between Rock, Paper and Scissors.\nMake your choice: ")
        if not Player_1.lower() in Options:
            print("Invalid choice.")
        else:
            break
    print(f"You chose {Player_1}.")
    print(f"Player 2 chose {Player_2}.")
    if Player_1.lower()=="rock" and Player_2=="scissors":
        print("You win!")
    elif Player_1.lower()=="paper" and Player_2=="rock":
        print("You win!")
    elif Player_1.lower()=="scissors" and Player_2=="paper":
        print("You win!")
    elif Player_1==Player_2:
        print("It's a draw!")
    else:
        print("You lose :(")

    decision=input("Play again? (y/n) ").lower()
    Choices=("y","n")
    while decision not in Choices:
        print("Invalid Choice.")
        decision=input("Play again? (y/n) ").lower()
        
    if decision=="n":
        Running=False



