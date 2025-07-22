'''
128. Longest Consecutive Sequence
Solved
Medium
Topics
conpanies icon
Companies
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109

'''


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_seqlen = 0

        for num in num_set:
            if num-1 not in num_set:
                curr_num = num
                seq_len = 1

                while curr_num+1 in num_set:
                    seq_len += 1
                    curr_num += 1

                max_seqlen = max(seq_len, max_seqlen)

        return max_seqlen


    '''def longestConsecutive(self, nums: List[int]) -> int:
        seqs_start = {n:n for n in nums}
        seqs_end = {n:n for n in nums}

        for n in seqs_start.keys():
            if n+1 in seqs_start:
                seqs_start[n] = seqs_start[n+1]
                seqs_end[seqs_start[n]] = n
                del seqs_start[n+1]

            if n-1 in seqs_end:
                seqs_end[n] = seqs_end[n-1]
                seqs_start[seqs_end[n]] = n
                del seqs_end[n-1]


        res = 0
        for n in seqs_start.keys():
            res = max(res, seqs_start[n] - n + 1)

        return res
       '''     
        # Time complexity: O(n)
        # Space complexity: O(n)