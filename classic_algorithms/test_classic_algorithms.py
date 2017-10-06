'''
Created on 3 de out de 2017

@author: fernando
'''
import unittest

from classic_algorithms.backtracking import solve_sudoku
from classic_algorithms.binary_trees import BinarySearchTree, TreeNode
from classic_algorithms.graphs import dijkstra_min_paths, GraphNode, print_minimum_path

import pprint

class Test(unittest.TestCase):


    def testSudokuSolver(self):
        initial_game =  [[5,1,7,6,0,0,0,3,4],
                         [2,8,9,0,0,4,0,0,0],
                         [3,4,6,2,0,5,0,9,0],
                         [6,0,2,0,0,0,0,1,0],
                         [0,3,8,0,0,6,0,4,7],
                         [0,0,0,0,0,0,0,0,0],
                         [0,9,0,0,0,0,0,7,8],
                         [7,0,3,4,0,0,5,6,0],
                         [0,0,0,0,0,0,0,0,0]]
        
        result = solve_sudoku(initial_game)
        
        assert(result != None)
        
        pprint.pprint(result)
        
        
    def testBinarySearchTree(self):
        binary_tree = BinarySearchTree()
        
        binary_tree.insert(TreeNode(10))
        binary_tree.insert(TreeNode(5))
        binary_tree.insert(TreeNode(7))
        binary_tree.insert(TreeNode(11))
        
        assert(binary_tree.min().val == 5)
        assert(binary_tree.max().val == 11)
        assert(binary_tree.search(7) != None)
        
        assert(binary_tree.successor(binary_tree.search(5)).val == 7)
        

    def testDijkstra(self):
        graph = [GraphNode() for _ in range(5)]
        
        graph[0].connect(graph[1], 10)
        graph[0].connect(graph[2], 5)
        
        graph[1].connect(graph[2], 2)
        graph[1].connect(graph[3], 1)
        
        graph[2].connect(graph[1], 3)
        graph[2].connect(graph[3], 9)
        graph[2].connect(graph[4], 2)
        
        graph[3].connect(graph[4], 4)
        
        graph[4].connect(graph[0], 7)
        graph[4].connect(graph[3], 6)

        dijkstra_min_paths(graph)
        
        print_graph = print_minimum_path(graph)
        print(print_graph)
        assert(print_graph == '5 -> 8, 0 -> 5, 8 -> 9, 5 -> 7, ')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSudokuSolver']
    unittest.main()