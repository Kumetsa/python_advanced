rows, cols = [int(el) for el in input().split()]

matrix = [[el for el in input().split()] for _ in range(rows)]

match_counter = 0

for row_index in range(rows - 1):
    for col_index in range(cols - 1):
        current_symbol = matrix[row_index][col_index]
        below_symbol = matrix[row_index + 1][col_index]
        next_symbol = matrix[row_index][col_index + 1]
        diagonal_symbol = matrix[row_index + 1][col_index + 1]
        if current_symbol == below_symbol == next_symbol == diagonal_symbol:
            match_counter += 1

print(match_counter)