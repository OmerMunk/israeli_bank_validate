def validate_GROW_account(account_number: str, branch_number: str):
    if not branch_number.isdigit() or 1> len(branch_number) <900:
        return False

    if not account_number.isdigit() or len(account_number) < 6 or len(account_number) > 8:
        return False
    account_number = account_number.lstrip('0')
    try:
        full_account = int(branch_number + account_number[:-2])
    except ValueError:
        return False
    check_account = full_account % 97
    criticism_literature = account_number[-2:]
    try:
        criticism_literature = int(criticism_literature)
    except ValueError:
        return False

    return 98 - check_account == criticism_literature