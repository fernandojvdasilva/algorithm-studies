'''
314. Binary Tree Vertical Order Traversal
Attempted
Medium
Topics
Companies
Hint
Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Example 2:


Input: root = [3,9,8,4,0,1,7]
Output: [[4],[9],[3,0,1],[8],[7]]
Example 3:


Input: root = [1,2,3,4,10,9,11,null,5,null,null,null,null,null,null,null,6]
Output: [[4],[2,5],[1,10,9,6],[3],[11]]
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def count_columns_left(self, node: TreeNode) -> int:
        if node is None:
            return 0
        else:
            return max(self.count_columns_left(node.left) + 1, self.count_columns_left(node.right)-1)

    def count_columns_right(self, node: TreeNode) -> int:
        if node is None:
            return 0
        else:
            return max(self.count_columns_right(node.right) + 1, self.count_columns_right(node.left)-1)

    def height(self, node: TreeNode) -> int:
        if node is None:
            return 0
        else:
            return max(self.height(node.left), self.height(node.right)) + 1
    

    def getColumnVals(self, node: TreeNode, col: int, row: int, res: List[int], seek_col: int):
        if node is None:
            return

        if col == seek_col and row == 1:
            res.append(node.val)

        elif row > 1:
            self.getColumnVals(node.left, col-1, row-1, res, seek_col)
            self.getColumnVals(node.right, col+1, row-1, res, seek_col)


    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        num_cols_left = self.count_columns_left(root)
        num_columns = num_cols_left + self.count_columns_right(root) - 1

        h = self.height(root)

        res = []

        for i in range(1, num_columns+1):
            curr_res = []
            for j in range(1, h+1):
                self.getColumnVals(root, num_cols_left, j, curr_res, i)
            res.append(curr_res)

        return res