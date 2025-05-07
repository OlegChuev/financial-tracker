import unittest
from app.transaction import Transaction

class TestTransaction(unittest.TestCase):
    def setUp(self):
        self.transaction = Transaction(
            id="123",
            amount=100.50,
            category="Food",
            date="2024-03-20",
            description="Grocery shopping"
        )

    def test_transaction_creation(self):
        """Test if transaction is created with correct attributes"""
        self.assertEqual(self.transaction.id, "123")
        self.assertEqual(self.transaction.amount, 100.50)
        self.assertEqual(self.transaction.category, "Food")
        self.assertEqual(self.transaction.date, "2024-03-20")
        self.assertEqual(self.transaction.description, "Grocery shopping")

    def test_transaction_str(self):
        """Test string representation of transaction"""
        expected_str = "Mar 20, 2024 - Food: $100.50 - Grocery shopping"
        self.assertEqual(str(self.transaction), expected_str)

    def test_transaction_to_dict(self):
        """Test conversion to dictionary"""
        expected_dict = {
            "id": "123",
            "amount": 100.50,
            "category": "Food",
            "date": "2024-03-20",
            "description": "Grocery shopping"
        }
        self.assertEqual(self.transaction.to_dict(), expected_dict)

if __name__ == '__main__':
    unittest.main()
