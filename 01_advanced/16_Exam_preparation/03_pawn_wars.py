SIZE = 8

board = []

black_position = []
white_position = []

for index in range(SIZE):
    row = input().split()
    if "b" in row:
        black_position = [index, row.index("b")]
    if "w" in row:
        white_position = [index, row.index("w")]
    board.append(row)

if abs(black_position[1] - white_position[1]) == 1:
    place = (white_position[0] + black_position[0]) // 2
    # pieces can meet
    if white_position[0] % 2 == black_position[0] % 2:
        print(f"Game over! Black win, capture on {chr(97 + white_position[1])}{SIZE - place}.")
    else:
        print(f"Game over! White win, capture on {chr(97 + black_position[1])}{SIZE - place}.")
else:
    # pieces cannot meet
    if SIZE - white_position[0] - 1 <= black_position[0]:
        print(f"Game over! Black pawn is promoted to a queen at {chr(97 + black_position[1])}1.")
    else:
        print(f"Game over! White pawn is promoted to a queen at {chr(97 + white_position[1])}8.")
