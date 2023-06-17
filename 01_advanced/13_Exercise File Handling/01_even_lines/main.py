import os

file_name = "text.txt"
path_to_root = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(path_to_root, file_name)

symbols = ["-", ",", ".", "!", "?"]

with open(file_path, "r") as file:
    text = file.readlines()

# итерираме през всеки ред и на всеки ред проверяваме дали има символа и ако го има го заместваме
for row in range(0, len(text), 2):

    for symbol in symbols:
        text[row] = text[row].replace(symbol, "@")
    # взимаме всеки елемент от text[row], разпакет. и сплитваме по спейс като им ревърсваме реда и разделяме по спейс
    print(*text[row].split()[::-1], sep=" ")

