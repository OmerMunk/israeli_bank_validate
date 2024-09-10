def validate_Jerusalem_account(account_number: str, branch_number: str) -> bool:
    # Lists of exceptional branches
    except_2 = ['385', '384', '365', '347', '363', '362', '361']
    except_4 = ['361', '362', '363']

    try:
        # Check input length and validity
        if not (2 < len(account_number) <= 6 and len(branch_number) == 3):
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