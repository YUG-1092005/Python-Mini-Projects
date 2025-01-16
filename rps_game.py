print("--------ROCK PAPER SCISSOR GAME----------")
import random

while True:

    choose = input("Choose Rock, Paper or Scissor or Exit: ").capitalize()
    List = ["Rock", "Paper", "Scissor"]
    r = random.choice(List)

    if (
        (choose == "Rock" and r == "Scissor")
        or (choose == "Scissor" and r == "Paper")
        or (choose == "Paper" and r == "Rock")
    ):
        print("You won")

    elif choose == r:
        print("Tie, play again")

    elif choose =="Exit":
        print("Byee")
        break

    else:
        print("AI won!")
    
