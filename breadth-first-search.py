#file = open("C:\Users\islam\Desktop\Books\large.graph", "r")
# WIP breadth-search algorithm
from queue import Queue
import math


# Using dictionaries for majority of the variables due to dictionaries taking up less space and time than lists, and is
# faster due to hash tables.

graph = {
    'A':['B','D'],
    'B':['A','C'],
    'C':['B']
}
graph = open(r"C:\Users\islam\Desktop\Books\large.txt", "r") # Original graph, set in dictionary format
Q = Queue() # Queue time
inf = math.inf # Initializing by infinity
output = []

color = {} # the nodes that were already inspected
d = {}
parent = {}

def BFS(G, s):
    
    for u in graph.keys():       # for loop iterates through the dict keys 
        color[u] = False         # False means white node, which is not inspected yet
        d[u] = inf               # Initialize by infinity
        parent[u] = None         # parent of initialize node
    color[s] = True              # initial node now has been inspected (gray)
    d[s] = 0                     
    parent[s] = None             # parent node initially has no color
    Q.put(s)                     # puts it in queue
    
    while not Q.empty():
        u = Q.get()              # since using dict, .get is used to get the element instead of .pop, which is for lists
        #output.append(u)         # Code follows the pseudocode given
        for v in graph[u]:       
            if color[v]==False:
                color[v]=True
                d[v] = d[u]+1 
                parent[v] = u
                Q.put(v)