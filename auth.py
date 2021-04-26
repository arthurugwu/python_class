import random
from getpass import getpass

import validation
import database


# database = {
#     6463070355: ['Arthur', 'Ugwu', 'oaugwu@gmail.com', 'arthurPassword']
# }


def init() -> object:
    print("Welcome to Hills Bank")

    have_account = int(input("Do you have an account with us: \n (1) Yes (2) No \n"))

    if have_account == 1:
        login()

    elif have_account == 2:
        register()

    else:
        print("Invalid Option")
        init()


def login():
    print("====Login====")

    account_number_from_user = input("What is your account number \n")

    is_valid_account_number = validation.account_number_validation(account_number_from_user)

    if is_valid_account_number:

        password = getpass("What is your password \n")

        user = database.authenticated_user(account_number_from_user, password)

        if user:
            bank_operations(user)

        print("Invalid account or password")
        login()

    else:
        print("Account Number Invalid: Please confirm number is 10 digits")
        init()


def register():
    print("====Register====")
    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = getpass("Create a password for yourself \n")

    account_number = generation_account_number()

    prepared_user_details = first_name + "," + last_name + "," + email + "," + password, "," + str(0)

    is_user_created = database.create(account_number,  first_name, last_name, email, password)
    # is_user_created = database.create(account_number, prepared_user_details)

    # user = database[account_number]

    if is_user_created:
        print("Your account has been created")
        print("***** ***** ***** ***** *****")
        print("Your account number is %d \n" % user_account_number)
        print("***** ***** ***** ***** *****")

        login()
    else:
        print("Something Went Wrong, Please try again")
        register()


def bank_operations(user):
    print("Welcome %s %s " % (user[0], user[1]))

    selected_option = int(input("What would you like to do? \n (1) Deposit (2) Withdrawal (3) Logout (4) Exit \n "))

    if selected_option == 1:
        deposit_operation()

    elif selected_option == 2:
        withdrawal_operation()

    elif selected_option == 3:
        logout()

    elif selected_option == 4:
        exit()
    else:
        print("Invalid Option Selected")
        bank_operations(user)


def withdrawal_operation():
    print("====Withdrawal====")

    withdraw_option = int(input("Choose an option \n (1) Check Balance (2) Select Amount (3) Exit \n "))

    if withdraw_option == 1:
        current_balance = get_current_balance()
        get_current_balance()

    elif withdraw_option == 2:
        print("Bills will come $5, $10, $20 ")

        user_choice = int(input("(1) $20 (2) $50 (3) $100 (4) Input Amount \n "))

        if user_choice == (1, 2, 3):
            print("Please Take your Cash")
            withdrawal_operation()

        elif user_choice == 4:
            user_withdraw = int(input("Withdrawal Amount: "))

            current_balance = get_current_balance()

            if user_withdraw <= current_balance:
                print("$", user_withdraw, "has been withdrawn from your account")
                withdrawal_operation()

    elif withdraw_option == 3:
        exit()


def deposit_operation():
    print("====Deposit====")

    deposit_option = int(input("Choose an option \n (1) Cash (2) Check (3) Exit \n "))

    if deposit_option == 1:
        user_deposit = input("Deposit Amount: ")
        print("$", user_deposit, "has been deposited into your account")

        more_deposit = int(input("Make Another Deposit \n (1) Yes (2) No \n "))

        if more_deposit == 1:
            deposit_operation()

        elif more_deposit == 2:
            bank_operations(user)


    elif deposit_option == 2:

        check_deposit = input("Deposit Amount: ")
        print("$", check_deposit, "has been deposited into your account")

        more_deposit = int(input("Make Another Deposit \n (1) Yes (2) No "))

        if more_deposit == 1:
            deposit_operation()

        elif more_deposit == 2:
            bank_operations(user)

    elif deposit_option == 3:
        exit()


def generation_account_number():
    return random.randrange(1111111111, 9999999999)


def set_current_balance(user_details, balance):
    user_details[4] = balance


def get_current_balance(user_details):
    return user_details[4]


def logout():
    login()


def exit():
    print("Thank you for Banking with Hills Bank \n Have a nice day \n")


init()
