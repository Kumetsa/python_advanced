"""
Recursive solution for traversing folders from certain starting point.
"""
import os


def save_extensions(dir_name):
    for file_name in os.listdir(dir_name):
        file = os.path.join(dir_name, file_name)  # Absolute path to our file

        if os.path.isfile(file):
            extension = file_name.split(".")[-1]

            if extension not in extensions:
                extensions[extension] = []

            extensions[extension].append(file_name)

        elif os.path.isdir(file):
            save_extensions(file)   # If the object is folder it will call the func again while there is folders


directory = input()
extensions = {} # {.py: [example.py, example2.py],...}
try:
    save_extensions(directory)
except FileNotFoundError:
    print("Enter valid folder")

result = []

extensions = sorted(extensions.items(), key=lambda x: x[0])

for extension, files in extensions:
    result.append(f"{extension}")
    [result.append(f"---{file}") for file in sorted(files)]

with open("report.txt", "w") as report_file:
    report_file.write("\n".join(result))

