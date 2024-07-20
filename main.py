import pandas as pd
import csv
from datetime import datetime
from data_entry import get_amount, get_category, get_date, get_description, get_payment_type
import matplotlib.pyplot as plt

class CSV:
    CSV_FILE = "Finance_data.csv"
    COLUMNS = ["Date", "Amount", "Category", "Payment_type", "Description"]
    FORMAT = "%d-%m-%Y"

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)
            
    @classmethod
    def add_entry(cls, date, amount, category, payment_type, description):
        new_entry = {
            "Date": date,
            "Amount": amount,
            "Category": category,
            "Payment_type": payment_type,
            "Description": description
        }
        
        with open(cls.CSV_FILE, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Your Entry Is Added Successfully")
        
    @classmethod
    def get_transactions(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_FILE)
        df["Date"] = pd.to_datetime(df["Date"], format=CSV.FORMAT)
        start_date = datetime.strptime(start_date, CSV.FORMAT)
        end_date = datetime.strptime(end_date, CSV.FORMAT)
        
        mask = (df["Date"] >= start_date) & (df["Date"] <= end_date)
        filtered_df = df.loc[mask]
        
        if filtered_df.empty:
            print("No transactions found in the given date range")
        else:
            print(f"Transactions from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}")
            print(filtered_df.to_string(
                index=False, formatters={"Date": lambda x: x.strftime(CSV.FORMAT)}
            ))
            
            total_income = filtered_df[filtered_df["Category"] == "Income"]["Amount"].sum()
            total_expense = filtered_df[filtered_df["Category"] == "Expense"]["Amount"].sum()
            print("\nSummary: ")
            print(f"Total Income: ${total_income:.2f}")
            print(f"Total Expense: ${total_expense:.2f}")
            print(f"Net Savings: ${(total_income - total_expense):.2f}")
        return filtered_df

def add():
    CSV.initialize_csv()
    date = get_date("Enter the date of the transaction in the format (dd-mm-yyyy) or press enter for today's date: ", allow_default=True)
    amount = get_amount()
    category = get_category()
    payment_type = get_payment_type()
    description = get_description()
    CSV.add_entry(date, amount, category, payment_type, description)

def plot_graph(df):
    df.set_index('Date', inplace=True)  
    income_df = (
        df[df["Category"] == "Income"]
        .resample("D")
        .sum()
        .reindex(df.index, fill_value=0)
    )
    
    expense_df = (
        df[df["Category"] == "Expense"]
        .resample("D")
        .sum()
        .reindex(df.index, fill_value=0)
    )
    
    plt.figure(figsize=(10, 5))
    plt.plot(income_df.index, income_df["Amount"], label="Income", color="g")
    plt.plot(expense_df.index, expense_df["Amount"], label="Expense", color="r")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title('Income and Expense over time')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    while True:
        print("\n1. Add a new transaction ")
        print("2. View transactions and summary within the date range")
        print("3. Exit")
        choice = input("Enter the choice you want: ")
        
        if choice == "1":
            add()
        elif choice == "2":
            start_date = get_date("Enter the start date (dd-mm-yyyy): ")
            end_date = get_date("Enter the end date (dd-mm-yyyy): ")
            df = CSV.get_transactions(start_date, end_date)
            if input("Do you want to see the graph of your INCOME and EXPENSE? (y/n)").lower() == "y":
                plot_graph(df)  # Pass the dataframe to the plot_graph function
        elif choice == "3":
            print("Exiting. Enjoy!!")
            break
        else:
            print("Invalid choice, enter 1, 2, or 3. Thanks!!")

if __name__ == "__main__":
    main()
