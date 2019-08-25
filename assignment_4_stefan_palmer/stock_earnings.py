"""
*****************************************************************************************
Description: This program creates a table with stock, share number, earnings/loss, and
yearly earnings/loss, with given data for a particular user, stored in a dictionary,
with the calculations in functions.
Author: Stefan Palmer
Last Revision: 07/14/2019
*****************************************************************************************
"""
# Import stock_functions module
import stock_functions

# Dictionary for stock earnings summary
stock_earnings_summary = {
    'Bob Smith' : {
        'stock_symbol' : ['GOOGL', 'MSFT', 'RDS-A', 'AIG', 'FB', 'M', 'F', 'IBM'],
        'number_of_shares' : [125, 85, 400, 235, 150, 425, 85, 80],
        'purchase_price' : [772.88, 56.60, 49.58, 54.21, 124.31, 30.30, 12.58, 150.37],
        'current_value' : [941.53, 73.04, 55.74, 65.27, 172.45, 23.98, 10.95, 145.30],
        'purchase_date' : ['8/1/2015', '8/1/2015', '8/1/2015', '8/1/2015', '8/1/2015', '1/10/2017', '2/17/2017', '5/12/2017']
    }
}

# Loop through stock earnings summary
for user, values in stock_earnings_summary.items():

    # Titles and columns for data table
    print ("\nStock ownership for " + user + "\n")
    print ("-----------------------------------------\n")
    print ("STOCK\tSHARE#\tEARNINGS/LOSS\tYEARLY EARNING/LOSS\n")
    print ("-----------------------------------------\n")

    #Data
    for i in range(len(values['stock_symbol'])) :

        # Calculate earnings/loss
        earnings_or_loss = stock_functions.earnings_loss(values['number_of_shares'][i], values['current_value'][i], \
            values['purchase_price'][i])

        # Calculate yearly earnings/loss
        yearly_earnings_or_loss = stock_functions.yearly_earnings_loss(values['current_value'][i], 
            values['purchase_price'][i], values['purchase_date'][i])

        # Print values for stock, share#, earnings/loss, and yearly earnings/loss
        print (values['stock_symbol'][i] + "\t" + str(values['number_of_shares'][i]) +
            "\t" + str(earnings_or_loss) + "\t\t" + str(yearly_earnings_or_loss) + "%")

