import unittest
import os
import csv
from portfolio_tracker import (
    STOCK_PRICES,
    get_portfolio_summary,
    save_to_txt,
    save_to_csv
)

class TestStockPortfolioTracker(unittest.TestCase):
    def setUp(self):
        # Sample portfolio for testing
        self.portfolio = {
            "AAPL": 10.0,   # 10 * 180 = 1800
            "TSLA": 5.0,    # 5 * 250 = 1250
            "GOOG": 2.5     # 2.5 * 140 = 350
        }
        # Expected total: 1800 + 1250 + 350 = 3400.0
        self.expected_total = 3400.0
        self.txt_test_file = "test_portfolio.txt"
        self.csv_test_file = "test_portfolio.csv"

    def tearDown(self):
        # Clean up test files if they exist
        for filepath in (self.txt_test_file, self.csv_test_file):
            if os.path.exists(filepath):
                try:
                    os.remove(filepath)
                except OSError:
                    pass

    def test_get_portfolio_summary_empty(self):
        details, total = get_portfolio_summary({})
        self.assertEqual(details, [])
        self.assertEqual(total, 0.0)

    def test_get_portfolio_summary_calculation(self):
        details, total = get_portfolio_summary(self.portfolio)
        self.assertEqual(total, self.expected_total)
        self.assertEqual(len(details), 3)

        # Check details for AAPL
        aapl_detail = next(item for item in details if item["ticker"] == "AAPL")
        self.assertEqual(aapl_detail["quantity"], 10.0)
        self.assertEqual(aapl_detail["price"], 180.0)
        self.assertEqual(aapl_detail["value"], 1800.0)

        # Check details for GOOG
        goog_detail = next(item for item in details if item["ticker"] == "GOOG")
        self.assertEqual(goog_detail["quantity"], 2.5)
        self.assertEqual(goog_detail["price"], 140.0)
        self.assertEqual(goog_detail["value"], 350.0)

    def test_save_to_txt(self):
        save_to_txt(self.txt_test_file, self.portfolio)
        self.assertTrue(os.path.exists(self.txt_test_file))
        
        with open(self.txt_test_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        self.assertIn("AAPL", content)
        self.assertIn("TSLA", content)
        self.assertIn("GOOG", content)
        self.assertIn("TOTAL INVESTMENT VALUE", content)
        self.assertIn("3400.00", content)

    def test_save_to_csv(self):
        save_to_csv(self.csv_test_file, self.portfolio)
        self.assertTrue(os.path.exists(self.csv_test_file))
        
        rows = []
        with open(self.csv_test_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            rows = list(reader)
            
        # Header + 3 stocks + empty row + total row = 6 rows
        self.assertEqual(len(rows), 6)
        
        # Verify header
        self.assertEqual(rows[0], ["Ticker", "Quantity", "Price Per Share", "Total Value"])
        
        # Verify AAPL row
        aapl_row = next(row for row in rows if row and row[0] == "AAPL")
        self.assertEqual(aapl_row, ["AAPL", "10.0000", "180.00", "1800.00"])
        
        # Verify Total row
        total_row = next(row for row in rows if row and row[0] == "TOTAL INVESTMENT VALUE")
        self.assertEqual(total_row[3], "3400.00")

if __name__ == "__main__":
    unittest.main()
