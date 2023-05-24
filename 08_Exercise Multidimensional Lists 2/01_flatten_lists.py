from collections import deque

matrix = [deque(el for el in element.split()) for element in input().split("|")]

flatten = []

for _ in range(len(matrix)):
    sublist = matrix.pop()
    for _ in range(len(sublist)):
        flatten.append(sublist.popleft())

print(' '.join(flatten))
