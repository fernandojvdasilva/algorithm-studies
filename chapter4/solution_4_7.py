'''
Created on 25 de nov de 2021

@author: fernando
'''

'''
You are given a list of projects and a list of dependencies (which is a list of pairs of
projects, where the second project is dependent on the first project). All of a project's dependencies
must be built before the project is. Find a build order that will allow the projects to be built. If there
is no valid build order, return an error.
EXAMPLE
Input:
projects: a, b, c, d, e, f
dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
Output: f, e, a, b, d, c

our answer (also valid): e f b d c a


|-- a <---|
v         |
d <- b <- f
|
v
c     e


f b d c a e


   a b c d e f
a  0 0 0 0 0 1
b  0 0 0 0 0 1
c  0 0 1 0 0 0  
d  1 1 0 0 0 0
e  0 0 0 0 0 0
f  0 0 0 0 0 0



'''

class GraphNode:

    def __init__(self, val):
        self.val = val
        self.edges = []
        self.visited = False

class GraphEdge:
    def __init__(self, node):
        self.node = node


def dfs_print(node):
    if not node.visited:
        print(node.val)
        node.visited = True

    for e in node.edges:
        dfs_print(e.node)


def find_build_order(projects, deps):    
    nodes = {p: GraphNode(p) for p in projects}
    first_node = [nodes[k] for k in nodes.keys()]

    for d in deps:
        nodes[d[0]].edges.append(GraphEdge(nodes[d[1]]))
        if nodes[d[1]] in first_node:
            first_node.remove(nodes[d[1]])

    if len(first_node) == 0:
        print("Error: no valid order")
        return
    
    for n in first_node:
        dfs_print(n)

