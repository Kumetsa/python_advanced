def check_next_position(direction, pos):
    row, col = pos
    new_row = row + directions[direction][0]
    new_col = col + directions[direction][1]

    return new_row, new_col


def check_valid_index(position, field):
    rows = len(field)
    cols = len(field[0])

    if 0 <= position[0] < rows and 0 <= position[1] < cols:
        return True
    return False


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

rows, cols = map(int, input().split(","))

mouse_position = tuple()

next_position = tuple()

cupboard = []

cheese_count = 0

for index in range(rows):
    row = input()
    if "M" in row:
        mouse_position = (index, row.index("M"))
    cheese_count += row.count("C")
    cupboard.append(list(row))

while True:
    command = input()
    if command == "danger":
        if cheese_count > 0:
            print("Mouse will come back later!")

        break

    next_position = check_next_position(command, mouse_position)

    if not check_valid_index(next_position, cupboard):
        print("No more cheese for tonight!")
        break

    if cupboard[next_position[0]][next_position[1]] == "@":
        continue

    elif cupboard[next_position[0]][next_position[1]] == "C":
        cheese_count -= 1
        cupboard[mouse_position[0]][mouse_position[1]] = "*"
        mouse_position = next_position
        cupboard[mouse_position[0]][mouse_position[1]] = "M"
        if cheese_count == 0:
            print("Happy mouse! All the cheese is eaten, good night!")
            break

    elif cupboard[next_position[0]][next_position[1]] == "T":
        cupboard[mouse_position[0]][mouse_position[1]] = "*"
        mouse_position = next_position
        cupboard[mouse_position[0]][mouse_position[1]] = "M"
        print("Mouse is trapped!")
        break

    elif cupboard[next_position[0]][next_position[1]] == "*":
        cupboard[mouse_position[0]][mouse_position[1]] = "*"
        mouse_position = next_position
        cupboard[mouse_position[0]][mouse_position[1]] = "M"

for row in cupboard:
    print(''.join(row))
