from typing import List, Tuple

def is_clean(grid: List[List[int]]) -> bool:
    return all(all(cell == 0 for cell in row) for row in grid)

def get_successors(pos: Tuple[int, int], grid: List[List[int]]) -> List[Tuple[Tuple[int,int], List[List[int]]]]:
    x, y = pos
    moves = [(0,1),(0,-1),(1,0),(-1,0)]
    successors = []
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            new_grid = [row[:] for row in grid]
            if new_grid[nx][ny] == 1:   
                new_grid[nx][ny] = 0
            successors.append(((nx, ny), new_grid))
    return successors

def dfs(pos: Tuple[int,int], grid: List[List[int]], visited: set) -> bool:
    if is_clean(grid):
        return True
    state = (pos, tuple(tuple(row) for row in grid))  
    if state in visited:
        return False
    visited.add(state)
    for nxt_pos, nxt_grid in get_successors(pos, grid):
        if dfs(nxt_pos, nxt_grid, visited):
            return True
    return False

if __name__ == "__main__":
    grid = [
        [0,1,1,1],
        [0,0,1,0],
        [1,0,0,1],
        [1,1,1,0]
    ]
    start = (0,0)
    if dfs(start, grid, set()):
        print("The room can be cleaned.")
    else:
        print("The room cannot be cleaned.")
