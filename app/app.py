from pkg.Board import Board
from pkg.Player import Player
from pkg.Homepage import Homepage
from pkg.Game import Game

while True:
    Homepage.show_homepage()
    choice = input("\nWhat's next? ")
    is_numeric_input = Game.is_float(choice)
    if is_numeric_input == False:
        print("Not a valid option. Select again. You can exit with 6.")
        continue

    if int(choice) == 1:
        print("Let's play! Please choose two players.")
        print("\n=== Player A ===")
        info_playerA = Homepage.choose_player()
        playerA = Player(info_playerA[0], info_playerA[1], info_playerA[2])
        print("\n=== Player B ===")
        info_playerB = Homepage.choose_player()
        
        while info_playerB[0] == info_playerA[0]:
            print(f"\nPlease select a DIFFERENT NAME for Player B! It cannot be the same as for Player A ('{info_playerA[0]}').\n")
            print("\n=== Player B ===")
            info_playerB = Homepage.choose_player()

        playerB = Player(info_playerB[0], info_playerB[1], info_playerB[2])

        print("\nThanks! Let's set up the board and start!")
        board = Board(playerA, playerB)
        game = Game(playerA, playerB, board)
        game.game_loop()

    elif int(choice) == 2:
        Homepage.show_highscores()
    elif int(choice) == 3:
        Homepage.show_rules()
    elif int(choice) == 4:
        print("Thanks for stopping by!")
        break
    else:
        print("That's not a valid option. Select 4 if you want to exit.")
        continue