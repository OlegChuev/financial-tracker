import tkinter as tk
from tkinter import ttk, messagebox
from ..file_manager import FileManager
from ..constants import (
    APP_TITLE,
    MAIN_WINDOW_SIZE,
    TITLE_FONT,
    BUTTON_WIDTH
)
from .add_expense_form import AddExpenseForm
from .expense_table import ExpenseTable
from .analysis_window import AnalysisWindow

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title(APP_TITLE)
        self.root.geometry(MAIN_WINDOW_SIZE)

        style = ttk.Style()
        style.configure("TButton", padding=6, relief="flat", background="#007AFF")
        style.configure("TLabel", padding=4)
        style.configure("TEntry", padding=4)
        style.configure("TFrame", background="white")

        self.transactions = FileManager.load_transactions()

        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        ttk.Label(main_frame, text=APP_TITLE, font=TITLE_FONT).pack(pady=10)
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill="x", padx=10)

        ttk.Button(button_frame, text="Add Expense", command=self.show_add_transaction_form, width=BUTTON_WIDTH, style="TButton").pack(pady=8, fill="x")
        ttk.Button(button_frame, text="View Expenses", command=self.show_balance, width=BUTTON_WIDTH, style="TButton").pack(pady=8, fill="x")
        ttk.Button(button_frame, text="Expense Analysis", command=self.show_expense_plot, width=BUTTON_WIDTH, style="TButton").pack(pady=8, fill="x")
        ttk.Button(button_frame, text="Save and Exit", command=self.save_and_exit, width=BUTTON_WIDTH, style="TButton").pack(pady=8, fill="x")

    def show_add_transaction_form(self):
        def add_transaction(transaction):
            self.transactions[transaction.id] = transaction
        AddExpenseForm(self.root, add_transaction)

    def show_balance(self):
        ExpenseTable(self.root, self.transactions)

    def show_expense_plot(self):
        AnalysisWindow(self.root, self.transactions)

    def save_and_exit(self):
        FileManager.save_transactions(self.transactions)
        messagebox.showinfo("Info", "Data saved. Exiting...")
        self.root.destroy() 
