rows, cols = [int(el) for el in input().split(", ")]

matrix = []

for _ in range(rows):
    inner_list = [int(el) for el in input().split()]
    matrix.append(inner_list)

for col_index in range(cols):
    sum_cols_els = 0
    for row_index in range(rows):
        sum_cols_els += matrix[row_index][col_index]
    print(sum_cols_els)