"""
*****************************************************************************************
Description: This program creates a table with stock, share number, earnings/loss, and
yearly earnings/loss, with given data for a particular user from CSV files. Also 
there is a subsection in the table for a bond entry. The table is shown in a new text
document created in the program.
Author: Stefan Palmer
Last Revision: 07/28/2019
*****************************************************************************************
"""

# Import modules
import csv
from datetime import datetime
from stock_module import Stock, Bond

# Store file paths in variables
stock_file_path = 'assignment_6_stefan_palmer/Lesson6_Data_Stocks.csv'
bond_file_path = 'assignment_6_stefan_palmer/Lesson6_Data_Bonds.csv'

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

# File where output is written
output_file = 'stocksData.txt'

# Output to file
with open(output_file, 'w') as file_object:
    # Titles and columns for stocks data table
    file_object.write("\nStock ownership for Bob Smith\n")
    file_object.write("-----------------------------------------\n")
    file_object.write("STOCK\tSHARE#\tEARNINGS/LOSS\tYEARLY EARNING/LOSS\n")
    file_object.write("-----------------------------------------\n")

    # Loop through rows of stock data
    for s_row in stock_reader:
        # Stocks Document Row: Symbol, Number of Shares, Purchase Price, Current Value, Purchase Date
        s_instance = Stock(s_row[0], int(s_row[1]), float(s_row[2]), float(s_row[3]), s_row[4])
        # Write output
        try:
            file_object.write(s_instance.stock_symbol + "\t\t" + str(s_instance.number_of_shares) +
            "\t\t" + str(s_instance.earnings_loss()) + "\t\t" + str(s_instance.yearly_earnings_loss()) + "%\n")
        except IOError:
            print("Error with writing to file.")
    
    # Titles and columns for bonds section
    file_object.write ("-----------------------------------------\n")
    file_object.write ("\nBond ownership for Bob Smith\n")
    file_object.write ("------------------------------------------------------------------------------\n")
    file_object.write ("BOND\t\tSHARE#\tEARNINGS/LOSS\tYEARLY EARNING/LOSS\tCOUPON\tYIELD\n")
    file_object.write ("------------------------------------------------------------------------------\n") 

    # Loop through bond data
    for b_row in bond_reader:
        # Bonds Document Row: Symbol, Number of Shares, Purchase Price, Current Value, Purchase Date, Coupon, Yield
        b_instance = Bond(b_row[0], int(b_row[1]), float(b_row[2]), float(b_row[3]), b_row[4], b_row[5], b_row[6])
        # Write output
        try:
            file_object.write(b_instance.stock_symbol + "\t\t" + str(b_instance.number_of_shares) +
            "\t\t\t" + str(b_instance.earnings_loss()) + "\t\t\t\t" + str(b_instance.yearly_earnings_loss()) +
            "%" + "\t\t\t" + str(b_instance.coupon) + "\t" + str(b_instance.bond_yield) + "%\n")
        except IOError:
            print("Error with writing to file.")
    
    
