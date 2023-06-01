from string import punctuation
import os

file_name = "text.txt"
path_to_root = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(path_to_root, file_name)

with open(file_path, "r") as file:
    text = file.readlines()

output_file = open("output.txt", "w")

for i in range(len(text)):
    letters, marks = 0, 0

    for symbol in text[i]:
        if symbol.isalpha():
            letters += 1
        elif symbol in punctuation:
            marks += 1

    output_file.write(f"Line: {i + 1}: {''.join(text[i][:-1])} ({letters})({marks})\n")

output_file.close()
