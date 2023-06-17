from collections import deque


def milkshaker(chocolates, milk):

    milkshake_counter = 0
    while chocolates and milk and milkshake_counter < 5:
        choco = chocolates.pop()
        cup_of_milk = milk.popleft()

        if choco <= 0 or cup_of_milk <= 0:
            if choco > 0:
                chocolates.append(choco)
            if cup_of_milk > 0:
                milk.appendleft(cup_of_milk)
            continue

        if choco == cup_of_milk:
            milkshake_counter += 1
        else:
            milk.append(cup_of_milk)
            choco -= 5
            chocolates.append(choco)

    if milkshake_counter == 5:
        print("Great! You made all the chocolate milkshakes needed!")
    else:
        print("Not enough milkshakes.")

    if chocolates:
        print(f"Chocolate: {', '.join(map(str, chocolates))}")
    else:
        print("Chocolate: empty")
    if milk:
        print(f"Milk: {', '.join(map(str, milk))}")
    else:
        print("Milk: empty")


chocolates = deque(int(x) for x in input().split(", "))
milk = deque(int(x) for x in input().split(", "))
milkshaker(chocolates, milk)
