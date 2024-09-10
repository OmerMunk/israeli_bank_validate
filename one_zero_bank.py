def validate_One_Zero_account(account_number: str, branch_number: str):
    '''
    This function validates the account number and branch number format.
    Length of account number should be 9 digits.
    Length of branch number should be between 1-3 digits.
    Last two digits of account number is the review_digits number.
    The formula is;
        1. Add the branch number to the beginning of the account number(1 for privet customers)
        2. Take the result and divide the modulo by 97.
        3. Subtract the result from 98, and it should be equal to the literature number.
    Note: This code checks only private customers (branch number 1)
    '''
    LENGTH_OF_ACCOUNT_NUMBER = 9
    MIN_LENGTH_OF_BRANCH_NUMBER = 1
    MAX_LENGTH_OF_BRANCH_NUMBER = 3
    MODULUS_NUMBER = 97
    SUBTRACT_AFTER_MODULUS_RESULT = 98
    FIRST_OPTION_FOR_BRANCH_NUMBER = 1
    SECOND_OPTION_FOR_BRANCH_NUMBER = 2
    THIRD_OPTION_FOR_BRANCH_NUMBER = 3

    # Checking if the account number and branch number are numeric.
    if(not account_number.isdigit() or not branch_number.isdigit()):
        return False
    # Checking the length of the account number and the length of the branch number.
    if len(account_number) != LENGTH_OF_ACCOUNT_NUMBER or MIN_LENGTH_OF_BRANCH_NUMBER <= len(branch_number) <= MAX_LENGTH_OF_BRANCH_NUMBER:
        return False

    # Checking the format of entering the branch numberץ
    if len(branch_number) == FIRST_OPTION_FOR_BRANCH_NUMBER:
        branch_code = branch_number[FIRST_OPTION_FOR_BRANCH_NUMBER-1]
    if len(branch_number) == SECOND_OPTION_FOR_BRANCH_NUMBER:
        branch_code = branch_number[SECOND_OPTION_FOR_BRANCH_NUMBER -1]
    if len(branch_number) == THIRD_OPTION_FOR_BRANCH_NUMBER:
        branch_code = branch_number[THIRD_OPTION_FOR_BRANCH_NUMBER-1]

    # Adding the branch number at the beginning of the account number.
    account_code_after_adding_branch_code = branch_code + account_number
    # Create a variable that holds the check digit.
    review_digits = int(account_number[-2:])
    # Calculation according to modulus 97 for the account number, not including the check digit.
    res_after_mod_97 = int(account_code_after_adding_branch_code[:-2]) % MODULUS_NUMBER

    if review_digits == SUBTRACT_AFTER_MODULUS_RESULT - res_after_mod_97:
        return True
    else:
        return False
