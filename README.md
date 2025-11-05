CodeAlpha_StockPortfolioTracke

The Stock Portfolio Tracker is a simple, interactive Python program that allows users to manage and calculate their investment portfolio directly from the command line.
You can enter stock names, quantities, and instantly view total investment values.
The app also let you to save your summary as a .txt or .csv file for future reference.

Key Features:
1. Predefined stock list: Includes popular companies like AAPL, TSLA, MSFT, and more.
2. Automatic value calculation: Calculates total value for each stock and the overall portfolio.
3. File saving options: Save your report in .txt or .csv format using a file dialog box.
4. Repeat session: Add more stocks or restart without closing the program.
5. Timestamps: Each saved report includes the current date and time.
6. Error handling: Validates stock names and quantities to prevent user mistakes.

Installation & Usage
Step 1: Clone the Repository
git clone https://github.com/your-username/stock-portfolio-tracker.git

Step 2: Navigate to the Folder
cd stock-portfolio-tracker

Step 3: Run the Program
python Main.py

Dependencies:
This project uses only built-in Python libraries — no installation required:
1. datetime: for timestamps
2. csv: to write data in CSV format
3. os: for clearing the console
4. time: for delay before exit
5. tkinter.filedialog: for save dialog box

