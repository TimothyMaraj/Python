# Book 9-1 thru 9-3
#
#




import time
from datetime import date as date

class Restaurant(): 

    def __init__(self,name,food_type):
        self.name = name
        self.food_type = food_type
    
    def describe(self):
        print(self.name,self.food_type) 

    def open_or_closed(self):
        print("{} is open".format(self.name))

def restaurant_class_call(): 
    restaurant = Restaurant("Timmy's Tacos","Mexican")
    restaurant.describe()
    restaurant.open_or_closed()


class Users(): 
    def __init__(self,first_name,last_name,userName,birthday):
        self.first_name = first_name
        self.last_name = last_name
        self.userName = userName
        self.birthday = birthday

    def describe(self): 
        now = time.ctime(time.time())
        dateNow = date.today()
        print("Hi {}, or should I call you {} {}. Today is {}...and time {}. but your birthday is {} ".format(self.userName, self.first_name, self.last_name, dateNow,now,self.birthday))

# idea:!!!!! make a module that does some time conversion
# 
def call_user_class(): 
    user1 = Users("Tim","Maraj","AlternateBased","2000-01-04")
    userlist = []
    for i in range(0,4,1): 
        user
        userlist.append()

    user1.describe()

call_user_class()