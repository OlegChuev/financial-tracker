from datetime import datetime

class Transaction:
    """
    A class representing a financial transaction.
    Stores information about income or expense transactions including amount, category, and date.

    Attributes:
        id (str): Unique identifier for the transaction
        amount (float): Monetary value of the transaction
        category (str): Category the transaction belongs to
        date (str): Date when the transaction occurred
        description (str): Optional description about the transaction
    """

    def __init__(self, id, amount, category, date, description=""):
        """
        Initialize a new Transaction object.

        Args:
            id (str): Unique identifier for the transaction
            amount (float): Monetary value of the transaction
            category (str): Category the transaction belongs to
            date (str): Date when the transaction occurred
            description (str, optional): Description about the transaction. Defaults to empty string.
        """
        self.id = id
        self.amount = float(amount)
        self.category = category
        self.date = date
        self.description = description

    def to_dict(self):
        """
        Convert the Transaction object to a dictionary for JSON serialization.

        Returns:
            dict: Dictionary containing all transaction attributes
        """
        return {
            "id": self.id,
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
            "description": self.description
        }

    def __str__(self):
        """
        Create a string representation of the Transaction.

        Returns:
            str: Formatted string containing all transaction details
        """
        date_obj = datetime.strptime(self.date, "%Y-%m-%d")
        formatted_date = date_obj.strftime("%b %d, %Y")
        return f"{formatted_date} - {self.category}: ${self.amount:.2f} - {self.description}"
