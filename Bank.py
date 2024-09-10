def validate_the_international_account(account_number: str,  branch_number: str) -> bool:
    """
    Validate an international account number using a weighted sum calculation.
    If the account is not valid for a 9-digit check, it checks the last 6 digits.
    If both checks fail, it validates using the the_soldiers_treasure account validation.
    """
    max_len = 9
    account_n = f"{account_number:0>{max_len}}"

    if not max_len >= len(account_number) >= 2:
        return False

    def check(an: str, ml: int = max_len) -> bool:
        list_of_an = map(int, an)
        list_of_keys = range(ml, 0, -1)
        return sum(n * k for n, k in zip(list_of_an, list_of_keys)) % 11 in (0, 6)

    if check(account_n):
        return True

    if check(account_n[-6:], 6):
        return True

    return validate_the_soldiers_treasure_account(account_number, branch_number)
