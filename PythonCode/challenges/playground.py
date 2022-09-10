def stripLastThreeCharactersOfString():
    list = ["12345678","12345678"]
    for item in list: 
        if item[-3:] == "678": 
            print(item[:-3])

# takes a list of lists of lists and prints them out 
def superNested(list):
    for i in list: 
        for j in i: 
            for k in j: 
                print(k,end=" ")
    
    return None

#list = [[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]]]
#superNested(list)
def sumOf100():
    i = 0
    sum = 0
    while i < 100:
        sum += i
        i+=1

    print(sum)


def ifThereIs100(list):
    for i in list:
        if i == 100: 
            print(list.index(i))
        else: 
            continue

lst=[10, 99, 98, 85, 45, 59, 65, 66, 76, 12, 35, 13, 100, 80, 95]
#ifThereIs100(lst)

#cubes = [cube**3 for cube in range(1,11,1)]
#print(cubes)

def check(dict2): 
    print(dict2[(1,2)])
    print(dict2.get((1,3)))

dict1 = {(1,2):"22"}

check(dict1)
ifThereIs100(lst)

tuple1 = (0,2)
a,b = tuple1
print(a,b)

