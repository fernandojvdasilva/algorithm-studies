'''
Created on 7 de out de 2017

@author: fernando
'''

'''
Given a specific type of DAG that forms a pyramid (the links have up-down direction), in which the node labels are integer, find the path that has the maximum sum of node values. what is the time/space complexity of the algorithm? 

e.g: 
             3 
            / \ 
           9 4 
         / \ / \ 
        1 8 2 
      / \ / \ / \ 
    4  5  8   2 
answer: <3,9,8,8>, sum = 3+9+8+8=28
'''

class GraphNode:
    def __init__(self, label):
        self.val = -float('inf')
        self.predecessor = None
        self.label = label
        self.edges = []
    
    def add_edge(self, node):
        self.edges.append(GraphEdge(node, self.label))

    def calculate_path(self):
        if len(self.edges) == 0:
            self.val += self.label

        for e in self.edges:
            if e.node.val < self.val + e.weight:
                e.node.predecessor = self
                e.node.val =  self.val + e.weight
                e.node.calculate_path()    

    def get_leaves(self):
        result = []
        if len(self.edges) == 0:
            return [self]    
        for e in self.edges:
            result.extend(e.node.get_leaves())

        return result

class GraphEdge:
    def __init__(self, node, weight):
        self.node = node
        self.weight = weight
        
class PyramidGraph:
        def __init__(self):
            self.first_node = None        

        def get_max_leaf(self):
            if self.first_node is None:
                return None
            leaves = self.first_node.get_leaves()
            max_val = -float('inf')
            max_leaf = None
            for l in leaves:
                if l.val > max_val:
                    max_val = l.val
                    max_leaf = l
        
            return     max_leaf     
        
        
        def calculate_max_path(self):
            if self.first_node is None:
                return
            self.first_node.val = 0
            self.first_node.calculate_path()

        def get_max_path(self):
            if self.first_node is None:
                return None

            result = []
            
            self.calculate_max_path()
            max_leaf = self. get_max_leaf()
                        
            curr_node = max_leaf
            while curr_node != None:
                result.append(curr_node)
                curr_node = curr_node.predecessor
            
            result = result[::-1]

            return result

        def print_max_path(self):
            max_path = self.get_max_path()
            for node in max_path:
                print(node.label)   