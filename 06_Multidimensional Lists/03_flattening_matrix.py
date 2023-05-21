rows = int(input())

matrix = []
flatten = []

for _ in range(rows):
    inner_list = [int(el) for el in input().split(", ")]
    matrix.append(inner_list)

for row_index in range(len(matrix)):
    for col_index in range(len(matrix[row_index])):
        flatten.append(matrix[row_index][col_index])

print(flatten)

# Alt flattening
#
# rows = int(input())
#
# flatten = []
#
# for _ in range(rows):
#     inner_list = [int(el) for el in input().split(", ")]
#     flatten.extend(inner_list)
#
# print(flatten)
