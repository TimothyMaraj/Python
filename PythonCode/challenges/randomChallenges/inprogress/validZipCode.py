def zipValidation(zipString): 
    #length = len(zipString)
    if len(zipString) != 5: 
        return False
    list = ["0","1","2","3","4","5","6","7","8","9"]
    for char in zipString: 
        if char not in list: 
           # print(char)
            return False
    
    return True

def isAZipCode(zipCode):
    return len(zipCode) == 5 and zipCode.isdigit()

print(zipValidation("12345"))
print(zipValidation("1"))
print(zipValidation("145"))
print(zipValidation("x"))
print(isAZipCode("1234x"))
    
