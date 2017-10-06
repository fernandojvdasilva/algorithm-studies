'''
Created on 30 de set de 2017

@author: fernando
'''
import unittest

from chapter1.solution_1_1 import has_all_unique_characters
from chapter1.solution_1_4 import are_anagrams

class Test(unittest.TestCase):


    def testSolution1_1(self):
        result = has_all_unique_characters("cafdgbc")
        
        assert(result == False)
        
        result = has_all_unique_characters("adfegbc")
        
        assert(result)
        
        
    def testSolution1_4(self):
        result = are_anagrams('ovo', 'voo')
        
        assert(result)
        
        result = are_anagrams('voo', 'vo')
        
        assert(result == False)
        
        result = are_anagrams('ovo', 'novo')
        
        assert(result == False)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSolution1_1']
    unittest.main()