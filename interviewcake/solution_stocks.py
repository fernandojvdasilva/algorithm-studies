'''
Created on 3 de out de 2017

@author: fernando
'''

'''

 Suppose we could access yesterday's stock prices as a list, where:

    The indices are the time in minutes past trade opening time, which was 9:30am local time.
    The values are the price in dollars of Apple stock at that time.

So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.

Write an efficient function that takes stock_prices_yesterday and returns the best profit 
I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday.

For example:

  stock_prices_yesterday = [10, 7, 5, 8, 11, 9]  

get_max_profit(stock_prices_yesterday)
# returns 6 (buying for $5 and selling for $11)

No "shorting"—you must buy before you sell. You may not buy and sell in the same time step 
(at least 1 minute must pass). 

'''

def find_best_prices(stock_prices):  
    check_buy = 0
    check_sell = 1
    diff = -float('inf')
    
    while check_sell < len(stock_prices):
        if stock_prices[check_sell] - stock_prices[check_buy] > diff:
            diff = stock_prices[check_sell] - stock_prices[check_buy]
                        
        if stock_prices[check_sell] < stock_prices[check_buy]:
            check_buy = check_sell
            
        check_sell += 1
            
    return diff