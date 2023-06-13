from collections import deque


def sufficient_materials(mats):
    for value in mats.values():
        if value < 1:
            return False
    return True


def move(r_position, direction):
    row, col = r_position

    if direction == "up":
        row -= 1
        if row < 0:
            row = SIZE - 1
    elif direction == "down":
        row += 1
        if row > SIZE - 1:
            row = 0
    elif direction == "left":
        col -= 1
        if col < 0:
            col = SIZE - 1
    elif direction == "right":
        col += 1
        if col > SIZE - 1:
            col = 0

    return row, col


SIZE = 6

field = []

rover_position = ()

mats_collected = {
    "W": 0,
    "M": 0,
    "C": 0
}

for index in range(SIZE):
    row = input().split()
    if "E" in row:
        rover_position = (index, row.index("E"))
    field.append(row)

commands = deque(input().split(", "))

for _ in range(len(commands)):
    current_command = commands.popleft()
    new_position = move(rover_position, current_command)
    if field[new_position[0]][new_position[1]] == "-":
        field[new_position[0]][new_position[1]] = "E"
    elif field[new_position[0]][new_position[1]] == "W":
        mats_collected["W"] += 1
        print(f"Water deposit found at ({new_position[0]}, {new_position[1]})")
        field[new_position[0]][new_position[1]] = "E"
    elif field[new_position[0]][new_position[1]] == "M":
        mats_collected["M"] += 1
        print(f"Metal deposit found at ({new_position[0]}, {new_position[1]})")
        field[new_position[0]][new_position[1]] = "E"
    elif field[new_position[0]][new_position[1]] == "C":
        mats_collected["C"] += 1
        print(f"Concrete deposit found at ({new_position[0]}, {new_position[1]})")
        field[new_position[0]][new_position[1]] = "E"
    elif field[new_position[0]][new_position[1]] == "R":
        print(f"Rover got broken at {new_position}")
        break #TODO edge case to move the rover here ?

    rover_position = new_position

if sufficient_materials(mats_collected):
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
