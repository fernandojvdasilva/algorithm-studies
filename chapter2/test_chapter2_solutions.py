'''
Created on 2 de out de 2017

@author: fernando
'''
import unittest


from chapter2.solution_2_1 import remove_duplicates, Node

class Test(unittest.TestCase):



    def check_repeated(self, linked_list):
        val_hash = set()
        curr_node = linked_list
        repeated = False
        while curr_node != None:
            if curr_node.val in val_hash:
                repeated = True
                break
            else:
                val_hash.add(curr_node.val)
                curr_node = curr_node.next
        
        assert(not repeated)

    def testSolution2_1(self):
        
        linked_list = Node(2)
        linked_list.next = Node(1)
        linked_list.next.next = Node(2)
        linked_list.next.next.next = Node(3)
         
        
        remove_duplicates(linked_list)
        
        self.check_repeated(linked_list)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSolution2_1']
    unittest.main()