'''
Created on 1 de out de 2017

@author: fernando
'''


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
                

'''
Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?

'''
def remove_duplicates(linked_list):
    
    curr_node = linked_list
    while curr_node != None:
        prev_node = curr_node
        curr_node2 = curr_node.next
        while curr_node2 != None:
            if curr_node2.val == curr_node.val:
                prev_node.next = curr_node2.next
            else:
                prev_node = curr_node2
            curr_node2 = curr_node2.next
        curr_node = curr_node.next
        