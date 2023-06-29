def print_board(board):
    """
    Prints the Tic-Tac-Toe board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
def check_winner(board):
    """
    Checks if there is a winner.
    """
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None


def play_game():
    """
    Runs the Tic-Tac-Toe game.
    """
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    winner = None
    moves = 0

    while winner is None and moves < 9:
        print_board(board)

        print(f"Player {current_player}'s turn.")
        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))

        if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != " ":
            print("Invalid move. Try again.")
            continue

        board[row][col] = current_player
        moves += 1

        winner = check_winner(board)

        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

    print_board(board)

    if winner:
        print(f"Player {winner} wins!")
    else:
        print("It's a tie!")

play_game()
