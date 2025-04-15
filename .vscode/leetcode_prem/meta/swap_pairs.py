'''
24. Swap Nodes in Pairs
Solved
Medium
Topics
Companies
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

Example 1:

Input: head = [1,2,3,4]

Output: [2,1,4,3]

Explanation:



Example 2:

Input: head = []

Output: []

Example 3:

Input: head = [1]

Output: [1]

Example 4:

Input: head = [1,2,3]

Output: [2,1,3]

 

Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def swap_list(self, node: ListNode, prev_node: ListNode=None) -> ListNode:
        if node is None:
            return None
        else:
            
            if prev_node != None:                
                prev_node.next = node.next
                node.next = prev_node
                next_node = self.swap_list(prev_node.next, None)
                prev_node.next = next_node

                return node
            else:
                next_node = self.swap_list(node.next, node)

                if next_node is None:
                    return node
                else:
                    return next_node
                



    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = self.swap_list(head, None)

        return head