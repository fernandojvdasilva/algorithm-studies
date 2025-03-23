'''
Binary Tree Right Side View
Solved 
You are given the root of a binary tree. Return only the values of the nodes that are visible from the right side of the tree, ordered from top to bottom.

Example 1:



Input: root = [1,2,3]

Output: [1,3]
Example 2:

Input: root = [1,2,3,4,5,6,7]

Output: [1,3,7]
Constraints:

0 <= number of nodes in the tree <= 100
-100 <= Node.val <= 100

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def get_tree_height(self, root: TreeNode) -> int:
        if root is None:
            return 0

        return max(self.get_tree_height(root.left), \
                  self.get_tree_height(root.right)) + 1


    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        h = self.get_tree_height(root)

        for i in range(1, h+1):
            res.append(self.right_by_level(root, i))

        return res
        
        
    def right_by_level(self, root: TreeNode, level: int) -> int:
        if root is None:
            return None

        if level == 1:
            return root.val
        elif level > 1:
            res = self.right_by_level(root.right, level-1)
            if res is None:
                res = self.right_by_level(root.left, level-1)

            return res