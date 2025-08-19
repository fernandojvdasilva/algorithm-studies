'''
169. Majority Element
Solved
Easy
Topics
conpanies icon
Companies
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 

Follow-up: Could you solve the problem in linear time and in O(1) space?
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_elements = {}

        for n in nums:
            if n in count_elements.keys():
                count_elements[n] += 1
            else:
                count_elements[n] = 0

        for n in count_elements.keys():
            if count_elements[n] >= len(nums)//2:
                return n