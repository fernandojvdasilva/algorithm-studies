'''
Created on 3 de out de 2017

@author: fernando
'''
import unittest

import os, sys

sys.path.append(os.path.join(os.getcwd(), '.'))
sys.path.append(os.path.join(os.getcwd(), 'chapter4'))


from chapter4.solution_4_1 import *
from chapter4.solution_4_2 import *
from chapter4.solution_4_7 import *

class Test(unittest.TestCase):


    def testSolution_4_1(self):

        node1 = GraphNode()
        node2 = GraphNode()
        node3 = GraphNode()
        node4 = GraphNode()

        node1.edges.append(GraphEdge(node2))
        node2.edges.append(GraphEdge(node3))


        assert(find_path(node1, node3))
        assert(not find_path(node2, node4))

    def testSolution_4_2(self):
        tree = list_to_minheight_tree([1, 2, 3, 4, 5])
        assert(tree != None)

    def testSolution_4_7(self):        
        find_build_order(['a', 'b', 'c', 'd', 'e', 'f'], \
                        [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')])

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSolution_3_1']
    unittest.main()