'''
408. Valid Word Abbreviation
Solved
Easy
Topics
Companies
A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros.

For example, a string such as "substitution" could be abbreviated as (but not limited to):

"s10n" ("s ubstitutio n")
"sub4u4" ("sub stit u tion")
"12" ("substitution")
"su3i1u2on" ("su bst i t u ti on")
"substitution" (no substrings replaced)
The following are not valid abbreviations:

"s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
"s010n" (has leading zeros)
"s0ubstitution" (replaces an empty substring)
Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

A substring is a contiguous non-empty sequence of characters within a string.

 

Example 1:

Input: word = "internationalization", abbr = "i12iz4n"
Output: true
Explanation: The word "internationalization" can be abbreviated as "i12iz4n" ("i nternational iz atio n").
Example 2:

Input: word = "apple", abbr = "a2e"
Output: false
Explanation: The word "apple" cannot be abbreviated as "a2e".
 

Constraints:

1 <= word.length <= 20
word consists of only lowercase English letters.
1 <= abbr.length <= 10
abbr consists of lowercase English letters and digits.
All the integers in abbr will fit in a 32-bit integer.
'''

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0

        res = True

        curr_abbr = ''
        
        while i < len(word) and j < len(abbr):
            
            
            if word[i] == abbr[j]:

                if len(curr_abbr) > 0:
                    i += int(curr_abbr)
                    curr_abbr = ''
                    continue

                i += 1
                j += 1

                curr_abbr = ''

            elif ord(abbr[j]) in range(ord('0'), ord('9')+1):

                if len(curr_abbr) == 0 and abbr[j] == '0':
                    res = False
                    break

                curr_abbr += abbr[j]
                j += 1

            else:
                if len(curr_abbr) > 0:                    
                    i += int(curr_abbr)
                    curr_abbr = ''
                else:
                    res = False
                    break

        if i < len(word) or j < len(abbr):
            if len(curr_abbr) > 0:
                if i + int(curr_abbr) != len(word):
                    res = False
            else:
                res = False

        return res