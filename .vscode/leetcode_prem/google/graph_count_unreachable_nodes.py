'''
You are given an integer n. There is an undirected graph with n nodes, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.

Return the number of pairs of different nodes that are unreachable from each other.

 

Example 1:


Input: n = 3, edges = [[0,1],[0,2],[1,2]]
Output: 0
Explanation: There are no pairs of nodes that are unreachable from each other. Therefore, we return 0.
Example 2:


Input: n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
Output: 14
Explanation: There are 14 pairs of nodes that are unreachable from each other:
[[0,1],[0,3],[0,6],[1,2],[1,3],[1,4],[1,5],[2,3],[2,6],[3,4],[3,5],[3,6],[4,6],[5,6]].
Therefore, we return 14.
'''

class Solution:

    '''

         n = 7, edges = [[0,2], [0,5], [2,4], [1,6], [5,4]]

         [
            0 1 2 3 4 5 6
          0 f f T f f T f
          1 f f f f f f T
          2 T f f f T f f 
          3 f f f f f f f
          4 f f T f f T f
          5 T f f f T f f
          6 f T f f f f f 
         ]

         
         [
            0 1 2 3 4 5 6
          0     T   T T
          1
          2 T   T   T T
          3
          4     T     T
          5
          6
         ]

    '''

    def checkReachable(self, n: int, i: int, adjmatrix: List[List[int]], reachdict: Dict) -> List[int]:
        '''
        if i in reachdict.keys():
            return [k for k in range(len(reachdict[i])) if reachdict[i][k] is True]
        else:
        '''
        if not i in reachdict.keys():
            reachdict[i] = [False] * n 
        result = []

        for j in range(len(adjmatrix[i])):
            if adjmatrix[i][j] is True:
                reachdict[i][j] = adjmatrix[i][j]
                if not j in reachdict.keys():
                    reachdict[j] = [False] * n
                reachdict[j][i] = adjmatrix[j][i]
                result.append(j)
                if j in reachdict.keys():
                    reachable = [k for k in range(len(reachdict[j])) if reachdict[j][k] is True]
                else:
                    reachable = self.checkReachable(n, j, adjmatrix, reachdict, checked_nodes)
                    
                
                for k in reachable:
                    reachdict[i][k] = True
                    if not k in result:
                        result.append(k)

                    if not k in reachdict.keys():
                        reachdict[k] = [False] * n
                    reachdict[k][i] = True

        return result


    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        adjmatrix = [[False] * n for i in range(n)]    
        reachdict = {}
 
        for e in edges:
            i = e[0]
            j = e[1]
            adjmatrix[i][j] = True
            adjmatrix[j][i] = True

        for i in range(len(adjmatrix)):
            _ = self.checkReachable(n, i, adjmatrix, reachdict)
            

        count_unreachable = 0
        for i in reachdict.keys():
            for j in range(i+1, len(reachdict[i])):
                if reachdict[i][j] is False:
                    count_unreachable += 1

        return count_unreachable