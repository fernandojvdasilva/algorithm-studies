'''
2184. Number of Ways to Build Sturdy Brick Wall
Attempted
Medium
Topics
Companies
Hint
You are given integers height and width which specify the dimensions of a brick wall you are building. You are also given a 0-indexed array of unique integers bricks, where the ith brick has a height of 1 and a width of bricks[i]. You have an infinite supply of each type of brick and bricks may not be rotated.

Each row in the wall must be exactly width units long. For the wall to be sturdy, adjacent rows in the wall should not join bricks at the same location, except at the ends of the wall.

Return the number of ways to build a sturdy wall. Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:


Input: height = 2, width = 3, bricks = [1,2]
Output: 2
Explanation:
The first two walls in the diagram show the only two ways to build a sturdy brick wall.
Note that the third wall in the diagram is not sturdy because adjacent rows join bricks 2 units from the left.
Example 2:

Input: height = 1, width = 1, bricks = [5]
Output: 0
Explanation:
There are no ways to build a sturdy wall because the only type of brick we have is longer than the width of the wall.

'''

import copy

class Solution:
    '''
    
    height = 2, width = 3, bricks = [1,2]

    count_walls = 0

    rows = [
        
        [ 1 ,2, 2 ]

        [2, 2, 1]
        
    ]

    n! (?)


    height = 2, width = 5, bricks = [1,2]

    count_walls = 0

    rows = [
        
        [ 2, 2, 1, 2, 2 ]

        [1, 2, 2, 1]
        
    ]

    '''



    def is_valid_row(self, width, row):
        if len(row) == width:
            return True
        else:
            return False

    def is_valid_brick(self, width, row, brick):
        if len(row) + brick <= width:
            return True
        else:
            return False

    def backtrack_row(self, width, row, bricks):
        if self.is_valid_row(width, row):
            self.possible_rows.append(copy.deepcopy(row))
            return

        for i in range(len(bricks)):
            brick = bricks[i]
            if self.is_valid_brick(width, row, brick):
                row.extend([brick]*brick)
                self.backtrack_row(width, row, bricks)
                for j in range(brick):
                    row.remove(brick)


    def is_valid_wall(self, height, wall):
        if len(wall) == height:
            return True
        else:
            return False

    def is_valid_wall_row(self, row, wall):
        if len(wall) == 0:
            return True

        last_row = wall[-1]
        res = True
        i = 0
        j = 0
        while i < len(row) and j < len(last_row):            
            j = i
            num_equal = 0
            end = i + row[i]
            while i < len(row) and j < len(last_row) and j < end:
                if row[i] == last_row[j]:
                    num_equal += 1
                i += 1
                j += 1

            if num_equal == row[i-1]:
                res = False
                break


        return res

    def backtrack_wall(self, height, wall, rows):
        if self.is_valid_wall(height, wall):
            self.num_walls += 1
            return

        for row in rows:
            if self.is_valid_wall_row(row, wall):
                wall.append(row)
                self.backtrack_wall(height, wall, rows)
                wall.remove(row)



    def buildWall(self, height: int, width: int, bricks: List[int]) -> int:
        self.possible_rows = []

        # 1st build possible rows
        self.backtrack_row(width, [], bricks)
        self.num_walls = 0
        self.backtrack_wall(height, [], self.possible_rows)

        return self.num_walls