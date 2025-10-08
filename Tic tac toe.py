
board = ['X','O','X',
         'O','X','X',
         ' ',' ','O']
def print_board():
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("-+-+-")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-+-+-")
    print(f"{board[6]}|{board[7]}|{board[8]}")

def is_victory(icon):
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    return any(all(board[i]==icon for i in combo) for combo in win_conditions)

print_board()

if is_victory('X'):
    print("X wins! 🎉")
elif is_victory('O'):
    print("O wins! 🎉")
else:
    print("It's a draw!")
