# Objective: Write a python program to implement Breadth First Search Traversal.
from collections import deque
def bfs(graph,start_node):
    visited= set()
    queue= deque([start_node])
    traversal=[]
    while(queue):
        node=queue.popleft()
        if node not in visited:
            visited.add(node)
            traversal.append(node)
            for n in graph [node]:
                if n not in visited:
                    queue.append(n)
    return traversal 
graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[]
}
result=bfs(graph,'A')
print("bfs traversal is :",result)

