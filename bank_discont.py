# 4. קבוצת דיסקונט
def validateDiscount_account(account_number: str, branch_number: str):
    if len(account_number) != 9:
        return False
    list_account_number = [int(num) for num in account_number]
    NUM_MULTIPLITED_INDEX = 1
    MULTIPLITER_NUMBER_INDEX = 0
    sum_multiple_numbers = sum(list(map(lambda x: x[NUM_MULTIPLITED_INDEX] * x[MULTIPLITER_NUMBER_INDEX], enumerate(list_account_number, start=NUM_MULTIPLITED_INDEX))))
    if sum_multiple_numbers / 11 == 0 or 2 or 4:
        return True

print(validateDiscount_account("111111111", "123456"))