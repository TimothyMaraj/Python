

class dog(): 
    def __init__(self,breed): 
        self.breed = breed

# inheritance here of the attriubte breed from the parent class dog 
# lol, the puppy class inherited the dog's class breed type 
class puppy(dog): 
    def __init__(self,breed,name): 
        super().__init__(breed)
        self.breed = breed
        self.name = name
    
    def describe(self):
        print(self.breed, self.name)


lab = dog("lab")
labPuppy = puppy("lab","Jazz")
labPuppy.describe()
    

