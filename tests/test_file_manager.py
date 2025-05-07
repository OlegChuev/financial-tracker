import unittest
import json
from unittest.mock import patch, mock_open
from app.file_manager import FileManager
from app.transaction import Transaction

class TestFileManager(unittest.TestCase):
    def setUp(self):
        self.file_manager = FileManager()
        self.test_transactions = {
            "123": Transaction("123", 100.50, "Food", "2024-03-20", "Test1"),
            "124": Transaction("124", 200.75, "Food", "2024-03-20", "Test2")
        }

    def test_save_transactions(self):
        """Test saving transactions to file"""
        mock_file = mock_open()
        with patch('builtins.open', mock_file):
            self.file_manager.save_transactions(self.test_transactions)
            mock_file.assert_called_once()
            # Verify that the file was opened in write mode
            mock_file.assert_called_with("data/transactions.json", 'w')

    def test_load_transactions(self):
        """Test loading transactions from file"""
        test_data = {
            "transactions": [
                {
                    "id": "123",
                    "amount": 100.50,
                    "category": "Food",
                    "date": "2024-03-20",
                    "description": "Test1"
                },
                {
                    "id": "124",
                    "amount": 200.75,
                    "category": "Food",
                    "date": "2024-03-20",
                    "description": "Test2"
                }
            ]
        }
        
        mock_file = mock_open(read_data=json.dumps(test_data))
        with patch('builtins.open', mock_file):
            loaded_transactions = self.file_manager.load_transactions()
            self.assertEqual(len(loaded_transactions), 2)
            self.assertIn("123", loaded_transactions)
            self.assertIn("124", loaded_transactions)

    def test_load_transactions_empty_file(self):
        """Test loading transactions from empty file"""
        mock_file = mock_open(read_data='{"transactions": []}')
        with patch('builtins.open', mock_file):
            loaded_transactions = self.file_manager.load_transactions()
            self.assertEqual(len(loaded_transactions), 0)

if __name__ == '__main__':
    unittest.main()
