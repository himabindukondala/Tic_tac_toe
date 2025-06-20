
print("Welcome to Tic-Tac-Toe!")
board = [[" " for _ in range(3)] for _ in range(3)]
player = "X"

def show_board():
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def game_over():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    for row in board:
        for cell in row:
            if cell == " ":
                return None
    return "Draw"

show_board()

while True:
    try:
        move = input(f"Player {player}, enter your move (row and column from 1-3, e.g. 1 3): ")
        r, c = map(int, move.split())
        r -= 1
        c -= 1
        if board[r][c] != " ":
            print("That spot is already taken. Try again.")
            continue
        board[r][c] = player
        show_board()
        result = game_over()
        if result == "X" or result == "O":
            print(f"Player {result} wins!")
            break
        elif result == "Draw":
            print("It's a draw!")
            break
        player = "O" if player == "X" else "X"
    except:
        print("Invalid input. Please enter row and column numbers between 1 and 3.")
