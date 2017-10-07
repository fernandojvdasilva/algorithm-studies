'''
Created on 6 de out de 2017

@author: fernando
'''
import unittest

from careercup.min_diff_nodes_bst import BinarySearchTree, TreeNode
from careercup.max_path_pyramid_graph import GraphNode, GraphEdge, PyramidGraph

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
        

    def testMaxPathPyramidGraph(self):
        graph = PyramidGraph()

        node1 = GraphNode(3)
        
        node2_1= GraphNode(9)
        node2_2 = GraphNode(4)
        
        node1.add_edge(node2_1)
        node1.add_edge(node2_2)
        
        node3_1 = GraphNode(1)
        node3_2 = GraphNode(8)
        node3_3 = GraphNode(2)
        
        node2_1.add_edge(node3_1)
        node2_1.add_edge(node3_2)
        node2_2.add_edge(node3_2)
        node2_2.add_edge(node3_3)
        
        
        node4_1 = GraphNode(4)
        node4_2 = GraphNode(5)
        node4_3 = GraphNode(8)
        node4_4 = GraphNode(2)
        
        node3_1.add_edge(node4_1)
        node3_1.add_edge(node4_2)
        node3_2.add_edge(node4_2)
        node3_2.add_edge(node4_3)
        node3_3.add_edge(node4_3)
        node3_3.add_edge(node4_4)
        
        graph.first_node = node1
        
        max_path = graph.get_max_path()
        
        assert(max_path == [node1, node2_1, node3_2, node4_3])



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testMinDiffNodes1']
    unittest.main()