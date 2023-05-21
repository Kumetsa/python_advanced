rows = int(input())

matrix = []

for _ in range(rows):
    inner_list = [int(el) for el in input().split()]
    matrix.append(inner_list)

sum_diagonals = 0

for row_index in range(len(matrix)):
    current_number = matrix[row_index][row_index]
    sum_diagonals += current_number

print(sum_diagonals)