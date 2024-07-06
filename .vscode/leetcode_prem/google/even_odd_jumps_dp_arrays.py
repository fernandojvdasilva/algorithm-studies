'''
You are given an integer array arr. From some starting index, you can make a series of jumps. The (1st, 3rd, 5th, ...) jumps in the series are called odd-numbered jumps, and the (2nd, 4th, 6th, ...) jumps in the series are called even-numbered jumps. Note that the jumps are numbered, not the indices.

You may jump forward from index i to index j (with i < j) in the following way:

During odd-numbered jumps (i.e., jumps 1, 3, 5, ...), you jump to the index j such that arr[i] <= arr[j] and arr[j] is the smallest possible value. If there are multiple such indices j, you can only jump to the smallest such index j.
During even-numbered jumps (i.e., jumps 2, 4, 6, ...), you jump to the index j such that arr[i] >= arr[j] and arr[j] is the largest possible value. If there are multiple such indices j, you can only jump to the smallest such index j.
It may be the case that for some index i, there are no legal jumps.
A starting index is good if, starting from that index, you can reach the end of the array (index arr.length - 1) by jumping some number of times (possibly 0 or more than once).

Return the number of good starting indices.

 

Example 1:

Input: arr = [10,13,12,14,15]
Output: 2
Explanation: 
From starting index i = 0, we can make our 1st jump to i = 2 (since arr[2] is the smallest among arr[1], arr[2], arr[3], arr[4] that is greater or equal to arr[0]), then we cannot jump any more.
From starting index i = 1 and i = 2, we can make our 1st jump to i = 3, then we cannot jump any more.
From starting index i = 3, we can make our 1st jump to i = 4, so we have reached the end.
From starting index i = 4, we have reached the end already.
In total, there are 2 different starting indices i = 3 and i = 4, where we can reach the end with some number of
jumps.
Example 2:

Input: arr = [2,3,1,1,4]
Output: 3
Explanation: 
From starting index i = 0, we make jumps to i = 1, i = 2, i = 3:
During our 1st jump (odd-numbered), we first jump to i = 1 because arr[1] is the smallest value in [arr[1], arr[2], arr[3], arr[4]] that is greater than or equal to arr[0].
During our 2nd jump (even-numbered), we jump from i = 1 to i = 2 because arr[2] is the largest value in [arr[2], arr[3], arr[4]] that is less than or equal to arr[1]. arr[3] is also the largest value, but 2 is a smaller index, so we can only jump to i = 2 and not i = 3
During our 3rd jump (odd-numbered), we jump from i = 2 to i = 3 because arr[3] is the smallest value in [arr[3], arr[4]] that is greater than or equal to arr[2].
We can't jump from i = 3 to i = 4, so the starting index i = 0 is not good.
In a similar manner, we can deduce that:
From starting index i = 1, we jump to i = 4, so we reach the end.
From starting index i = 2, we jump to i = 3, and then we can't jump anymore.
From starting index i = 3, we jump to i = 4, so we reach the end.
From starting index i = 4, we are already at the end.
In total, there are 3 different starting indices i = 1, i = 3, and i = 4, where we can reach the end with some
number of jumps.
Example 3:

Input: arr = [5,1,3,4,2]
Output: 3
Explanation: We can reach the end from starting indices 1, 2, and 4.
'''

class Solution:
    '''
    arr = [10,13,12,14,15]

    i = 4
    [15]
    odd_jumps = 0
    even_jumps = 0
    smallest_ind = 4
    biggest_ind =  4

    i = 3
    [14, 15]
    odd_jumps[] = 4
    even_jumps[] = -1
    smallest_ind = 4
    biggest_ind = 3

    i = 2
    [12, 14, 15]
    for j in range(i+1, len(smallest_ind)):
        if arr[j] > arr[i]:
            odd_jump[i] = j

    odd_jumps[] = 3
    even_jumps[] = -1



    '''

    def calculate_jumps(self, arr: List[int], i: int):
        if i == len(arr)-1:
            self.odd_jump[i] = 0
            self.even_jump[i] = 0
            return
        
        smallest = float('inf')
        for j in range(i+1, len(arr)):
            if arr[j] >= arr[i] and arr[j] < smallest:
                self.odd_jump[i] = j
                smallest = arr[j]


        largest = float('-inf')
        for j in range(i+1, len(arr)):
            if arr[j] <= arr[i] and arr[j] > largest:
                self.even_jump[i] = j
                largest = arr[j]





    def jump(self, i: int, is_odd: bool, arr: List[int], num_jumps: int) -> int:
        if i == len(arr)-1:
            return num_jumps
        else:
            if is_odd:
                if self.odd_jump[i] >= 0:
                    return self.jump(self.odd_jump[i], False, arr, num_jumps+1)
                else:
                    return -1

            else:
                if self.even_jump[i] >= 0:
                    return self.jump(self.even_jump[i], True, arr, num_jumps+1)
                else:
                    return -1


    def oddEvenJumps(self, arr: List[int]) -> int:
        self.odd_jump = [-1 for _ in range(len(arr))]
        self.even_jump = [-1 for _ in range(len(arr))]
        
        i = len(arr)-1
        while i >= 0:
            self.calculate_jumps(arr, i)
            i -= 1

        count_valid = 0
        for i in range(len(arr)):
            check = self.jump(i, True, arr, 0)

            if check >= 0:
                count_valid += 1

        return count_valid