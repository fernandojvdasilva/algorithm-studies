'''
17. Letter Combinations of a Phone Number
Solved
Medium
Topics
Companies
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
'''
class Solution:

    def combine(self, a_list: List[str], b_list: List[str]) -> List[str]:
        res = []

        for a in a_list:
            for b in b_list:
                res.append(a+b)

        return res


    def letterCombinations(self, digits: str) -> List[str]:
        chars = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        i = 0

        translated_chars = [chars[d] for d in digits]

        res = []
        for t in translated_chars:
            if len(res) == 0:
                res = [c for c in t]
            else:
                res = self.combine(res, t)


        return res

        