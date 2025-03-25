'''
Binary Tree Level Order Traversal
Solved 
Given a binary tree root, return the level order traversal of it as a nested list, where each sublist contains the values of nodes at a particular level in the tree, from left to right.

Example 1:



Input: root = [1,2,3,4,5,6,7]

Output: [[1],[2,3],[4,5,6,7]]
Example 2:

Input: root = [1]

Output: [[1]]
Example 3:

Input: root = []

Output: []
Constraints:

0 <= The number of nodes in both trees <= 1000.
-1000 <= Node.val <= 1000


'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def height(self, node: TreeNode) -> int:
        if node is None:
            return 0

        else:
            return max(self.height(node.left), self.height(node.right)) + 1


    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        h = self.height(root)

        levels = []
        for i in range(1, h+1):
            curr_level = []
            self.items_at_level(root, i, curr_level)
            levels.append(curr_level)

        return levels
            


    def items_at_level(self, root: TreeNode, level: int, curr_level: List[int]):
        if root is None:
            return
        
        if level == 1:
            curr_level.append(root.val)

        elif level > 1:
            self.items_at_level(root.left, level-1, curr_level)
            self.items_at_level(root.right, level-1, curr_level)





