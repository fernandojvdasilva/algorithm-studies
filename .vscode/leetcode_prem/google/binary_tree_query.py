class TreeNode2:

    def __init__(self, tree_node: TreeNode):
        
        self.val = tree_node.val
        if not tree_node.left is None:
            self.left = TreeNode2(tree_node.left)
        else:
            self.left = None

        if not tree_node.right is None:
            self.right = TreeNode2(tree_node.right)
        else:
            self.right = None

        self.active = True
        if self.val is None:
            self.active = False


    def find(self, val: int):
        result = None
        if self.val == val:
            self.active = False
            result = self
        else:
            if not self.left is None:
                result = self.left.find(val)
            
            if result is None and not self.right is None:
                result = self.right.find(val)

        return result
            

    def get_height(self) -> int:
        result = 0		
                            
        if not self.left is None and self.left.active:
            result = 1 + self.left.get_height()

        if not self.right is None and self.right.active:
            tmp_result = 1 + self.right.get_height()
            if tmp_result > result:
                result = tmp_result

        return result


class Solution:

    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        result = []

        root_node = TreeNode2(root)


        for i in range(len(queries)):
            curr_node = root_node.find(queries[i])

            result.append(root_node.get_height())

            curr_node.active = True

        return result