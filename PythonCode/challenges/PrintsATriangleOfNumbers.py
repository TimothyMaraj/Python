#https://pynative.com/python-basic-exercise-for-beginners/
# above is some challenges


def printTriangle(numOfRows): 
    numOfRows = int(numOfRows)

    for i in range(numOfRows+1): 
        for j in range(1+i): 
            print(i, end=" ")
        print('\n')


userInput = input("Count to what number?: ")
printTriangle(userInput)

