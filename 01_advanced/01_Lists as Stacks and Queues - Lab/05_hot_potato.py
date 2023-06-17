from collections import deque

kids = deque(input().split())
rotation = int(input()) - 1

while len(kids) > 1:
    kids.rotate(-rotation)
    print(f"Removed {kids.popleft()}")

print(f"Last is {kids.popleft()}")