'''
Created on 3 de out de 2017

@author: fernando
'''
import unittest

from chapter3.solution_3_1 import ArrayStack
from chapter3.solution_3_4 import hannoi_tower

class Test(unittest.TestCase):


    def testSolution_3_1(self):
        triple_stack = ArrayStack()
        triple_stack.push(0, 0)
        triple_stack.push(1, 0)
        triple_stack.push(2, 0)
        triple_stack.push(10, 1)
        triple_stack.push(11, 1)
        triple_stack.push(20, 2)
        
        res = triple_stack.pop(0)
        
        assert(res == 2)
        
        res = triple_stack.pop(1)
        
        assert(res == 11)
        
        res = triple_stack.pop(2)
        
        assert(res == 20)

    def testSolution_3_4(self):
        rods = hannoi_tower(3)
        
        for i in range(1, len(rods[2].values)):
            assert(rods[2].values[i] < rods[2].values[i-1])


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSolution_3_1']
    unittest.main()