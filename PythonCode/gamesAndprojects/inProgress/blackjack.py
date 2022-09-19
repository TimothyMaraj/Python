"""
   -  Tie is broken!!!!!!!!!!!!!!!!!!
   - fix the double win condition
   - fix bot so if user doesnt take a hit and is still lower, bot wont take a hit and will win/-yj
   - look into oop versus proc for deck class
    - if you win off rip then what ? 21 on draw ? do you win? 
    - source the win conditional check to a function_ 
"""

import random
cardList = [2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]

def botHand():
    listTest = [2, 'Queen', 6]
    botList = []
    for i in range(3): 
        botList.append(cardList[random.randrange(0,len(cardList),1)])
    # how can i make this a list comprehension
    return botList

def userHand(): 
    listTest = [2, 'Queen', 7]
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

# count must be an int from cardCount()                   
def bust(count): 
    """ a function to determine if you pass 21 or not"""
    return count>21

def hit(): 
    """returns user or bot a random card that would be 
        appended to the card list of them respectivly  
    """
    return cardList[random.randrange(0,len(cardList),1)]


def printOut(userList,botList): 
    """print out will display cards of each player and print count
       something like: [list], count: 21 for example
    """
    userCount = cardCount(userList)
    botCount = cardCount(botList)
    print("User Cards:{} User Count: {}".format(userList, userCount))
    print("Bot Cards:{} Bot Count: {}".format(botList, botCount))
        

def main(): 
    """a main looping function that while ask user for hit or another round"""
    gameloop = True
    while gameloop: 
        print("\n")
        print("New Round")
        print("\n")
        #1) get both hands and PRINT
        #2) check if any busted, if so WHO WON? 
            # if so 2a) new round 
        #3) ask user if they want a hit
            #3a) if they do then append to list and count cards
            #3b) if they bust bot wins NEW ROUND
            #3c) if they hit 21 they win
            #3d) if they dont want any more hits CONINTUE
        #4) check if bot count is under 18
            #4a) if so then hit 
                # if bot hits 21 here they win 
                # if bot busts then user wins 
            #4b) if not then continue 
        #5) if no one busted or won check who has higher cards 
        userList = userHand()
        botList = botHand()

        if bust(cardCount(userList)) or bust(cardCount(botList)) : 
            print("Reshuffle")
            continue
        else: 
            printOut(userList,botList)
            while input("Do you want a hit: ") == "yes": 
                userList.append(hit())
                # it skips over this if you bust? or for some rzn yes in some form does not 
                # reg as yes ? and skips to the if statemetn to check bot? 
                printOut(userList,botList)
                if bust(cardCount(userList)):
                    print("Bot Won")
                    break
                elif cardCount(userList) == 21: 
                    print("You won!")
                    break
                else: 
                    continue
            if cardCount(botList) < 18: 
                while cardCount(botList) != 17 and cardCount(botList) < 20: 
                    botList.append(hit())
                    printOut(userList,botList)
                    if bust(cardCount(botList)): 
                        print("User won")
                        break
                    else: 
                        continue
        if bust(cardCount(userList)): 
            print("Bot Won")
        elif not bust(cardCount(userList)) and not bust(cardCount(botList)) and cardCount(botList) < cardCount(userList): 
            print("User Won")
        elif bust(cardCount(botList)): 
            print("user Won")
        else: 
            print("tie")              

        
main()

def tests(): 
    userListCards = userHand()
    print(userListCards)
    print(cardCount(userListCards))
    print(hit())
    print(bust(cardCount(userListCards)))