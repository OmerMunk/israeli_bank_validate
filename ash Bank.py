from logging import exception
from wsgiref.validate import validator


def validate_esh_account(account_number: str, branch_number: str):
    if(len(account_number)<9 or len(account_number) >9):
        raise ValueError("The account number must be exactly 9 digits long")
    divide_num = 11
    list =[]
    for i in range(len(account_number)):
        list.append(int(account_number[i])*(i+1))
    result = sum(list)
    int_num = int(result /divide_num)
    float_num = result /divide_num
    if  int_num == float_num:
        return True
    else:
        return False



