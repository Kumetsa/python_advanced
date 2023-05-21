matrix = []

for _ in range(int(input())):
    inner_list = [int(el) for el in input().split(", ") if int(el) % 2 == 0]
    matrix.append(inner_list)

print(matrix)