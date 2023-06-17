from collections import deque

bees = deque(int(x) for x in input().split())
nectars = deque(int(x) for x in input().split())
chars = deque(input().split())

honey_made = 0

while bees and nectars:
    bee = bees.popleft()
    nectar = nectars.pop()

    if nectar >= bee:
        current_char = chars.popleft()
        if current_char == "/" and nectar == 0:
            continue
        nectar_made = eval(str(bee) + current_char + str(nectar))
        honey_made += abs(nectar_made)
    else:
        bees.appendleft(bee)

print(f"Total honey made: {honey_made}")
if bees:
    print(f"Bees left: {', '.join([str(el) for el in bees])}")
if nectars:
    print(f"Nectar left: {', '.join([str(el) for el in nectars])}")
