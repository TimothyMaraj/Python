def countToTwenty(): 
    for i in range(1,21,1): 
        print(i,end=" ")

def OneMillionPrint(): 
    for i in range(1,1000001,1): 
        print(i)

def sumOfMillion():
    Mlist = []
    for i in range(1,1000001,1):
        Mlist.append(i)
    print(min(Mlist))
    print(max(Mlist))
    print(sum(Mlist))

def listOfThrees(): 
    lst = []
    for i in range(3,30,3): 
        lst.append(i)
    print(lst)

def cubes(): 
    cubes = []
    for i in range(1,11,1):
        cubes.append(i**3) 
    for cube in cubes: 
        print(cube,end=" ")

def cube_comprehension(): 
    cubes = [cube**3 for cube in range(1,11,1)]
    print(cubes)

def odd(num): 
    if num%2 == 1: 
        return True
    else: 
        return False

# note to self 
# a slice is :: not just : 
def copyList(): 
    lst = [lst*7 for lst in range(1,11,1) if odd(lst) ]
    list2 = lst[::-1]
    print(list2)

copyList()