
def validate_Leumi_account(account_number:str,branch_number:str) -> bool:
    """
    This function compares the calculated check digit with the actual check digits provided in the account number.

    Parameters:
    calculated_check_digit (int): The check digit that was calculated based on the account number and branch code.
    check_digits (list of int): A list containing the last two digits (check digits) from the account number.

    Returns:
    bool: True if the calculated check digit matches the actual check digits from the account number, False otherwise.

    Explanation:
    The function takes two check digits from the account number (check_digits) and combines them to form a two-digit number.
    It multiplies the first check digit by 10 to position it in the tens place, then adds the second check digit (units place).
    It compares this two-digit number with the calculated check digit to verify the validity of the account number.

    """
    account_multipliers:list[int] = [7,6,5,4,3,2]
    branch_multipliers:list[int] = [10,9,8]

    account_digits:list[int] = [int(digit) for digit in account_number]
    branch_digits:list[int] = [int(digit) for digit in branch_number]

    check_digits:list[int] = account_digits[-2:]
    account_digits:list[int] = account_digits[:-2]

    account_sum:int = sum(account_digits[i] * account_multipliers[i] for i in range(len(account_multipliers)))
    branch_sum:int = sum(branch_digits[i] * branch_multipliers[i] for i in range(len(branch_multipliers)))
    total_sum:int = account_sum + branch_sum
    fifth_sixth_digits:list[int] = account_digits[4:]

    if fifth_sixth_digits != [0, 0] and fifth_sixth_digits != [2, 0] and fifth_sixth_digits != [2, 3]:
        account_types:list[int] = [330, 340, 180, 128]
    else:
        account_types:list[int] = [330, 340, 110, 180, 128]

    results:list[int] = [total_sum + account_type for account_type in account_types]

    valid = False
    for result in results:
        last_two_digits:int = result % 100
        if last_two_digits == 0:
            calculated_check_digit = 0
        else:
            calculated_check_digit = 100 - last_two_digits

        if calculated_check_digit == check_digits[0] * 10 + check_digits[1]:
            valid = True
            return valid

        return valid

