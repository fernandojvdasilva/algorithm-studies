'''
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
'''
class Solution:

    '''
        [1, 1, -2, 2, 3] k=3

        [1, 2, 0, 2, 5]

        [1, 1, 1] k=2

        [1, 2, 3]

    '''
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum = 0
        subsets = {0: 1}

        res = 0

        for i in range(len(nums)):
            sum += nums[i]            

            if (sum - k) in subsets:
                res += subsets[(sum - k)]
            
            if not sum in subsets:
                subsets[sum] = 1
            else:
                subsets[sum] += 1

            

        return res