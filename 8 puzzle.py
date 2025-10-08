# 8 Puzzle Game (Beginner Version without classes)

# Goal state
goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]  # 0 = blank space

# Print the puzzle
def print_puzzle(puzzle):
    for row in puzzle:
        print(" ".join(str(x) if x != 0 else "_" for x in row))
    print()

# Find blank (0) position
def find_blank(puzzle):
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == 0:
                return i, j

# Move the blank tile
def move(puzzle, direction):
    x, y = find_blank(puzzle)

    if direction == "up" and x > 0:
        puzzle[x][y], puzzle[x-1][y] = puzzle[x-1][y], puzzle[x][y]
    elif direction == "down" and x < 2:
        puzzle[x][y], puzzle[x+1][y] = puzzle[x+1][y], puzzle[x][y]
    elif direction == "left" and y > 0:
        puzzle[x][y], puzzle[x][y-1] = puzzle[x][y-1], puzzle[x][y]
    elif direction == "right" and y < 2:
        puzzle[x][y], puzzle[x][y+1] = puzzle[x][y+1], puzzle[x][y]
    else:
        print("Invalid move!")

# ===== Main Program =====
puzzle = [[1, 2, 3],
          [4, 0, 6],
          [7, 5, 8]]  # Example starting state

print("Welcome to the 8 Puzzle Game!")
print("Use commands: up, down, left, right")
print("Goal is:")
print_puzzle(goal_state)

# Play until solved
while puzzle != goal_state:
    print("Current puzzle:")
    print_puzzle(puzzle)
    move_dir = input("Enter move (up/down/left/right): ").lower()
    move(puzzle, move_dir)

print("🎉 Congratulations! You solved the puzzle!")
