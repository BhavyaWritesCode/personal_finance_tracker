import pandas as pd 
import csv
from datetime import datetime 
from data_entry import get_amount, get_category, get_date, get_description, get_payment_type

class CSV:
    CSV_FILE = "Finance_data.csv"
    COLUMNS = ["Date", "Amount", "Category", "Payment_type", "Description"]
    FORMAT = "%d-%m-%Y"
    @classmethod #this will have access to the class itself but it won't have access to its instance of the class
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns= cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)
            
#creating a new dictionary which takes all the data 
    
    @classmethod 
    def add_entry(cls,date,amount,category,payment_type,description):
        new_entry = {
            "Date": date,
            "Amount": amount,
            "Category": category,
            "Payment_type": payment_type,
            "Description": description
        }
#opening a CSV file in append mode 
#it will append the data directly and ensure closing of file with context manager

        with open(cls.CSV_FILE, "a", newline ="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Your Entry Is Added Successfully")
        
    @classmethod
    def get_transactions(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_FILE)
        df["date"] = pd.to_datetime(df["date"], format=CSV.FORMAT)
        start_date = datetime.strptime(start_date, CSV.FORMAT)
        end_date = datetime.strptime(end_date, CSV.FORMAT)
        
        mask = (df["date"] >= start_date) & (df["date"] <= end_date)  
        #(&) is only being used when working with pandas or mask specifically
        filtered_df = df.loc[mask]
        #this will return a filtered dataframe that only contains the row when the above condition is true
        
        if filtered_df.empty:
            print("no ytransactions found in the given date")
        else:
            print(
            f"Transactions from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}"
            )
            print(filtered_df.to_string(
                index=False, formatters={"date": lambda x: x.strftime(CSV.FORMAT)}
                )
            )
            

def add():
    CSV.initialize_csv()
    date = get_date("enter the date of the transaction in the format (dd-mm-yyyy) or enter the present date: ", allow_default= True )
    amount = get_amount()
    category = get_category()
    description = get_description()
    payment_type = get_payment_type()
    CSV.add_entry(date, amount, category, description, payment_type)
    
add()
        
