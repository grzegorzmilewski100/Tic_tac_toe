from board import Board
from player import Player


class TicTacToe:

    def start(self):
        print("***************")
        print("Welcome Tic-Tac_Toe")
        print("***************")


        board = Board()
        player = Player()
        computer = Player(False)

        board.print_board()
        # Ask user if user would like to play another round
        while True:
            # Main Game, get move, check tie, check game over
            while True:

                player_move = player.get_move()
                board.submit_move(player, player_move)
                board.print_board()

                if board.check_is_tie():
                    print("It's tie!!. Try again")
                elif board.check_is_game_over(player, player_move):
                    print("You won the game!")
                    break
                else:
                    computer_move = computer.get_move()
                    board.submit_move(computer, computer_move)
                    board.print_board()

                    if board.check_is_game_over(computer, computer_move):
                        print("You lost the game! ")
                        break

            play_again = input("Would you like to play again?. Enter X for yes or O for no\n").upper()
            if play_again == "O":
                print("Thank you for the game. Bye")
                break
            elif play_again == "X":
                self.start_new_round(board)
            else:
                print("Your input is not a valid but you probably to play again")
                self.start_new_round(board)

    def start_new_round(self, board):
        print("*****************")
        print(" NEW ROUND ")
        print("*****************")
        board.reset_board()
        board.print_board()

game = TicTacToe()
game.start()

