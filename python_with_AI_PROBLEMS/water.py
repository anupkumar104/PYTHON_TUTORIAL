from collections import deque

def get_next_states(x, y, max_x=3, max_y=5):
    states = []
    states.append((max_x, y))
    states.append((x, max_y))
    states.append((0, y))
    states.append((x, 0))
    transfer = min(x, max_y - y)
    states.append((x - transfer, y + transfer))
    transfer = min(y, max_x - x)
    states.append((x + transfer, y - transfer))

    return states

def water_jug_bfs(max_x, max_y, target):
    start = (0, 0)
    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        (x, y), path = queue.popleft()
        
        if x == target or y == target:
            return path
 
        for next_state in get_next_states(x, y, max_x, max_y):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [next_state]))

    return None


result = water_jug_bfs(3,5,4)
if result:
    print("Solution found:")
    for step in result:
        print(step)
else:
    print("No solution found.")