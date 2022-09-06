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
    #botPick = botChoice()
    #userPick = userChoice()
    #print(botPick,userPick)

    botPick = "rock"
    userPick = "paper"
    #need to to logic here for the check

    if botPick == "rock" and userPick == "rock":
        print("tie") 
    elif botPick == "rock" and userPick == "paper": 
        print("user win")
    else: 
        print("tf bro")

game()