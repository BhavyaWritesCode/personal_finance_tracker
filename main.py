import pandas as pd 
import csv
from datetime import datetime 

class CSV:
    CSV_FILE = "Finance_data.csv"
    
    @classmethod #this will have access to the class itself but it won't have access to its instance of the class
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=["Date", "Amount", "Category", "Payment_type", "Description"])
            df.to_csv(cls.CSV_FILE, index=False)
            
CSV.initialize_csv()