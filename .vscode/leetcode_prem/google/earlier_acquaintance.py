'''
There are n people in a social group labeled from 0 to n - 1. You are given an array logs where logs[i] = [timestampi, xi, yi] indicates that xi and yi will be friends at the time timestampi.

Friendship is symmetric. That means if a is friends with b, then b is friends with a. Also, person a is acquainted with a person b if a is friends with b, or a is a friend of someone acquainted with b.

Return the earliest time for which every person became acquainted with every other person. If there is no such earliest time, return -1.

 
'''

class Solution:
    '''
    logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], n = 6
Output: 20190301


    friendship = 

            0           1           2       3               4   5 
        0           20190101
        1   20190101
        2                               20190107
        3                       20190107            20190104
        4                        20190107       20190104
        5

    '''

    def all_acquain(self, n: int):
        return self.count_acquain == (n**2 - n)//2


    def mark_acquain(self, acquain: List[List[int]], log, n: int):
        timestamp = log[0]
        friend_A = log[1]
        friend_B = log[2]
        
        if self.all_acquain(n):
            return

        if acquain[friend_A][friend_B] is None:
            acquain[friend_A][friend_B] = timestamp
            acquain[friend_B][friend_A] = timestamp
            self.count_acquain += 1
            
            if self.all_acquain(n):
                self.earlier_timestamp = timestamp

            else:
                for i in range(len(acquain[friend_A])):
                    if i != friend_B and not acquain[friend_A][i] is None:
                        self.mark_acquain(acquain, [timestamp, friend_B, i], n)
                        if self.all_acquain(n):
                            break

                if not self.all_acquain(n):
                    for i in range(len(acquain[friend_B])):
                        if i != friend_A and not acquain[friend_B][i] is None:
                            self.mark_acquain(acquain, [timestamp, friend_A, i], n)
                            if self.all_acquain(n):
                                break
            


    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs = sorted(logs, key=lambda x: x[0])

        acquain = [[None for i in range(n)] for j in range(n)]

        self.count_acquain = 0
        self.earlier_timestamp = None

        for log in logs: 
            self.mark_acquain(acquain, log, n)
            if self.all_acquain(n):
                break

        if self.all_acquain(n):
            return self.earlier_timestamp
        else:
            return -1