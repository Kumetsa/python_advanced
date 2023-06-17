from collections import deque

dispenser_liters = int(input())
queue = deque()

while True:
    command = input()
    if command == "Start":
        break
    queue.append(command)

while True:
    command = input()
    if command == "End":
        break

    if command.startswith("refill"):
        command = command.split(" ")
        liters_to_add = int(command[1])
        dispenser_liters += liters_to_add
    else:
        water_requested = int(command)
        if dispenser_liters >= water_requested:
            print(f"{queue.popleft()} got water")
            dispenser_liters -= water_requested
        else:
            print(f"{queue.popleft()} must wait")

print(f"{dispenser_liters} liters left")