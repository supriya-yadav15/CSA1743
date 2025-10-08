from typing import List, Tuple
from collections import deque

State = Tuple[int, int, int, int, int]

def is_valid_state(state: State) -> bool:
    m1, c1, m2, c2, boat = state
    if m1 < 0 or c1 < 0 or m2 < 0 or c2 < 0:
        return False
    if (m1 > 0 and m1 < c1):
        return False
    if (m2 > 0 and m2 < c2):
        return False
    return True

def get_successors(state: State) -> List[State]:
    m1, c1, m2, c2, boat = state
    successors = []
    moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]
    if boat == 1:
        for m, c in moves:
            new_state = (m1-m, c1-c, m2+m, c2+c, 0)
            if is_valid_state(new_state):
                successors.append(new_state)
    else:
        for m, c in moves:
            new_state = (m1+m, c1+c, m2-m, c2-c, 1)
            if is_valid_state(new_state):
                successors.append(new_state)
    return successors

def breadth_first_search() -> List[State]:
    initial_state = (3, 3, 0, 0, 1)
    goal_state = (0, 0, 3, 3, 0)
    visited = set()
    queue = deque([(initial_state, [])])
    while queue:
        state, path = queue.popleft()
        if state == goal_state:
            return path + [state]
        if state in visited:
            continue
        visited.add(state)
        for successor in get_successors(state):
            if successor not in visited:
                queue.append((successor, path + [state]))
    return []

if __name__ == "__main__":
    solution = breadth_first_search()
    for step, state in enumerate(solution):
        print(f"Step {step}: {state}")
