# function to print tic tac toe
def print_game(values):
    print("\n")
    print("\t    |    |")
    print("\t  {} |  {} |  {}".format(values[0], values[1], values[2]))
    print("\t____|____|____")

    print("\t    |    |")
    print("\t  {} |  {} |  {}".format(values[3], values[4], values[5]))
    print("\t____|____|____")

    print("\t    |    |")
    print("\t  {} |  {} |  {}".format(values[6], values[7], values[8]))
    print("\t____|____|____")


def check_win(player_position, current_player):
    possible_values = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for i in possible_values:
        if all(y in player_position[current_player] for y in i):
            return True
    return False


def check_draw(player_position):
    if len(player_position["X"]) + len(player_position["O"]) == 9:
        return True
    return False


def single_game(current_player):
    values = [" " for x in range(9) ]
    player_position = {"X": [], "O": []}

    while True:
        print_game(values=values)
        try:
            print("player",current_player,"turn. Which box?", end="")
            move= int(input())
        except ValueError:
            print("Wrong Input Try again!")
            continue

        if move<1 or move>9:
            print("wrong input try again!")
            continue

        if values[move-1] != " ":
            print("place already filled try again!")
            continue
        values[move-1] = current_player
        player_position[current_player].append(move)

        if check_win(player_position, current_player):
            print_game(values)
            print(f"player {current_player} won the game!")
            print("\n")
            return current_player

        if check_draw(player_position):
            print_game(values)
            print("game drawn")
            print("\n")
            return "D"

        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"


def print_scoreboard(score_board):
    print("--------------------------------")
    print("            SCOREBOARD       ")
    print("--------------------------------")

    players = list(score_board.keys())
    print("   ", players[0], "    ", score_board[players[0]])
    print("   ", players[1], "    ", score_board[players[1]])

    print("--------------------------------\n")


if __name__ == "__main__":
    print("player_1")
    player_1 = input("Enter name: ")
    print("\n")
    print("player_2")
    player_2 = input("Enter name: ")
    print("\n")

    current_player = player_1
    player_choice = {"X": " ", "O": " "}
    options = ["X", "O"]
    scoreboard = {player_1: 0, player_2: 0}

    while True:
        print(f"turn to choose for {current_player}")
        print("Enter 1 for X")
        print("Enter 2 for O")
        print("Enter 3 for exit")

        try:
            choice = int(input())
        except ValueError:
            print("please enter a valid number")

        if choice == 1:
            player_choice["X"] = current_player
            if current_player == player_1:
                player_choice["O"] = player_2
            else:
                player_choice["O"] = player_1

        elif choice == 2:
            player_choice["O"] = current_player
            if current_player == player_1:
                player_choice["X"] = player_2
            else:
                player_choice["X"] = player_1

        elif choice == 3:
            print("Final scores")
            print_scoreboard(scoreboard)
            break

        else:
            print("invalid choice try again \n")

        winner = single_game(options[choice-1])

        if winner != "D":
            player_won = player_choice[winner]
            scoreboard[player_won] = scoreboard[player_won]+1

        print_scoreboard(scoreboard)

        if current_player == player_1:
            current_player = player_2
        else:
            current_player= player_1










