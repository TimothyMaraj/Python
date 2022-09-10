

class Backpack(): 
    def __init__(self,list,numOfItem): 
        self.contains = list
        self.item_count = numOfItem
    
    def addItem(self,item_to_add):
        self.contains.append(item_to_add)
        self.item_count += 1
    
    def describe(self): 
        print(self.contains)
        print(self.item_count)

def main(): 
    backpack_items = ["pencil","5 dollars","laptop"]
    mi_mochila = Backpack(backpack_items,len(backpack_items))
    mi_mochila.addItem("phone charger")
    mi_mochila.describe()

main()