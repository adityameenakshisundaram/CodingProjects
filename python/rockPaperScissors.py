import random as rn 
choices = ["Rock", "Paper", "Scissors"]
compChoice = rn.choice(choices)
print(compChoice)

#establish the values for the points
cPoints = 0 
uPoints = 0

#determine who wins the game
cont = True
while cont == True:
    userChoice = input("What do you want to pick (Rock, Paper, Scissors)")

    if compChoice == userChoice:
        print("Tie")
    if compChoice == "Scissors" and userChoice == "Rock" or compChoice == "Paper" and userChoice == "Scissors" or compChoice == "Rock" and userChoice == "Paper":
        uPoints = uPoints + 1
        print("User Wins")
    if compChoice == "Scissors" and userChoice == "Paper" or compChoice == "Paper" and userChoice == "Rock" or compChoice == "Rock" and userChoice == "Scissors":
        cPoints = cPoints +1
        print("Computer wins")
    
    ask = input("Would you like to continue(Yes or No)")
    if ask == "yes":
        cont = True
    else:
        cont = False
print("User points:", uPoints, "Computer Points:", cPoints)
if cPoints > uPoints:
    print("The computer wins the game, better luck next time")
elif cPoints<uPoints:
    print("You win the game, great job")
else:
    print("This is unfortunate as the game ends in a tie")
