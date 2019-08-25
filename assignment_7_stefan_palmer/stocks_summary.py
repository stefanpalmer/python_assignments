"""
*****************************************************************************************
Description: This program calculates earnings/loss, and yearly earnings/loss for stocks 
and bonds with given data for a particular user from CSV files. The results are inserted
in tables stored in a SQlite database.
Author: Stefan Palmer
Last Revision: 08/04/2019
*****************************************************************************************
"""

# Import modules and classes
import csv
import sqlite3
from stocks_module import Stock, Bond

# Store file paths in variables
stock_file_path = 'assignment_7_stefan_palmer/Lesson6_Data_Stocks1.csv'
bond_file_path = 'assignment_7_stefan_palmer/Lesson6_Data_Bonds.csv'

try:
    # Open the CSV files
    stock_file = open(stock_file_path, newline='')
    bond_file = open(bond_file_path, newline='')
    # Read files
    stock_reader = csv.reader(stock_file)
    bond_reader = csv.reader(bond_file)
except IOError:
    print("File cannot be read.")

# Headers
stock_header = next(stock_reader)
bond_header = next(bond_reader)

# Database connect
conn = sqlite3.connect('stock_summary1.db')

# Cursor
c = conn.cursor()

# Create tables
try:
    c.execute("""CREATE TABLE IF NOT EXISTS stocks (
                stock_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, stock_symbol TEXT, number_of_shares INTEGER, 
                earnings_loss REAL, yearly_earnings_percent REAL);""")

    c.execute("""CREATE TABLE IF NOT EXISTS bonds (
                bond_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, stock_symbol TEXT, number_of_shares INTEGER, 
                earnings_loss REAL, yearly_earnings_percent REAL, coupon TEXT, bond_yield TEXT);""")

    c.execute("""CREATE TABLE IF NOT EXISTS investors (
                investor_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name TEXT, address TEXT, 
                phone_number TEXT);""")
except sqlite3.OperationalError:
    print("Tables cannot be created.")


# Insert Investor
try:
    c.execute("""INSERT INTO investors (name, address, phone_number) 
                VALUES ('Bob Smith', '10245 Park Road', '902-303-402')""")
except sqlite3.OperationalError:
    print("Data not be inserted in table.")

# Loop through rows of stock data
for s_row in stock_reader:
    # Stocks Document Row: Symbol, Number of Shares, Purchase Price, Current Value, Purchase Date
    s_instance = Stock(s_row[0], int(s_row[1]), float(s_row[2]), float(s_row[3]), s_row[4])
    # Insert data into stocks table
    try:
        c.execute("""INSERT INTO stocks (stock_symbol, number_of_shares, earnings_loss, yearly_earnings_percent) 
                        VALUES (:symbol, :shares, :earnings, :yearly)""",
            {'symbol': s_instance.stock_symbol, 'shares': s_instance.number_of_shares,
            'earnings': s_instance.earnings_loss(), 'yearly': s_instance.yearly_earnings_loss()})
    except sqlite3.OperationalError:
        print("Data cannot be inserted in table.")
    
# Loop through bond data
for b_row in bond_reader:
    # Bonds Document Row: Symbol, Number of Shares, Purchase Price, Current Value, Purchase Date, Coupon, Yield
    b_instance = Bond(b_row[0], int(b_row[1]), float(b_row[2]), float(b_row[3]), b_row[4], b_row[5], b_row[6])
    # Insert data into bonds table
    try:
        c.execute("""INSERT INTO bonds (stock_symbol, number_of_shares, earnings_loss, yearly_earnings_percent, coupon, bond_yield) 
                    VALUES (:symbol, :shares, :earnings, :yearly, :coupon, :yield)""",
            {'symbol': b_instance.stock_symbol, 'shares': b_instance.number_of_shares,
            'earnings': b_instance.earnings_loss(), 'yearly': b_instance.yearly_earnings_loss(), 
            'coupon': b_instance.coupon, 'yield': b_instance.bond_yield})
    except sqlite3.OperationalError:
        print("Data cannot be inserted in table.")

# Commit and close
conn.commit()

conn.close()