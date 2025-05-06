import json

from app.transaction import Transaction

class FileManager:
    """
    A utility class for handling file operations related to transaction data.
    Provides methods for loading and saving transactions to/from JSON files.
    """

    @staticmethod
    def load_transactions(filename="data/transactions.json"):
        """
        Loads transactions from a JSON file and converts them to Transaction objects.

        Args:
            filename (str): Path to the JSON file containing transaction data. 
                          Defaults to 'transactions.json'.

        Returns:
            dict: A dictionary mapping transaction IDs to Transaction objects.
                 Returns empty dict if file is not found or contains invalid JSON.

        Example:
            transactions = FileManager.load_transactions('my_transactions.json')
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                transactions = {}
                for t in data.get("transactions", []):
                    transactions[t["id"]] = Transaction(
                        t["id"], t["amount"], t["category"], t["date"], t["description"]
                    )
                return transactions
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    @staticmethod
    def save_transactions(transactions, filename="data/transactions.json"):
        """
        Saves a dictionary of transactions to a JSON file.

        Args:
            transactions (dict): Dictionary mapping transaction IDs to Transaction objects
            filename (str): Path where the JSON file should be saved.
                          Defaults to 'transactions.json'.

        Example:
            FileManager.save_transactions(transactions, 'my_transactions.json')
        """
        data = {"transactions": [t.to_dict() for t in transactions.values()]}
        with open(filename, 'w') as file:
            json.dump(data, file, indent=2)
