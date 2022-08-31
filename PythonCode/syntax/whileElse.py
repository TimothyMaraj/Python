def phrase():
    phrase = input("A phrase: ")
    for  letter in phrase: 
        print(letter,end =" ")



# if the while loop ends normally 
# then it will also print out the else statement
def whileEsle(): 
    i = 0
    list = [1,2,3,4,3,1,2]
    while i in list: 
        if i > 5: 
            break
        else:
            print(i, end = " ")
            i+=1
    else: 
        print("Ended WithOut Interuption")

whileEsle()