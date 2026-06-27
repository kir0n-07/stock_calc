# stock_calc
Stock Portfolio Tracker

Project Description

This is a simple Python-based Stock Portfolio Tracker that allows users to enter stock names and quantities, calculates the total investment value using predefined stock prices, and saves the portfolio summary to a text file.

Features

- Accepts user input for stock names and quantities.
- Uses hardcoded stock prices.
- Calculates investment value for each stock.
- Displays the total investment value.
- Saves the portfolio summary to a "portfolio.txt" file.

Technologies Used

- Python 3
- Dictionary
- Loops
- Conditional Statements
- File Handling

Hardcoded Stock Prices

Stock| Price ($)
AAPL| 180
TSLA| 250
GOOGL| 140
MSFT| 330
AMZN| 150

How to Run

1. Make sure Python 3 is installed.
2. Save the program as "stock_portfolio.py".
3. Open a terminal or command prompt.
4. Run the program using:

python stock_portfolio.py

5. Enter the number of stocks.
6. Enter the stock names and quantities when prompted.
7. The program will display the investment summary and create a file named "portfolio.txt".

Sample Output

Enter the number of stocks: 2
Enter stock name (AAPL, TSLA, GOOGL, MSFT, AMZN): AAPL
Enter quantity of AAPL: 5
Enter stock name (AAPL, TSLA, GOOGL, MSFT, AMZN): TSLA
Enter quantity of TSLA: 3

------ Portfolio Summary ------
AAPL: 5 shares × $180 = $900
TSLA: 3 shares × $250 = $750

Total Investment Value = $1650

Portfolio saved successfully in 'portfolio.txt'.

Output File

The program generates a file named "portfolio.txt" containing:

- Stock names
- Quantities
- Investment value for each stock
- Total investment value

Author

Kiran 
