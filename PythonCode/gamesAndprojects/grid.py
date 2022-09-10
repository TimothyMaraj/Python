
# count is not working
# local variable and scope issue



#idea for a grid simiplified 
# use a dict 
# the key would be the list of cordinates
# the value then would be the grid value
import random
import time
def ranNumber(): 
    return random.randrange(1,2,1)

def defineGrid(row,col): 
    gameGrid = {}
    for i in range(row): 
        for j in range(col): 
                if ranNumber() == 0:  
                    gameGrid[(i,j)]=["O"]
                else: 
                    gameGrid[(i,j)]=["X"]



    return gameGrid

#def changeGrid(row,col): 


    #how can i take an input 
    # and then change a given number 
    # of col and row

def printGrid(grid_in,row,col): 
    for i in range(row):
        for j in range(col): 
            print(grid_in[(i,j)],end=" ")
        print("")
    
    print("")
    print("")
    print("")


def userInput(): 
    userData = int(input("gimme a number to make the grid: "))
    return userData

def changeCells(grid,grid_size):
    
    # so we iterate r and c till they are == to the row and column we need one by one so first value 
    # has 0,0? and we serach row +1 and col +1 to see if they are a live 
    row = col = grid_size
    for r in range(grid_size): 
        for c in range(grid_size):
            count = findNeighbor(grid,(r,c),grid_size)
            if count>1: 
                #change cell to "alive or what that might be"
                grid[(r,c)] = ["X"]
                print("updates")
            else: 
                grid[(r,c)] = ["O"]
                print("no update")
    
    printGrid(grid,grid_size,grid_size)
    #print("\n")
            

# can customie it so that any char is alive and vice cera for dead

def findNeighbor(grid,key_coordinate,grid_size): 
    row , col = key_coordinate
    count = 0
    print(row,col)
    if grid.get((row-1,col)) == ["X"]: 
        count+=1
        print("A")
    else: 
        if grid.get((row,col-1)) == ["X"]:
            cout+=1
            print("B")
        else: 
            if grid.get((row+1,col)) == ["X"]:
                count+1
                print("C")
            else: 
                if grid.get((row,col+1)) == ["X"]:
                    count+1
                    print("D")
    
    print(count)
    
    return count

def some_tests(): 

    row = col = userInput()
    grid_made = {}
    grid_made = defineGrid(row,col)
    i = 0
    printGrid(grid_made,row,col)
    while i != 1: 
        changeCells(grid_made,row)
        time.sleep(3)
   # print(grid_made.keys())
   # print(grid_made.values())


some_tests()