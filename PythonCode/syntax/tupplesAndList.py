def indexValues():    
    list1 = list()
    for i in range(9): 
        list1.append(i)

    print(list1)
    return list1


def listToTuple(list):
    return tuple(list)


def oddNumFromZeroToTwenty(): 
    lst = list()
    for i in range(0,21,1):
        if i%2 == 1:
            lst.append(i)
        else: 
            continue
            

    print(lst)




