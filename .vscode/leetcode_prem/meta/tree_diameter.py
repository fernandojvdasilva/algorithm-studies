'''
543. Diameter of Binary Tree
Solved
Easy
Topics
Companies
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

 

Example 1:


Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def max_path(self, node: TreeNode) -> (int, int):
        if node is None:
            return 0, 0
        else:
            max_left, h_left = self.max_path(node.left) 
            max_right, h_right = self.max_path(node.right)

            max_val, h = 0, 0

            max_val = max(h_left + h_right, max_left, max_right)
            h = max(h_left, h_right) + 1

            return max_val, h


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_val, h = self.max_path(root)

        return max_val