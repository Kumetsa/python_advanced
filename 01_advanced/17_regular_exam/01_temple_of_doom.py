from collections import deque

tools = deque(map(int, input().split()))
substances = deque(map(int, input().split()))

challenges = list(map(int, input().split()))

while tools and substances:
    tool = tools.popleft()
    substance = substances.pop()

    result = tool * substance

    if result in challenges:
        challenges.remove(result)
    else:
        tool += 1
        tools.append(tool)
        substance -= 1
        if substance > 0:
            substances.append(substance)

    if not challenges:
        break

if challenges:
    print("Harry is lost in the temple. Oblivion awaits him.")
else:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")

if tools:
    print(f"Tools: {', '.join([str(tool) for tool in tools])}")
if substances:
    print(f"Substances: {', '.join([str(sub) for sub in substances])}")
if challenges:
    print(f"Challenges: {', '.join([str(chal) for chal in challenges])}")