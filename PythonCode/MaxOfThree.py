
# note boolean operator is and in python unsimilar to 
# & or && in C++ Native Lang
def maxOfThree(a,b,c): 
    if a > b and a > c: 
        print("a")
        return a
    elif b > a and b > c: 
        print("b")
        return b   
    else: 
        print("c")
        return c




a = int(input("Enter a number to assign to a: "))
b = int(input("Enter a number to assign to b: "))
c = int(input("Enter a number to assign to c: "))

max = maxOfThree(a,b,c)

print(max)