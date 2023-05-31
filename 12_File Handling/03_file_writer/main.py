import os

file_name = "my_first_file.txt"
path_to_root = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(path_to_root, file_name)


try:
    file = open(file_path, "w")
    file.write('I just created my first file!')
except FileNotFoundError:
    print("File not found")


