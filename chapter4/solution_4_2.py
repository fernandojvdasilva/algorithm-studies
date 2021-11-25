'''
Created on 24 de nov de 2021

@author: fernando
'''

'''
 Given a sorted (increasing order) array with unique integer elements, write an algo­
rithm to create a binary search tree with minimal height.

'''
            


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None

    def add(self, node):        
        if node.val <= self.val:
            if self.left is None:
                self.left = node
            else:
                self.left.add(node)
        else:
            if self.right is None:
                self.right = node
            else:
                self.right.add(node)

        node.parent = self

def list_to_minheight_tree(list) -> TreeNode:
    i = int(len(list) / 2)
    root = TreeNode(list[i])
    j = i - 1
    i += 1
    while i < len(list) and j >= 0:
        if i < len(list):
            root.add(TreeNode(list[i]))
            i += 1
        if j >= 0:
            root.add(TreeNode(list[j]))
            j -= 1

    return root