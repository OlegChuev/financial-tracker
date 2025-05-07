# Financial Tracker

A Python-based desktop application for tracking personal finances, built with Tkinter. This application helps you manage your income and expenses, categorize transactions, and visualize your financial data.

## Features

- Track income and expenses
- Categorize transactions
- Add comments to transactions
- View transaction history
- Visualize financial data with graphs
- Data persistence using JSON storage

## Requirements

- Python 3.8 or higher
- Tkinter (usually comes with Python)
- Matplotlib (for data visualization)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/OlegChuev/financial-tracker.git
cd financial-tracker
```

2. Create a virtual environment (recommended):

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the application:
```bash
python3 -m app.main
```

2. Using the application:
   - Add new transactions using the "Add Transaction" button
   - View your transaction history in the main window
   - Use the visualization features to analyze your spending patterns
   - Export your data using the file menu options

## Project Structure

| File/Folder                | Description                                 |
|----------------------------|---------------------------------------------|
| `app/main.py`              | Main application entry point                |
| `app/ui/main_window.py`    | Main window and navigation logic            |
| `app/ui/add_expense_form.py` | Add Expense dialog/form UI                |
| `app/ui/expense_table.py`  | Expense history table UI (grouped/sortable) |
| `app/ui/analysis_window.py`| Expense analysis/chart UI                   |
| `app/transaction.py`       | Transaction class definition                |
| `app/file_manager.py`      | Data persistence handling                   |
| `app/plotter.py`           | Data visualization utilities                |
| `app/constants.py`         | UI and category constants                   |
| `requirements.txt`         | Python dependencies                         |

All UI-related code is now organized under the `app/ui/` directory for clarity and maintainability.

## Testing

The project includes a comprehensive test suite using Python's built-in `unittest` framework. Tests are organized in the `tests/` directory and cover core functionality of the application.

### Running Tests

To run all tests:
```bash
python -m unittest discover tests
```

To run a specific test file:
```bash
python -m unittest tests/test_transaction.py
```

### Test Structure

| Test File                  | Description                                 |
|---------------------------|---------------------------------------------|
| `tests/test_transaction.py` | Tests for Transaction class creation and methods |
| `tests/test_file_manager.py` | Tests for data persistence and file operations |
| `tests/test_console_app.py` | Tests for console interface functionality |

### Writing New Tests

When adding new features, please ensure to:
1. Create corresponding test cases in the appropriate test file
2. Follow the existing test structure using `unittest.TestCase`
3. Use meaningful test method names starting with `test_`
4. Include docstrings explaining what each test verifies
5. Mock external dependencies (file operations, user input) when necessary

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with Python and Tkinter
- Uses Matplotlib for data visualization
