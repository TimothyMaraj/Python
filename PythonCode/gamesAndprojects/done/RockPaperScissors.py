# can I make a gui to let users pick ?

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
    print("rock: 1")
    print("paper: 2")
    print("scissors: 3")
    print("pick: ",end=" ")
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
    if botPick == userPick: 
        print("tie")
    else: 
        if botPick == "rock" and userPick == "scissors" or botPick == "paper" and userPick == "rock" or botPick == "scissors" and userPick == "paper":
            print("bot won")
        else: 
            print("user win")

    return None

game()