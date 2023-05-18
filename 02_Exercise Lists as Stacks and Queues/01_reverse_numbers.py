text = input().split()
stack = []

for index in range(len(text)):
    stack.append(text.pop())

print(" ".join(stack))