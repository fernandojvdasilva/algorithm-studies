'''
Longest Consecutive Sequence
Solved 
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [2,20,4,10,3,4,5]

Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:

Input: nums = [0,3,2,5,4,6,1,1]

Output: 7
Constraints:

0 <= nums.length <= 1000
-10^9 <= nums[i] <= 10^9
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        counter_dict = {}
        max_count = 0
        max_val = 0

        print(nums)

        unique_nums = []

        for i in range(len(nums)):
            if not nums[i] in counter_dict.keys():
                counter_dict[nums[i]] = 0
                unique_nums.append(nums[i])

        for num in unique_nums:  
            counter_dict[num] = 1

            if num-1 in counter_dict.keys():
                counter_dict[num] += counter_dict[num-1]
                                    
            if num+1 in counter_dict.keys():
                counter_dict[num] += counter_dict[num+1]

            if num-1 in counter_dict.keys():
                counter_dict[num - counter_dict[num-1]] = counter_dict[num]

            if num+1 in counter_dict.keys():
                counter_dict[num + counter_dict[num+1]] = counter_dict[num]    

            if counter_dict[num] > max_count:
                max_val = counter_dict[num]

            print("num=%d" % num)
            print(counter_dict)
            print("---")


        return max_val
