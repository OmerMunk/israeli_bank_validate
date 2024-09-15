def validate_Jerusalem_account(account_number: str, branch_number: str) -> bool:
    return (type(branch_number) == str and
        type(account_number) == str and
        str.isdigit(branch_number) and
        str.isdigit(account_number))

