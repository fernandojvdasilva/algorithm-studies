'''
K Closest Points to Origin
Solved 
You are given an 2-D array points where points[i] = [xi, yi] represents the coordinates of a point on an X-Y axis plane. You are also given an integer k.

Return the k closest points to the origin (0, 0).

The distance between two points is defined as the Euclidean distance (sqrt((x1 - x2)^2 + (y1 - y2)^2)).

You may return the answer in any order.

Example 1:



Input: points = [[0,2],[2,2]], k = 1

Output: [[0,2]]
Explanation : The distance between (0, 2) and the origin (0, 0) is 2. The distance between (2, 2) and the origin is sqrt(2^2 + 2^2) = 2.82842. So the closest point to the origin is (0, 2).

Example 2:

Input: points = [[0,2],[2,0],[2,2]], k = 2

Output: [[0,2],[2,0]]
Explanation: The output [2,0],[0,2] would also be accepted.

Constraints:

1 <= k <= points.length <= 1000
-100 <= points[i][0], points[i][1] <= 100
'''

from math import sqrt
import heapq

class Solution:


    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        short_dist = float('inf')
        res = []

        maxHeap = []

        for p in points:
            dist = sqrt((p[0] - 0.0)**2 + (p[1] - 0.0)**2) * -1

            heapq.heappush(maxHeap, [dist, p])

            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        for i in range(k):
            dist, p = heapq.heappop(maxHeap)
            res.append(p)

        return res


        '''
        My own heap (doesn't work...)
        
        class MinHeap:

        def __init__(self):
            self.heap = []

        def insert(self, val: List):
            self.heap.append(val)

            index = len(self.heap) -1

            while index > 0 and self.heap[(index-1) //2][0] > self.heap[index][0]:
                self.heap[(index-1) // 2][0], self.heap[index][0] = self.heap[index][0], self.heap[(index-1) // 2][0]

                index = (index -1) // 2


        def delete(self) -> int:
            self.heap[0][0], self.heap[-1][0] = self.heap[-1][0], self.heap[0][0]

            res = self.heap.pop()            

            self.heapify()

            return res


        def heapify(self):

            index = 0
            while True:
                left_child = 2 * index + 1
                right_child = 2 * index + 2

                smallest = index

                if len(self.heap) > left_child and self.heap[left_child][0] > self.heap[smallest][0]:
                    smallest = left_child

                if len(self.heap) > right_child and self.heap[right_child][0] > self.heap[smallest][0]:
                    smallest = right_child

                if smallest != index:
                    self.heap[smallest][0], self.heap[index][0] = self.heap[index][0], self.heap[smallest][0]
                    index = smallest
                else:
                    break


        
        heap = Solution.MinHeap()

        for p in points:
            print(p)
            dist = sqrt((p[0] - 0.0)**2 + (p[1] - 0.0)**2)

            heap.insert([dist, p])

        for i in range(k):
            res.append(heap.delete()[1])

        return res
        '''
