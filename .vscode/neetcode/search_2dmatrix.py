'''
Search a 2D Matrix
Solved 
You are given an m x n 2-D integer array matrix and an integer target.

Each row in matrix is sorted in non-decreasing order.
The first integer of every row is greater than the last integer of the previous row.
Return true if target exists within matrix or false otherwise.

Can you write a solution that runs in O(log(m * n)) time?

Example 1:



Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10

Output: true
Example 2:



Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15

Output: false
Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10000 <= matrix[i][j], target <= 10000
'''

class Solution:
    def find_row(self, matrix: List[List[int]], target: int) -> int:
        left, right = 0, len(matrix)-1

        while left < right:
            mid = left + (right - left) // 2

            if target < matrix[mid][0]:
                right = mid
            else:
                left = mid + 1

        if target < matrix[left][0]:
            return left - 1
        else:
            return left

    def find_val(self, row: List[int], target: int) -> bool:

        left, right = 0, len(row)-1

        while left < right:
            mid = left + (right - left) // 2

            if target <= row[mid]:
                right = mid
            else:
                left = mid + 1

        print("left = %d" % left)

        if row[left] == target:
            return True
        else:
            return False


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_ind = self.find_row(matrix, target)
        print('row_ind = %d' % row_ind)
        res = self.find_val(matrix[row_ind], target)

        return res