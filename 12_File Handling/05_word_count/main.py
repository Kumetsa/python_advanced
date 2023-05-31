import os
import re
from collections import defaultdict


def read_content(file_path):
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        print("File not found!")
        exit(0)


root_dir = os.path.dirname(os.path.abspath(__file__))
# Words
words_file_name = "words.txt"
words_file_path = os.path.join(root_dir, words_file_name)

# Text
text_file_name = "text.txt"
text_file_path = os.path.join(root_dir, text_file_name)

words = read_content(words_file_path).lower().split()
text = read_content(text_file_path).lower()
text_content = re.sub(r"[^\w+\s]", '', text)
text_content_line = text_content.split("\n")

word_count = defaultdict(lambda: 0)

for word in words:
    for text_line in text_content_line:
        if word in text_line:
            word_count[word] += 1

with open("output.txt", "w") as file:
    for key, value in sorted(word_count.items(), key=lambda x: -x[1]):
        file.write(f"{key} - {value}\n")
