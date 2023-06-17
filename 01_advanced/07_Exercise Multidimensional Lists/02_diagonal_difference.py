rows = int(input())

matrix = [[int(el) for el in input().split()] for _ in range(rows)]
primary_diagonal = [matrix[row_index][row_index] for row_index in range(len(matrix))]
secondary_diagonal = [matrix[len(matrix) - 1 - row_index][row_index] for row_index in range(len(matrix) - 1, - 1, -1)]

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))
