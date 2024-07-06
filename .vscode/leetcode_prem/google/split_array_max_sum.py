'''
Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

Return the minimized largest sum of the split.

A subarray is a contiguous part of the array.

 

Example 1:

Input: nums = [7,2,5,10,8], k = 2
Output: 18
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.
Example 2:

Input: nums = [1,2,3,4,5], k = 2
Output: 9
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is only 9.
 
'''

class Solution:
    
    '''
    There is a bug with this test case:
    [2,3,1,2,4,3]
    '''    
    
    
    def splitby2(self, nums: List[int], si: int = 0, ei: int = -1) -> (int, int):
        i = si
        
        if ei == -1:
            ei = len(nums)-1
        else:
            ei = ei-1

        j = ei

        cumm_sum_left = [0] * len(nums)
        cumm_sum_right = [0] * len(nums)
        while i < si+(ei-si+1):
            if i > 0:
                cumm_sum_left[i] = nums[i] + cumm_sum_left[i-1]
            else:
                cumm_sum_left[i] = nums[i]
                
            if j < si+(ei-si):
                cumm_sum_right[j] = nums[j] + cumm_sum_right[j+1]
            else:
                cumm_sum_right[j] = nums[j]
                
            i += 1
            j -= 1
                        
        min_sum = float('inf')
        best_i = 0
        for i in range(si, ei):
            if cumm_sum_left[i] < min_sum and cumm_sum_right[i+1] < min_sum:
                best_i = i
                min_sum = max(cumm_sum_left[i], cumm_sum_right[i+1])
        
        if si == ei:
            best_i = si
            min_sum = cumm_sum_left[si]

        return best_i, min_sum
    
    
    def splitArray(self, nums: List[int], k: int) -> int:
        ''' nums = [7,2,5,10,8], k = 2
         [7] [2, 5, 10, 8] = max = 25
         
         cum_left:
         [7, 9, 14, 24, 32]
         [32, 25, 23, 18, 8]
         
         
         [7, 2] [5, 10, 8] = max = 23
         [7, 2, 5] [10, 8] = max = 18
         [7, 2, 5, 10] [8] = max = 24
        '''
        
        ''' nums = [7,2,5,10,8], k = 3
         
         [7, 2, 5] [10, 8] = max = 18         
         [7, 2, 5] [10] [8] = max = 14
        '''
        i = 0
        j = -1
        cumm_sum_left = [0] * len(nums)
        cumm_sum_right = [0] * len(nums)
        while i < len(nums):
            if i > 0:
                cumm_sum_left[i] = nums[i] + cumm_sum_left[i-1]
            else:
                cumm_sum_left[i] = nums[i]
                
            if j < -1:
                cumm_sum_right[j] = nums[j] + cumm_sum_right[j+1]
            else:
                cumm_sum_right[j] = nums[j]
                
            i += 1
            j -= 1

        if k == 1:
            return cumm_sum_right[0]
        
        si = 0
        ei = len(nums)-1
        min_sum = float('inf')
        for k_ in range(2, k+1):
            left_min_sum = float('inf')
            curr_min_sum = float('inf')
            right_i, right_min_sum = self.splitby2(nums, si=si)
            if si > 0:
                left_i, left_min_sum = self.splitby2(nums, ei=ei)
            
            if right_min_sum < left_min_sum:                                
                #curr_min_sum = max(right_min_sum, cumm_sum_right[right_i+1])
                curr_min_sum = right_min_sum                
                ei = right_i+1
                si = right_i+1
            else:
                si = left_i+1
                ei = left_i                
                curr_min_sum = left_min_sum
                #curr_min_sum = max(left_min_sum, cumm_sum_left[left_i+1])
                

            min_sum = min(min_sum, curr_min_sum)
        
        return min_sum