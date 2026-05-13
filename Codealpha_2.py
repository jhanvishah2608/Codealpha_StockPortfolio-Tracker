
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 120,
    "MSFT": 310
}

my_portfolio = []

print("Welcome to Stock Tracker!")
print("Available stocks: AAPL, TSLA, GOOGL, AMZN, MSFT")
print("Type 'done' when you are finished.\n")


while True:
    name = input("Enter stock name: ").upper()

    if name == "DONE":
        break

   
    if name not in stock_prices:
        print("Sorry, that stock is not available. Try again.")
        continue

    quantity = int(input("Enter quantity: "))

   
    price = stock_prices[name]
    total = price * quantity

   
    my_portfolio.append([name, quantity, price, total])
    print(f"{name} added! Cost: {total}\n")


print("\n---------- YOUR PORTFOLIO ----------")
grand_total = 0

for item in my_portfolio:
    print(f"Stock: {item[0]} | Quantity: {item[1]} | Price: {item[2]} | Total: {item[3]}")
    grand_total = grand_total + item[3]

print(f"\nTotal Investment: {grand_total}")


save = input("\nDo you want to save the result? (yes/no): ").lower()

if save == "yes":
    # Ask what type of file
    file_type = input("Save as txt or csv? ").lower()

    if file_type == "txt":
        file = open("portfolio.txt", "w")
        file.write("YOUR PORTFOLIO\n")
        file.write("Stock | Quantity | Price | Total\n")
        for item in my_portfolio:
            file.write(f"{item[0]} | {item[1]} | {item[2]} | {item[3]}\n")
        file.write(f"\nTotal Investment: {grand_total}")
        file.close()
        print("Saved as portfolio.txt")

    elif file_type == "csv":
        file = open("portfolio.csv", "w")
        file.write("Stock,Quantity,Price,Total\n")
        for item in my_portfolio:
            file.write(f"{item[0]},{item[1]},{item[2]},{item[3]}\n")
        file.write(f"Total,,, {grand_total}")
        file.close()
        print("Saved as portfolio.csv")

else:
    print("Result not saved. Goodbye!")
