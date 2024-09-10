#The function receives the account number and the branch number
# and sends both as a parameter to the function that calculates
# the multiplication of the serial number
# and after that it checks if the last
# two formulas are 90,72,70,60,20 and if
# so then the calculation makes sense
def validate_Association_account(account_number: str,branch_number: str):
    try:
        calculat = str(calculate_bank_agod(account_number,branch_number))
        options = ["90","72","70","60","20"]
        if calculat[-2:] in options:
            return True
        return False
    #If for any reason there is an error from the function,
    # then the error will be displayed, but if what is returned
    # is not in the list, then it means that it is not a valid account number
    except ValueError:
        return TypeError

#A function that calculates the multiplication
# of the serial number
# from 10 to 2 and then adds the serial number
def calculate_bank_agod(account_number: str,branch_number: str):
    if 2 < len(account_number) + len(branch_number) < 10:
        return -1
    CRITICISM_LITERATURE = int(account_number[-2:])
    multiplier = 10
    sum_calculate = 0
    branch_number += account_number[:-3]
    for i in range(len(branch_number)):
        if multiplier >= 2 and i != "-":
            sum_calculate += int(branch_number[i]) * multiplier
            multiplier -= 1
        else:
            continue

    return sum_calculate + CRITICISM_LITERATURE
