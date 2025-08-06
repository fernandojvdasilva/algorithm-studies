'''
20. Valid Parentheses
Solved
Easy
Topics
conpanies icon
Companies
Hint
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

'''

class Solution:
    def isValid(self, s: str) -> bool:
        bracket_stack = []
        open_chars = set("([{")
        close_chars = set(")]}")

        char_map = {")": "(", \
                    "]": "[", \
                    "}": "{"}

        res = True
        for i in range(len(s)):
            if s[i] in open_chars:
                bracket_stack.append(s[i])

            else:
                if len(bracket_stack) > 0:
                    last_open = bracket_stack.pop()
                    if last_open != char_map[s[i]]:
                        res = False
                        break
                else:
                    res = False
                    break

        if len(bracket_stack) > 0:
            res = False

        return res  
