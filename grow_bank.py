def validate_grow_account(account_number: str, branch_number: str) -> bool:
    """
    This function validates a GROW bank account.

    It checks the branch number and account number, and calculates the check digits
    using the modulus 97 algorithm. It returns True if the account is valid, otherwise False.

    Explanation:
    - The account number includes the last two digits, which are the check digits.
    - Before performing the modulus calculation, we remove these last two digits to form the full account number.
    - The check digits are calculated separately and need to be validated against the rest of the account and branch number combination.
    """

    MAX_BRANCH_NUMBER = 899
    MIN_BRANCH_NUMBER = 1

    # Validate that the branch number is numeric and falls within the valid range (1-899).
    if not branch_number.isdigit() or not (MIN_BRANCH_NUMBER <= int(branch_number) <= MAX_BRANCH_NUMBER):
        return False

    MAX_LEN_ACCOUNT = 8
    MIN_LEN_ACCOUNT = 6

    # Validate that the account number is numeric and its length is within the valid range (6-8 digits).
    if not account_number.isdigit() or len(account_number) < MIN_LEN_ACCOUNT or len(account_number) > MAX_LEN_ACCOUNT:
        return False

    # Remove leading zeros from the account number.
    # This ensures that numbers like "0012345" are treated as "12345".
    account_number = account_number.lstrip('0')

    try:
        # Concatenate the branch number with the account number (excluding the last two digits) and convert to an integer.
        # The last two digits of the account number are the check digits, so we exclude them from the modulus calculation.
        full_account = int(branch_number + account_number[:-2])
    except ValueError:
        # Return False if the concatenation fails (e.g., due to non-numeric values).
        return False

    # Calculate the remainder when dividing the full account by 97.
    check_account = full_account % 97

    # Extract the last two digits as the check digits.
    criticism_literature = account_number[-2:]

    try:
        # Convert the check digits to an integer.
        criticism_literature = int(criticism_literature)
    except ValueError:
        # Return False if the check digits are not valid integers.
        return False

    # Return True if the check digits match the calculation (98 - remainder), otherwise return False.
    return 98 - check_account == criticism_literature
