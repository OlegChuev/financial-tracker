import matplotlib.pyplot as plt # type: ignore
from collections import defaultdict
from datetime import datetime

class Plotter:
    """
    A utility class for generating visualizations of financial data.
    Provides static methods for creating various plots and charts.
    """

    @staticmethod
    def plot_expenses(transactions):
        """
        Generates visualizations of expenses:
        1. A line chart showing total expenses per month
        2. A pie chart showing distribution by category

        Args:
            transactions (dict): Dictionary mapping transaction IDs to Transaction objects

        Returns:
            matplotlib.figure.Figure: A Figure object containing the visualizations.
                                    Returns None if there are no transactions to plot.
        """
        if not transactions:
            return None

        # Create figure with two subplots
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

        # --- 1. Aggregate expenses by month ---
        expenses_by_month = defaultdict(float)
        for t in transactions.values():
            month = datetime.strptime(t.date, "%Y-%m-%d").strftime("%Y-%m")
            expenses_by_month[month] += t.amount
        months = sorted(expenses_by_month.keys())
        totals = [expenses_by_month[m] for m in months]

        # Plot line chart of total expenses per month
        ax1.plot(months, totals, marker='o', linestyle='-')
        ax1.set_title("Total Expenses Over Time")
        ax1.set_xlabel("Month")
        ax1.set_ylabel("Total Expenses ($)")
        ax1.tick_params(axis='x', rotation=45)

        # --- 2. Pie chart by category ---
        expenses_by_category = defaultdict(float)
        for t in transactions.values():
            expenses_by_category[t.category] += t.amount
        categories = list(expenses_by_category.keys())
        cat_amounts = list(expenses_by_category.values())
        ax2.pie(cat_amounts, labels=categories, autopct='%1.1f%%')
        ax2.set_title("Distribution by Category")

        plt.tight_layout()
        return fig

    @staticmethod
    def plot_expenses_for_month(transactions, month):
        """
        Plot expenses for a single month (line/bar and pie chart).
        Args:
            transactions (dict): All transactions
            month (str): 'YYYY-MM'
        Returns:
            matplotlib.figure.Figure or None
        """
        # Filter transactions for the month
        month_transactions = [t for t in transactions.values() if t.date.startswith(month)]
        if not month_transactions:
            return None

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

        # Line/bar chart: expenses by day
        days = []
        amounts = []
        by_day = defaultdict(float)
        for t in month_transactions:
            day = t.date
            by_day[day] += t.amount
        for day in sorted(by_day.keys()):
            days.append(day)
            amounts.append(by_day[day])
        ax1.bar(days, amounts)
        ax1.set_title(f"Expenses in {month}")
        ax1.set_xlabel("Day")
        ax1.set_ylabel("Total Expenses ($)")
        ax1.tick_params(axis='x', rotation=45)

        # Pie chart: by category
        by_cat = defaultdict(float)
        for t in month_transactions:
            by_cat[t.category] += t.amount
        categories = list(by_cat.keys())
        cat_amounts = list(by_cat.values())
        ax2.pie(cat_amounts, labels=categories, autopct='%1.1f%%')
        ax2.set_title("By Category")

        plt.tight_layout()
        return fig

    @staticmethod
    def get_months(transactions):
        """
        Return a sorted list of months (YYYY-MM) present in transactions.
        """
        months = set()
        for t in transactions.values():
            months.add(t.date[:7])
        return sorted(months)
