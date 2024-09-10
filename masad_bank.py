

def validate_masad_account(account_number: str, branch_number: str) -> bool:
    """
    This function validates a Bank Massad account number (bank code 46) according to a specific checksum method.

    Validation checks:
    1. The account number length must be between 2 and 6 digits.
    2. The branch number length must be exactly 3 digits.
    3. Both the account number and branch number must contain only digits.
    4. The digits of the branch and account numbers are multiplied by specific multipliers.
    5. The sum of these products must be divisible by 11 with no remainder, except for certain branch numbers
       where the sum is valid if divisible by 2.

    :param account_number:(str) The account number to be validated .
    :param branch_number:(str) The branch number to be validated.
    :return: bool: True if the account is valid based on the checksum rules, False otherwise.
    """
    ACCOUNT_NUMBER_MAX_LENGTH = 6
    ACCOUNT_NUMBER_MIN_LENGTH = 2
    BRANCH_NUMBER_LENGTH = 3

    if len(account_number) > ACCOUNT_NUMBER_MAX_LENGTH \
            or len(account_number) < ACCOUNT_NUMBER_MIN_LENGTH:
        return False
    if len(branch_number) > BRANCH_NUMBER_LENGTH:
        return False
    if not account_number.isdigit() or not branch_number.isdigit():
        return False

    account_number = account_number.zfill(ACCOUNT_NUMBER_MAX_LENGTH)
    branch_number = branch_number.zfill(BRANCH_NUMBER_LENGTH)

    lst_exceptional = ["154", "166", "178", "181", "183", "191", "192", "503", "505", "507", "515", "516", "527", "539"]

    sum_total = 0

    branch_multipliers = [9, 8, 7]
    account_multipliers = [6, 5, 4, 3, 2, 1]

    for i, n in enumerate(branch_number):
        sum_total += branch_multipliers[i] * int(n)

    for i, n in enumerate(account_number):
        sum_total += account_multipliers[i] * int(n)

    if branch_number in lst_exceptional and sum_total % 11 == 2:
        return True

    return sum_total % 11 == 0

print(validate_masad_account('041116', '571'))