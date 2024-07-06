'''
Given a string s, find the length of the longest 
substring without repeating characters.

 
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            if s is None:
                raise Exception("s is None, is that expected?")

            long_len = 0 
            last_char_map = {}

            i = 0  
            while i < len(s): 
                current_sub_chars = set() 
                current_sub_len = 0

                while i < len(s):
                        if not s[i] in current_sub_chars: 
                            current_sub_chars.add(s[i])
                            current_sub_len += 1
                            last_char_map[s[i]] = i
                            i += 1
                        else:
                            i = last_char_map[s[i]] + 1
                            break
                    

                if current_sub_len > long_len:
                    long_len = current_sub_len

            return long_len
    

sol = Solution()

testCases = [("abcabcbb", 3),
             ("bbbbb", 1),
             ("pwwkew", 3),
             ("aab", 2)]

for s, res in testCases:
    if sol.lengthOfLongestSubstring(s) == res:
         print("Test Ok: %s" % s)
    else:
         print("Test failed: %s" % s)