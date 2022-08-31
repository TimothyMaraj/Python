def evenIndexLetter(phrase):
    size = len(phrase)
    for i in range(0,size,2):
        print(phrase[i])

evenIndexLetter("mips")



def oddIndexLetter(phrase): 
    size = len(phrase)
    for i in range(0,size,1): 
        print(phrase[i])


oddIndexLetter("legv8")