odd_set = set()
even_set = set()

for row in range(1, int(input() + 1)):
    name_ascii_value = sum([ord(el) for el in input()]) // row
    if name_ascii_value % 2 == 0:
        even_set.add(name_ascii_value)
    else:
        odd_set.add(name_ascii_value)

if sum(odd_set) == sum(even_set):
    union_set = even_set | odd_set
    print(", ".join(map(str, list(union_set))))
elif sum(odd_set) > sum(even_set):
    diff_set = odd_set - even_set
    print(", ".join(map(str, list(diff_set))))
elif sum(odd_set) < sum(even_set):
    sym_set = odd_set ^ even_set
    print(", ".join(map(str, list(sym_set))))