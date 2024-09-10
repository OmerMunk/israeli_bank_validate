# 10 . בנק הדואר
def validate_The_Mail_account(acount : str):
    # 059121900
    try:
        if not acount.isdigit() or len(acount) > 9:
            raise ValueError("שגיאה: מספר החשבון חייב להכיל רק ספרות ואורכו לא יכול לעלות על 9 ספרות.")

        acount_number : str = acount.zfill(9)
        sum = 0
        for i in range(0, 9):
            sum += (9 - i) * int(acount_number[i])
        if sum % 10 == 0:
            return True
        else:
            return False
    except ValueError as e:
        print(e)
        return False

print(validate_The_Mail_account("059121900"))