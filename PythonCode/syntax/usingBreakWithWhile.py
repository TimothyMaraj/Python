def bankBalance(): 
    userInput = int(input("How much Money in your bank: "))
    return userInput


def transaction(checkingAccount,cost): 
    if cost > checkingAccount:
        print("Invalid, insufficent funds\n")
        return checkingAccount
    else: 
        print("Transaction Approved")
        return (checkingAccount-cost)


def fee(): 
    transactionFee = int(input("What is the transaction fee?: "))
    return transactionFee

def spendUntilEmpty(): 
    acountAmount = bankBalance()
    chargeAmount = fee()
    transaction(acountAmount,chargeAmount)
    userInput = input("would you like to spend indef? ")
    if userInput == "yes": 
        while transaction != None: 
            acountAmount = transaction(acountAmount,chargeAmount)
            print(acountAmount)
            if(acountAmount <= 50): 
                print("At min bank balance, unable to spend. Please see your bank")
                break
    else: 
        return 


spendUntilEmpty()