from cProfile import run
import random
import os 


# need a func that generates random num
# need a func that welcomes user
# need a func that validates user input, and counts down from 3 guess or some

def randomNumber(a,b): 
    return random.randrange(a,b,1)

def welcomeUser(): 
    print("Hello {}. Let's play a game \n".format(os.getlogin()))

def startGame(): 
   a,b = input("What two positive numbers would you like to guess between ? ").split()
   a = int(a)
   b = int(b)
   print("Now lets begin! \n")
   randNum = randomNumber(a,b)

   userGuess = -1
   tries = 3

   while tries != 0: 
    userGuess = int(input("Take a guess: "))
    if userGuess == randNum: 
        print("Congrants you guess right!")
        break
    else: 
        tries -= 1
        print("try again... remaining tries {}".format(tries))
        
    if tries == 0: 
        print("Better Luck next time...")
        print("Random Num was: {}".format(randNum))


def runProgram(): 
    welcomeUser()
    startGame()

runProgram()