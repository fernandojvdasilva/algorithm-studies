'''
680. Valid Palindrome II
Solved
Easy
Topics
Companies
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.

'''
class Solution:
    def checkPalindrome(self, s: str, i:int, j:int) -> bool:

        res = True
        while j > i:
            if s[i] != s[j]:
                res = False
                break
            i += 1
            j -= 1

        return res
   
   
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1

        res = True
        while j > i and res:
            if s[i] != s[j]:
                res = self.checkPalindrome(s, i, j-1) or self.checkPalindrome(s, i+1, j)
                break
            i += 1
            j -= 1

        return res
    '''    
        i = 0
        j = len(s)-1
        

        num_errors = 0
        res = True

        while j > i and res:
            if s[i] != s[j]:
                if num_errors > 0:
                    res = False
                else:
                    num_errors += 1

                    if s[i+1] == s[j] and s[i] == s[j-1] and j-i > 1:

                        if s[i+1] == s[j] and s[i+2] == s[j-1]:
                            i += 1
                        elif s[i] == s[j-1] and s[i+1] == s[j-2]:
                            j -= 1
                        else:
                            res = False                        
                    else:
                        if s[i+1] == s[j]:
                            i += 1
                        elif s[i] == s[j-1]:
                            j -= 1
                        else:
                            res = False
            
            else:
                i += 1
                j -= 1

        return res

'''