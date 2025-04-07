'''
Add Two Numbers
Solved
Medium
Topics
Companies
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def getNumber(self, node: ListNode, factor: int=1):
        res = None

        if node is None:
            return 0

        else:
            if factor > self.max_factor:
                self.max_factor = factor

            res =  node.val * factor + self.getNumber(node.next, factor * 10)

        return res


    def numToList(self, num: int) -> Optional[ListNode]:
        factor = self.max_factor

        num_stack = []
        curr_num = num
        while factor > 0:
            num_stack.append(curr_num // factor)
            curr_num = curr_num % factor
            factor //= 10

        curr_node = None
        first_node = None
        while len(num_stack) > 0:
            if curr_node != None:
                curr_node.next = ListNode(num_stack.pop(), None)
                curr_node = curr_node.next
            else:
                curr_node = ListNode(num_stack.pop(), None)
                first_node = curr_node

        return first_node




    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        l1_node = l1
        l2_node = l2

        res = None
        res_node = None

        residual = 0

        while l1_node != None or l2_node != None or residual != 0:
            
            val = residual

            if l1_node != None:
                val += l1_node.val
                l1_node = l1_node.next

            if l2_node != None:
                val += l2_node.val
                l2_node = l2_node.next

            if val > 9:
                residual = 1
                val = val - 10
            else:
                residual = 0

            if res_node is None:
                res_node = ListNode(val, None)
                if res is None:
                    res = res_node                    
            else:
                res_node.next = ListNode(val, None)
                res_node = res_node.next

        return res




        '''self.max_factor = 1
        num = self.getNumber(l1, 1) 
        
        max_factor_l1 = self.max_factor
        self.max_factor = 1

        num += self.getNumber(l2, 1)
        max_factor_l2 = self.max_factor

        self.max_factor = '''
        


        return self.numToList(num)