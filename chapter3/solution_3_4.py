'''
Created on 5 de out de 2017

@author: fernando
'''

'''
In the classic problem of the Towers of Hanoi, you have 3 rods and N disks of different
sizes which can slide onto any tower. The puzzle starts with disks sorted in ascending
order of size from top to bottom (e.g., each disk sits on top of an even larger one). You
have the following constraints:
(A) Only one disk can be moved at a time.
(B) A disk is slid off the top of one rod onto the next rod.
(C) A disk can only be placed on top of a larger disk.
Write a program to move the disks from the first rod to the last using Stacks

'''

class MyStack:
    
    def __init__(self, values):
        self.values = values
    
    def push(self, val):
        self.values.append(val)

    def pop_(self):
        result = self.values[-1]
        self.values.remove(self.values[-1])

        return result

    def move(self, n, buffer, dest):
        if n > 0:
            self.move(n-1, dest, buffer)

            val = self.pop_()
            dest.push(val)

            buffer.move(n-1, self, dest)


def hannoi_tower(n_disks):
    rod = []
    rod.append(MyStack([n_disks-i for i in range(1, n_disks+1)]))
    rod.append(MyStack([]))
    rod.append(MyStack([]))

    rod[0].move(n_disks, rod[1], rod[2])
    
    return rod
