row, col = [int(el) for el in input().split(", ")]

matrix = []
total_sum = 0

for _ in range(row):
    inner_list = [int(el) for el in input().split(", ")]
    total_sum += sum(inner_list)
    matrix.append(inner_list)

print(total_sum)
print(matrix)

