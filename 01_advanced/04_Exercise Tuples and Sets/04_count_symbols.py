my_dict = {}

for el in input():
    if el not in my_dict:
        my_dict[el] = 0
    my_dict[el] += 1

for key, value in sorted(my_dict.items()):
    print(f"{key}: {value} time/s")

#Alternative solution
# text = input()
# for letter in sorted(set(text)):
#     print(f"{letter}: {text.count(letter)} time/s")