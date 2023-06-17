line = input().split()

nums_dict = {}

for number in line:
    if number not in nums_dict:
        nums_dict[number] = 0
    nums_dict[number] += 1

for number, count in nums_dict.items():
    number = float(number)
    print(f"{number:.1f} - {count} times")