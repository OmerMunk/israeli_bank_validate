def validate_the_operatives_account(account_number: str, branch_number: str) -> bool:
    '''
    This function checks if the account number is valid or not.
    :param account_number: string of the account number
    :param branch_number: string of the branch number
    :return: True if successful, False otherwise
    '''

    # check if the length of the acoount number and branch number are correct
    # otherwise adding zeros
    ACOUNT_DIGITS = 6
    BRANCH_DIGITS = 3

    if len(account_number) < ACOUNT_DIGITS:
        account_number = f"{account_number:0 > ACOUNT_DIGITS}"
        print(account_number)
    if len(branch_number) < BRANCH_DIGITS:
        branch_number = f"{branch_number:0 > BRANCH_DIGITS}"
        print(branch_number)

    result: int= 0
    NUMBER_TO_DIVIDE: int = 11
    calculation: str = branch_number + account_number

    # calculate the sum of all the account and branch numbers
    for i in range(1, len(calculation) + 1) :
        result += i * int(calculation[-i])
    remainder: int = result % NUMBER_TO_DIVIDE

    # check if the remainder is a legal number
    if remainder % 2 == 0 and remainder <= round(NUMBER_TO_DIVIDE / 2) or remainder == 0:
        return True
    return False








