from collections import deque

materials = deque(map(int, input().split()))
magic = deque(map(int, input().split()))

toys_crafted = {"Bicycle": 0, "Doll": 0, "Teddy bear": 0, "Wooden train": 0}

magic_value_for_toy = {150: "Doll", 250: "Wooden train", 300: "Teddy bear", 400: "Bicycle"}

while materials and magic:
    current_mat = materials.pop()
    current_magic = magic.popleft()

    if current_mat == 0 or current_magic == 0:
        if current_mat == 0:
            magic.appendleft(current_magic)
        if current_magic == 0:
            materials.append(current_mat)
        continue

    result = current_mat * current_magic
    if result in magic_value_for_toy:
        toys_crafted[magic_value_for_toy[result]] += 1
    elif result < 0:
        result = current_mat + current_magic
        materials.append(result)
    else:
        current_mat += 15
        materials.append(current_mat)

if toys_crafted["Doll"] >= 1 and toys_crafted["Wooden train"] >= 1 or toys_crafted["Teddy bear"] >= 1 and toys_crafted["Bicycle"] >= 1:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials][::-1])}")
if magic:
    print(f"Magic left: {', '.join(map(str, magic))}")


for toy, value in toys_crafted.items():
    if value > 0:
        print(f"{toy}: {value}")
