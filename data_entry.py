#this file contains all the functions related to the data asked by the user 

from datetime import datetime

date_format = "%d-%m-%Y"
CATEGORIES = {"I": "Income", "E":"Expense"}
PAYMENT_METHODS = {"U": "UPI", "C": "Cash"}


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
    try:
        amount = float(input("enter the amount which is spent"))
        if amount <= 0:
            raise ValueError("Amount must be positive and greater then zero ")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()
    
    
def get_category():
    category = input("enter the category 'I' for income and 'E' for expense : ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]
    
    print("Invalid category , please enter either I or E for the Income and Expense")
    return get_category
 
       
def get_description():
    return input("enter the description for the money spent ")


def get_payment_type():
    method = input("enter the payment method you did 'U' for 'UPI' or 'C' for 'Cash'")
    if method in PAYMENT_METHODS:
        return PAYMENT_METHODS[method]
    
 