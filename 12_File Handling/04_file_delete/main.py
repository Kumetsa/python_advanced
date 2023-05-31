import os

file_name = "my_first_file.txt"
path_to_root = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(path_to_root, file_name)


if os.path.isfile(file_name):
    os.remove(file_path)

#Works, if the file is in the same directory
