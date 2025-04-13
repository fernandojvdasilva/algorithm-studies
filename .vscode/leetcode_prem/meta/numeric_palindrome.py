'''
9. Palindrome Number
Solved
Easy
Topics
Companies
Hint
Given an integer x, return true if x is a palindrome, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?

'''
class Solution:


    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        units = []

        factor = 9 # 1 billion 2^31 is a bit higher than 2 billion
        
        while factor >= 0:
            curr_unit = x // (10**factor)
            if len(units) == 0:
                if curr_unit > 0:
                    units.append(curr_unit)
            
            else:
                units.append(curr_unit)

            x -= curr_unit * (10**factor)
            factor -= 1

        
        i = 0
        j = len(units)-1

        res = True

        while i < j:
            if units[i] != units[j]:
                res = False
                break
            i += 1
            j -= 1

        return res