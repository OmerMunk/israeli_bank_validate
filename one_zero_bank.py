def validate_One_Zero_account(account_number: str, branch_number: str):
    if len(account_number) != 9 or 0 > len(branch_number) <= 3:
        return False
    if len(branch_number) == 1:
        branch_code = branch_number[0]
    if len(branch_number) == 2:
        branch_code = branch_number[1]
    if len(branch_number) == 3:
        branch_code = branch_number[2]
    account_code = branch_code + account_number
    review_literature = int(account_number[-2:])
    res_after_mod_97 = int(account_code[:-2]) % 97
    if review_literature == 98 - res_after_mod_97:
        return True
    else:
        return False
