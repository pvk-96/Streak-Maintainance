# --- Tic-Tac-Toe Game ---
# --- By pvk-96 ---
board = [' ' for x in range(10)]

def print_board(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def is_space_free(board, position):
    return board[position] == ' '

def insert_letter(letter, position):
    board[position] = letter

# 5. Function to Check for a Win
def check_win(board, letter):
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or 
            (board[4] == letter and board[5] == letter and board[6] == letter) or 
            (board[1] == letter and board[2] == letter and board[3] == letter) or 
            (board[1] == letter and board[4] == letter and board[7] == letter) or 
            (board[2] == letter and board[5] == letter and board[8] == letter) or 
            (board[3] == letter and board[6] == letter and board[9] == letter) or 
            (board[1] == letter and board[5] == letter and board[9] == letter) or 
            (board[3] == letter and board[5] == letter and board[7] == letter)) 

def is_board_full(board):
    for i in range(1, 10):
        if is_space_free(board, i):
            return False
    return True

def play_game():
    print('Welcome to Tic Tac Toe!')
    print('Use numbers 1-9 to select your move:')
    print(' 1 | 2 | 3')
    print('-----------')
    print(' 4 | 5 | 6')
    print('-----------')
    print(' 7 | 8 | 9')
    print('\n')

    # Reset the board for a new game
    global board
    board = [' ' for x in range(10)]
    print_board(board)

    player_turn = 'X' # 'X' goes first

    while not is_board_full(board):
        if player_turn == 'X':
            print(f"It's {player_turn}'s turn.")
            try:
                move = int(input('Enter your move (1-9): '))
            except ValueError:
                print('Invalid input. Please enter a number between 1 and 9.')
                continue 

            if move >= 1 and move <= 9:
                if is_space_free(board, move):
                    insert_letter('X', move)
                    if check_win(board, 'X'):
                        print_board(board)
                        print('X wins!')
                        break
                    player_turn = 'O' 
                else:
                    print('This position is already taken! Choose another.')
            else:
                print('Invalid move. Please enter a number between 1 and 9.')
        else: 
            print(f"It's {player_turn}'s turn.")
            try:
                move = int(input('Enter your move (1-9): '))
            except ValueError:
                print('Invalid input. Please enter a number between 1 and 9.')
                continue 

            if move >= 1 and move <= 9:
                if is_space_free(board, move):
                    insert_letter('O', move)
                    if check_win(board, 'O'):
                        print_board(board)
                        print('O wins!')
                        break
                    player_turn = 'X'
                else:
                    print('This position is already taken! Choose another.')
            else:
                print('Invalid move. Please enter a number between 1 and 9.')
        
        print_board(board) 
    else: 
        if not check_win(board, 'X') and not check_win(board, 'O'):
            print('It\'s a Draw!')

# --- Game Start ---
if __name__ == "__main__":
    while True:
        play_game()
        answer = input('Do you want to play again? (yes/no): ').lower()
        if answer != 'yes' or 'y':
            break

