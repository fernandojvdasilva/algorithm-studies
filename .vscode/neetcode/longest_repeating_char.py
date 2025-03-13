'''
Longest Repeating Character Replacement
You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

Example 1:

Input: s = "XYYX", k = 2

Output: 4
Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

Example 2:

Input: s = "AAABABB", k = 1

Output: 5
Constraints:

1 <= s.length <= 1000
0 <= k <= s.length
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        substr_pos = {}
        

        for i in range(len(s)):

            if not s[i] in substr_pos.keys():
                substr_pos[s[i]] = [{'first': i, 'last': i, 'count': 1}]
            else:
                if (i - substr_pos[s[i]][-1]['last']) <= k+1:
                    substr_pos[s[i]][-1]['last'] = i
                    substr_pos[s[i]][-1]['count'] += 1
                else:
                    substr_pos[s[i]].append({'first': i, 'last': i, 'count': 1})



        max_len = 0
        for key in substr_pos.keys():
            for sub in substr_pos[key]:
                if sub['count'] + k > max_len:
                    max_len = sub['count'] + k
                    if max_len > len(s):
                        max_len = len(s)
                                

        return max_len
                
