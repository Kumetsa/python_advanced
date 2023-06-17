def check_valid_index(coord):
    if 0 <= coord[0] < rows and 0 <= coord[1] < cols:
        return True


rows = int(input())

matrix = [[int(el) for el in input().split()] for _ in range(rows)]
cols = len(matrix[0])

while True:
    command_arg = input().split()
    if command_arg[0] == "END":
        break

    command, coordinates, value = command_arg[0], (int(command_arg[1]), int(command_arg[2])), int(command_arg[3])

    if check_valid_index(coordinates):
        if command == "Add":
            matrix[coordinates[0]][coordinates[1]] += value
        elif command == "Subtract":
            matrix[coordinates[0]][coordinates[1]] -= value
    else:
        print("Invalid coordinates")

[print(*row, sep=" ") for row in matrix]
