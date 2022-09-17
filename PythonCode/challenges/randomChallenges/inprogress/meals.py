
    # """Given a list of meals served over some period of time, return True if the
   # same meal has ever been served two days in a row, and False otherwise.
    # """

def func(meals):
    a = (len(meals)-1)
    i = 0
    while i < (a): 
        # i need the index of meal
        # then meals[index+1]
        # are they the same check? 
        if meals[i] == meals[i+1]: 
            return True
        else:
            i+=1
            continue
        
    return False

list = ["egg","carrot","spam","spam","apple","ketchup"]
print(func(list))