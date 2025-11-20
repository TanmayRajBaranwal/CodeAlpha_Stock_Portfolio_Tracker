# Stock Portfolio Tracker

# Hardcoded stock prices (dictionary)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 130
}

portfolio = {}  # dictionary to store stock and quantity
total_investment = 0

print("------ Stock Portfolio Tracker ------")
print("Available Stock Prices:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")
print("-------------------------------------")

# Taking user input
while True:
    stock_name = input("Enter stock symbol (or type 'done' to finish): ").upper()
    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("❌ Stock not found. Please choose from the list above.")
        continue

    quantity = int(input(f"Enter quantity for {stock_name}: "))
    portfolio[stock_name] = quantity

# Calculating total investment
for stock, qty in portfolio.items():
    investment = qty * stock_prices[stock]
    total_investment += investment
    print(f"{stock}: {qty} shares → Value: ${investment}")

print("-------------------------------------")
print(f"💰 Total Investment Value = ${total_investment}")
print("-------------------------------------")

# Optional: Save to file
save_choice = input("Do you want to save results to a file? (yes/no): ").lower()
if save_choice == "yes":
    with open("portfolio_report.txt", "w") as file:
        file.write("Stock Portfolio Report\n")
        file.write("--------------------------\n")
        for stock, qty in portfolio.items():
            file.write(f"{stock}: {qty} shares - Value: ${qty * stock_prices[stock]}\n")
        file.write("--------------------------\n")
        file.write(f"Total Investment: ${total_investment}\n")

    print("📁 Report saved successfully as portfolio_report.txt")
