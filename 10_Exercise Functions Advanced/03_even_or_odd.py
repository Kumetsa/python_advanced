def even_odd(*args):
    command, data = args[-1], args[:-1]
    if command == "even":
        numbers = [int(el) for el in data if int(el) % 2 == 0]
    else:
        numbers = [int(el) for el in data if int(el) % 2 != 0]
    return numbers


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))