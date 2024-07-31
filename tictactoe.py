import random

# Constants
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 5)

def check_winner(board, player):
    win_conditions = [
        # Horizontal
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        # Vertical
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        # Diagonal
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    return [player] * 3 in win_conditions

def is_board_full(board):
    return all(cell != EMPTY for row in board for cell in row)

def minimax(board, depth, is_maximizing):
    if check_winner(board, PLAYER_X):
        return 10 - depth
    if check_winner(board, PLAYER_O):
        return depth - 10
    if is_board_full(board):
        return 0
    
    if is_maximizing:
        best_score = -float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    board[row][col] = PLAYER_X
                    score = minimax(board, depth + 1, False)
                    board[row][col] = EMPTY
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    board[row][col] = PLAYER_O
                    score = minimax(board, depth + 1, True)
                    board[row][col] = EMPTY
                    best_score = min(score, best_score)
        return best_score

def find_best_move(board):
    best_score = -float('inf')
    best_move = (-1, -1)
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                board[row][col] = PLAYER_X
                score = minimax(board, 0, False)
                board[row][col] = EMPTY
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    return best_move

def play_game():
    board = [[EMPTY] * 3 for _ in range(3)]
    current_player = PLAYER_O  # Human starts first

    while True:
        print_board(board)
        
        if current_player == PLAYER_X:
            row, col = find_best_move(board)
            board[row][col] = PLAYER_X
        else:
            while True:
                try:
                    row = int(input("Enter row (0, 1, 2): "))
                    col = int(input("Enter column (0, 1, 2): "))
                    if board[row][col] == EMPTY:
                        board[row][col] = PLAYER_O
                        break
                    else:
                        print("Cell is already taken, choose another one.")
                except (ValueError, IndexError):
                    print("Invalid input, try again.")

        if check_winner(board, PLAYER_X):
            print_board(board)
            print("AI (X) wins!")
            break
        elif check_winner(board, PLAYER_O):
            print_board(board)
            print("You (O) win!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = PLAYER_X if current_player == PLAYER_O else PLAYER_O

if __name__ == "__main__":
    play_game()
