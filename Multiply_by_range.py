
"""
The function receives a string that consists of the branch number + account number,
and the range of numbers to be multiplied by.
note that the range does not include the last digit so you need to add a number!
"""
def multiply_by_range(account_str, rng):
    zip1 =  zip(account_str, reversed(rng))
    res = sum(map(lambda  x: int(x[0]) * int(x[1]), zip1))
    return (res)
