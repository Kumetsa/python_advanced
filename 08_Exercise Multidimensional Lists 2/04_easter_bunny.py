def check_valid_index(coord):
    if 0 <= coord[0] < rows and 0 <= coord[1] < rows:
        return True
    return False


rows = int(input())

matrix = [[int(el) if el.isdigit() else el for el in input().split()] for _ in range(rows)]

bunny_position = None

for row_index in range(rows):
    for col_index in range(rows):
        if matrix[row_index][col_index] == "B":
            bunny_position = (row_index, col_index)


#to be continued...

print(*matrix, sep="\n")
print(bunny_position)

