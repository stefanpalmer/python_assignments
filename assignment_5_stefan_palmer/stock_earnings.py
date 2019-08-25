"""
*****************************************************************************************
Description: This program creates a table with stock, share number, earnings/loss, and
yearly earnings/loss, with given data for a particular user, stored in a dictionary. A 
stock entry is an instance of the Stock class. Also there is a subsection in the table
for a bond entry (instance of the Bond class for an Investor). A bond entry also has 
the coupon and yield attributes.
Author: Stefan Palmer
Last Revision: 07/21/2019
*****************************************************************************************
"""

# Import classes from module and data from dictionary
from stock_module import Stock, Investor, Bond
from earnings_summary import stock_earnings_summary

# Loop through stock earnings summary
for user, values in stock_earnings_summary.items():

    # Instance of Investor class with Bob Smith
    investor_instance = Investor(1, user, '1020 Park Rd', '919-208-5421')

    # Titles of stocks table
    print ("\nStock ownership for " + investor_instance.name + "\n")
    print ("-----------------------------------------\n")
    print ("STOCK\tSHARE#\tEARNINGS/LOSS\tYEARLY EARNING/LOSS\n")
    print ("-----------------------------------------\n")
    
    # Instances of each stock from Stock class with needed data
    for i in range(len(values['stock_symbol'])):
        stock_instance = Stock(i+1, values['stock_symbol'][i], values['number_of_shares'][i], values['purchase_price'][i],
        values['current_value'][i], values['purchase_date'][i])
        # Print as row on table
        stock_instance.print_values()

    # Titles of bonds section
    print ("-----------------------------------------\n")
    print ("\nBond ownership for " + investor_instance.name + "\n")
    print ("------------------------------------------------------------------------------\n")
    print ("BOND\t\tSHARE#\tEARNINGS/LOSS\tYEARLY EARNING/LOSS\tCOUPON\tYIELD\n")
    print ("------------------------------------------------------------------------------\n")
    
    # Instance of Bond class printed on table
    bond_instance = Bond(i+2, 'GT2:GOV', 200, 100.02, 100.05, '8/1/2017', 1.38, 0.0135)
    bond_instance.print_values()
    print("\n")