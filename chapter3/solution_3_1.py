'''
Created on 3 de out de 2017

@author: fernando
'''


'''
Describe how you could use a single array to implement three stacks
'''


class ArrayStack:
    
    def __init__(self):
        self.array = [None, None, None]
        self.next_stack_pointer = [0, 1, 2]
        self.curr_stack_pointer = [None, None, None]
        
    def push(self, val, stack_index):
        if self.next_stack_pointer[stack_index] >= len(self.array):
            self.array.extend([None, None, None])
        
        self.array[self.next_stack_pointer[stack_index]] = val
        self.curr_stack_pointer[stack_index] = self.next_stack_pointer[stack_index]
        self.next_stack_pointer[stack_index] = self.next_stack_pointer[stack_index] + 3


    def pop(self, stack_index):
        result = None
        if self.curr_stack_pointer[stack_index] != None:
            result = self.array[self.curr_stack_pointer[stack_index]]
            self.curr_stack_pointer[stack_index] -= 3
            if self.curr_stack_pointer[stack_index] < 0:
                self.curr_stack_pointer[stack_index] = None
            self.next_stack_pointer[stack_index] -= 3
            
        return result
        
            
        
        