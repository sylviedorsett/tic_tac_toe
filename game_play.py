from board_function import print_board
from update_tic_tac_toe_list import update_board

def play(board_list, turn):
    if turn == "X":
        x = int(input("X's turn to choose a square (1-9): "))
        board_list = update_board("X", x, board_list)
        print_board(board_list)     
    else:
        o = int(input("O's turn to choose a square (1-9): "))
        board_list = update_board("O", o, board_list)
        print_board(board_list)        
        
    return board_list


def change_turn(turn):
    if turn == "X":
        turn = "O"
    else:
        turn = "X"

    return turn
            