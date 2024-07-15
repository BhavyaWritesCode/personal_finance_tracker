import pandas as pd 
import csv
from datetime import datetime 

class CSV:
    CSV_FILE = "Finance_data.csv"
    COLUMNS = ["Date", "Amount", "Category", "Payment_type", "Description"]
    
    @classmethod #this will have access to the class itself but it won't have access to its instance of the class
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns= cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)
            
#creating a new dictionary which takes all the data 
    
    @classmethod 
    def add_entry(cls,Date,Amount,Category,Payment_type,Description):
        new_entry = {
            "Date": Date,
            "Amount": Amount,
            "Category": Category,
            "Payment_type": Payment_type,
            "Description": Description
        }
#opening a CSV file in append mode 
#it will append the data directly and ensure closing of file with context manager

        with open(cls.CSV_FILE, "a", newline ="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Your Entry Is Added Successfully")
        
    
            
CSV.initialize_csv()
CSV.add_entry("01-06-2024","500","expense","UPI","Swiggy food")