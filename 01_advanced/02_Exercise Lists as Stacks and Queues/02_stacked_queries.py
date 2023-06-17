query_number = int(input())
stack = []

for _ in range(query_number):
    command_arg = input().split()
    command = command_arg[0]

    if command == "1":
        value = int(command_arg[1])
        stack.append(value)

    elif command == "2":
        if stack:
            stack.pop()

    elif command == "3":
        if stack:
            print(max(stack))

    elif command == "4":
        if stack:
            print(min(stack))

while stack:
    print(stack.pop(), end="")
    if stack:
        print(", ", end="")
