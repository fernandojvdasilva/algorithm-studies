'''
You are given an integer n, which indicates that there are n courses labeled from 1 to n. You are also given an array relations where relations[i] = [prevCoursei, nextCoursei], representing a prerequisite relationship between course prevCoursei and course nextCoursei: course prevCoursei has to be taken before course nextCoursei.

In one semester, you can take any number of courses as long as you have taken all the prerequisites in the previous semester for the courses you are taking.

Return the minimum number of semesters needed to take all courses. If there is no way to take all the courses, return -1.

 

Example 1:


Input: n = 3, relations = [[1,3],[2,3]]
Output: 2
Explanation: The figure above represents the given graph.
In the first semester, you can take courses 1 and 2.
In the second semester, you can take course 3.
Example 2:


Input: n = 3, relations = [[1,2],[2,3],[3,1]]
Output: -1
Explanation: No course can be studied because they are prerequisites of each other.
 

'''

class Solution:
    '''
        n = 3, relations = [[1,3], [2,3]]

        prev_courses = {1: [], 2: [], 3: [1,2]}
        next_courses = {1: [3], 2: [3], 3: []}

        prev_courses = {3: [1,2]}
        next_courses = {1: [3], 2: [3], 3: []}
        next_semester = [3]


        ==============


        n = 5, relations = [[1,3], [2,3], [3,4], [1,5], [4,5]]

        next_semester = [1,2]

        prev_courses = {1: [], 2: [], 3:[1,2], 4:[3], 5:[1,4]}
        next_courses = {1: [3,5], 2:[3], 3:[4], 4:[5] 5:[] }
        next_semester = [3,5]


        prev_courses = {3:[], 4:[3], 5:[4]}
        next_courses = {1: [3,5], 2:[3], 3:[4], 4:[5] 5:[] }
        next_semester = [3]

        

    '''


    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        
        prev_courses = {}
        next_courses = {}

        for r in relations: # O(r)
            if not r[0] in next_courses.keys():
                next_courses[r[0]] = [r[1]]
            else:
                next_courses[r[0]].append(r[1])

            if not r[0] in prev_courses.keys():
                prev_courses[r[0]] = []


            if not r[1] in prev_courses.keys():
                prev_courses[r[1]] = [r[0]]
            else:
                prev_courses[r[1]].append(r[0])

            if not r[1] in next_courses.keys():
                next_courses[r[1]] = []

        next_semester = [k for k in range(1, n+1) if k in prev_courses.keys() and len(prev_courses[k]) == 0]

        if len(next_semester) == 0:
            return -1

        count_semesters = 0
        while len(next_semester) > 0:
            count_semesters += 1

            new_next_semester = []
            for k in next_semester: # O(n)
                
                for nk in next_courses[k]: # O(r)
                    prev_courses[nk].remove(k)
                    if not nk in new_next_semester and len(prev_courses[nk]) == 0:
                        new_next_semester.append(nk)
                    
                next_courses.pop(k, None)
                prev_courses.pop(k, None)

            next_semester = new_next_semester

        # Complexity: O(nr)

        if len(next_courses) > 0:
            return -1
            
        return count_semesters


