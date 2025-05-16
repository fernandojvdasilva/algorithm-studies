'''
1. Two Sum
Solved
Easy
Topics
Companies
Hint
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_set = {}

        res = []
        for i in range(len(nums)):
            if not nums[i] in num_set:
                num_set[nums[i]] = {i}
            else:
                num_set[nums[i]].add(i)

        for i in range(len(nums)):
            search_num = (target - nums[i])
            if search_num in num_set.keys():
                if i in num_set[search_num]:
                    if len(num_set[search_num]) > 1:
                        for j in num_set[search_num]:
                            if j != i:
                                res = [i, j]
                                break
                else:
                    j = num_set[search_num].pop()
                    res = [i, j]
            
            if len(res) > 0:
                break

        return res
            