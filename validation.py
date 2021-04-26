
def account_number_validation(account_number):
    if account_number:

        try:
            int(account_number)

            if len(str(account_number)) == 10:
                return True

        except ValueError:
            #print(" ==== ERROR ==== \n Account Number cannot be alphanumeric ")
            return False
        except TypeError:
            #print("Invalid Account Type")
            return False


    return False
