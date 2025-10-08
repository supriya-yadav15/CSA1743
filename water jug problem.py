from collections import deque

def water_jug_problem(jug1, jug2, target):
    visited = set()
    queue = deque()
    queue.append((0, 0, []))
    while queue:
        a, b, steps = queue.popleft()
        if (a, b) in visited:
            continue
        visited.add((a, b))
        if a == target or b == target:
            steps.append((a, b))
            return steps
        queue.append((jug1, b, steps + [(jug1, b)]))  
        queue.append((a, jug2, steps + [(a, jug2)]))  
        queue.append((0, b, steps + [(0, b)]))        
        queue.append((a, 0, steps + [(a, 0)]))        
        pour = min(a, jug2 - b)
        queue.append((a - pour, b + pour, steps + [(a - pour, b + pour)]))
        pour = min(b, jug1 - a)
        queue.append((a + pour, b - pour, steps + [(a + pour, b - pour)]))

    return None
steps = water_jug_problem(4, 3, 2)
if steps:
    for state in steps:
        print(f"Jug1: {state[0]}L, Jug2: {state[1]}L")
    print("Done.")
else:
    print("No solution found.")
