def validate_the_operatives_account(account_number: str, branch_number: str):
    '''
    This function checks if the account number is valid or not.
    :param account_number: string of the account number
    :param branch_number: string of the branch number
    :return: True if successful, False otherwise
    '''
    result: int= 0
    NUMBER_TO_DIVIDE: int = 11
    calculation: str = branch_number + account_number
    for i in range(1, len(calculation)+1) :
        result += i * int(calculation[-i])
    is_legal: int = result % NUMBER_TO_DIVIDE

    if is_legal % 2 == 0 and is_legal <= round(NUMBER_TO_DIVIDE / 2) or is_legal == 0:
        return True
    return False


print(validate_the_operatives_account('065257', "698"))






