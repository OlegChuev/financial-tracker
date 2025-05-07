from datetime import datetime
from typing import Dict, Optional

from app.transaction import Transaction
from app.file_manager import FileManager
from app.plotter import Plotter

class ConsoleApp:
    def __init__(self):
        self.transactions: Dict[str, Transaction] = {}
        self.file_manager = FileManager()
        self.plotter = Plotter()

    def load_data(self):
        """Load transactions from file"""
        self.transactions = self.file_manager.load_transactions()

    def save_data(self):
        """Save transactions to file"""
        self.file_manager.save_transactions(self.transactions)

    def add_transaction(self):
        """Add a new transaction"""
        print("\n=== Add New Transaction ===")
        
        # Generate a simple ID based on timestamp
        transaction_id = datetime.now().strftime("%Y%m%d%H%M%S")
        
        try:
            amount = float(input("Enter amount: $"))
            category = input("Enter category: ")
            date = input("Enter date (YYYY-MM-DD): ")
            description = input("Enter description (optional): ")
            
            transaction = Transaction(transaction_id, amount, category, date, description)
            self.transactions[transaction_id] = transaction
            self.save_data()
            print("Transaction added successfully!")
        except ValueError as e:
            print(f"Error: {str(e)}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def view_transactions(self):
        """Display all transactions"""
        if not self.transactions:
            print("\nNo transactions found.")
            return

        print("\n=== Transaction History ===")
        for transaction in self.transactions.values():
            print(transaction)

    def analyze_expenses(self):
        """Show expense analysis and charts"""
        if not self.transactions:
            print("\nNo transactions to analyze.")
            return

        print("\n=== Expense Analysis ===")
        
        # Show monthly totals
        expenses_by_month = {}
        for transaction in self.transactions.values():
            month = transaction.date[:7]  # YYYY-MM
            expenses_by_month[month] = expenses_by_month.get(month, 0) + transaction.amount

        print("\nMonthly Totals:")
        for month, total in sorted(expenses_by_month.items()):
            print(f"{month}: ${total:.2f}")

        # Show category totals
        expenses_by_category = {}
        for transaction in self.transactions.values():
            expenses_by_category[transaction.category] = expenses_by_category.get(transaction.category, 0) + transaction.amount

        print("\nCategory Totals:")
        for category, total in sorted(expenses_by_category.items()):
            print(f"{category}: ${total:.2f}")

        # Generate and save plots
        fig = self.plotter.plot_expenses(self.transactions)
        if fig:
            fig.savefig('expense_analysis.png')
            print("\nAnalysis plots have been saved to 'expense_analysis.png'")

    def run(self):
        """Main application loop"""
        self.load_data()
        
        while True:
            print("\n=== Financial Tracker ===")
            print("1. Add Transaction")
            print("2. View Transactions")
            print("3. Analyze Expenses")
            print("4. Exit")
            
            choice = input("\nEnter your choice (1-4): ")
            
            if choice == "1":
                self.add_transaction()
            elif choice == "2":
                self.view_transactions()
            elif choice == "3":
                self.analyze_expenses()
            elif choice == "4":
                print("\nSaving data and exiting...")
                self.save_data()
                break
            else:
                print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    app = ConsoleApp()
    app.run() 
