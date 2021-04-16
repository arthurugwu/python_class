import random
from getpass import getpass

import datetime

database = {}


def init():

    print("Welcome to Hills Bank")
    import datetime
    now = datetime.datetime.now()
    dateStr = now.strftime("%m-%d-%Y %H:%M:%S")

    haveAccount = int(input("Do you have an account with us: \n (1) Yes (2) No \n"))

    if(haveAccount == 1):
        login()

    elif(haveAccount == 2):
        register()

    else: 
        print("Invalid Option")
        init()

def login():

    print("====Login====")

    accountNumberFromUser = int(input("What is your account number \n"))
    password = input("What is your password \n")

    for accountNumber,user in database.items():
        if(accountNumber == accountNumberFromUser):
            if(user[3] == password):
                bankOperations(user)
    
    print("Invalid account or password")
    login()

def register():

    print("====Register====")
    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = getpass("Create a password for yourself \n")

    accountNumber = generationAccountNumber()

    database[accountNumber] = [ first_name, last_name, email, password ]

    user = database[accountNumber]

    print("Your account has been created")
    print("***** ***** ***** ***** *****")
    print("Your account number is %d \n" % accountNumber)
    print("***** ***** ***** ***** *****")

    login()

def bankOperations(user):
    print("Welcome %s %s " % ( user[0], user[1] ))

    selectedOption = int(input("What would you like to do? \n (1) Deposit (2) Withdrawal (3) Logout (4) Exit \n "))

    if(selectedOption == 1):
        depositOperation()

    elif(selectedOption == 2):
        withdrawalOperation()

    elif(selectedOption == 3):
        logout()

    elif(selectedOption == 4):
        exit()
    else:
        print("Invalid Option Selected")
        bankOperations(user)

def withdrawalOperation():
    print("====Withdrawal====")

    withdrawOption = int(input("Choose an option \n (1) Check Balance (2) Select Amount (3) Exit \n "))

    if(withdrawOption == 1):
        currentBalance = getCurrentBalance()
        getCurrentBalance()
    
    elif(withdrawOption == 2):
        print("Bills will come $5, $10, $20 ")

        userChoice = int(input("(1) $20 (2) $50 (3) $100 (4) Input Amount \n "))

        if (userChoice ==  1, 2, 3 ):
            print("Please Take your Cash")
            withdrawalOperation()

        elif(userChoice == 4):
            userWithdraw = input("Withdrawal Amount: ")
            if(userWithdraw <= currentBalance):
                print("$", userWithdraw, "has been withdrawn from your account")
                withdrawalOperation()

    elif(withdrawOption == 3):
        exit()    

def depositOperation():
    print("====Deposit====")

    depositOption = int(input("Choose an option \n (1) Cash (2) Check (3) Exit \n "))

    if(depositOption == 1):
        userDeposit = input("Deposit Amount: ")
        print("$", userDeposit, "has been deposited into your account")
        
        moreDeposit = int(input("Make Another Deposit \n (1) Yes (2) No \n "))

        if(moreDeposit == 1):
            depositOperation()
        
        elif(moreDeposit == 2):
            bankOperations(user)

            
    elif(depositOption == 2):
        checkDeposit = input("Deposit Amount: ")
        print("$", checkDeposit, "has been deposited into your account")
        
        moreDeposit = int(input("Make Another Deposit \n (1) Yes (2) No "))

        if(moreDeposit == 1):
            depositOperation()
        
        elif(moreDeposit == 2):
            bankOperations(user)

    elif(depositOption == 3):
        exit()    


def generationAccountNumber():
    return random.randrange(1111111111,9999999999)

def getCurrentBalance():
    return random.randrange(11111,99999)

def logout():
    login()

def exit():
    print("Thank you for Banking with Hills Bank \n Have a nice day \n")


init()  