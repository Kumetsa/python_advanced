box_of_clothes_stack = [int(el) for el in input().split()]
max_rack_size = int(input())

current_rack_size = 0
rack_count = 1

for parcalka in range(len(box_of_clothes_stack)):
    current_parcalka = box_of_clothes_stack.pop()
    if current_parcalka + current_rack_size <= max_rack_size:
        current_rack_size += current_parcalka
    else:
        rack_count += 1
        current_rack_size = 0
        current_rack_size += current_parcalka

print(rack_count)