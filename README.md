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

| File | Description |
|------|-------------|
| `app/main.py` | Main application entry point |
| `app/tkinter_app.py` | GUI implementation |
| `app/transaction.py` | Transaction class definition |
| `app/file_manager.py` | Data persistence handling |
| `app/plotter.py` | Data visualization utilities |


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
