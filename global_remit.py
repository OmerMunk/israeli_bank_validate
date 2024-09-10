def validate_global_remit_account(account_number: str, branch_number: str):
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
