"""
*****************************************************************************************
Description: This program creates a line graph with Matplotlib for stock data imported 
from a JSON file. The graph shows variation in closing price for each stock over time. 
Author: Stefan Palmer
Last Revision: 08/13/2019
*****************************************************************************************
"""

# Import libraries
import json
import matplotlib.pyplot as plt
from datetime import datetime

filepath = 'assignment_8_stefan_palmer/AllStocks.json'

# Store data from JSON file
try:
    with open(filepath) as f:
        dataset = json.load(f)
except FileNotFoundError:
    print ('File cannot be found.')

# Lists for stock dates (AIG, F, FB, GOOG, IBM, M, MSFT, RDS-A)
aig_date, f_date, fb_date, goog_date, ibm_date, m_date, msft_date, rdsa_date = ([] for i in range(8))
# Lists for stock prices
aig_price, f_price, fb_price, goog_price, ibm_price, m_price, msft_price, rdsa_price = ([] for i in range(8))

# Loop through each stock
# Append date and price for each stock in lists
for stock in dataset:
    if stock['Symbol'] == 'AIG':
        aig_date.append(datetime.strptime(stock['Date'], '%d-%b-%y'))
        aig_price.append(stock['Close'])
    elif stock['Symbol'] == 'F':
        f_date.append(datetime.strptime(stock['Date'], '%d-%b-%y'))
        f_price.append(stock['Close'])
    elif stock['Symbol'] == 'FB':
        fb_date.append(datetime.strptime(stock['Date'], '%d-%b-%y'))
        fb_price.append(stock['Close'])
    elif stock['Symbol'] == 'GOOG':
        goog_date.append(datetime.strptime(stock['Date'], '%d-%b-%y'))
        goog_price.append(stock['Close'])
    elif stock['Symbol'] == 'IBM':
        ibm_date.append(datetime.strptime(stock['Date'], '%d-%b-%y'))
        ibm_price.append(stock['Close'])
    elif stock['Symbol'] == 'M':
        m_date.append(datetime.strptime(stock['Date'], '%d-%b-%y'))
        m_price.append(stock['Close'])
    elif stock['Symbol'] == 'MSFT':
        msft_date.append(datetime.strptime(stock['Date'], '%d-%b-%y'))
        msft_price.append(stock['Close'])
    elif stock['Symbol'] == 'RDS-A':
        rdsa_date.append(datetime.strptime(stock['Date'], '%d-%b-%y'))
        rdsa_price.append(stock['Close'])
    else:
        print ('Unexpected value')


# Set size for plot image
plt.figure(figsize=(10, 10))

# Plot data for stocks
plt.plot(aig_date, aig_price, label='AIG')
plt.plot(f_date, f_price, label='F')
plt.plot(fb_date, fb_price, label='FB')
plt.plot(goog_date, goog_price, label='GOOG')
plt.plot(ibm_date, ibm_price, label='IBM')
plt.plot(m_date, m_price, label='M')
plt.plot(msft_date, msft_price, label='MSFT')
plt.plot(rdsa_date, rdsa_price, label='RDS-A')

# Labels, title, legend
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.title('Variation in Stock Prices')
plt.legend()
plt.savefig('stockLineGraph.png')
