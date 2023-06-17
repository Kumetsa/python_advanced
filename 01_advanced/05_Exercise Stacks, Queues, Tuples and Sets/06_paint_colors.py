from collections import deque

text = deque(input().split())

all_colors = {"red", "yellow", "blue", "orange", "purple", "green"}
req_colors = {
    "orange": {"yellow", "red"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"},
}

result = []

while text:
    first_word = text.popleft()
    second_word = text.pop() if text else ""

    for color in (first_word + second_word, second_word + first_word):
        if color in all_colors:
            result.append(color)
            break
    else:
        for el in first_word[:-1], second_word[:-1]:
            if el:
                text.insert(len(text) // 2, el)


for color in set(req_colors.keys()).intersection(result):
    if not req_colors[color].issubset(result):
        result.remove(color)

print(result)