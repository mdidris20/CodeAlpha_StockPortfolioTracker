# Stock Protfolio Tracker


import datetime, csv, os, time
from tkinter import filedialog

# stock prices

def spt():
    stock_prices = {
        "AAPL": 223,
        "TSLA": 242,
        "MSFT": 417,
        "GOOGL": 182,
        "AMZN": 169,
        "NVDA": 116,
        "META": 519,
        "NFLX": 658,
        "AMD": 128,
        "INTC": 46,
        "IBM": 188,
        "ORCL": 132,
        "ADBE": 598,
        "PYPL": 72,
        "PEP": 169
    }


    # store user-input stocks and quantities
    portfolio = {}

    print("Welcome to the Stock Portfolio Tracker!")
    print("\n\nAvailabe stocks and prices:")
    for stock, price in stock_prices.items():
        print(f"    {stock}: ${price}")

    # User enters stock and quantities
    while True:
        print("\nEnter stock name and quantity (or type 'done' to finish)")
        stock = input("Enter stock name: ").upper()
        if stock =="DONE":
            break
        if stock not in stock_prices:
            print("Stock not available. Please choose from the list.")
            continue
        try:
            qty =int(input(f"Enter qty of {stock}: "))
            portfolio[stock] = portfolio.get(stock, 0) + qty
        except ValueError:
            print("Please enter a valid number.")

    # Calculate total investment
    total_investment = 0
    print("\n\nYour Portfolio Summary:")
    print("-"*50)
    print(f"{'Stock':<10}{'Quantity':<12}{'Price ($)':<12}{'Value ($)':<12}")
    print("-"*50)

    for stock, qty in portfolio.items():
        value = stock_prices[stock]*qty
        total_investment += value
        print(f"{stock:<10}{qty:<12}{stock_prices[stock]:<12}{value:<12}\n")

    print("-"*50)
    print(f"{'Total Investment Value:':<34}${total_investment}")
    print("-"*50)

    # Save results in .txt or .csv file
    save = input("\n\nWould yo like to save this summary? (y/n): ").lower()

    if save in ("yes", "y"):
        f_type = input(("\nWhich type of file do you want to save (.txt or .csv)?: ")).lower()

        if f_type in("txt", ".txt"):
            file_path = filedialog.asksaveasfilename(
                title="Save As",
                defaultextension=".txt",
                filetypes=[("Text Files","*.txt")]
            )
            if file_path:
                with open(file_path,"w") as file:
                    file.write(f"Stock Portfolio Summary {datetime.datetime.now()}\n\n")
                    file.write("-"*50+"\n")
                    file.write(f"{'Stock':<10}{'Quantity':<12}{'Price ($)':<12}{'Value ($)':<12}\n")
                    file.write("-"*50+"\n")
                    for stock, qty in portfolio.items():
                        value = stock_prices[stock]*qty
                        file.write(f"{stock:<10}{qty:<12}{stock_prices[stock]:<12}{value:<12}\n")
                    file.write("-"*50+"\n")
                    file.write(f"{'Total Investment Value:':<34}${total_investment}\n")
                print("\nFile created successfully.")
            else:
                print("\nFile not created!")


        elif f_type in ("csv",".csv"):
            file_path = filedialog.asksaveasfilename(
                title="Save As",
                defaultextension=".csv",
                filetypes=[(" ","*.csv")]
            )
            if file_path:
                with open(file_path, "w", newline = "") as cf:
                    write = csv.writer(cf)
                    write.writerow(f"Stock Portfolio Summary {datetime.datetime.now()}")
                    write.writerow(["Stock", "Quantity","Price ($)", "Value ($)"])
                    for stock, qty in portfolio.items():
                        value = stock_prices[stock]*qty
                        write.writerow([stock,qty,stock_prices[stock],value])
                    write.writerow([])
                    write.writerow(["Total Investment Value","","",total_investment])
                print("\nFile created successfully.")
            else:
                print("\nFile not created!")

    y_n = input("\nWant to add more stock and quantities? (y/n): ")
    if y_n in ["y","yes"]:
        os.system("cls")
        spt()
    else:
        print("\nThank you for using the Stock Portfolio Tracker")
        time.sleep(3)
        exit()

spt()