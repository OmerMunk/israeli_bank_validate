def validate_grow_account(account_number: str, branch_number: str):
    """
    This function validates a GROW bank account by checking the branch number,
    account number, and calculating the check digits using the modulus 97 algorithm.
    It returns True if the account is valid, otherwise returns False.

    Explanation:
    - The account number includes the last two digits, which are the check digits (criticism literature).
    - Before performing the modulus calculation, we remove these two digits to form the full account number.
    - This is because the check digits are calculated separately, and we need to validate them against
      the rest of the account and branch number combination.
    """

    max_branch_number = 900
    min_branch_number = 1

    # Validate that the branch number is numeric and falls within the valid range (1-899).
    if not branch_number.isdigit() or min_branch_number > int(branch_number) or int(branch_number) >= max_branch_number:
        return False

    max_len_account = 8
    min_len_account = 6

    # Validate that the account number is numeric and its length is within the valid range (6-8 digits).
    if not account_number.isdigit() or len(account_number) < min_len_account or len(account_number) > max_len_account:
        return False

    # Remove leading zeros from the account number.
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

    # Extract the last two digits as the check digits (criticism literature).
    criticism_literature = account_number[-2:]

    try:
        # Convert the check digits to an integer.
        criticism_literature = int(criticism_literature)
    except ValueError:
        # Return False if the check digits are not valid integers.
        return False

    # Return True if the check digits match the calculation (98 - remainder), otherwise return False.
    return 98 - check_account == criticism_literature
