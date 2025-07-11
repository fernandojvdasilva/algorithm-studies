'''
121. Best Time to Buy and Sell Stock
Solved
Easy
Topics
conpanies icon
Companies
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104

'''

import heapq

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_r = [0] * len(prices)

        max_r[-1] = prices[-1]
        for i in range(len(prices)-2,-1, -1):
            max_r[i] = max(prices[i], max_r[i+1])

        min_heap = []
        for i in range(len(prices)):
            heapq.heappush(min_heap, [prices[i], i])

        max_val = 0
        for i in range(len(prices)):
            min_val, min_ind = heapq.heappop(min_heap)
            max_val = max(max_val, max_r[min_ind] - min_val)

        return max_val