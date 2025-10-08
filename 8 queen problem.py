def solve_queens(n):
    board = [-1] * n  
    def is_valid(row, col):
        for i in range(row):
            if board[i] == col or abs(row - i) == abs(col - board[i]):
                return False
        return True
    def backtrack(row):
        if row == n:
            print_board(board)
            return True
        for col in range(n):
            if is_valid(row, col):
                board[row] = col
                if backtrack(row + 1):
                    return True
                board[row] = -1
        return False

    def print_board(board):
        for row in range(n):
            line = ""
            for col in range(n):
                if board[row] == col:
                    line += "Q "
                else:
                    line += "- "
            print(line)

    backtrack(0)
solve_queens(8)
