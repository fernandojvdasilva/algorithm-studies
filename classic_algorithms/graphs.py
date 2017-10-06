'''
Created on 4 de out de 2017

@author: fernando
'''
from platform import node

class GraphNode:
    
    def __init__(self):
        self.val = float('inf')
        self.edges = []
        self.evaluated = False
        self.predecessor = None

    def connect(self, node, weight):
        self.edges.append(GraphEdge(node, weight))


class GraphEdge:
    
    def __init__(self, node, weight):
        self.node = node
        self.weight = weight
        self.relaxed = False
        


def find_min_not_evaluated(graph):
    min = float('inf')
    result = None
    for v in graph:
        if not v.evaluated and v.val <= min:
            result = v
            min = v.val
    
    return result

def dijkstra_min_paths(graph):
    
    curr_node = graph[0] 
    
    curr_node.val = 0
    
    while curr_node != None:
        for e in curr_node.edges:
            if e.node.val > curr_node.val + e.weight:
                e.node.val = curr_node.val + e.weight                
                e.node.predecessor = curr_node
        
        curr_node.evaluated = True
        curr_node = find_min_not_evaluated(graph) 
        
        
def print_minimum_path(graph):
    result = ''
    for v in graph:
        if v.predecessor != None:
            result += "%d -> %d, " % (v.predecessor.val, v.val)        
        
    return result