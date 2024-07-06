'''
You are given a 0-indexed 2D integer array grid of size m x n. Each cell has one of two values:

0 represents an empty cell,
1 represents an obstacle that may be removed.
You can move up, down, left, or right from and to an empty cell.

Return the minimum number of obstacles to remove so you can move from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1).

 

Example 1:


Input: grid = [[0,1,1],[1,1,0],[1,1,0]]
Output: 2
Explanation: We can remove the obstacles at (0, 1) and (0, 2) to create a path from (0, 0) to (2, 2).
It can be shown that we need to remove at least 2 obstacles, so we return 2.
Note that there may be other ways to remove 2 obstacles to create a path.
Example 2:


Input: grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
Output: 0
Explanation: We can move from (0, 0) to (2, 4) without removing any obstacles, so we return 0.

'''

class Solution:
    '''
    Input: grid = [
            [0,1,1],
            [1,1,0],
            [1,1,0]
        ]

    Output: 2
    



    '''

    class Node:
        def __init__(self):
            self.val = float("inf")
            self.pred = None
            self.edges = []
            self.eval = False

    class Edge:
        def __init__(self, w: int, node):
            self.w = w
            self.node = node


    def get_next_node(self, grid_nodes):
        min_val = float('inf')
        next_node = None

        for i in range(len(grid_nodes)):
            for j in range(len(grid_nodes[i])):
                if not grid_nodes[i][j].eval:
                    if grid_nodes[i][j].val < min_val:
                        next_node = grid_nodes[i][j]
                        min_val = next_node.val

        return next_node

    def djikstra(self, start_node, grid_nodes):
        curr_node = start_node
        curr_node.val = 0
        while curr_node != None:         
            for e in curr_node.edges:
                if e.node.val > e.w + curr_node.val:
                    e.node.val = e.w + curr_node.val
                    e.node.pred = curr_node
            
            curr_node.eval = True
            curr_node = self.get_next_node(grid_nodes)



    def build_graph(self, grid):
        grid_nodes = [[self.Node() for _ in range(len(grid[0]))] for _ in range(len(grid))]

        for i in range(len(grid_nodes)):
            for j in range(len(grid_nodes[i])):
                if j < len(grid_nodes[i])-1:
                    grid_nodes[i][j].edges.append(self.Edge(grid[i][j+1], grid_nodes[i][j+1]))

                if j > 0:
                    grid_nodes[i][j].edges.append(self.Edge(grid[i][j-1], grid_nodes[i][j-1]))


                if i < len(grid_nodes)-1:
                    grid_nodes[i][j].edges.append(self.Edge(grid[i+1][j], grid_nodes[i+1][j]))

                if i > 0:
                    grid_nodes[i][j].edges.append(self.Edge(grid[i-1][j], grid_nodes[i-1][j]))

        return grid_nodes


    def minimumObstacles(self, grid: List[List[int]]) -> int:
        grid_nodes = self.build_graph(grid)
        self.djikstra(grid_nodes[0][0], grid_nodes)

        return grid_nodes[-1][-1].val