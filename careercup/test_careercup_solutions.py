'''
Created on 6 de out de 2017

@author: fernando
'''
import unittest

from careercup.min_diff_nodes_bst import BinarySearchTree, TreeNode


class Test(unittest.TestCase):


    def testMinDiffNodes1(self):
        
        tree = BinarySearchTree()
        tree.root = None
        
        assert(tree.min_diff_nodes() == None)
    
    def testMinDiffNodes2(self):    
        tree = BinarySearchTree()
        tree.root = TreeNode(10)
        assert(tree.min_diff_nodes() == float('inf'))
        
    def testMinDiffNodes3(self):
        tree = BinarySearchTree()
        tree.root = TreeNode(5)
        tree.root.left = TreeNode(-5)
        tree.root.left.right = TreeNode(1)
        
        tree.root.right = TreeNode(0)
        
        assert(tree.min_diff_nodes() == 5)
        
    def testMinDiffNodes4(self):
        tree = BinarySearchTree()
        tree.root = TreeNode(1)
        tree.root.right = TreeNode(2)
        tree.root.right.right = TreeNode(3)
        tree.root.right.right.right = TreeNode(4)
        
        assert(tree.min_diff_nodes() == float('inf'))
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testMinDiffNodes1']
    unittest.main()