import random

def botChoice(): 
    pick = random.randrange(1,3,1)
    if pick == 1: 
        return "rock"
    elif pick == 2: 
        return "paper"
    else: 
        return "scissors"

def userChoice(): 
    print("Welcome to the game:")
    userInput = ""
    print("pick: ")
    print("rock: 1")
    print("paper: 2")
    print("scissors: 3")

    userInput = int(input())
    
    if userInput == 1: 
        return "rock"
    elif userInput == 2: 
        return "paper"
    else: 
        return "scissors"
    

def game(): 
    botPick = botChoice()
    userPick = userChoice()
    print(botPick,userPick)

    botPick = "rock"
    userPick = "rock"

    if botPick == userChoice:
        print("user won")
    elif botPick == "paper" and userChoice == "scissor":
        print("user won")
    elif botPick == "scissor" and userChoice == "rock":
        print("user won")
    elif botPick == "paper" and userChoice == "rock":
        print("bot won")
    elif botPick == "scissor" and userChoice == "paper":
        print("bot won")
    elif botPick == "rock" and userChoice == "scissor":
        print("bot won")
    else: 
        print("tie")

game()