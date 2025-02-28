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

    def get_root_height(self, root: TreeNode, count: int=1) -> int:
        left_height = count if root is None else self.get_root_height(root.left, count+1)
        right_height = count if root is None else self.get_root_height(root.right, count+1)

        return max(left_height, right_height)



    def get_num_left_root(self, root: TreeNode, curr_count: int=0) -> int:
        if root.left is None:
            return curr_count
        else:
            return self.get_num_left_root(root.left, curr_count+1)

    def get_num_right_root(self, root: TreeNode, curr_count: int=0) -> int:
        if root.right is None:
            return curr_count
        else:
            return self.get_num_right_root(root.right, curr_count+1)

    def count_columns(self, root: TreeNode) -> (int, int): # a tuple with the (number of columns, root position)
        num_left =  0 if root is None else self.get_num_left_root(root)
        num_right = 0 if root is None else self.get_num_right_root(root)

        return num_left + num_right + 1, num_left


    def add_to_column_list(self, node: TreeNode, column_list: List[List[int]], index: int, level: int):
        if node is None:
            return

        if level == 1:
            column_list[index].append(node.val)
        else:
            self.add_to_column_list(node.left, column_list, index-1, level-1)
            self.add_to_column_list(node.right, column_list, index+1, level-1)


    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None:
            num_columns = 0
            pos_root = 0
        else:
            num_columns, pos_root = self.count_columns(root)

        column_list = [[] for _ in range(num_columns)]

        h = self.get_root_height(root)

        for i in range(1, h+1):
            self.add_to_column_list(root, column_list, pos_root, i)

        return column_list