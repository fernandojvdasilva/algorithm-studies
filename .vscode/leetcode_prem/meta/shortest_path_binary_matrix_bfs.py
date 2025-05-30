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
from collections import deque

class Solution:

    def check_valid_pos(self, i, j, grid) -> bool:
        return i >= 0 and i < len(grid) and j >= 0 and j < len(grid[i]) 
    

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        queue = deque()


        if grid[0][0] == 1:
            return -1

        if grid[-1][-1] == 1:
            return -1

        queue.append((0,0))                

        grid[0][0] = 1

        while len(queue) > 0:
            curr = queue.popleft()

            if curr[0] == len(grid)-1 and curr[1] == len(grid[0]) -1:
                return grid[curr[0]][curr[1]]        

            #grid[curr[0]][curr[1]] = 1

            for i in range(-1,2):
                
                for j in range(-1,2):
                
                    if self.check_valid_pos(curr[0]+i, curr[1]+j, grid) and grid[curr[0]+i][curr[1]+j] == 0:
                        grid[curr[0]+i][curr[1]+j] = grid[curr[0]][curr[1]] + 1
                        queue.append((curr[0]+i, curr[1]+j))

        return -1