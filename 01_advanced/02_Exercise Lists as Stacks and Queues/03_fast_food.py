from collections import deque

food_quantity = int(input())
orders = input().split()
queue = deque([int(el) for el in orders])
unserviced_orders = []

print(max(queue))

if sum(queue) <= food_quantity:
    print("Orders complete")
else:
    while len(queue) > 0:
        current_order = queue.popleft()
        if food_quantity >= current_order:
            food_quantity -= current_order
        else:
            unserviced_orders.append(str(current_order))
            while len(queue) > 0:
                unserviced_orders.append(str(queue.popleft()))
    print(f"Orders left: {' '.join(unserviced_orders)}")
