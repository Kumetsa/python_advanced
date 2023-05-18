from collections import deque
customers = deque()
while True:
    command = input()
    if command == "End":
        break

    if command != "Paid":
        customers.append(command)
    else:
        while customers:
            print(customers.popleft())

print(f"{len(customers)} people remaining.")