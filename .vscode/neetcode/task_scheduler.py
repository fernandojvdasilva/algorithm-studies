'''
Task Scheduler
Solved 
You are given an array of CPU tasks tasks, where tasks[i] is an uppercase english character from A to Z. You are also given an integer n.

Each CPU cycle allows the completion of a single task, and tasks may be completed in any order.

The only constraint is that identical tasks must be separated by at least n CPU cycles, to cooldown the CPU.

Return the minimum number of CPU cycles required to complete all tasks.

Example 1:

Input: tasks = ["X","X","Y","Y"], n = 2

Output: 5
Explanation: A possible sequence is: X -> Y -> idle -> X -> Y.

Example 2:

Input: tasks = ["A","A","A","B","C"], n = 3

Output: 9
Explanation: A possible sequence is: A -> B -> C -> Idle -> A -> Idle -> Idle -> Idle -> A.

Constraints:

1 <= tasks.length <= 1000
0 <= n <= 100

'''

import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        task_count = {}
        for t in tasks:
            if not t in task_count.keys():
                task_count[t] = 1
            else:
                task_count[t] += 1

        task_heap = [v*-1 for v in task_count.values()]

        heapq.heapify(task_heap)
        task_queue = deque([])

        time = 0
        while len(task_heap) > 0 or len(task_queue) > 0:

            print("time=%d" % time)
            print("task_heap")
            print(task_heap)

            print("task_queue")
            print(task_queue)

            print("-----")

            time += 1

            if len(task_heap) == 0:
                time = task_queue[0][1]
            else:
                curr_task = heapq.heappop(task_heap)+1

                if curr_task < 0:
                    task_queue.append([curr_task, time+n])


            if len(task_queue) > 0 and task_queue[0][1] == time:
                task = task_queue.popleft()
                heapq.heappush(task_heap, task[0])
                                    

            

        return time