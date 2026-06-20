import csv
import os

# Hardcoded dictionary defining stock prices
STOCK_PRICES = {
    "AAPL": 180.0,
    "TSLA": 250.0,
    "MSFT": 350.0,
    "AMZN": 150.0,
    "GOOG": 140.0,
    "NVDA": 480.0
}

def display_available_stocks():
    """Prints the list of available stocks and their prices."""
    print("\n" + "=" * 35)
    print(f"{'Stock Ticker':<15}{'Price per Share':>15}")
    print("-" * 35)
    for ticker, price in STOCK_PRICES.items():
        print(f"{ticker:<15}${price:>14.2f}")
    print("=" * 35 + "\n")

def get_portfolio_summary(portfolio):
    """
    Calculates details for each stock in the portfolio and the total value.
    Returns:
        tuple: (list of dicts containing detail rows, total portfolio value)
    """
    details = []
    total_value = 0.0
    for ticker, quantity in portfolio.items():
        price = STOCK_PRICES[ticker]
        value = price * quantity
        total_value += value
        details.append({
            "ticker": ticker,
            "quantity": quantity,
            "price": price,
            "value": value
        })
    return details, total_value

def display_portfolio(portfolio):
    """Prints a formatted summary table of the portfolio."""
    if not portfolio:
        print("\nYour portfolio is currently empty.")
        return

    details, total_value = get_portfolio_summary(portfolio)
    
    print("\n" + "=" * 55)
    print(f"{'Ticker':<10}{'Quantity':>12}{'Price':>12}{'Total Value':>18}")
    print("-" * 55)
    for item in details:
        print(f"{item['ticker']:<10}{item['quantity']:>12.4f}${item['price']:>11.2f}${item['value']:>17.2f}")
    print("-" * 55)
    print(f"{'TOTAL INVESTMENT VALUE:':<34}${total_value:>17.2f}")
    print("=" * 55 + "\n")

def save_to_txt(filepath, portfolio):
    """Saves the portfolio summary to a formatted text file."""
    details, total_value = get_portfolio_summary(portfolio)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write("=== Stock Portfolio Tracker Report ===\n")
        f.write(f"{'Ticker':<10}{'Quantity':>12}{'Price':>12}{'Total Value':>18}\n")
        f.write("-" * 55 + "\n")
        for item in details:
            f.write(f"{item['ticker']:<10}{item['quantity']:>12.4f}${item['price']:>11.2f}${item['value']:>17.2f}\n")
        f.write("-" * 55 + "\n")
        f.write(f"{'TOTAL INVESTMENT VALUE:':<34}${total_value:>17.2f}\n")
        f.write("======================================\n")

def save_to_csv(filepath, portfolio):
    """Saves the portfolio details to a CSV file."""
    details, total_value = get_portfolio_summary(portfolio)
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Ticker", "Quantity", "Price Per Share", "Total Value"])
        for item in details:
            writer.writerow([item['ticker'], f"{item['quantity']:.4f}", f"{item['price']:.2f}", f"{item['value']:.2f}"])
        writer.writerow([])
        writer.writerow(["TOTAL INVESTMENT VALUE", "", "", f"{total_value:.2f}"])

def main():
    print("Welcome to the Stock Portfolio Tracker!")
    portfolio = {}
    
    while True:
        display_available_stocks()
        
        # Get Stock Ticker
        ticker_input = input("Enter stock ticker to add/update (or press Enter to finish): ").strip().upper()
        if not ticker_input:
            break
            
        if ticker_input not in STOCK_PRICES:
            print(f"Error: '{ticker_input}' is not in our tracked list. Please select from the list above.")
            continue
            
        # Get Quantity
        try:
            qty_input = input(f"Enter quantity of {ticker_input} shares: ").strip()
            quantity = float(qty_input)
            if quantity <= 0:
                print("Error: Quantity must be greater than zero.")
                continue
        except ValueError:
            print("Error: Please enter a valid number for quantity.")
            continue
            
        # Add/update portfolio
        portfolio[ticker_input] = portfolio.get(ticker_input, 0.0) + quantity
        print(f"Added {quantity:.4f} shares of {ticker_input} to your portfolio.")
    
    display_portfolio(portfolio)
    
    if portfolio:
        save_choice = input("Would you like to save your portfolio to a file? (y/n): ").strip().lower()
        if save_choice in ('y', 'yes'):
            print("\nSelect export format:")
            print("1. Text File (.txt)")
            print("2. CSV File (.csv)")
            format_choice = input("Enter 1 or 2: ").strip()
            
            filename = input("Enter filename (without extension): ").strip()
            if not filename:
                filename = "portfolio_summary"
                
            if format_choice == '2':
                filepath = f"{filename}.csv"
                save_to_csv(filepath, portfolio)
                print(f"Portfolio saved to CSV: {os.path.abspath(filepath)}")
            else:
                filepath = f"{filename}.txt"
                save_to_txt(filepath, portfolio)
                print(f"Portfolio saved to Text file: {os.path.abspath(filepath)}")
                
    print("\nThank you for using Stock Portfolio Tracker!")

if __name__ == "__main__":
    main()
