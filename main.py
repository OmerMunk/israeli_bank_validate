def check_valid_str(account_numbers: str, branch_number: str):
    REQUIRED_ACCOUNT_DIGITS = 9
    REQUIRED_BRANCH_DIGITS = 3
    if not account_numbers.isdigit() or len(account_numbers) != REQUIRED_ACCOUNT_DIGITS:
        return False
    if not branch_number.isdigit() or len(branch_number) != REQUIRED_BRANCH_DIGITS:
        return False
    return True

def validate_hsbc_account(account_number: str, branch_number: str):
    if not check_valid_str(account_number, branch_number):
        return False
    BRANCH_NUM = "101"
    VALIDATION_INDEX = 6
    VALIDATION = "4"
    if branch_number == BRANCH_NUM:
        if account_number[VALIDATION_INDEX] != VALIDATION:
            return False
    return True



