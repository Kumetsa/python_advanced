#Example 1
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