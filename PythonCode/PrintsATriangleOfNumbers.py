
def printTriangle(numOfRows): 
    numOfRows = int(numOfRows)

    for i in range(numOfRows): 
        for j in range(i): 
            print(i, end=" ")
        print('\n')


userInput = input("How many Rows: ")
printTriangle(userInput)

