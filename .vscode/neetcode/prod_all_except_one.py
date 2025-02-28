'''
Products of Array Except Self
Solved 
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in 
O
(
n
)
O(n) time without using the division operation?

Example 1:

Input: nums = [1,2,4,6]

Output: [48,24,12,8]
Example 2:

Input: nums = [-1,0,1,2,3]

Output: [0,-6,0,0,0]
Constraints:

2 <= nums.length <= 1000
-20 <= nums[i] <= 20

'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1

        zero_ind = None
        all_zeros = False

        for i in range(len(nums)):
            n = nums[i]
            if n != 0:
                total *= n
            else:
                if zero_ind is None:
                    zero_ind = i
                else:
                    all_zeros = True
                    break


        if all_zeros:
            res = [0] * len(nums)

        else:
            res = []

            for i in range(len(nums)):

                n = nums[i]

                if i == zero_ind:
                    res.append(total)
                elif zero_ind is None:
                    res.append(total//n)
                else:
                    res.append(0)

        return res