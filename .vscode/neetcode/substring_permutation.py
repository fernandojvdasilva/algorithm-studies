'''
Permutation in String
Solved 
You are given two strings s1 and s2.

Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.

Both strings only contain lowercase letters.

Example 1:

Input: s1 = "abc", s2 = "lecabee"

Output: true
Explanation: The substring "cab" is a permutation of "abc" and is present in "lecabee".

Example 2:

Input: s1 = "abc", s2 = "lecaabee"

Output: false
Constraints:

1 <= s1.length, s2.length <= 1000

'''

import copy

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # Check the right limit of the window and count the new occurrence
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1

            if s1Count[index] == s2Count[index]:
                matches += 1

            # As it's the right limit, we may have just passed the number of
            # occurrences of that letter. We then decrement the matches
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1


            # Now remove the lower left limit (window move)
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1        

            # If we matched by removing it...
            if s1Count[index] == s2Count[index]:
                matches += 1

            # if we don't match anymore...
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1

            l += 1
            
        return matches == 26