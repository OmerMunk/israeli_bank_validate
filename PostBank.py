def validate_The_Mail_account(account: str):
    """
    Validates a bank account number for the Post Office Bank.

    This function checks if the given account number:
    1. Contains only digits.
    2. Does not exceed 9 digits in length.
    3. Passes a custom validation algorithm where the weighted sum 
       of the digits (from left to right) is divisible by 10.

    Parameters:
    account (str): The account number to validate, as a string.

    Returns:
    bool: True if the account number is valid according to the rules, 
          False otherwise.

    Raises:
    ValueError: If the account number contains non-digit characters or 
                exceeds the length limit of 9 digits.

    Example:
    >>> validate_The_Mail_account("059121900")
    True
    >>> validate_The_Mail_account("12345678")
    False
    """
    # Constants
    LIMIT_SIZE = 9

    try:
        # Check if the account number consists only of digits and does not exceed the limit size
        if not account.isdigit() or len(account) > LIMIT_SIZE:
            raise ValueError("שגיאה: מספר החשבון חייב להכיל רק ספרות ואורכו לא יכול לעלות על 9 ספרות.")

        # Pad the account number with zeros to the left if it is less than the limit size
        account_number = account.zfill(LIMIT_SIZE)
        calculate_multiply = 0

        # Perform the calculation as described
        for i in range(0, LIMIT_SIZE):
            calculate_multiply += (LIMIT_SIZE - i) * int(account_number[i])

        # Check if the calculation result is divisible by 10
        return calculate_multiply % 10 == 0

    except ValueError as e:
        print(e)
        return False



