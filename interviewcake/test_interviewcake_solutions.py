'''
Created on 3 de out de 2017

@author: fernando
'''
import unittest


from interviewcake.solution_stocks import find_best_prices
from interviewcake.multiply_int_list import get_products_of_all_ints_except_at_index
from interviewcake.max_product import find_highest_product

class Test(unittest.TestCase):


    def testSolutionStocks(self):
        res = find_best_prices([10, 7, 5, 8, 11, 9])
        
        assert(res == 6)
        
        res = find_best_prices([5, 11, 4, 2, 1])
        
        assert(res == 6)
        
    def testMultiplyIntegers(self):
        
        integers = [1, 7, 3, 4]
        
        multiplied = get_products_of_all_ints_except_at_index(integers)
        
        assert(multiplied == [84, 12, 28, 21])
        
    def testHighestProduct(self):
        
        integers = [1, 3, -10, 2, -10]
        
        result = find_highest_product(integers)
        
        assert(result == 300)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSolutionStocks']
    unittest.main()