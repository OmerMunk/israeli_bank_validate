"""
 Validates a Jerusalem bank account number according to specific rules.

    This function checks the validity of a Jerusalem bank account number using a custom
    algorithm. It takes into account special cases for certain branch numbers.

    Parameters:
    account_number (str): The account number to validate. Must be between 2 and 6 digits.
    branch_number (str): The branch number associated with the account. Must be exactly 3 digits.

    Returns:
    bool: True if the account number is valid, False otherwise.

    Algorithm:
    1. Check if the input lengths are valid.
    2. Calculate a weighted sum for the account number (right to left, weights 6 to 1).
    3. Calculate a weighted sum for the branch number (right to left, weights 9 to 7).
    4. Sum the results from steps 2 and 3.
    5. Check if the total sum is divisible by 11 (normal case).
    6. If not, check for special cases:
       - If remainder is 2 and branch is in the except_2 list.
       - If remainder is 4 and branch is in the except_4 list.

    Special Cases:
    - Branches in except_2 list: ['385', '384', '365', '347', '363', '362', '361']
    - Branches in except_4 list: ['361', '362', '363']

    Error Handling:
    - Returns False for any input that causes ValueError or IndexError (e.g., non-digit characters).

    Note:
    This function assumes the input strings contain only digits. Any non-digit character
    will cause the function to return False.
"""


def validate_Jerusalem_account(account_number: str, branch_number: str) -> bool:
    # Lists of exceptional branches
    except_2 = ['385', '384', '365', '347', '363', '362', '361']
    except_4 = ['361', '362', '363']

    try:
        # Check input length and validity
        if not (2 <= len(account_number) <= 6 and len(branch_number) == 3):
            raise ValueError("Invalid input length")

        # Calculation for account number
        sum_account = sum(int(char) * (6-i) for i, char in enumerate(account_number.zfill(6)))

        # Calculation for branch number
        sum_branch = sum(int(char) * (9-i) for i, char in enumerate(branch_number))

        total_sum = sum_account + sum_branch

        # Normal case
        if total_sum % 11 == 0:
            return True

        # Exceptions for remainder 2
        elif total_sum % 11 == 2 and branch_number in except_2:
            return True

        # Exceptions for remainder 4
        elif total_sum % 11 == 4 and branch_number in except_4:
            return True

        # Default - not valid
        return False

    except (ValueError, IndexError):
        # Handle errors for invalid length or characters
        return False

# Check
print(validate_Jerusalem_account("141116", "368" ))