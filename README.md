# Stock Portfolio Tracker

A simple command-line Stock Portfolio Tracker built in Python. This tool helps users track their investments based on hardcoded stock prices, calculate individual and total portfolio values, and export reports in CSV or Text formats.

## Features

- **Hardcoded Price Reference**: AAPL ($180.00), TSLA ($250.00), MSFT ($350.00), AMZN ($150.00), GOOG ($140.00), NVDA ($480.00).
- **Interactive CLI**: Add new stocks, update quantities of existing stocks, and view the formatted table.
- **Robust Input Validation**:
  - Tickers are case-insensitive and verified against the tracked list.
  - Shares/quantities must be positive numbers.
- **Export Options**: Save the portfolio summary to a formatted Text file (`.txt`) or a CSV file (`.csv`).

## Getting Started

### Prerequisites
- Python 3.x

### Running the App
1. Initialize the virtual environment (if not already done):
   ```powershell
   python -m venv .venv
   ```
2. Run the application:
   ```powershell
   .venv\Scripts\python.exe portfolio_tracker.py
   ```

### Running Tests
Unit tests are written using the standard `unittest` library. Run them using:
```powershell
.venv\Scripts\python.exe -m unittest test_portfolio_tracker.py
```
