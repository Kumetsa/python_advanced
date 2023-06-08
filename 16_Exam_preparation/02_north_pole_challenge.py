def check_valid_index(position):
    if 0 <= position[0] < rows and 0 <= position[1] < cols:
        return True
    return False


def move_player(direction, directions, player_row, player_col):
    next_position = (player_row + directions[direction][0], player_col + directions[direction][1])

    return next_position


rows, cols = map(int, input().split(", "))

player_row, player_col = None, None

elements_collected = {
    "D": 0,
    "G": 0,
    "C": 0,
}

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

workshop = []
for row in range(rows):
    col = []
    for el in input().split():
        if el == "Y":
            player_row, player_col = row, el.index("Y")
        col.append(el)
    workshop.append(col)

while True:
    command_arg = input().split("-")
    if command_arg[0] == "End":
        break

    direction, steps = command_arg[0], int(command_arg[1])
    for _ in range(steps):
        next_position = move_player(direction, directions, player_row, player_col)
        if check_valid_index(next_position):
            if workshop[next_position[0]][next_position[1]] in elements_collected:
                elements_collected[workshop[next_position[0]][next_position[1]]] += 1
            workshop[next_position[0]][next_position[1]] = "Y"
            workshop[player_row][player_col] = "x"
        else:
            if direction == "up":
                next_position = rows - 1, player_col
            elif direction == "down":
                next_position = 0, player_col
            elif direction == "left":
                next_position = player_row, cols - 1
            elif direction == "right":
                next_position = player_row, 0

            if workshop[next_position[0]][next_position[1]] in elements_collected:
                elements_collected[workshop[next_position[0]][next_position[1]]] += 1
            workshop[next_position[0]][next_position[1]] = "Y"
            workshop[player_row][player_col] = "x"

        player_row, player_col = next_position

# TODO да сложа функционалност която да спира играта ако събера всичко, без следващ ход
# TODO проверка на логиката за излизане от матрицата ако са само 2 колони


print(*workshop, sep="\n")
print(elements_collected)
