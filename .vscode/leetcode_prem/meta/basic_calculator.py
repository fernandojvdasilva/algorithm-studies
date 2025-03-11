'''
227. Basic Calculator II
Attempted
Medium
Topics
Companies
Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "3+2*2"
Output: 7
Example 2:

Input: s = " 3/2 "
Output: 1
Example 3:

Input: s = " 3+5 / 2 "
Output: 5
 

Constraints:

1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.

PS: THIS VERSION DOESN'T PASS IN THE TEST: 1*2*3*4*5*6*7*8*9*10
'''
class Solution:
    def calculate(self, s: str) -> int:
        num_stack = []

        is_neg = False
        curr_number = ''
        div_mode = False
        mult_mode = False
        for i in range(len(s)):
            if s[i] == ' ':
                continue

            if s[i] == '-':
                is_neg = True
            
            if ord(s[i]) in range(ord('0'), ord('9')+1):
                if is_neg:
                    curr_number = '-'
                    is_neg = False
                
                curr_number += s[i]

            elif len(curr_number) > 0:
                new_num = int(curr_number)                
                curr_number = ''

                if div_mode:
                    last_num = num_stack.pop()
                    if last_num < 0: 
                        new_num = (last_num*-1) // new_num
                        new_num *= -1
                    else:
                        new_num = last_num // new_num
                    div_mode = False
                    
                elif mult_mode:
                    new_num = num_stack.pop() * new_num
                    mult_mode = False

                num_stack.append(new_num)

            
            if s[i] == '*':
                mult_mode = True

            elif s[i] == '/':
                div_mode = True
                
        if len(curr_number) > 0:
            new_num = int(curr_number)                
            curr_number = ''

            if div_mode:
                last_num = num_stack.pop()
                if last_num < 0: 
                    new_num = (last_num*-1) // new_num
                    new_num *= -1
                else:
                    new_num = last_num // new_num
                div_mode = False
                
            elif mult_mode:
                new_num = num_stack.pop() * new_num
                mult_mode = False

            num_stack.append(new_num)


        res = 0
        for i in range(len(num_stack)):
           res += num_stack[i]

        return res 
        
