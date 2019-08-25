"""
*****************************************************************************************
Description: This program creates a pie chart with Matplotlib for stock data imported 
from a JSON file. The chart shows the average percentages of the total stock value for 
each stock, based on their average closing prices.
Author: Stefan Palmer
Last Revision: 08/24/2019
*****************************************************************************************
"""

import json
import matplotlib.pyplot as plt

filepath = 'assignment_10_final_stefan_palmer/AllStocks.json'

# Store data from JSON file
try:
    with open(filepath) as f:
        dataset = json.load(f)
except FileNotFoundError:
    print ('File cannot be found.')

# Lists for stock prices
aig_price, f_price, fb_price, goog_price, ibm_price, m_price, msft_price, rdsa_price = ([] for i in range(8))

# Loop through each stock
# Append price for each stock in lists
for stock in dataset:
    if stock['Symbol'] == 'AIG':
        aig_price.append(stock['Close'])
    elif stock['Symbol'] == 'F':
        f_price.append(stock['Close'])
    elif stock['Symbol'] == 'FB':
        fb_price.append(stock['Close'])
    elif stock['Symbol'] == 'GOOG':
        goog_price.append(stock['Close'])
    elif stock['Symbol'] == 'IBM':
        ibm_price.append(stock['Close'])
    elif stock['Symbol'] == 'M':
        m_price.append(stock['Close'])
    elif stock['Symbol'] == 'MSFT':
        msft_price.append(stock['Close'])
    elif stock['Symbol'] == 'RDS-A':
        rdsa_price.append(stock['Close'])
    else:
        print ('Unexpected value')

# Function to find average
def find_average(lst):
    return sum(lst) / len(lst)

# Calculate and save average for each stock closing price
aig_average = find_average(aig_price)
f_average = find_average(f_price)
fb_average = find_average(fb_price)
goog_average = find_average(goog_price)
ibm_average = find_average(ibm_price)
m_average = find_average(m_price)
msft_average = find_average(msft_price)
rdsa_average = find_average(rdsa_price)

# Set size of chart
plt.figure(figsize=(7,6))

# Title of chart
plt.title("Percentage of Total Value for Each Stock")

# Labels and values lists for pie chart
stockLabels = ['AIG', 'F', 'FB', 'GOOG', 'IBM', 'M', 'MSFT', 'RDS-A']
averageValues = [aig_average, f_average, fb_average, goog_average, ibm_average, m_average,
msft_average, rdsa_average]
# Distinguish GOOG since it has the greatest proportion by far of total value
explode = [0, 0, 0, 0.05, 0, 0, 0, 0]

# Pie chart with average closing price of each stock, stock names, edges, percentages of total value
plt.pie(averageValues, labels=stockLabels, wedgeprops={'edgecolor': 'gray'}, 
autopct="%.1f%%", explode=explode)

plt.show()