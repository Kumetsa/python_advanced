"""
Recursive solution for traversing folders from certain starting point.
"""
import os


def save_extensions(dir_name, first_level=False):
    for file_name in os.listdir(dir_name):
        file = os.path.join(dir_name, file_name)  # Absolute path to our file

        if os.path.isfile(file):
            extension = file_name.split(".")[-1]

            if extension not in extensions:
                extensions[extension] = []

            extensions[extension].append(file_name)

        elif os.path.isdir(file) and not first_level:
            save_extensions(file, first_level=True)   # We give True to the function, and next check will fail


directory = input()
extensions = {} # {.py: [example.py, exmple2.py],...}
try:
    save_extensions(directory)
except FileNotFoundError:
    print("Enter valid folder")

print(extensions)