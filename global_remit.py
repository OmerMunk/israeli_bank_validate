def validate_global_remit_account(account_number: str, branch_number: str):
    """
        Validates a Global Remit account number using a weighted checksum calculation.

        The account number must consist of 8 digits followed by a check digit. The function computes
        a weighted sum of the first 8 digits, divides the sum by 11, and compares the complement
        of the remainder (mod 11) with the provided check digit.

        The function supports account numbers that start with 0 and includes them in the calculation.

        :param account_number: A string containing the account number to be validated. It should
                               be 9 digits long (8 digits + 1 check digit). Leading zeros are included.
        :param branch_number: This parameter is not used in the validation process.
        :return: True if the account number is valid, False otherwise.

    """
    WEIGHT_FACTORS = [9, 8, 6, 4, 3, 7, 2, 5]
    ACCOUNT_LENGTH = 8
    CHECKSUM_BASE = 11

    filtered_account_number = ''.join(filter(str.isdigit, account_number))

    if len(filtered_account_number) != ACCOUNT_LENGTH + 1:
        return False

    weighted_sum = sum(
        WEIGHT_FACTORS[i] * int(filtered_account_number[i])
        for i in range(ACCOUNT_LENGTH)
    )

    remainder = weighted_sum % CHECKSUM_BASE

    calculated_check_digit = (CHECKSUM_BASE - remainder) % CHECKSUM_BASE

    check_digit = int(filtered_account_number[-1])
    if calculated_check_digit == check_digit:
        return True

    return False
