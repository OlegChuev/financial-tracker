import tkinter as tk
from tkinter import ttk
from datetime import datetime
from collections import defaultdict
from ..constants import BALANCE_WINDOW_SIZE, BALANCE_FONT

class ExpenseTable:
    def __init__(self, master, transactions):
        self.top = tk.Toplevel(master)
        self.top.title("Expense History")
        self.top.geometry(BALANCE_WINDOW_SIZE)
        self.top.grab_set()

        main_frame = ttk.Frame(self.top, padding="20")
        main_frame.pack(fill="both", expand=True)

        total_expenses = sum(t.amount for t in transactions.values())
        ttk.Label(main_frame, text=f"Total Expenses: ${total_expenses:.2f}", font=BALANCE_FONT).pack(pady=10)

        columns = ("date", "category", "amount", "description")
        self.tree = ttk.Treeview(main_frame, columns=columns, show="headings", height=15)
        for col in columns:
            self.tree.heading(col, text=col.capitalize(), command=lambda c=col: self._sort_treeview(c, False))
        self.tree.column("date", width=100, anchor="center")
        self.tree.column("category", width=120, anchor="center")
        self.tree.column("amount", width=100, anchor="e")
        self.tree.column("description", width=200, anchor="w")

        # Group transactions by month
        grouped = defaultdict(list)
        for t in transactions.values():
            month = t.date[:7]  # 'YYYY-MM'
            grouped[month].append(t)
        for month in sorted(grouped.keys(), reverse=True):
            month_str = datetime.strptime(month, "%Y-%m").strftime("%B %Y")
            parent = self.tree.insert("", "end", values=(month_str, "", "", ""), open=True)
            for t in sorted(grouped[month], key=lambda x: x.date, reverse=True):
                self.tree.insert(parent, "end", values=(t.date, t.category, f"{t.amount:.2f}", t.description))

        self.tree.pack(fill="both", expand=True, pady=10)
        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

    def _sort_treeview(self, col, reverse):
        # Get all items except month headers (which have empty category/amount/description)
        items = [(self.tree.set(k, col), k) for k in self.tree.get_children("") for k in self.tree.get_children(k)]
        try:
            if col == "amount":
                items.sort(key=lambda t: float(t[0]), reverse=reverse)
            elif col == "date":
                items.sort(key=lambda t: t[0], reverse=reverse)
            else:
                items.sort(key=lambda t: t[0].lower(), reverse=reverse)
        except Exception:
            items.sort(key=lambda t: t[0], reverse=reverse)
        for index, (val, k) in enumerate(items):
            self.tree.move(k, '', index)
        self.tree.heading(col, command=lambda: self._sort_treeview(col, not reverse)) 