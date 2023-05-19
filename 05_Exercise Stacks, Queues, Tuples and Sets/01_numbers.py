from collections import deque

first_sequence = set(int(x) for x in input().split())
second_sequence = set(int(x) for x in input().split())

for _ in range(int(input())):
    command_arg = deque(input().split())
    arg = command_arg.popleft()

    if arg == "Add":
        select_sequence = command_arg.popleft()
        if select_sequence == "First":
            while command_arg:
                first_sequence.add(int(command_arg.popleft()))
        elif select_sequence == "Second":
            while command_arg:
                second_sequence.add(int(command_arg.popleft()))

    elif arg == "Remove":
        select_sequence = command_arg.popleft()
        if select_sequence == "First":
            while command_arg:
                el = int(command_arg.popleft())
                first_sequence.discard(el)
        elif select_sequence == "Second":
            while command_arg:
                el = int(command_arg.popleft())
                second_sequence.discard(el)

    elif arg == "Check":
        subset = first_sequence < second_sequence or first_sequence > second_sequence
        print(subset)

print(*sorted(first_sequence), sep=", ")
print(*sorted(second_sequence), sep=", ")


#Alternatoive solution (sleeker code)

# first_sequence = set(input().split())
# second_sequence = set(input().split())
#
# for _ in range(int(input())):
#     first_command, second_command, *data = input().split()
#
#     if first_command == "Add":
#         if second_command == "First":
#             first_sequence.add(el for el in data)
#         elif second_command == "Second":
#             second_sequence.add(el for el in data)
#     elif first_command == "Remove":
#         if second_command == "First":
#             first_sequence.discard(el for el in data)
#         elif second_command == "Second":
#             second_sequence.discard(el for el in data)
#     elif first_command == "Check":
#         print(first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence))
#
# print(*sorted(first_sequence), sep=", ")
# print(*sorted(second_sequence), sep=", ")








