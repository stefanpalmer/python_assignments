"""
******************************************************************************
Description: This program creates a table with stock, share number, and
earnings/loss, with given data from a user
Author: Stefan Palmer
Last Revision: 6/23/2019
******************************************************************************
"""

stock_symbol = ['GOOGL', 'MSFT', 'RDS-A', 'AIG', 'FB']
number_of_shares = [125, 85, 400, 235, 150]
purchase_price = [772.88, 56.60, 49.58, 54.21, 124.31]
current_value = [941.53, 73.04, 55.74, 65.27, 172.45]

print ("\nStock ownership for Bob Smith\n")
print ("-----------------------------------------\n")
print ("STOCK\tSHARE#\tEARNINGS/LOSS\n")
print ("-----------------------------------------\n")

for i in range(0,5) :
    earnings_or_loss = (number_of_shares[i] * current_value[i]) - (number_of_shares[i] * purchase_price[i])
    print(stock_symbol[i] + "\t" + str(number_of_shares[i]) + "\t" + "$" +
         str(earnings_or_loss))
    
print ("\n\n")