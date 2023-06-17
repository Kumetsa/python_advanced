def check_valid_index(row, col):
    if 0 <= row < SIZE and 0 <= col < SIZE:
        return True
    return False


def player_position(matrix):
    for row in range(SIZE):
        if "A" in matrix[row]:
            return row, matrix[row].index("A")

    # return None


def move_player(direction, steps):

    curr_row, curr_col = player_position(matrix)
    new_row, new_col = curr_row, curr_col

    if direction == "left":
        new_row, new_col = curr_row, curr_col - steps
    elif direction == "right":
        new_row, new_col = curr_row, curr_col + steps
    elif direction == "up":
        new_row, new_col = curr_row - steps, curr_col
    elif direction == "down":
        new_row, new_col = curr_row + steps, curr_col

    if check_valid_index(new_row, new_col) and matrix[new_row][new_col] != "x":
        matrix[new_row][new_col] = "A"
        matrix[curr_row][curr_col] = "."


def shoot_target(direction):
    player_row, player_col = player_position(matrix)
    next_row, next_col = player_row + directions[direction][0], player_col + directions[direction][1]

    while check_valid_index(next_row, next_col):
        if matrix[next_row][next_col] == "x":
            matrix[next_row][next_col] = "."
            return next_row, next_col
        elif matrix[next_row][next_col] == ".":
            next_row += directions[direction][0]
            next_col += directions[direction][1]
    #     else:
    #         break
    #
    # return None


SIZE = 5

matrix = [[el for el in input().split()] for _ in range(SIZE)]
total_targets = sum(row.count("x") for row in matrix)


n_commands = int(input())

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

targets_shot = []

for _ in range(n_commands):
    command, *info = input().split()

    if command == "move":
        direction = info[0]
        steps = int(info[1])
        move_player(direction, steps)

    elif command == "shoot":
        direction = info[0]
        target = shoot_target(direction)
        if target:
            targets_shot.append(target)

    # print(*matrix, sep="\n")
    # print("New Matrix")

if total_targets > len(targets_shot):
    print(f"Training not completed! {total_targets - len(targets_shot)} targets left.")
else:
    print(f"Training completed! All {total_targets} targets hit.")


if targets_shot:
    for target in targets_shot:
        print(list(target))
