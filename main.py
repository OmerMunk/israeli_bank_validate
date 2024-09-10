def validate_Citibank_account(account: str, branch: str) -> bool:
    multipliers = [3, 2, 7, 6, 5, 4, 3, 2]
    len_account = 9
    len_branch = 3
    if account.isdigit() and len(account) == len_account and len(branch) == len_branch and branch.isdigit():
        verification_digit = account[-1]
        total_sum = sum(map(lambda x, y: int(x) * y, account[:8], multipliers))
        result = total_sum % 11
        check_digit = 11 - result if result != 0 else 0
        if check_digit == int(verification_digit):
            return True
    return False

