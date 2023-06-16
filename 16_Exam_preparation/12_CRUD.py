import ast


def calculate_next_nposition(pos, direction):
    row, col = pos
    new_row = row + directions[direction][0]
    new_col = col + directions[direction][1]

    return new_row, new_col


SIZE = 6

matrix = [input().split() for row in range(SIZE)]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

starting_position = input()
position = ast.literal_eval(starting_position)

while True:
    line = input()
    if line == "Stop":
        break

    command, *args = line.split(", ")

    direction = args[0]
    position = calculate_next_nposition(position, direction)

    if command == "Create":
        value =  args[1]
        if matrix[position[0]][position[1]] == ".":
            matrix[position[0]][position[1]] = value

    elif command == "Update":
        value = args[1]
        if matrix[position[0]][position[1]] != ".":
            matrix[position[0]][position[1]] = value

    elif command == "Delete":
        if matrix[position[0]][position[1]] != ".":
            matrix[position[0]][position[1]] = "."

    elif command == "Read":
        if matrix[position[0]][position[1]] != ".":
            print(matrix[position[0]][position[1]])


for row in matrix:
    print(' '.join(row))

