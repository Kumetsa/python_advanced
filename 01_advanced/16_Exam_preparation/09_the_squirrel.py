from collections import deque


def check_valid_index(position, field):
    rows = len(field)
    cols = len(field[0])

    if 0 <= position[0] < rows and 0 <= position[1] < cols:
        return True
    return False


def calculate_position(squir_pos, direction):
    row, col = squir_pos
    new_row = row + directions[direction][0]
    new_col = col + directions[direction][1]

    return new_row, new_col


size = int(input())

commands = deque(input().split(", "))

squirrel_position = ()

field = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

hazelnut_count = 0

activated_trap = False
left_field = False

for index in range(size):
    field_row = [el for el in input()]
    if "s" in field_row:
        squirrel_position = (index, field_row.index("s"))
    field.append(field_row)

while commands and hazelnut_count < 3:
    direction = commands.popleft()
    next_position = calculate_position(squirrel_position, direction)

    if not check_valid_index(next_position, field):
        left_field = True
        break

    elif field[next_position[0]][next_position[1]] == "t":
        activated_trap = True
        break

    elif field[next_position[0]][next_position[1]] == "h":
        hazelnut_count += 1
        field[squirrel_position[0]][squirrel_position[1]] = "*"
        field[next_position[0]][next_position[1]] = "s"
        squirrel_position = next_position

    elif field[next_position[0]][next_position[1]] == "*":
        field[squirrel_position[0]][squirrel_position[1]] = "*"
        field[next_position[0]][next_position[1]] = "s"
        squirrel_position = next_position


if left_field:
    print("The squirrel is out of the field.")
elif activated_trap:
    print("Unfortunately, the squirrel stepped on a trap...")
elif hazelnut_count < 3:
    print("There are more hazelnuts to collect.")
elif hazelnut_count == 3:
    print("Good job! You have collected all hazelnuts!")

print(f"Hazelnuts collected: {hazelnut_count}")
