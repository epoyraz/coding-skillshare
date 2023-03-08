def draw_board(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-+-+-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-+-+-")
    print(board[6] + "|" + board[7] + "|" + board[8])

def check_win(board):
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != " ":
            return True
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != " ":
            return True
    if board[0] == board[4] == board[8] != " " or \
       board[2] == board[4] == board[6] != " ":
        return True
    return False

def tic_tac_toe():
    board = [" "] * 9
    player = "X"
    game_over = False

    while not game_over:
        draw_board(board)
        print("It's your turn, " + player)
        move = int(input("Enter a position (1-9): ")) - 1
        if board[move] == " ":
            board[move] = player
            if check_win(board):
                draw_board(board)
                print(player + " wins!")
                game_over = True
            elif " " not in board:
                draw_board(board)
                print("It's a tie!")
                game_over = True
            else:
                player = "O" if player == "X" else "X"
        else:
            print("That position is already taken. Try again.")

tic_tac_toe()
