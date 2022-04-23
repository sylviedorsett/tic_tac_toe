""" 
    Tic Tac Toe Game
    By Sylvie Dorsett
"""
from board_function import print_board
from game_play import play, change_turn
from check_for_winner import check_winner

def main():
    """
        A program that initiates and displays a tic-tac-toe game board for the user.
        Two users take turns picking a number square 1-9.
        After selecting a square the program displays an updated board with either 'X' or 'O' in the spot selected.
        The program checks to see if either user has completed three in a row to win the game.
    """
    print("Welcome to Tic-Tac-Toe.")
    
    play_again = "Yes"
    turn = "O"

    while play_again.lower() == "yes":
        board_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        turn = change_turn(turn)
        winner = False
        count = 0
        print_board(board_list)

        for i in range(9):
            if count < 8:
                board_list = play(board_list, turn)
                winner = check_winner(board_list, winner)
                #if there is a winner, print congrats and ask to play again
                if winner:
                    print(f"Congratulations! {turn}'s win!")
                    play_again = input("Would you like to play again? 'Yes' or 'No': ")
                    break

            elif not winner and count == 8:
                board_list = play(board_list, turn)
                print("It's a tie!")
                play_again = input("Would you like to play again? 'Yes' or 'No': ")
                break

            count += 1
            turn = change_turn(turn)

    print()
    print("Thank you for playing. Goodbye.")

if __name__ == "__main__":
    main()