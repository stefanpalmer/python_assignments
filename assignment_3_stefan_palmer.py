"""
******************************************************************************
Description: This program creates a table with stock, share number, and
earnings/loss, with given data for a particular user, stored in a dictionary
Author: Stefan Palmer
Last Revision: 07/07/2019
******************************************************************************
"""
"""
Reflection: In this scenario it is better to use a dictionary. The code may be
longer for this problem, but when there is more data, with additional users, it
is easier and more efficient to store all the information in a single dictionary 
and then to loop through it to display what is necessary. Making separate lists 
for the shares, purchase price, and current value for each user would be 
problematic if the number of users is bigger.
"""

# Dictionary for stock earnings summary
stock_earnings_summary = {
    'Bob Smith' : {
        'stock_symbol' : ['GOOGL', 'MSFT', 'RDS-A', 'AIG', 'FB'],
        'number_of_shares' : [125, 85, 400, 235, 150],
        'purchase_price' : [772.88, 56.60, 49.58, 54.21, 124.31],
        'current_value' : [941.53, 73.04, 55.74, 65.27, 172.45]
    }
}

# Loop through dictionary
for user, values in stock_earnings_summary.items():

    # Titles and columns for data table
    print ("\nStock ownership for " + user + "\n")
    print ("-----------------------------------------\n")
    print ("STOCK\tSHARE#\tEARNINGS/LOSS\n")
    print ("-----------------------------------------\n")

    #Data
    for i in range(len(values['stock_symbol'])) :
        # Calculate earnings/loss
        earnings_or_loss = (values['number_of_shares'][i] * values['current_value'][i]) \
            - (values['number_of_shares'][i] * values['purchase_price'][i])
        # Print values for stock, share#, and earnings/loss
        print (values['stock_symbol'][i] + "\t" + str(values['number_of_shares'][i]) +
            "\t" + str(earnings_or_loss))

