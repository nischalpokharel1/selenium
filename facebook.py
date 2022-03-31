game_still_going = True
current_player = "X"
winner = None

board = ["_","_","_","_","_","_","_","_","_",]

def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

# display_board()

def play_game():
#  first display board 
    display_board()

    while game_still_going:
        handle_turn(current_player)

        check_if_game_over()

        flip_player()

    #check if winner
    if winner == "X" or winner == "O":
        print(winner + "Won..!!")
    elif winner == None:
        print("Its a Tie..!!")


def handle_turn(player):
    position = input("choose position between 1 to 9: ")
    position = int(position) - 1
    board[position] = "X"
    display_board()

def check_if_game_over():
    check_if_winner()
    check_if_tie()

def check_if_winner():
    global winner

    row_winner = check_row()
    column_winner = check_column()
    diagonal_winner = check_diagonal()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return

def check_row():
    global game_still_going
    row_1 = (board[0] == board[1] == board[2]) and board[0] != "-"
    row_2 = (board[3] == board[4] == board[5]) and board[3] != "-"
    row_3 = (board[6] == board[7] == board[8]) and board[6] != "-"

    print(row_1)
    print(row_2)
    print(row_3)
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_column():
    global game_still_going
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"

    if col_1 or col_2 or col_3:
        game_still_going = False
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    return


def check_diagonal():
    global game_still_going
    dia_1 = board[0] == board[4] == board[8] != "-"
    dia_2 = board[2] == board[4] == board[6] != "-"

    if dia_1 or dia_2:
        game_still_going = False
    if dia_1:
        return board[0]
    elif dia_2:
        return board[2]
    return





def check_if_tie():
    return

def flip_player():
    return

play_game()

    