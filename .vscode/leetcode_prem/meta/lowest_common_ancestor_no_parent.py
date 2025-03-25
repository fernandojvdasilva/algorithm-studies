'''
236. Lowest Common Ancestor of a Binary Tree
Solved
Medium
Topics
Companies
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    



    def find_nodes(self, curr_node: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> bool:
        res = False
        
        if curr_node is None:
            return False
        
        else:
            
            check_right = self.find_nodes(curr_node.right, p, q)
            check_left = self.find_nodes(curr_node.left, p, q)
            
            if curr_node == p or curr_node == q:
                res = True
                          
                if check_right or check_left:
                    self.common_ancestor = curr_node
                
            else:
                res = check_right or check_left
                
                if check_right and check_left:
                    self.common_ancestor = curr_node

        return res

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        self.common_ancestor = None

        _ = self.find_nodes(root, p, q)

        return self.common_ancestor