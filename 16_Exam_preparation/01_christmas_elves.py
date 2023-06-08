from collections import deque

elfs = deque(int(el) for el in input().split())
materials = deque(int(el) for el in input().split())

total_energy_spent = 0
toys = 0
elf_counter = 1

while elfs and materials:
    elf = elfs.popleft()
    if elf < 5:
        continue

    material = materials.pop()

    if elf_counter % 3 == 0 and elf_counter % 5 == 0:
        if elf >= material * 2:
            elf -= material * 2
            elfs.append(elf)
            total_energy_spent += material * 2
        else:
            materials.append(material)
            elf = elf * 2
            elfs.append(elf)

    elif elf_counter % 3 == 0:
        if elf >= material * 2:
            elf -= material * 2
            toys += 2
            elf += 1
            elfs.append(elf)
            total_energy_spent += material * 2
        else:
            materials.append(material)
            elf = elf * 2
            elfs.append(elf)

    elif elf_counter % 5 == 0:
        if elf >= material:
            elf -= material
            elfs.append(elf)
            total_energy_spent += material
        else:
            materials.append(material)
            elf = elf * 2
            elfs.append(elf)

    elif elf >= material:
        elf -= material
        elf += 1
        elfs.append(elf)
        toys += 1
        total_energy_spent += material
    else:
        materials.append(material)
        elf *= 2
        elfs.append(elf)

    elf_counter += 1

print(f"Toys: {toys}")
print(f"Energy: {total_energy_spent}")
if elfs:
    print(f"Elves left: {', '.join(str(elf) for elf in elfs)}")
if materials:
    print(f"Boxes left: {', '.join(str(mat) for mat in materials)}")
