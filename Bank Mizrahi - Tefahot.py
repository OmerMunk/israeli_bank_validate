def test_Bank_20(account_number: str, branch_number: str):
    # Runs a testing function
    initial_tests(account_number, branch_number)

    # Convert branch number to int
    branch_number_int_conversion = int(branch_number)

    # Branches in the range of 401-799 must subtract 400
    if 800 > branch_number_int_conversion > 400:
        branch_number_int_conversion -= 400

    tamp = 0
    multiplier = 1

    for num in account_number[::-1]:
        if int(num) == 0:
            continue
        tamp += int(num) * multiplier
        multiplier += 1

    multiplier += 1

    for num in str(branch_number_int_conversion)[::-1]:
        if int(num) == 0:
            continue
        tamp += int(num) * multiplier
        multiplier += 1

    CONNECTING_SHOULD_DIVIDED = 11
    return (tamp % CONNECTING_SHOULD_DIVIDED == 0
            or tamp % CONNECTING_SHOULD_DIVIDED == 2
            or tamp % CONNECTING_SHOULD_DIVIDED == 4)


def initial_tests(account_number, branch_number):
    if type(account_number) is not str or type(branch_number) is not str:
        raise TypeError("Only strings are allowed")
    if len(account_number) != 6 or len(branch_number) != 3:
        raise Exception("account number must be 6 end branch number must be 3")
    try:
        int(account_number)
        int(branch_number)
    except:
        raise Exception("Must contain only whole numbers")
    if not 1000 > int(branch_number) > 400:
        raise Exception("Invalid branch number, a number between 401 and 999 must be given")


a = "160778"
b = "406"
print(test_Bank_20(a, b))

