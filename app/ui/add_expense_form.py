import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from datetime import datetime
import uuid
from ..constants import ADD_FORM_SIZE, EXPENSE_CATEGORIES
from ..transaction import Transaction

class AddExpenseForm:
    def __init__(self, master, on_add):
        """
        master: parent window
        on_add: callback function to add a transaction (should accept a Transaction object)
        """
        self.top = tk.Toplevel(master)
        self.top.title("Add Expense")
        self.top.geometry(ADD_FORM_SIZE)
        self.top.grab_set()
        self.on_add = on_add

        form_frame = ttk.Frame(self.top, padding="20")
        form_frame.pack(fill="both", expand=True)

        ttk.Label(form_frame, text="Amount:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.amount_entry = ttk.Entry(form_frame)
        self.amount_entry.grid(row=0, column=1, sticky="ew")

        ttk.Label(form_frame, text="Category:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.category_var = tk.StringVar(value=EXPENSE_CATEGORIES[0])
        self.category_menu = ttk.Combobox(form_frame, textvariable=self.category_var, values=EXPENSE_CATEGORIES, state='readonly')
        self.category_menu.grid(row=1, column=1, sticky="ew")

        ttk.Label(form_frame, text="Date:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.date_picker = DateEntry(form_frame, date_pattern='yyyy-mm-dd', state='readonly')
        self.date_picker.grid(row=2, column=1, sticky="ew")

        ttk.Label(form_frame, text="Description:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.comment_entry = ttk.Entry(form_frame)
        self.comment_entry.grid(row=3, column=1, sticky="ew")

        form_frame.columnconfigure(1, weight=1)

        ttk.Button(form_frame, text="Add Expense", command=self.submit).grid(row=4, column=0, columnspan=2, pady=15)

    def validate_amount(self, amount_str):
        try:
            amount = float(amount_str)
            if amount <= 0:
                raise ValueError("Amount must be positive")
            return amount
        except ValueError:
            return None

    def submit(self):
        amount = self.validate_amount(self.amount_entry.get())
        category = self.category_var.get()
        date = self.date_picker.get()
        comment = self.comment_entry.get().strip()

        if amount is None:
            messagebox.showerror("Error", "Invalid amount. Must be a positive number.")
            return

        transaction = Transaction(str(uuid.uuid4()), amount, category, date, comment)
        self.on_add(transaction)
        messagebox.showinfo("Success", "Expense added successfully.")
        self.top.destroy() 