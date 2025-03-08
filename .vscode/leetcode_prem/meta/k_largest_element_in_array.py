'''
215. Kth Largest Element in an Array
Attempted
Medium
Topics
Companies
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104

CHALLENGE: REIMPLEMENT WITH A HEAP!!!!!
'''

class Solution:
    
    def find_pos(self, num: int, k_list: List[int]) -> int:
        left, right = 0, len(k_list)

        while left < right:
            mid = left + (right-left)//2

            if num > k_list[mid]:
                right = mid
            else:
                left = mid+1

        return left


    def insert_k(self, num: int, k_list: List[int]):
        pos = self.find_pos(num, k_list)

        if pos > len(k_list)-1:
            return

        i = len(k_list)-1
        while i > pos:
            k_list[i] = k_list[i-1]
            i -= 1   

        k_list[pos] = num


    def findKthLargest(self, nums: List[int], k: int) -> int:
        i = 0
        k_list = [float("inf")*-1] * k

        for i in range(len(nums)):
            self.insert_k(nums[i], k_list)    

        return k_list[-1]