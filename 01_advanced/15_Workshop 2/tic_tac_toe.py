from collections import deque
from pyfiglet import Figlet
import speech_recognition as sr


def get_name(player_number):
    while True:
        with sr.Microphone() as source:
            r = sr.Recognizer()
            print(f"{player_number} please say your name: ")

            audio = r.record(source, duration=3)
            print("Recognizing...")

            try:
                return r.recognize_google(audio)
            except sr.exceptions.UnknownValueError:
                print("Please say your name again.")


def check_for_win():
    player_name, player_symbol = players[0]

    first_diagonal_win = all(board[i][i] == player_symbol for i in range(SIZE))
    second_diagonal_win = all(board[i][SIZE - i - 1] == player_symbol for i in range(SIZE))

    row_win = any([all(player_symbol == pos for pos in row) for row in board])
    col_win = any([all(board[r][c] == player_symbol for r in range(SIZE)) for c in range(SIZE)])

    if any([first_diagonal_win, second_diagonal_win, row_win, col_win]):
        print_board()
        print(f"{player_name} won !")

        raise SystemExit


def place_symbol(row, col):
    board[row][col] = players[0][1]

    check_for_win()
    print_board()

    if turns == SIZE * SIZE:
        print("Draw !")

        raise SystemExit

    players.rotate()


def print_board(begin=False):
    figlet = Figlet(font="big")
    print(figlet.renderText("Tic-Tac_Toe"))

    if begin:
        print("This is the numeration of the board:")
        [print(f"| {' | '.join(row)} |") for row in board]

        for row in range(SIZE):
            for col in range(SIZE):
                board[row][col] = " "
    else:
        [print(f"| {' | '.join(row)}") for row in board]


def choose_position():
    global turns
    while True:
        try:
            position = int(input(f"{players[0][0]} choose a free position in range from 1 to {SIZE * SIZE}."))
            row, col = (position - 1) // SIZE, (position - 1) % SIZE
        except ValueError:
            print(f"{players[0][0]} please select valid position")
            continue

        if 1 <= position <= SIZE * SIZE and board[row][col] == " ":
            place_symbol(row, col)
            turns += 1
        else:
            print(f"{players[0][0]} please select valid position")


def start():
    player_one_name = get_name("one")  #input("Player one please enter your name: ")
    player_two_name = get_name("two")  #input("Player two please enter your name: ")

    while True:
        player_one_symbol = input(f"{player_one_name} would you like to play with X or O ?").upper()

        if player_one_symbol not in ["X", "O"]:
            print(f"{player_one_name} please select valid option !")
        else:
            break
    player_two_symbol = "O" if player_one_symbol == "X" else "O"

    players.append([player_one_name, player_one_symbol])
    players.append([player_two_name, player_two_symbol])

    print_board(begin=True)
    choose_position()


SIZE = 3
turns = 0

board = [[str(i), str(i + 1), str(i + 2)] for i in range(1, SIZE * SIZE + 1, SIZE)]
players = deque()

# print(*board, sep="\n")
start()
