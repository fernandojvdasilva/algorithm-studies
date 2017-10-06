'''
Created on 6 de out de 2017

@author: fernando
'''

'''
Given an input BST, find the minimum value difference between any two nodes in the tree.

e.g:
....10
5         16
........12    20
answer: 2 (it happens between nodes 12 and 10)

describe the test cases you would use here?

'''

'''
Test Cases:

#1

None

#2

10

#3

    5
  1   8
  
  
#4

        5
-5           0
    1   

#5
1
   2
      3
         4



'''

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

    def min_diff_nodes(self):
        result = float('inf')
        if self.right != None and self.left != None:
            result = self.right.val - self.left.val
        if self.right != None:
            result = min(result, self.right.min_diff_nodes())
        if self.left != None:
            result = min(result, self.left.min_diff_nodes())
        return result

class BinarySearchTree:
    def __init__(self):
        self.root = None    
        self.min = float('inf')

    def min_diff_nodes(self):
        if self.root != None:
            return self.root.min_diff_nodes()
        else:
            return None        

