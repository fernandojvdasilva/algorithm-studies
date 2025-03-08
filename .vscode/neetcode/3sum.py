'''
3Sum
Solved 
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].

Example 2:

Input: nums = [0,1,1]

Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]

Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:

3 <= nums.length <= 1000
-10^5 <= nums[i] <= 10^5
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pair_sums = []
        values_pos = {}

        for i in range(len(nums)):
            if nums[i] in values_pos.keys():
                values_pos[nums[i]].add(i)
            else:
                values_pos[nums[i]] = set({i})

            for j in range(i+1, len(nums)):
                pair_sums.append((nums[i]+nums[j], [i, j]))

        print(pair_sums)

        res = []
        res_set = set()

        for item in pair_sums:
            k = item[0]
            i = item[1][0]
            j = item[1][1]


            seek_val = 0-k

            print("seek_val = %d" % seek_val)
            print("seek_val in values_pos.keys() = %s" % str(seek_val in values_pos.keys()))
            print("i=%d, j=%d"% (i, j))
            if seek_val in values_pos.keys():
                print("values_pos[seek_val] = %s" % str(values_pos[seek_val]))
                     


            if seek_val in values_pos.keys() and \
            ((not i in values_pos[seek_val] and \
             not j in values_pos[seek_val]) or len(values_pos[seek_val]) > 2):

                check_res = tuple(sorted([nums[i], nums[j], seek_val]))
                if not check_res in res_set:
                    res.append([nums[i], nums[j], seek_val])
                    res_set.add(check_res)
                    print(res)

            print("---")   
        return res