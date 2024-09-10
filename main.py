def validate_Jerusalem_account(account_number: str, branch_number: str):
    if (type(branch_number) != str or
        type(account_number) != str or
        not str.isdigit(branch_number) or
        not str.isdigit(account_number)):
        return False
    return True
