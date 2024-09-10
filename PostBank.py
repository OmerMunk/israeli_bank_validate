# 10 . בנק הדואר
def validate_The_Mail_account(acount : str):
    # 059121900
    SIZE_OF_ACOUNT = len(acount)
    LIMIT_SIZE = 9
    try:
        if not acount.isdigit() or len(acount) > LIMIT_SIZE:
            raise ValueError("שגיאה: מספר החשבון חייב להכיל רק ספרות ואורכו לא יכול לעלות על 9 ספרות.")

        acount_number: str = acount.zfill(SIZE_OF_ACOUNT)
        calculate_multply = 0
        for i in range(0, SIZE_OF_ACOUNT):
            calculate_multply += (SIZE_OF_ACOUNT - i) * int(acount_number[i])
        if calculate_multply % 10 == 0:
            return True
        else:
            return False
    except ValueError as e:
        print(e)
        return False

print(validate_The_Mail_account("00059121900"))