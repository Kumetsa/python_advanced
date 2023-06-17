set_elements = set()

for _ in range(int(input())):
    for el in input().split():
        set_elements.add(el)

print(*set_elements, sep="\n")