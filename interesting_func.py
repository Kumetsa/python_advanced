#Example 1
from datetime import datetime
import os

my_dict = {}
sorted(my_dict.items(), key=lambda x: x[0], reverse=True)

# .items returns us tuple of the key and value, then with key we determine sorting principle
# lambda x: - this takes the whole first element as tuple, then x[0] provides the key for sorting, if give [1] it will be the value
# reverse=True - default is False, we determine the order

#Example 2
def sorting_cheeses(**kwargs):
    sorted_cheeses = sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

#Фунцкията взима kwargs (речник), и в ламбда първо сортира по дължината на стойностите(броя), и после сортира по азбучен ред ключа.

#Example 3
def even_odd_filter(**kwargs):
    return dict(sorted(kwargs.items(), key=lambda x: -len(x[1])))
# сортираме по дължината на value (x[1]), в речник от kwargs
#decending е с минус

#Example 4
def concatenate(*args, **kwargs):
    text = ''.join(args)

    for key, val in kwargs.items():
        text = text.replace(key, val)

    return text

#съединява аргументите в стринг, итерира през речника по ключ и ако намеро с replace замества match-a с value-то

#Example 5
file_info = os.stat(file_path) #можем да си извадим статистики за файловете
print(f"file size: {file_info.st_size} bytes") #размера на файла
print(f"Last Modified: {datetime.fromtimestamp(int(file_info.st_mtime))}")


# Example 6
def move(direction, steps):  # създаваме фунцкия move, първи параметър посоката и втори стъпките int
    r = my_position[0] + (directions[direction][0] * steps)  # намираме реда и колоната като умножаваме стойностите от
    c = my_position[1] + (directions[direction][1] * steps)  # посоката по стъпките и събираме с текущите координати


# Example 6 - 1 pos movement func

def move(direction_, position_):
    if direction_ == 'up':
        position_[0] -= 1
    elif direction_ == 'down':
        position_[0] += 1
    elif direction_ == 'left':
        position_[1] -= 1
    elif direction_ == 'right':
        position_[1] += 1
    return position_


#Example 7
def get_time(self):
    return "{:02d}:{:02d}:{:02d}".format(self.hours, self.minutes, self.seconds)
""""In this code, "{:02d}" is the format specifier for an integer with a minimum width of 2 digits,
padded with leading zeros if necessary. The format method is then used to apply this formatting to the hours,
minutes, and seconds values."""

