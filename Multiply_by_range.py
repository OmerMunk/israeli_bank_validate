def multiply_by_range(account_str, rng):
    """
    The function receives a string that consists of the branch number + account number,
    and the range of numbers to be multiplied by.
    note that the range does not include the last digit so you need to add a number!
    """
    num_multiplier_tuples =  zip(account_str, reversed(rng))
    res = sum(map(lambda  x: int(x[0]) * int(x[1]), num_multiplier_tuples))
    return (res)
