rows, cols = [int(el) for el in input().split()]

matrix = [[int(el) for el in input().split()] for _ in range(rows)]

max_sum = float('-inf')
biggest_submatrix = []

for row_index in range(rows - 2):
    for col_index in range(cols - 2):
        first_row = matrix[row_index][col_index:col_index + 3]
        second_row = matrix[row_index + 1][col_index:col_index + 3]
        third_row = matrix[row_index + 2][col_index:col_index + 3]
        if sum(first_row + second_row + third_row) > max_sum:
            max_sum = sum(first_row + second_row + third_row)
            biggest_submatrix = [first_row, second_row, third_row]

print(f"Sum = {max_sum}")
[print(*row) for row in biggest_submatrix]