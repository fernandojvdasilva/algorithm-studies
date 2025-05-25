'''
1091. Shortest Path in Binary Matrix
Solved
Medium
Topics
Companies
Hint
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

 

Example 1:


Input: grid = [[0,1],[1,0]]
Output: 2
Example 2:


Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
Example 3:

Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1

'''
class Node:
    def __init__(self, val):
        self.val = val
        self.edges = []
        self.pred = None
        self.eval = False

    def __lt__(self, other):
        return self.val < other.val


class Edge:
    def __init__(self, node, w):
        self.node = node
        self.w = w

import heapq

class Solution:

    def djikstra(self, start_node, nodes):
        start_node.val = 0
        curr_node = heapq.heappop(nodes)
        heapq.heapify(nodes)

        while curr_node != None:
            for e in curr_node.edges:
                if e.node.val > e.w + curr_node.val:
                    e.node.pred = curr_node
                    e.node.val = e.w + curr_node.val
                    heapq.heappush(nodes, e.node)
                            
            #heapq.heapify(nodes)
            

            curr_node.eval = True
            if len(nodes) > 0:
                curr_node = heapq.heappop(nodes)
            else:
                curr_node = None



    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
            root = None

            nodes = []
            nodes_grid = []            

            if len(grid) == 1 and len(grid[0]) == 1 and grid[0][0] == 0:
                return 1

            for i in range(len(grid)):
                nodes_grid.append([])
                for j in range(len(grid[i])):
                    if i == 0 and j == 0 and grid[i][j] == 1:
                        return -1

                    if i == 0 and j == 0:
                        val = 0
                    else:
                        val = float("inf")
                    
                    if grid[i][j] == 0:
                        curr_node = Node(val)
                        heapq.heappush(nodes, curr_node)
                        nodes_grid[i].append(curr_node)

                        if root is None:
                            root = curr_node

                        if i > 0: 
                            if nodes_grid[i-1][j] != None:
                                nodes_grid[i-1][j].edges.append(Edge(nodes_grid[i][j], 1))
                                nodes_grid[i][j].edges.append(Edge(nodes_grid[i-1][j], 1))

                            if j > 0 and nodes_grid[i-1][j-1] != None:
                                nodes_grid[i-1][j-1].edges.append(Edge(nodes_grid[i][j], 1))
                                nodes_grid[i][j].edges.append(Edge(nodes_grid[i-1][j-1], 1))

                            if j < len(nodes_grid[i-1])-1 and nodes_grid[i-1][j+1] != None:
                                nodes_grid[i-1][j+1].edges.append(Edge(nodes_grid[i][j], 1))
                                nodes_grid[i][j].edges.append(Edge(nodes_grid[i-1][j+1], 1))
                        if j > 0:
                            if nodes_grid[i][j-1] != None:
                                nodes_grid[i][j-1].edges.append(Edge(nodes_grid[i][j], 1))
                                nodes_grid[i][j].edges.append(Edge(nodes_grid[i][j-1], 1))

                            

                    else:
                        nodes_grid[i].append(None)

            self.djikstra(root, nodes)

            curr_node = nodes_grid[-1][-1]

            count = 0
            while curr_node != None:
                count += 1
                curr_node = curr_node.pred

                if curr_node == nodes_grid[0][0]:
                    count += 1
                    break

            if curr_node != nodes_grid[0][0]:
                return -1
            else:
                return count