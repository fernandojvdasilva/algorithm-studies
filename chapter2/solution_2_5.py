'''
Created on 2 de out de 2017

@author: fernando
'''

'''
Given a circular linked list, implement an algorithm which returns node at the begin-
ning of the loop.

DEFINITION
Circular linked list: A (corrupt) linked list in which a node’s next pointer points to an
earlier node, so as to make a loop in the linked list.

EXAMPLE
input: A -> B -> C -> D -> E -> C [the same C as earlier]
output: C

'''

''' This first solution uses a O(n) space '''
def detect_loop(linked_list):
    pointed_nodes = set()
    
    curr_node = linked_list
    while curr_node != None and not curr_node in pointed_nodes:
        pointed_nodes.add(curr_node)
        curr_node = curr_node.next
        
    return curr_node    

''' This is the solution from the book: uses 2 pointers, one stepping one node at the time and another
at 2 nodes at the time. In an ordinary loop, they will meet when p1 does 1 lap while p2 does 2. As
we have k nodes before the loop, they will meet when p1 does 1 lap - k nodes and p2 does 2 laps - k nodes.
So we just reset p1 to the head and step both at one node at the time until they meet at the start of 
the loop.
'''
def detect_loop_no_space(linked_list):
    curr_node1 = linked_list
    curr_node2 = linked_list
    
    result = None
    
    while curr_node2 != None and curr_node1 != curr_node2:
        curr_node1 = curr_node1.next
        if curr_node2.next != None:
            curr_node2 = curr_node2.next.next
        else:
            break

    
    if curr_node1 == curr_node2:
        curr_node1 = linked_list
        
        while curr_node1 != curr_node2:
            curr_node1 = curr_node1.next
            curr_node2 = curr_node2.next

        result = curr_node1
        
    return result
