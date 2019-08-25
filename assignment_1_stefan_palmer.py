"""
******************************************************************************
Description: This program calculates how much money a user has earned or lost
from a stock they own.
Author: Stefan Palmer
Last Revision: 6/23/2019
******************************************************************************
"""

name = input("Please enter your name: ")
stock_symbol = input("Enter stock symbol for the stock you own: ")
shares_number = input("How many shares do you own? ")
price_at_purchase = input("What was the price per share at purchase? ")
current_price = input("What is the current price per share? ")
earnings_or_loss = (float(shares_number) * float(current_price)) - (float(shares_number) * float(price_at_purchase))

print ("Stock ownership for " + name)
print ("--------------------------------------")
print (stock_symbol + ": " + shares_number + " shares")
print ("Purchase Price: " + price_at_purchase)
print ("Current Price per Share: " + current_price)
print ("Earnings/Loss to-date: $" + str(earnings_or_loss))