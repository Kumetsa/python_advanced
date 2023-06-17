# from collections import deque

# expression = deque(input().split())
# current_numbers = deque()
#
# while expression:
#     element = expression.popleft()
#     if element == "*":
#         result = current_numbers.popleft()
#         while current_numbers:
#             result *= current_numbers.popleft()
#         current_numbers.append(result)
#     elif element == "+":
#         result = current_numbers.popleft()
#         while current_numbers:
#             result += current_numbers.popleft()
#         current_numbers.append(result)
#     elif element == "-":
#         result = current_numbers.popleft()
#         while current_numbers:
#             result -= current_numbers.popleft()
#         current_numbers.append(result)
#     elif element == "/":
#         result = current_numbers.popleft()
#         while current_numbers:
#             result = result // current_numbers.popleft()
#         current_numbers.append(result)
#     else:
#         current_numbers.append(int(element))
#
# print(*current_numbers)


# Alternative with fuction

from collections import deque


def perform_calculation(expression):
    current_numbers = deque()

    while expression:
        el = expression.popleft()
        if el in ("*", "+", "-",):
            result = current_numbers.popleft()
            while current_numbers:
                result = eval(str(result) + el + str(current_numbers.popleft()))
            current_numbers.append(result)
        elif el == "/":
            result = current_numbers.popleft()
            while current_numbers:
                result //= current_numbers.popleft()
            current_numbers.append(result)
        else:
            current_numbers.append(int(el))

    return current_numbers


expression = deque(input().split())
print(*perform_calculation(expression))

