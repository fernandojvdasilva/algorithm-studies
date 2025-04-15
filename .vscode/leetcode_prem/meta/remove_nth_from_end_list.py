'''
19. Remove Nth Node From End of List
Solved
Medium
Topics
Companies
Hint
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def find(self, node: ListNode, n: int) -> int:
        if node is None:
            return 0
        else:
            count = self.find(node.next, n) + 1

            if count == n+1:
                node.next = self.next_node
                self.next_node = None
            

            elif count == n:
                self.next_node = node.next

            return count



    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        self.next_node = None

        count = self.find(head, n)

        if n == count:
            return self.next_node

        return head