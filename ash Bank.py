from logging import exception
from wsgiref.validate import validator

"""
פונקציה שבודקת תקינות של מספר חשבון של בנק אש
בעצם אני מקבל את המספרים כולל ספרת ביקורת ומכפיל אותם מ1 בסדר עולה עד 9 התוצאה שלהם חלקי 11 אמורה להיות מספר שלם

"""
def validate_esh_account(account_number: str, branch_number: str):
    grate_len_of_the_numbers = 9
    if(len(account_number)<grate_len_of_the_numbers or len(account_number) >grate_len_of_the_numbers):
        raise ValueError("The account number must be exactly 9 digits long")
    divide_num = 11
    list_of_numbers =[]
    for i in range(len(account_number)):
        #אני פה עושה את פעולת החשבון עבור כל מספר מהסטרינג שמגיע לי אני מכפיל אותו במספר ודוחף אותו כint לרשימה חדשה
        list.append(int(account_number[i])*(i+1))
    result = sum(list)
    int_num = int(result /divide_num)
    float_num = result /divide_num
    if  int_num == float_num:
        return True
    else:
        return False



