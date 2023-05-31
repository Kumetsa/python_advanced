import os

file_name = "my_first_file.txt"
path_to_root = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(path_to_root, file_name)


try:
    with open(file_path, "w") as file: # with manager - automaticlly closing the file when we complete the block of code
        file.write('I just created my first file!')
except FileNotFoundError:
    print("File not found")


