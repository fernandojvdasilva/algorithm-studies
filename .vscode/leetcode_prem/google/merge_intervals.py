'''
56. Merge Intervals
Solved
Medium
Topics
conpanies icon
Companies
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda x:x[0])

        res = []
        i = 0
        while i < len(sorted_intervals):
            curr_interval = sorted_intervals[i]
            j = i+1
            while j < len(sorted_intervals) and sorted_intervals[j][0] >= curr_interval[0] and sorted_intervals[j][0] <= curr_interval[1]:
                curr_interval[1] = max(sorted_intervals[j][1], curr_interval[1])
                j += 1
            i = j
            res.append(curr_interval)

        return res
    
    