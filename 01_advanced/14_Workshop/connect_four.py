from collections import deque
import operator
from colorama import Fore


def print_board():
    print_board()


def place_circle():
    row = 0

    while row != ROWS and board[row][player_col] == "0":
        row += 1

    board[row - 1][player_col] = player_symbol

    return row - 1


def get_circle_count(row, col, dx, dy, operator_func):
    current_count = 0
    for i in range(1, 4):
        new_row = operator_func(row, dx * i)
        new_col = operator_func(col, dy * i)

        if not (0 <= new_row < ROWS and 0 <= new_col < COLS):
            break

        if board[new_row][new_col] != player_symbol:
            break

        current_count += 1

    return current_count


def check_win(row, col):
    for x, y in directions:
        count = get_circle_count(row, col, x, y, operator.add) + get_circle_count(row, col, x, y, operator.sub) + 1

        if count >= 4:
            return True

    if counter_for_draw == ROWS * COLS:
        print_board()
        print("DRAW !")
        raise SystemExit

    return False


ROWS, COLS = 6, 7
counter_for_draw = 0
board = [["0"] * COLS for row in range(ROWS)]

player_one_symbol = Fore.YELLOW + "1" + Fore.RESET
player_two_symbol = Fore.RED + "2" + Fore.RESET

turn = deque([[1, player_one_symbol], [2, player_two_symbol]])

win = False

directions = {
    (-1, 0),  # top
    (0, -1),  # left
    (-1, -1), # topleft
    (-1, 1),  # topright
}

while not win:
    [print(f"[{', '.join(row)}]") for row in board]

    player_number, player_symbol = turn[0]
    try:
        player_col = int(input(f"Player {player_number}, please choose a column: ")) - 1
    except ValueError:
        print(Fore.RED + f"Select a valid number in the range (1-{COLS})" + Fore.RESET)
        continue

    if not 0 <= player_col < COLS:
        print(Fore.RED + f"Select a valid number in the range (1-{COLS})" + Fore.RESET)
        continue

    if board[0][player_col] != "0":
        print(Fore.RED + "No empty spaces on that column available, choose another !" + Fore.RESET)
        continue

    row = place_circle()
    counter_for_draw += 1
    win = check_win(row, player_col)

    turn.rotate()


print_board()
print(f"Player {turn[1][0]} wins")
