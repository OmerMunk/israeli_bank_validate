# Validate if the account and branch numbers contain the right characters and are in the right length
def check_valid_str(account_number: str, branch_number: str) -> bool:
    """
     Checks whether the input is a valid string that contains the required amount of digits.
    :param account_number:
    :param branch_number:
    :return:
    """
    REQUIRED_ACCOUNT_DIGITS = 9
    REQUIRED_BRANCH_DIGITS = 3
    if len(account_number) != REQUIRED_ACCOUNT_DIGITS or len(branch_number) != REQUIRED_BRANCH_DIGITS \
            or not account_number.isdigit() or not branch_number.isdigit():
        return False
    return True

# Validate the account number according to the banks formatting rules
def validate_hsbc_account(account_number: str, branch_number: str) -> bool:
    """
    Checks if the input account number meets the required standards of the HSBC account number.
    :param account_number:
    :param branch_number:
    :return:
    """
    if not check_valid_str(account_number, branch_number):
        return False
    BRANCH_NUM = "101"
    VALIDATION_INDEX = 6
    VALIDATION = "4"
    if branch_number == BRANCH_NUM:
        if account_number[VALIDATION_INDEX] != VALIDATION:
            return False
    return True
print(validate_hsbc_account("123456", "123"))
