rows = int(input())

matrix = [[int(el) for el in input().split(", ")] for _ in range(rows)]
primary_diagonal = []
secondary_diagonal = []

for row_index in range(len(matrix)):
    current_number = matrix[row_index][row_index]
    primary_diagonal.append(current_number)

for row_index in range(len(matrix) - 1, - 1, -1):
    current_number = matrix[len(matrix) - 1 - row_index][row_index]
    secondary_diagonal.append(current_number)

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")

