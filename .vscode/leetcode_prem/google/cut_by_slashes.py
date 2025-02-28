'''
This solution has a bug when the region is "crossed" like this one
where it returns 3 instead of 4:

\/
/\

959. Regions Cut By Slashes
Attempted
Medium
Topics
Companies
An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists of a '/', '\', or blank space ' '. These characters divide the square into contiguous regions.

Given the grid grid represented as a string array, return the number of regions.

Note that backslash characters are escaped, so a '\' is represented as '\\'.

 

Example 1:


Input: grid = [" /","/ "]
Output: 2
Example 2:


Input: grid = [" /","  "]
Output: 1
Example 3:


Input: grid = ["/\\","\\/"]
Output: 5
Explanation: Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.
 

Constraints:

n == grid.length == grid[i].length
1 <= n <= 30
grid[i][j] is either '/', '\', or ' '.
'''

class Solution:
    def findRegion(self, grid: List[str], i: int, j: int, visited: List[bool]) -> bool:
        
        # If we get into an edge of the grid, then we found a region
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return True
        
        # If we got a blank, then it's opened
        if grid[i][j] == " ":
            return False

        # If we already visited and it's closing, then it's a region!
        if visited[i][j]:
            return True
        
        visited[i][j] = True
        if grid[i][j] == "\\":
            return self.findRegion(grid, i+1, j+1, visited)
        else:
            return self.findRegion(grid, i+1, j-1, visited)


    def regionsBySlashes(self, grid: List[str]) -> int:
        visited = [[False for _ in range(len(grid[0]))] for __ in range(len(grid))]
        
        count_regions = 1
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if not visited[i][j] and grid[i][j] in ["/", "\\"]:
                    check_region = self.findRegion(grid, i, j, visited)
                    if check_region:
                        count_regions += 1

        return count_regions