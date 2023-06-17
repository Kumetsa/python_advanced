expression = input()

stack = []

for i in range(len(expression)):
    if expression[i] == "(":
        stack.append(i)
    elif expression[i] == ")":
        start_position = stack.pop()
        end_position = i + 1
        print(expression[start_position:end_position])

