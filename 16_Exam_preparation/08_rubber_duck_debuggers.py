from collections import deque

programmer_time = deque(map(int, input().split()))
number_of_tasks = deque(map(int, input().split()))

ducks = {
    "Darth Vader Ducky": 0,
    "Thor Ducky": 0,
    "Big Blue Rubber Ducky": 0,
    "Small Yellow Rubber Ducky": 0,
}

total_ducks = 0

while programmer_time and number_of_tasks:
    current_time = programmer_time.popleft()
    current_task = number_of_tasks.pop()

    result = current_time * current_task

    if result > 240:
        programmer_time.append(current_time)
        number_of_tasks.append(current_task - 2)
    elif 0 < result <= 60:
        ducks["Darth Vader Ducky"] += 1
        total_ducks += 1
    elif 61 <= result <= 120:
        ducks["Thor Ducky"] += 1
        total_ducks += 1
    elif 121 <= result <= 180:
        ducks["Big Blue Rubber Ducky"] += 1
        total_ducks += 1
    elif 181 <= result <= 240:
        ducks["Small Yellow Rubber Ducky"] += 1
        total_ducks += 1

print(f"Congratulations, all tasks have been completed! Rubber ducks rewarded:")

for duck, quantity in ducks.items():
    print(f"{duck}: {quantity}")
