import sys


def check_valid_index(coord, rows):
    if 0 <= coord[0] < rows and 0 <= coord[1] < rows:
        return True
    return False


def check_moves_result(matrix, bunny_pos):
    # Define the directions: up, down, left, right
    collected_positions = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    max_points = -sys.maxsize
    best_direction = None
    rows, cols = len(matrix), len(matrix[0])

    bunny_row, bunny_col = bunny_pos

    if check_valid_index(bunny_pos, rows):
        for direction in directions:
            points = 0
            dx, dy = direction

            x, y = bunny_row, bunny_col
            current_positions = []

            while 0 <= x < rows and 0 <= y < cols and matrix[x][y] != "X":
                if isinstance(matrix[x][y], int):
                    points += matrix[x][y]
                    current_positions.append([x, y])
                x += dx
                y += dy

            if points >= max_points:
                max_points = points
                if direction == (-1, 0):
                    best_direction = 'up'
                elif direction == (1, 0):
                    best_direction = 'down'
                elif direction == (0, -1):
                    best_direction = 'left'
                elif direction == (0, 1):
                    best_direction = 'right'
                collected_positions = current_positions

        return best_direction, collected_positions, max_points


rows = int(input())

matrix = [[int(el) if el.isdigit() else el for el in input().split()] for _ in range(rows)]

bunny_position = None

for row_index in range(rows):
    for col_index in range(rows):
        if matrix[row_index][col_index] == "B":
            bunny_position = (row_index, col_index)

result = check_moves_result(matrix, bunny_position)
print(result[0])
print(*result[1], sep="\n")
print(result[2])
