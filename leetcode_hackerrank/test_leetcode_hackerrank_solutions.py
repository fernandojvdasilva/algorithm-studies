'''
Created on 3 de out de 2017

@author: fernando
'''
import unittest


from leetcode.chess_probs import Solution

class Test(unittest.TestCase):


    def testSolutionChessProbs(self):
        sol = Solution()

        print(sol.knightProbability(3, 2, 0, 0))



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSolutionStocks']
    unittest.main()