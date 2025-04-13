'''
14. Longest Common Prefix
Solved
Easy
Topics
Companies
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.

'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        p = None

        res = ''
        while True:
            if len(strs) > 0 and len(strs[0]) > i:
                curr_char = strs[0][i]
            else:
                break

            check = True
            for j in range(1, len(strs)):
                if len(strs[j]) == i or strs[j][i] != curr_char:
                    check = False
                    break
            
            if check:
                p = i
            else:
                break

            i += 1

        if p != None:
            res = strs[0][:p+1]

        return res