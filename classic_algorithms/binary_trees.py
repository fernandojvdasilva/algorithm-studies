'''
Created on 4 de out de 2017

@author: fernando
'''

import pprint


class BinarySearchTree:
    
    def __init__(self):
        self.root = None
        
    def insert(self, item):
        if self.root is None:
            self.root = item
        else:
            self.root.insert(item)
            
    def show(self):
        pprint.pprint(self.root)
        
        
    def search(self, val):
        if self.root != None:
            return self.root.search(val)
        else:
            return None
        
    def max(self):
        if self.root != None:
            return self.root.max()
        else:
            return None
    
    def min(self):
        if self.root != None:
            return self.root.min()
        else:
            return None
        
    def successor(self, node):
        if node.right != None:
            return node.right.min()
        
        n_ = node
        p_ = node.parent
        while p_ != None and n_ != p_.left:
            n_ = p_
            p_ = p_.parent
            
        if p_ is None:
            return None
        
    
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        
    def insert(self, item):
        if self.val > item.val:
            if self.left is None:
                self.left = item
                item.parent = self
            else:
                self.left.insert(item)
        else:
            if self.right is None:
                self.right = item
                item.parent = self
            else:
                self.right.insert(item)
                
                
    def search(self, val):
        if self.val == val:
            return self
        elif self.val > val:
            if self.left != None:
                return self.left.search(val)
            else:
                return None
        elif self.val < val:
            if self.right != None:
                return self.right.search(val)
            else:
                return None
            
    def max(self):
        if self.right is None:
            return self
        else:
            return self.right.max()
    
    def min(self):
        if self.left is None:
            return self
        else:
            return self.left.min()
