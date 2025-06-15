'''
1768. Merge Strings Alternately
Solved
Easy
Topics
conpanies icon
Companies
Hint
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
 

Constraints:

1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
'''

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = 0
        res = ""

        source = word1        
        while i < len(word1) or j < len(word2):
            
            if i >= len(source) and id(source) == id(word1) or \
               j >= len(source) and id(source) == id(word2):
                source = self.switch_src(source, word1, word2)

            if id(source) == id(word1):
                res += source[i]
                i += 1
            else:
                res += source[j]
                j += 1

            source = self.switch_src(source, word1, word2)            
            
        return res

    def switch_src(self, source: str, word1: str, word2: str):
        return word1 if id(source) == id(word2) else word2