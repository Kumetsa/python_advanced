rows, cols = [int(el) for el in input().split(", ")]

matrix = []

for _ in range(rows):
    inner_list = [int(el) for el in input().split(", ")]
    matrix.append(inner_list)

max_sum = float("-inf")
sub_matrix = []

for row_index in range(rows - 1):
    for col_index in range(cols - 1):
        current_number = matrix[row_index][col_index]
        next_number = matrix[row_index][col_index + 1]
        below_number = matrix[row_index + 1][col_index]
        diagonal_number = matrix[row_index + 1][col_index + 1]
        sum_num = current_number + next_number + below_number + diagonal_number

        if max_sum < sum_num:
            max_sum = sum_num
            sub_matrix = [[current_number, next_number], [below_number, diagonal_number]]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)

