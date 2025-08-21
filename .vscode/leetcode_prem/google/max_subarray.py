'''
53. Maximum Subarray
Attempted
Medium
Topics
conpanies icon
Companies
Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''
class Solution:

    def maxSub(self, nums: List[int], max_left: List[int], i: int, j: int) -> int:
        if i > j:
            return float("inf")*-1
        elif i == j:
            return nums[i]

        # full subarray
        if i > 0:
            val1 = max_left[j]-max_left[i-1]
        else:
            val1 = max_left[j]

        # removing one at the left
        val2 = self.maxSub(nums, max_left, i+1, j)
        val3 = self.maxSub(nums, max_left, i, j-1)
        val4 = self.maxSub(nums, max_left, i+1, j-1)

        return max(val1, val2, val3, val4)

    def maxSubArray(self, nums: List[int]) -> int:
        '''
        [-2,1,-3,4,-1,2,1,-5,4]
                 i
                      e

        [-2,-1,-4,0,-1,1,2,-7,3]
        [  1, 3, 2,5,1,2,0,-1,4]
        '''
        max_left = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                max_left[i] = nums[i]
            else:
                max_left[i] = max_left[i-1] + nums[i]


        return self.maxSub(nums, max_left, 0, len(nums)-1)