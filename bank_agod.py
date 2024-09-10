
def validate_Association_account(account_number: str,branch_number: str):
    try:
        calculat = str(calculate_bank_agod(account_number,branch_number))
        ifts = ["90","72","70","60","20"]
        if calculat[-2:] in ifts:
            return True
    except ValueError:
        return False


def calculate_bank_agod(account_number: str,branch_number: str):
    if 2 < len(account_number) + len(branch_number) < 10:
        return -1
    criticism_literature = int(account_number[-2:])
    multiplier = 10
    sum_calculate = 0
    branch_number += account_number[:-3]
    for i in range(len(branch_number)):
        if multiplier >= 2 and i != "-":
            sum_calculate += int(branch_number[i]) * multiplier
            multiplier -= 1
        else:
            continue

    return sum_calculate + criticism_literature
