# a list of cards like a python list
# then make it rand when you want a "hit"
# user input for a yes no hit
# func that lists out your hand 
# counts up the Value of your hand 
# determins if you bust
# a limiting amount for bets 
# player starts at 500 dollars or we can call them 
# python pence 
# Ace is a special case can be 1 or 11?

""" some hopes for this would be a smart bot that will ask for a hit 
    if way too low or would stop if way too high like in 18-20 range
    would force user to take a hit if they need to get in range
"""

import random
cardList = [2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]

def botHand():
    botList = []
    for i in range(3): 
        botList.append(cardList[random.randrange(0,len(cardList),1)])
    # how can i make this a list comprehension
    return botList

def userHand(): 
    userList = []
    for i in range(3): 
        userList.append(cardList[random.randrange(0,len(cardList),1)])
    # how can i make this a list comprehension
    return userList



def cardCount(cards_in_hand): 
    card_count = 0
    higher_cards = ["Jack","Queen","King"]
    lower_cards = [2,3,4,5,6,7,8,9,10]

    for i in cards_in_hand: 
        if i in lower_cards: 
            card_count +=i
        else: 
            if i in higher_cards: 
                card_count+=10
            else: 
                aces = cards_in_hand.count("Ace")
                if aces > 1: 
                    while aces != 1:
                        card_count += 1
                    card_count+=11
                else: 
                    card_count+=11
                    
    return card_count
                    
def bust(): 
    """ a function to determine if you pass 21 or not"""
    pass
def win(): 
    """determines if you have won a round 
       but a check in main for card count == 21 would be ok too
    """
    pass

def hit(): 
    """returns user or bot a random card that would be 
        appended to the card list of them respectivly  
    """
    pass

def printOut(): 
    """print out will display cards of each player and print count
       something like: [list], count: 21 for example
    """
def main(): 
    """a main looping function that while ask user for hit or another round"""
    pass
userListCards = userHand()
print(userListCards)
print(cardCount(userListCards))