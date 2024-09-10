# 4. קבוצת דיסקונט
def validateDiscount_account(account_number: str, branch_number: str) -> bool:
    VALID_LENGTH = 9
    NUM_MULTIPLITED_INDEX = 1
    MULTIPLITER_NUMBER_INDEX = 0
    if len(account_number) != VALID_LENGTH:
        return False
    list_account_number = [int(num) for num in account_number]
    sum_multiple_numbers = sum(list(map(lambda x: x[NUM_MULTIPLITED_INDEX] * x[MULTIPLITER_NUMBER_INDEX], enumerate(list_account_number, start=NUM_MULTIPLITED_INDEX))))
    final_result = sum_multiple_numbers / 11
    valid_result = [0, 2, 4]
    if final_result in valid_result:
        return True

print(validateDiscount_account("111111111", "123456"))

