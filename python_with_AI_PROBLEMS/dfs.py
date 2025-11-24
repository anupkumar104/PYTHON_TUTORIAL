# Objective: Write a python program to implement depth First Search Traversal.
from collections import deque
def dfs(graph,start_node):
    visited= set()
    stack= deque([start_node])
    traversal=[]
    while(stack):
        node=stack.pop()
        if node not in visited:
            visited.add(node)
            traversal.append(node)
            for n in  reversed(graph.get(node,[])):
                if n not in visited:
                    stack.append(n)
    return traversal   
graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[]
}
result=dfs(graph,'A')
print("dfs traversal is :",result)

