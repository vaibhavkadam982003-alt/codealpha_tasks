# Hardcoded stock prices dictionary
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 300,
    "GOOG": 140
}

portfolio = {}
total_investment = 0

try:
    n = int(input("How many different stocks do you want to add? "))
except ValueError:
    print("⚠️ Please enter a valid number.")
    exit()

for i in range(n):
    stock = input(f"Enter stock symbol {i+1}: ").upper()
    try:
        qty = int(input(f"Enter quantity of {stock}: "))
    except ValueError:
        print("⚠️ Quantity must be a number. Skipping this stock.")
        continue

    if stock in stock_prices:
        price = stock_prices[stock]
        value = price * qty
        portfolio[stock] = {"qty": qty, "price": price, "value": value}
        total_investment += value
    else:
        print(f"⚠️ Stock {stock} not found in price list.")

print("\n--- Portfolio Summary ---")
for stock, data in portfolio.items():
    print(f"{stock}: {data['qty']} shares @ ${data['price']} = ${data['value']}")

print(f"\nTotal Investment Value: ${total_investment}")

# Optional: Save to file
save_choice = input("\nDo you want to save the result to a file? (y/n): ").lower()
if save_choice == "y":
    with open("portfolio.txt", "w") as f:
        f.write("--- Portfolio Summary ---\n")
        for stock, data in portfolio.items():
            f.write(f"{stock}: {data['qty']} shares @ ${data['price']} = ${data['value']}\n")
        f.write(f"\nTotal Investment Value: ${total_investment}\n")
    print("✅ Portfolio saved to portfolio.txt")