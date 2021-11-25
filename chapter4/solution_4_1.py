'''
Created on 24 de nov de 2021

@author: fernando
'''

'''
 Given a directed graph, design an algorithm to find out whether there is a
route between two nodes.

'''
class GraphNode:

    def __init__(self):
        self.edges = []        


class GraphEdge:
    def __init__(self, node):
        self.node = node
        self.visited = False


def depth_first_search(src, dst):
    if src == dst:
        return True

    found = False
    for e in src.edges:
        if not e.visited:
            found = found or depth_first_search(e.node, dst)
            if found:
                break
            else:
                e.visited = True

    return found



def find_path(node1, node2):
    return depth_first_search(node1, node2) or depth_first_search(node2, node1)