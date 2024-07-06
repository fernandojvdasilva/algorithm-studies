# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # Complexity: O(m + n) // n: number of nodes, m: nodes to delete

    def search_to_delete(self, root: TreeNode, to_delete: Set[int], nodes_to_delete: List[TreeNode]):	
        if root.val in to_delete:
            nodes_to_delete.append(root)
	
        if not root.left is None:
            self.search_to_delete(root.left, to_delete, nodes_to_delete)
        
        if not root.right is None:
            self.search_to_delete(root.right, to_delete, nodes_to_delete)
		

    def cut_forest(self, root: TreeNode, to_delete: Set[int], forest_roots: List[TreeNode]):
        if root.val in to_delete:
            if not root.left is None:
                self.cut_forest(root.left, to_delete, forest_roots)
            if not root.right is None:
                self.cut_forest(root.right, to_delete, forest_roots)
        else:
            if not root in forest_roots:
                forest_roots.append(root)


    def delete_nodes(self, root: TreeNode, to_delete:Set[int]):
        if not root.left is None:
            self.delete_nodes(root.left, to_delete)
            if root.left.val in to_delete:                
                root.left = None

        if not root.right is None:		
            self.delete_nodes(root.right, to_delete)
            if root.right.val in to_delete:
                root.right = None


    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        nodes_to_delete : List[TreeNode] = []
        
        to_delete = set(to_delete)

        self.search_to_delete(root, to_delete, nodes_to_delete) 
	
        forest_roots: List[TreeNode] = []
        if not root.val in to_delete:
            forest_roots.append(root)


        for node in nodes_to_delete:
            self.cut_forest(node, to_delete, forest_roots)

        self.delete_nodes(root, to_delete)

        return forest_roots
