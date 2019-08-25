"""
*****************************************************************************************
Description: This is a module with functions for the stock earnings program.
Author: Stefan Palmer
Last Revision: 07/14/2019
*****************************************************************************************
"""
# Import datetime module
from datetime import datetime

# Returns the amount that is earned or lost for a stock
def earnings_loss(number_shares, cur_value, pur_price):
    result = (number_shares * cur_value) - (number_shares * pur_price)
    return round(result, 2)

# Returns the yearly earnings or loss for a stock
def yearly_earnings_loss(cur_value, pur_price, pur_date):
    differenceInDays = ((datetime.today() - datetime.strptime(pur_date, '%m/%d/%Y')).days / 365)
    percentage_difference = (((cur_value - pur_price) / pur_price) / differenceInDays) * 100
    return round (percentage_difference, 2)