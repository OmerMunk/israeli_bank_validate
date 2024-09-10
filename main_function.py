bank_function_map = {
    10: validate_Leumi_account,
    12: validate_the_operatives_account,
    4: validate_yahav_account,
    11: validate_discount_account,
    17: validate_discount_account,
    20: validate_mizrahi_tefahot_account,
    13: validate_association_account,
    31: validate_the_international_account,
    52: validate_the_international_account,
    14: validate_the_soldiers_treasure_account,
    46: validate_masad_account,
    9: validate_the_mail_account,
    22: validate_citibank_account,
    54: validate_jerusalem_account,
    23: validate_HSBC_account,
    18: validate_one_zero_account,
    39: validate_the_indian_account,
    3: validate_esh_account,
    47: validate_global_remit_account,
    35: validate_GROW_account,
    15: validate_ofek_credit_union_account,
}

def validate_account(bank_code: int, account_number: str, branch_number: str):
    if bank_code in bank_function_map:
        result = bank_function_map[bank_code](account_number, branch_number)
        if result:
            return ("The bank account is in order")
        else:
            return ("The bank account is incorrect")
    else:
        return ("The bank does not exist")