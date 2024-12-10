
"""This function validates an account number for Ofek Credit Union Bank. It ensures that the account number is correct
    according to a specific algorithm. The function takes two parameters: an account number (account_number)
    and a branch number (branch_number), and returns a boolean value (True or False) indicating whether
    the account number is valid."""
def validate_ofek_credit_union_account(account_number: str, branch_number: str) -> bool:

    # Pad the account number to ensure it is 9 digits, filling with zeros on the left if necessary
    account_number_with_ziro: str = f"{account_number:0>9}"

    # Define the expected length for the account number
    ACCOUNT_NUMBER_LENGTH = 9

    # Check if the account number is exactly 9 digits and both account number and branch number are digits
    if len(account_number_with_ziro) != ACCOUNT_NUMBER_LENGTH or not account_number_with_ziro.isdigit() or not branch_number.isdigit():
        return False

    # Extract the base number, which is the first 7 digits of the padded account number
    base_number: int = int(account_number_with_ziro[:7])

    # Extract the criticism number, which is the last 2 digits of the padded account number
    criticism_number: int = int(account_number_with_ziro[7:])

    # Validate the account number using the formula: 98 - (base_number % 97) should equal the criticism number
    check_according_formula: bool = 98 - (base_number % 97) == criticism_number

    # Return True if the account number is valid according to the formula; otherwise, return False
    return check_according_formula
