'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Other test cases:
Input: nums1 = [], nums2 = [1]

Input: nums1 = [1,2], nums2 = [3,4,5]

Input: nums1 = [5], nums2 = [1,3,10, 100]

Input: nums1 = [2, 4, 5], nums2 = [1, 3, 10, 100]

Input: nums1 = [3, 4, 5], nums2 = [1, 2]

'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        middle = len(nums1)	

        all_nums = nums1 + nums2 
        

        swap = True

        while swap:
            swap = False
            
            i = middle
            j = middle - 1
            if j >= 0 and i < len(all_nums):
                while i > 0 :
                    if all_nums[j] > all_nums[i]:
                        temp = all_nums[j]
                        all_nums[j] = all_nums[i]
                        all_nums[i] = temp
                        i = j
                        j -= 1
                        swap = True
                    else:
                        break

            i = middle
            j = middle + 1
            
            if i >= 0 and j < len(all_nums):
                while i < len(all_nums)-1:            
                    if all_nums[j] < all_nums[i]:
                        temp = all_nums[j]
                        all_nums[j] = all_nums[i]
                        all_nums[i] = temp
                        i = j
                        j += 1
                        swap = True
                    else:
                        break

        if len(all_nums) % 2 == 0:
            result = float(all_nums[int(len(all_nums)/2)] + \
            all_nums[int(len(all_nums)/2)-1]) / 2.0
        else:
            result = all_nums[floor(len(all_nums)/2)]
        
        return result