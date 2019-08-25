"""
*****************************************************************************************
Description: This document is a module with the classes, with attributes and methods, for 
the stock earnings data: Stock, Investor, and Bond.
Author: Stefan Palmer
Last Revision: 07/21/2019
*****************************************************************************************
"""

# Import datetime module
from datetime import datetime

class Stock():
    # Initialize
    def __init__(self, purchase_id, stock_symbol, number_of_shares, purchase_price, 
    current_value, purchase_date):
        self.purchase_id = purchase_id
        self.stock_symbol = stock_symbol
        self.number_of_shares = number_of_shares
        self.purchase_price = purchase_price
        self.current_value = current_value
        self.purchase_date = purchase_date

    # Returns the amount that is earned or lost for a stock
    def earnings_loss(self):
        result = (self.number_of_shares * self.current_value) - (self.number_of_shares * self.purchase_price)
        return round(result, 2)
    
    # Returns the yearly earnings or loss for a stock
    def yearly_earnings_loss(self):
        differenceInDays = ((datetime.today() - datetime.strptime(self.purchase_date, '%m/%d/%Y')).days / 365)
        percentage_difference = (((self.current_value - self.purchase_price) / self.purchase_price) / differenceInDays) * 100
        return round (percentage_difference, 2)
    
    # Print values
    def print_values(self):
        print (self.stock_symbol + "\t" + str(self.number_of_shares) +
        "\t" + str(self.earnings_loss()) + "\t\t" + str(self.yearly_earnings_loss()) + "%")


class Investor():
    # Initialize
    def __init__(self, investor_id, name, address, phone_number):
        self.investorID = investor_id
        self.name = name
        self.address = address
        self.phoneNumber = phone_number

# Inherits from Stock class
class Bond(Stock):
    # Initialize
    def __init__(self, purchase_id, stock_symbol, number_of_shares, purchase_price,
    current_value, purchase_date, coupon, bond_yield):
        super().__init__(purchase_id, stock_symbol, number_of_shares, purchase_price,
        current_value, purchase_date)
        self.coupon = coupon
        self.bond_yield = bond_yield
    
    # Print values
    def print_values(self):
        print (self.stock_symbol + "\t\t" + str(self.number_of_shares) +
        "\t" + str(self.earnings_loss()) + "\t\t" + str(self.yearly_earnings_loss()) +
        "%" + "\t\t\t" + str(self.coupon) + "\t" + str(self.bond_yield * 100) + "%")
