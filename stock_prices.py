# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 150
}

portfolio = {}
total_investment = 0

# Number of stocks
n = int(input("Enter the number of stocks: "))

# User input
for i in range(n):
    stock = input("Enter stock name (AAPL, TSLA, GOOGL, MSFT, AMZN): ").upper()

    if stock in stock_prices:
        quantity = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = quantity
    else:
        print("Stock not available!")

print("\n------ Portfolio Summary ------")

# Calculate total investment
for stock, quantity in portfolio.items():
    investment = stock_prices[stock] * quantity
    total_investment += investment
    print(f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${investment}")

print(f"\nTotal Investment Value = ${total_investment}")

# Save to text file (optional)
with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("------------------------\n")

    for stock, quantity in portfolio.items():
        investment = stock_prices[stock] * quantity
        file.write(f"{stock}: {quantity} shares = ${investment}\n")

    file.write(f"\nTotal Investment Value = ${total_investment}")

print("\nPortfolio saved successfully in 'portfolio.txt'.")

