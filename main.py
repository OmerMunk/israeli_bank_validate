def validate_Citibank_account(account: str, branch: str) -> bool:
    """
       Validates a Citibank account number based on a checksum algorithm.

       The account number must be 9 digits long, and the branch number must be 3 digits long.

       Args:
       account (str): A 9-digit string representing the account number.
       branch (str): A 3-digit string representing the branch number.

       Returns:
       bool: Returns True if the account number is valid according to the checksum algorithm.
             Returns False if the account number or branch number is invalid..
       """
    MULTIPLIERS = [3, 2, 7, 6, 5, 4, 3, 2]
    LEN_ACCOUNT = 9
    LEN_BRANCH = 3
    MODULO = 11
    # Validate that the account number and branch number are digits of correct lengths
    if account.isdigit() and len(account) == LEN_ACCOUNT and len(branch) == LEN_BRANCH and branch.isdigit():
        verification_digit = account[-1]
        num_to_check = account[:8]
        # Calculate the sum of the first 8 digits multiplied by their corresponding multipliers
        total_sum = sum(map(lambda x, y: int(x) * y, num_to_check, MULTIPLIERS))

        result = total_sum % MODULO

        check_digit = MODULO - result if result != 0 else 0
        if check_digit == int(verification_digit):
            return True
    return False
