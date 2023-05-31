import os

path_to_root = os.path.dirname(os.path.abspath(__file__))  # в скобите е абстрактния път до тук (файла), извън скобите
# до директорията
file_path = os.path.join(path_to_root, "text.txt")  # joinваме директорията с файла txt който е в текущата директория

try:
    open(file_path, "r")
    print("File found")
except FileNotFoundError:
    print("File not found")

# Alternative solution - if we dont want to open the file,but just validate it exist
# if os.path.isfile(file_path):
#     print("File found")
# else:
#     print("File not found")
