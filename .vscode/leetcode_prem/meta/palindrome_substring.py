"""
Given a string s, return the longest 
palindromic
 
substring
 in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 
    """

class Solution:
    def isPalindrome(self, s: str) -> bool:     
        """
        s = bab

        i = 1
        j = 1
        """   
        i = 0
        j = len(s)-1
        check = True
        while check and i < len(s) and j > i:
            check = (s[i] == s[j])
            i += 1
            j -= 1

        return check


    def longestPalindrome(self, s: str) -> str:
        i = 0
        max_palindrome = ""
        max_palindrome_len = 0
        max_palindrome_end = -1

        char_pos = {}

        ''' babad  
        char_pos = {'b' = [0, 2], 'a' = [1, 3], 'd' = [4]}
        
        s[i] = b
        j = 1
        pos = 2
        i = 0
        '''
        for i in range(len(s)):
            if not s[i] in char_pos.keys():
                char_pos[s[i]] = [i]
            else:
                char_pos[s[i]].append(i)
        i = 0
        while i < len(s):
            j = len(char_pos[s[i]])-1
            while j >= 0:
                pos = char_pos[s[i]][j]
                if pos < max_palindrome_end:
                    break
                if pos != i:
                    if self.isPalindrome(s[i:pos+1]):
                        if (pos+1)-i > max_palindrome_len:
                            max_palindrome_len = (pos+1)-i
                            max_palindrome = s[i:pos+1]
                            max_palindrome_end = pos
                        break
                else:
                    if max_palindrome_len == 0:
                        max_palindrome_len = 1
                        max_palindrome = s[i]
                        max_palindrome_end = i

                j -= 1
            i += 1

        return max_palindrome