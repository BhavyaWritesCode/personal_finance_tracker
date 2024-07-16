#this file contains all the functions related to the data asked by the user 

from datetime import datetime

date_format = "%d-%m-%Y"


def get_date(prompt, allow_default = False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)
    
    try:
        valid_date = datetime.strptim(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid date format. please enter the correct format   ")
        return get_date(prompt, allow_default)
    
                

def get_amount():
    
   
def get_category():
    pass

def get_description():
    pass

def get_payment_type():
    pass
 