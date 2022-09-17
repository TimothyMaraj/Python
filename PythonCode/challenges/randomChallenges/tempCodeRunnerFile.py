def counter(hand): 
    highercards = ["K","Q","J"]
    lowerCard = ["1","2","3","4","5","6","7","8","9"]
    ace = ["A"]
    count = 0
    aceCount = 0
    for card in hand: 
        if card in highercards: 
            count+=10
        elif card in ace: 
            aceCount+= 1
        else: 
            count+=int(card)
    if aceCount == 1 and count <= 10:
        count+=11
    else: 
        while aceCount != 0: 
            if aceCount > 1: 
                while aceCount > 1: 
                    count+=1
                    aceCount-=1
            else: 
                if count <= 10: 
                    count+=11
                    aceCount-=1
    return count
    


def blackjack_hand_greater_than(hand_1, hand_2):
    totalValueOne = 0
    totalValueTwo = 0
    
    totalValueOne = counter(hand_1) 
    totalValueTwo = counter(hand_2)
    
    return totalValueOne > totalValueTwo


# what if i send it 21 aces? at 21st ace what happens? does my program
# add 11 to 20 ? 
a = ["A","10"]
b = ["K","10"]
print(blackjack_hand_greater_than(a,b))