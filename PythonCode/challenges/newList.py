#Using while loop and an if statement write a function named name_adder 
# which appends all the elements in a list to a new list unless the element is an empty string: "".



def name_adder(list):
    a = []
    i = 0
    size = len(list)

    #why does len(list[i]) only print out the first four? ['Joe', 'Sarah', 'Mike', 'Jess']
    while i < size: 
        if list[i] != "":
            a.append(list[i])
            i+=1
        else:
            i+=1
            continue


    return a

list2 = [""]
list=["Joe", "Sarah", "Mike", "Jess", "", "Matt", "", "Greg"]
#print(name_adder(list))


#a = []
#i = 0
#while i < len(list[i]): 
#    a.append(list[i])
#    print(list[i])
#    i+=1
# not if list[i] == a "" , a null value then len() 
# returns 0, so you have to capture the whole list
# not in c++ you wouldnt do i<arr[i] ? so relate 
# that here future Tim

    